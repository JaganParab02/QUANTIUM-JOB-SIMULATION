import csv
from pathlib import Path

data_path = Path("data")
Path("processed-data").mkdir(exist_ok=True)
input_files = [
    "daily_sales_data_0.csv",
    "daily_sales_data_1.csv",
    "daily_sales_data_2.csv"
]

output_file = Path() / f"processed-data/processed_sales_data.csv"

rows = []

for file_name in input_files:
    with open(data_path / file_name, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        reader.fieldnames = [name.strip().lower() for name in reader.fieldnames]
        for row in reader:
            if row["product"].strip().lower() == "pink morsel":
                sales = float(row["quantity"]) * float(row["price"].replace("$", ""))
                rows.append({
                    "Sales": round(sales, 2),
                    "Date": row["date"],
                    "Region": row["region"]
                })

with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Sales", "Date", "Region"])
    writer.writeheader()
    writer.writerows(rows)

print(f"Processed {len(rows)} rows")
print("Processed data saved to:", output_file)
