import sqlite3
import pandas as pd
import numpy as np

def process_data():

    conn = sqlite3.connect("bank.db")

    query = """
    SELECT c.customer_id, c.age, c.annual_income,
           t.avg_monthly_spend, t.credit_utilization,
           l.loan_amount, l.loan_term_months,
           l.interest_rate, l.default_status
    FROM Customers c
    JOIN Transactions t ON c.customer_id = t.customer_id
    JOIN Loans l ON c.customer_id = l.customer_id
    """

    df = pd.read_sql(query, conn)
    conn.close()

    df.drop_duplicates(inplace=True)

    df['annual_income'].fillna(df['annual_income'].median(), inplace=True)

    # Outlier capping
    for col in ['annual_income', 'avg_monthly_spend', 'loan_amount']:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        df[col] = np.clip(df[col], Q1 - 1.5*IQR, Q3 + 1.5*IQR)

    # Feature Engineering
    df['debt_to_income_ratio'] = df['avg_monthly_spend']*12 / df['annual_income']
    df['loan_to_income_ratio'] = df['loan_amount'] / df['annual_income']

    df['age_group'] = pd.cut(
        df['age'],
        bins=[0,25,40,60,100],
        labels=['<25','25-40','40-60','60+']
    )

    df['income_band'] = pd.qcut(
        df['annual_income'],
        q=3,
        labels=['Low','Medium','High']
    )

    df.to_csv("processed_data.csv", index=False)
    print("Data processed.")

if __name__ == "__main__":
    process_data()