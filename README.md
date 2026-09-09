# 📊 Financial Analyzer

An automated financial data cleaning and analysis tool built using Python, Pandas, Plotly and Streamlit.

The application allows users to upload CSV or Excel financial data and automatically clean, analyze and visualize company financial performance.

---

## 🚀 Project Overview

Financial data often requires cleaning and analysis before meaningful insights can be obtained.

This project automates the basic process.

Users can upload a financial dataset containing:

- Date
- Revenue
- Expenses
- Assets
- Liabilities
- Equity

The application processes the data and automatically calculates financial metrics and ratios.

---

## ✨ Features

### 📁 File Upload

Supports:

- CSV
- XLSX
- XLS

### 🧹 Data Cleaning

The application:

- Removes duplicate rows
- Converts financial columns into numerical format
- Converts dates into proper date format
- Handles missing numerical values
- Sorts financial data by date
- Validates required columns

### 💰 Financial Analysis

The application calculates:

- Profit
- Profit Margin
- Revenue Growth
- Profit Growth
- Return on Assets (ROA)
- Return on Equity (ROE)
- Liabilities-to-Equity Ratio

### 📊 Dashboard

The application provides:

- Total Revenue
- Total Expenses
- Total Profit
- Overall Profit Margin
- Average ROA
- Average ROE
- Average Liabilities-to-Equity

### 📈 Interactive Visualizations

The dashboard includes:

- Revenue vs Expenses
- Profit Trend
- Profit Margin Trend
- Revenue & Profit Growth
- ROA vs ROE
- Liabilities-to-Equity Trend

### 💡 Automatic Insights

The application identifies:

- Highest revenue period
- Highest profit period
- Lowest profit period
- Highest profit margin
- Highest ROA
- Highest ROE
- Highest liabilities-to-equity ratio

### 📥 Download

Users can download the analyzed financial data as a CSV report.

---

## 🧮 Financial Formulas

### Profit

Profit = Revenue − Expenses

### Profit Margin

Profit Margin = (Profit / Revenue) × 100

### Revenue Growth

Revenue Growth = ((Current Revenue − Previous Revenue) / Previous Revenue) × 100

### Profit Growth

Profit Growth = ((Current Profit − Previous Profit) / Previous Profit) × 100

### ROA

ROA = (Profit / Assets) × 100

### ROE

ROE = (Profit / Equity) × 100

### Liabilities-to-Equity

Liabilities-to-Equity = Liabilities / Equity

> Note: The dataset contains total liabilities rather than specifically interest-bearing debt, so this project uses liabilities-to-equity as a simplified leverage measure.

---

## 🛠️ Technologies Used

- Python
- Pandas
- Streamlit
- Plotly
- OpenPyXL
- XLRD

---

## 📂 Project Structure

```text
Financial-Analyzer/
│
├── app.py
├── Financial Analyzer.ipynb
├── sample_financial_data.csv
├── requirements.txt
└── README.md
## 🚀 Live Demo

[Open Financial Analyzer](https://financialanalyzer-stxnr7ortp6ms42g9ydsie.streamlit.app/)
