# End-to-End Retail Credit Risk & Customer Insights Platform

## Overview
This project simulates a real-world retail banking analytics system designed to:
- Predict customer loan default probability
- Identify high-risk customer segments
- Support credit underwriting decisions
- Reduce Non-Performing Assets (NPAs)

---

## Architecture

SQLite (Data Layer)
        ↓
Python (EDA & ML)
        ↓
FastAPI (Model Serving)
        ↓
Streamlit (Business Dashboard)

---

## Data Engineering

- Synthetic dataset of 5,000 customers
- Intentional missing values and outliers
- SQL joins used for unified analytics view
- Median imputation for missing income
- IQR method for outlier capping

---

## Model Selection: Why Random Forest?

- Handles nonlinear relationships
- Robust to outliers
- Works well with mixed financial features
- Built-in feature importance for explainability
- Class imbalance handled using `class_weight='balanced'`

---

## Business Value

This platform enables:

✔ Early identification of high-risk borrowers  
✔ Data-driven underwriting decisions  
✔ Reduction in loan default rates  
✔ Improved portfolio quality  
✔ Lower provisioning costs  
✔ Strategic credit policy design  

By predicting default risk before loan approval, banks can significantly reduce NPAs and improve capital efficiency.

---

## How to Run Locally

1. Install dependenciess