import sqlite3
import random
import numpy as np
from faker import Faker

def generate_database():
    fake = Faker()
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    with open("schema.sql", "r") as f:
        cursor.executescript(f.read())

    for i in range(1, 5001):

        # Age
        age = random.randint(21, 65)

        # Realistic Annual Income (₹ scale)
        income = np.random.lognormal(mean=13, sigma=0.5)  # ~3L–15L+
        income = round(income, 2)

        if random.random() < 0.05:
            income = None

        cursor.execute("""
            INSERT INTO Customers VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            i,
            fake.name(),
            age,
            random.choice(["Male", "Female"]),
            fake.city(),
            income,
            random.choice(["Salaried", "Self-Employed", "Business"])
        ))

        # Transaction behavior
        utilization = np.clip(np.random.normal(0.5, 0.2), 0.05, 0.99)
        avg_spend = random.uniform(10000, 100000)

        cursor.execute("""
            INSERT INTO Transactions VALUES (?, ?, ?, ?)
        """, (i, i, avg_spend, utilization))

        # Loan
        loan_amount = random.uniform(100000, 3000000)
        term = random.choice([12, 24, 36, 48, 60])
        interest = random.uniform(8, 16)

        # Risk Logic (Aligned to financial scale)
        risk = 0

        if income and income < 400000:
            risk += 1

        if utilization > 0.7:
            risk += 1

        if avg_spend > 80000:
            risk += 1

        if income:
            loan_to_income = loan_amount / income
            if loan_to_income > 3:
                risk += 1

        # Add probabilistic noise
        probability = min(0.05 + risk * 0.20, 0.85)
        default = 1 if random.random() < probability else 0

        cursor.execute("""
            INSERT INTO Loans VALUES (?, ?, ?, ?, ?, ?)
        """, (i, i, loan_amount, term, interest, default))

    conn.commit()
    conn.close()
    print("Database generated successfully.")

if __name__ == "__main__":
    generate_database()