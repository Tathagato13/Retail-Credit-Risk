import streamlit as st
import pandas as pd
import joblib

st.set_page_config(layout="wide")
st.title("Retail Credit Risk & Customer Insights Dashboard")

df = pd.read_csv("processed_data.csv")
model = joblib.load("credit_risk_model.pkl")

# KPIs
total_exposure = df['loan_amount'].sum()
default_rate = df['default_status'].mean()*100
high_risk = (model.predict_proba(df[[
    'age','annual_income','avg_monthly_spend',
    'credit_utilization','loan_amount',
    'debt_to_income_ratio','loan_to_income_ratio'
]])[:,1] > 0.7).mean()*100

expected_loss = (model.predict_proba(df[[
    'age','annual_income','avg_monthly_spend',
    'credit_utilization','loan_amount',
    'debt_to_income_ratio','loan_to_income_ratio'
]])[:,1] * df['loan_amount']).sum()

col1,col2,col3,col4,col5 = st.columns(5)
col1.metric("Total Customers", len(df))
col2.metric("Total Exposure", f"{total_exposure:,.0f}")
col3.metric("Default Rate (%)", f"{default_rate:.2f}")
col4.metric("High Risk %", f"{high_risk:.2f}")
col5.metric("Expected Loss", f"{expected_loss:,.0f}")

st.subheader("Default Rate by Income Band")
st.bar_chart(df.groupby('income_band')['default_status'].mean())

st.subheader("Default Rate by Age Group")
st.bar_chart(df.groupby('age_group')['default_status'].mean())

st.subheader("DTI Comparison")
st.bar_chart(df.groupby('default_status')['debt_to_income_ratio'].mean())

st.subheader("Customer Risk Prediction")

age = st.number_input("Age", 18, 80, 35)
income = st.number_input("Annual Income", 10000, 10000000, 500000)
spend = st.number_input("Avg Monthly Spend", 1000, 500000, 20000)
util = st.slider("Credit Utilization", 0.0, 1.0, 0.5)
loan = st.number_input("Loan Amount", 50000, 5000000, 300000)

if st.button("Predict Risk"):

    dti = spend*12/income
    lti = loan/income

    input_df = pd.DataFrame([{
        'age':age,
        'annual_income':income,
        'avg_monthly_spend':spend,
        'credit_utilization':util,
        'loan_amount':loan,
        'debt_to_income_ratio':dti,
        'loan_to_income_ratio':lti
    }])

    prob = model.predict_proba(input_df)[0][1]

    if prob < 0.3:
        band = "Low Risk"
    elif prob < 0.7:
        band = "Medium Risk"
    else:
        band = "High Risk"

    st.success(f"Default Probability: {prob:.2f}")
    st.write(f"Risk Band: {band}")