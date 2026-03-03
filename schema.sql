DROP TABLE IF EXISTS Loans;
DROP TABLE IF EXISTS Transactions;
DROP TABLE IF EXISTS Customers;

CREATE TABLE Customers (
    customer_id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    city TEXT,
    annual_income REAL,
    employment_type TEXT
);

CREATE TABLE Transactions (
    transaction_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    avg_monthly_spend REAL,
    credit_utilization REAL,
    FOREIGN KEY(customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE Loans (
    loan_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    loan_amount REAL,
    loan_term_months INTEGER,
    interest_rate REAL,
    default_status INTEGER,
    FOREIGN KEY(customer_id) REFERENCES Customers(customer_id)
);