from pathlib import Path


def create_project_structure() -> None:
    """Create the healthcare analytics project folder structure."""

    base_directory = Path.cwd()

    directories = [
        "data/raw/open_payments",
        "data/reference",
        "data/processed",
        "data/sample",
        "scripts",
        "sql",
        "tests",
        "dashboards/tableau",
        "docs",
    ]

    for directory in directories:
        directory_path = base_directory / directory
        directory_path.mkdir(parents=True, exist_ok=True)

        gitkeep_file = directory_path / ".gitkeep"
        gitkeep_file.touch(exist_ok=True)

        print(f"Created: {directory_path.relative_to(base_directory)}")

    readme_path = base_directory / "README.md"

    if not readme_path.exists():
        readme_path.write_text(
            "# US Healthcare Commercial Intelligence\n\nAnalytics of publicly available CMS Open Payments data.\n",
            encoding="utf-8",
        )
        print("Created: README.md")
    else:
        print("Skipped: README.md already exists")

    print("\nProject structure created successfully.")


if __name__ == "__main__":
    create_project_structure()
