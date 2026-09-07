"""Initial profiling for CMS Open Payments General Payments data."""

from datetime import datetime, timezone
from pathlib import Path
import json
import duckdb


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIRECTORY = PROJECT_ROOT / "data" / "raw" / "open_payments"
SAMPLE_DIRECTORY = PROJECT_ROOT / "data" / "sample"
PROFILE_DIRECTORY = PROJECT_ROOT / "docs" / "data-profiling"

SAMPLE_SIZE = 1_000


def find_source_file() -> Path:
    """Find the Open Payments General Payments CSV."""

    candidates = sorted(RAW_DIRECTORY.glob("*GNRL*.csv"))

    if not candidates:
        raise FileNotFoundError(
            "No General Payments CSV was found in "
            f"{RAW_DIRECTORY}. Expected a filename containing 'GNRL'."
        )

    if len(candidates) > 1:
        filenames = "\n".join(f"- {file.name}" for file in candidates)
        raise RuntimeError(
            "Multiple General Payments files were found:\n"
            f"{filenames}\n"
            "Keep only the intended source file in the raw directory."
        )

    return candidates[0]


def escape_sql_string(value: str) -> str:
    """Escape a value for use inside a DuckDB SQL string."""

    return value.replace("'", "''")


def format_bytes(size_bytes: int) -> str:
    """Convert bytes into a readable file-size string."""

    units = ["B", "KB", "MB", "GB", "TB"]
    size = float(size_bytes)

    for unit in units:
        if size < 1024 or unit == units[-1]:
            return f"{size:,.2f} {unit}"
        size /= 1024

    return f"{size_bytes:,} B"


def main() -> None:
    """Profile the source and create documentation artifacts."""

    source_file = find_source_file()
    source_sql_path = escape_sql_string(str(source_file))

    SAMPLE_DIRECTORY.mkdir(parents=True, exist_ok=True)
    PROFILE_DIRECTORY.mkdir(parents=True, exist_ok=True)

    sample_file = SAMPLE_DIRECTORY / "open_payments_sample.csv"
    profile_file = PROFILE_DIRECTORY / "open_payments_initial_profile.md"
    metadata_file = PROFILE_DIRECTORY / "open_payments_metadata.json"

    print(f"Source file: {source_file.name}")
    print(f"File size: {format_bytes(source_file.stat().st_size)}")
    print("Connecting to DuckDB...")

    connection = duckdb.connect()

    try:
        connection.execute(
            f"""
            CREATE OR REPLACE VIEW raw_open_payments AS
            SELECT *
            FROM read_csv(
                '{source_sql_path}',
                header = true,
                auto_detect = true,
                sample_size = 100000,
                all_varchar = true,
                parallel = true
            );
            """
        )

        print("Reading schema...")
        schema_rows = connection.execute("DESCRIBE raw_open_payments").fetchall()

        print("Counting records; this may take several minutes...")
        row_count = connection.execute(
            "SELECT COUNT(*) FROM raw_open_payments"
        ).fetchone()[0]

        print(f"Creating a {SAMPLE_SIZE:,}-row sample...")
        sample_sql_path = escape_sql_string(str(sample_file))

        connection.execute(
            f"""
            COPY (
                SELECT *
                FROM raw_open_payments
                LIMIT {SAMPLE_SIZE}
            )
            TO '{sample_sql_path}'
            (
                HEADER,
                DELIMITER ',',
                FORMAT CSV
            );
            """
        )

        generated_at = datetime.now(timezone.utc).isoformat()
        column_names = [row[0] for row in schema_rows]

        metadata = {
            "source_filename": source_file.name,
            "source_size_bytes": source_file.stat().st_size,
            "source_size_readable": format_bytes(source_file.stat().st_size),
            "row_count": row_count,
            "column_count": len(schema_rows),
            "columns": column_names,
            "sample_row_count": SAMPLE_SIZE,
            "generated_at_utc": generated_at,
        }

        metadata_file.write_text(
            json.dumps(metadata, indent=2),
            encoding="utf-8",
        )

        schema_table = "\n".join(f"| `{row[0]}` | `{row[1]}` |" for row in schema_rows)

        report = f"""# Open Payments Initial Data Profile

## Source summary

| Metric | Value |
|---|---:|
| Source file | `{source_file.name}` |
| File size | {format_bytes(source_file.stat().st_size)} |
| Records | {row_count:,} |
| Columns | {len(schema_rows):,} |
| Sample records | {SAMPLE_SIZE:,} |
| Profile generated | {generated_at} |

## Initial ingestion decision

The source was read using DuckDB with all fields initially treated as
strings. This prevents malformed or inconsistent values from causing
premature type-conversion failures. Data types will be assigned during
the staging transformation.

## Source schema

| Column | Initial type |
|---|---|
{schema_table}

## Data-use note

This dataset contains publicly reported administrative information from
CMS Open Payments. It does not contain patient-level clinical records.
Reported payments do not establish prescribing influence or causation.
"""

        profile_file.write_text(report, encoding="utf-8")

    finally:
        connection.close()

    print("\nProfiling completed successfully.")
    print(f"Sample: {sample_file.relative_to(PROJECT_ROOT)}")
    print(f"Report: {profile_file.relative_to(PROJECT_ROOT)}")
    print(f"Metadata: {metadata_file.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
