import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, classification_report, confusion_matrix

def train_model():

    df = pd.read_csv("processed_data.csv")

    X = df[[
        'age',
        'annual_income',
        'avg_monthly_spend',
        'credit_utilization',
        'loan_amount',
        'debt_to_income_ratio',
        'loan_to_income_ratio'
    ]]

    y = df['default_status']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    y_proba = model.predict_proba(X_test)[:,1]
    y_pred = model.predict(X_test)

    print("ROC-AUC:", roc_auc_score(y_test, y_proba))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

    coefficients = pd.Series(model.coef_[0], index=X.columns)
    print("Feature Coefficients:\n", coefficients.sort_values(ascending=False))

    joblib.dump(model, "credit_risk_model.pkl")
    print("Model saved.")

if __name__ == "__main__":
    train_model()