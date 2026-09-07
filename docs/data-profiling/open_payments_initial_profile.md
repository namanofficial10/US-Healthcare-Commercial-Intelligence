# Open Payments Initial Data Profile

## Source summary

| Metric | Value |
|---|---:|
| Source file | `OP_DTL_GNRL_PGYR2024_P06302026_06032026.csv` |
| File size | 8.35 GB |
| Records | 15,498,687 |
| Columns | 91 |
| Sample records | 1,000 |
| Profile generated | 2026-09-07T08:01:28.779217+00:00 |

## Initial ingestion decision

The source was read using DuckDB with all fields initially treated as
strings. This prevents malformed or inconsistent values from causing
premature type-conversion failures. Data types will be assigned during
the staging transformation.

## Source schema

| Column | Initial type |
|---|---|
| `Change_Type` | `VARCHAR` |
| `Covered_Recipient_Type` | `VARCHAR` |
| `Teaching_Hospital_CCN` | `VARCHAR` |
| `Teaching_Hospital_ID` | `VARCHAR` |
| `Teaching_Hospital_Name` | `VARCHAR` |
| `Covered_Recipient_Profile_ID` | `VARCHAR` |
| `Covered_Recipient_NPI` | `VARCHAR` |
| `Covered_Recipient_First_Name` | `VARCHAR` |
| `Covered_Recipient_Middle_Name` | `VARCHAR` |
| `Covered_Recipient_Last_Name` | `VARCHAR` |
| `Covered_Recipient_Name_Suffix` | `VARCHAR` |
| `Recipient_Primary_Business_Street_Address_Line1` | `VARCHAR` |
| `Recipient_Primary_Business_Street_Address_Line2` | `VARCHAR` |
| `Recipient_City` | `VARCHAR` |
| `Recipient_State` | `VARCHAR` |
| `Recipient_Zip_Code` | `VARCHAR` |
| `Recipient_Country` | `VARCHAR` |
| `Recipient_Province` | `VARCHAR` |
| `Recipient_Postal_Code` | `VARCHAR` |
| `Covered_Recipient_Primary_Type_1` | `VARCHAR` |
| `Covered_Recipient_Primary_Type_2` | `VARCHAR` |
| `Covered_Recipient_Primary_Type_3` | `VARCHAR` |
| `Covered_Recipient_Primary_Type_4` | `VARCHAR` |
| `Covered_Recipient_Primary_Type_5` | `VARCHAR` |
| `Covered_Recipient_Primary_Type_6` | `VARCHAR` |
| `Covered_Recipient_Specialty_1` | `VARCHAR` |
| `Covered_Recipient_Specialty_2` | `VARCHAR` |
| `Covered_Recipient_Specialty_3` | `VARCHAR` |
| `Covered_Recipient_Specialty_4` | `VARCHAR` |
| `Covered_Recipient_Specialty_5` | `VARCHAR` |
| `Covered_Recipient_Specialty_6` | `VARCHAR` |
| `Covered_Recipient_License_State_code1` | `VARCHAR` |
| `Covered_Recipient_License_State_code2` | `VARCHAR` |
| `Covered_Recipient_License_State_code3` | `VARCHAR` |
| `Covered_Recipient_License_State_code4` | `VARCHAR` |
| `Covered_Recipient_License_State_code5` | `VARCHAR` |
| `Submitting_Applicable_Manufacturer_or_Applicable_GPO_Name` | `VARCHAR` |
| `Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_ID` | `VARCHAR` |
| `Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_Name` | `VARCHAR` |
| `Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_State` | `VARCHAR` |
| `Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_Country` | `VARCHAR` |
| `Total_Amount_of_Payment_USDollars` | `VARCHAR` |
| `Date_of_Payment` | `VARCHAR` |
| `Number_of_Payments_Included_in_Total_Amount` | `VARCHAR` |
| `Form_of_Payment_or_Transfer_of_Value` | `VARCHAR` |
| `Nature_of_Payment_or_Transfer_of_Value` | `VARCHAR` |
| `City_of_Travel` | `VARCHAR` |
| `State_of_Travel` | `VARCHAR` |
| `Country_of_Travel` | `VARCHAR` |
| `Physician_Ownership_Indicator` | `VARCHAR` |
| `Third_Party_Payment_Recipient_Indicator` | `VARCHAR` |
| `Name_of_Third_Party_Entity_Receiving_Payment_or_Transfer_of_Value` | `VARCHAR` |
| `Charity_Indicator` | `VARCHAR` |
| `Third_Party_Equals_Covered_Recipient_Indicator` | `VARCHAR` |
| `Contextual_Information` | `VARCHAR` |
| `Delay_in_Publication_Indicator` | `VARCHAR` |
| `Record_ID` | `VARCHAR` |
| `Dispute_Status_for_Publication` | `VARCHAR` |
| `Related_Product_Indicator` | `VARCHAR` |
| `Covered_or_Noncovered_Indicator_1` | `VARCHAR` |
| `Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_1` | `VARCHAR` |
| `Product_Category_or_Therapeutic_Area_1` | `VARCHAR` |
| `Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_1` | `VARCHAR` |
| `Associated_Drug_or_Biological_NDC_1` | `VARCHAR` |
| `Associated_Device_or_Medical_Supply_PDI_1` | `VARCHAR` |
| `Covered_or_Noncovered_Indicator_2` | `VARCHAR` |
| `Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_2` | `VARCHAR` |
| `Product_Category_or_Therapeutic_Area_2` | `VARCHAR` |
| `Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_2` | `VARCHAR` |
| `Associated_Drug_or_Biological_NDC_2` | `VARCHAR` |
| `Associated_Device_or_Medical_Supply_PDI_2` | `VARCHAR` |
| `Covered_or_Noncovered_Indicator_3` | `VARCHAR` |
| `Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_3` | `VARCHAR` |
| `Product_Category_or_Therapeutic_Area_3` | `VARCHAR` |
| `Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_3` | `VARCHAR` |
| `Associated_Drug_or_Biological_NDC_3` | `VARCHAR` |
| `Associated_Device_or_Medical_Supply_PDI_3` | `VARCHAR` |
| `Covered_or_Noncovered_Indicator_4` | `VARCHAR` |
| `Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_4` | `VARCHAR` |
| `Product_Category_or_Therapeutic_Area_4` | `VARCHAR` |
| `Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_4` | `VARCHAR` |
| `Associated_Drug_or_Biological_NDC_4` | `VARCHAR` |
| `Associated_Device_or_Medical_Supply_PDI_4` | `VARCHAR` |
| `Covered_or_Noncovered_Indicator_5` | `VARCHAR` |
| `Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_5` | `VARCHAR` |
| `Product_Category_or_Therapeutic_Area_5` | `VARCHAR` |
| `Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_5` | `VARCHAR` |
| `Associated_Drug_or_Biological_NDC_5` | `VARCHAR` |
| `Associated_Device_or_Medical_Supply_PDI_5` | `VARCHAR` |
| `Program_Year` | `VARCHAR` |
| `Payment_Publication_Date` | `VARCHAR` |

## Data-use note

This dataset contains publicly reported administrative information from
CMS Open Payments. It does not contain patient-level clinical records.
Reported payments do not establish prescribing influence or causation.
