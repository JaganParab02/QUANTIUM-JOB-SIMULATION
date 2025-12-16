# Pink Morsel Sales Dashboard

This project was completed as part of the **Quantium Job Simulation on Forage**, designed to provide hands-on experience with the type of analytical and engineering tasks performed at Quantium. The simulation mirrors real-world work scenarios by presenting loosely defined business problems, raw datasets, and incremental technical requirements, similar to how tasks are assigned in a professional data and analytics environment.

The application analyses and visualises sales data for Soul Foods’ *Pink Morsel* product line. It processes raw transactional CSV files, generates a clean sales dataset, and presents an interactive Dash dashboard that clearly shows sales trends before and after the Pink Morsel price increase on **15 January 2021**.

---

## Project Context

This project simulates how analytical tasks are delivered at Quantium, where developers and analysts are expected to:

* Interpret business questions from minimal initial requirements
* Clean and structure raw data into analysis-ready formats
* Build simple, reliable visual tools that allow stakeholders to explore insights
* Apply testing and automation practices to ensure reliability

The tasks in this simulation were designed to closely resemble real Quantium workflows, focusing on clarity, correctness, and business relevance rather than unnecessary technical complexity.

---

## Project Overview

The project is built in three stages:

1. **Data Processing**
   Raw transaction data from multiple CSV files is filtered to include only Pink Morsel sales, total sales values are calculated, and the data is saved in a structured format for analysis.

2. **Data Visualisation**
   A Dash web application displays a time-series line chart of Pink Morsel sales. A region selector allows users to filter sales data by geographic region, and a reference line highlights the date of the price increase.

3. **Testing and CI Readiness**
   Automated UI tests verify that the dashboard renders correctly, and a bash script allows the test suite to be executed automatically in a continuous integration environment.

---

## Prerequisites

* Python 3.9 or later
* Git
* Google Chrome (for Dash UI testing)
* ChromeDriver (matching your Chrome version)
* Git Bash (recommended on Windows)

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/JaganParab02/QUANTIUM-JOB-SIMULATION.git
cd QUANTIUM-JOB-SIMULATION
```

---

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows (Git Bash)**

```bash
source venv/Scripts/activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
pip install "dash[testing]"
```

---

## Running the Application

### 1. Generate Processed Sales Data

```bash
python process_csv_sales_data.py
```

This generates the processed sales dataset inside the `processed-data/` directory.

---

### 2. Start the Dash Application

```bash
python app.py
```

Open your browser at:

```
http://127.0.0.1:8050/
```

---

## Running Tests

### Run Tests Manually

```bash
pytest
```

---

### Run Tests Using the CI Script

```bash
./run_tests.sh
```

The script exits with:

* `0` if all tests pass
* `1` if any test fails

---

## Project Structure

```
QUANTIUM-JOB-SIMULATION/
│
├── app.py
├── process_csv_sales_data.py
├── run_tests.sh
├── tests/
│   └── test_app.py
├── data/
├── processed-data/
├── requirements.txt
└── README.md
```

---

## Summary

This project was completed as part of the **Quantium Job Simulation on Forage** to gain practical experience with real-world analytical and engineering tasks. It demonstrates how raw business data is transformed into actionable insights through structured data processing, clear visualisation, automated testing, and CI-ready workflows—reflecting how similar tasks are approached in a professional Quantium environment.

---
