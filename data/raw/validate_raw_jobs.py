import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw/raw_jobs.csv")

EXPECTED_COLUMNS = [
    "job_id",
    "job_title",
    "company",
    "location",
    "employment_type",
    "work_model",
    "job_url",
    "source",
    "date_collected",
    "job_description",
]


def read_csv_safely(path):
    try:
        return pd.read_csv(path, encoding="utf-8")
    except UnicodeDecodeError:
        return pd.read_csv(path, encoding="latin1")


def main():
    df = read_csv_safely(RAW_PATH)

    print("Rows:", len(df))
    print("Columns:", list(df.columns))

    missing_columns = [col for col in EXPECTED_COLUMNS if col not in df.columns]

    if missing_columns:
        print("Missing columns:", missing_columns)
        return

    print("\nColumn check: OK")

    print("\nEmpty job descriptions:")
    print(df["job_description"].isna().sum())

    print("\nVery short job descriptions:")
    short_descriptions = df[df["job_description"].fillna("").str.len() < 100]
    print(len(short_descriptions))

    if len(short_descriptions) > 0:
        print(short_descriptions[["job_id", "job_title", "job_description"]].to_string(index=False))

    print("\nSkill keyword quick check:")
    for keyword in ["SQL", "Python", "Power BI", "Tableau", "Excel", "German", "English"]:
        count = df["job_description"].str.contains(keyword, case=False, na=False).sum()
        print(f"{keyword}: {count}")

    print("\nFirst 3 rows:")
    print(df[["job_id", "job_title", "company"]].head(3).to_string(index=False))


if __name__ == "__main__":
    main()