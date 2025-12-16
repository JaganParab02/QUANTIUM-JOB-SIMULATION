---

```markdown
# Quantium Job Simulation – Data Processing Task

This repository contains the solution for the data processing task in the Quantium Job Simulation.  
The objective of this task is to transform raw transaction data into a clean, structured dataset that can be used for analysis and visualization.

---

## 📊 Task Overview

Soul Foods provided three CSV files containing transaction-level data for different morsel products sold across regions and dates.  
The business question focuses specifically on **Pink Morsel** sales.

To support further analysis, the raw data is processed to:
- Filter only *Pink Morsel* transactions
- Compute total sales per transaction
- Output a clean, unified dataset

---

## 🛠️ Data Processing Logic

The processing script performs the following steps:

1. Reads all CSV files from the `data/` directory  
2. Filters rows where the product is **Pink Morsel**  
3. Calculates **Sales = Quantity × Price**  
4. Retains only the required fields:
   - `Sales`
   - `Date`
   - `Region`
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

1. Activate your Python virtual environment
2. Run the script:

```bash
python process_csv_sales_data.py
````

The processed output file will be generated in the `processed-data/` directory.

---

## 🧪 Output Format

The generated CSV contains exactly three fields:

```
Sales, Date, Region
```

Each row represents a single Pink Morsel transaction with computed sales value.

---

## ✅ Notes

* The output file name includes the current timestamp to avoid overwriting previous runs
* The `processed-data/` directory is created automatically if it does not exist
* Virtual environments are excluded from version control

---

This repository serves as the foundation for subsequent tasks involving data analysis and interactive visualization using Dash.

```

---

## 🏁 Final Verdict (Reviewer View)

✔ Clean folder separation  
✔ Defensive, production-safe code  
✔ Clear README  
✔ Correct output format  
✔ Timestamped outputs  
✔ Excellent job-simulation quality  

You are **100% ready to submit** 🚀  

If you want next:
- Help with **next Quantium task**
- README **shorter version**
- Resume-ready explanation of this task

Just tell me 👍
```
