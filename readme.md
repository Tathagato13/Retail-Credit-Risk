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

# Screenshots
<img width="1829" height="754" alt="Screenshot 2026-03-05 122046" src="https://github.com/user-attachments/assets/d307278f-4c9f-46b2-818d-4e733afa6070" />
<img width="1848" height="836" alt="Screenshot 2026-03-05 122100" src="https://github.com/user-attachments/assets/b2239560-a4ee-44e7-bb52-821040463599" />
<img width="1840" height="624" alt="Screenshot 2026-03-05 122122" src="https://github.com/user-attachments/assets/4a7f6e4d-cc51-4746-af92-33e37d3cc17d" />

---

## How to Run Locally


1. Install Requirements

## 📁 Project Structure

```text
Retail-Credit-Risk/
│
├── data/
│   ├── raw/                      # Raw generated or downloaded datasets
│   └── processed/                # Cleaned and feature-engineered datasets
│
├── models/
│   └── trained_model.pkl         # Saved ML model
│
├── notebooks/
│   └── exploratory_analysis.ipynb
│
├── src/
│   ├── generate_data.py          # Synthetic data generation
│   ├── data_processing.py        # Cleaning and feature engineering
│   └── train_model.py            # Model training pipeline
│
├── database/
│   ├── schema.sql                # Database schema
│   └── retail_credit.db          # SQLite database
│
├── app/
│   └── app.py                    # Streamlit dashboard
│
├── main.py                       # End-to-end pipeline runner
├── requirements.txt
├── README.md
└── .gitignore
```

# clone repo
git clone https://github.com/Tathagato13/Retail-Credit-Risk.git

cd Retail-Credit-Risk

# install dependencies
pip install -r requirements.txt

# run full pipeline
python main.py

# launch dashboard
streamlit run app/app.py




