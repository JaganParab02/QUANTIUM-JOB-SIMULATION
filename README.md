```markdown
# Quantium Job Simulation – Data Processing

This repository contains the solution for the data processing task in the Quantium Job Simulation.  
The objective of this task is to transform raw transaction data into a clean, structured dataset suitable for analysis and visualization.

---

## 📌 Task Description

Soul Foods provided three CSV files containing transaction data for its morsel product line.  
Each record represents the quantity sold, price, region, and date of sale.

The business focus of this task is on **Pink Morsel** sales only.

---

## 🔄 Data Processing Steps

The processing script performs the following operations:

1. Reads all transaction CSV files from the `data/` directory  
2. Filters records to include only **Pink Morsel**  
3. Calculates total sales using:

```

Sales = Quantity × Price

```

4. Retains only the required fields:
- Sales
- Date
- Region
5. Writes the processed data to a timestamped CSV file

---

## 📁 Project Structure

```

quantium-starter-repo/
│
├── data/
│   ├── daily_sales_data_0.csv
│   ├── daily_sales_data_1.csv
│   ├── daily_sales_data_2.csv
│
├── processed-data/
│   └── processed_sales_data_YYYY_MM_DD_HH_MM_SS.csv
│
├── process_csv_sales_data.py
├── requirements.txt
├── .gitignore
└── README.md

````

---

## ▶️ How to Run

1. Activate the Python virtual environment
2. Run the processing script:

```bash
python process_csv_sales_data.py
````

The processed output file will be created automatically in the `processed-data/` directory.

---

## 📄 Output Format

The generated CSV file contains exactly three columns:

```
Sales, Date, Region
```

Each row represents a processed Pink Morsel transaction.

---

## 📝 Notes

* Output files are timestamped to prevent overwriting previous runs
* The `processed-data/` directory is created automatically if it does not exist
* Virtual environments are excluded from version control

---

This repository provides a clean and reproducible foundation for further analysis and dashboard development using the Dash framework.

```

just tell me 👍
```
