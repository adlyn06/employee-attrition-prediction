from pydantic import BaseModel
from fastapi import FastAPI
import joblib
# import pandas as pd
import numpy as np
import shap

app = FastAPI()

# Load trained model
model = joblib.load("../attrition_model.pkl")
explainer = shap.TreeExplainer(model)

def risk_score(prob):
    if prob < 0.30:
        return "Low"
    elif prob < 0.50:
        return "Medium"
    else:
        return "High"
    
def retention_recommendation(probability):

    if probability >= 0.7:
        return [
            "Immediate HR intervention",
            "Conduct one-on-one meeting",
            "Review compensation and benefits",
            "Offer career growth opportunities"
        ]

    elif probability >= 0.3:
        return [
            "Monitor employee satisfaction",
            "Provide training opportunities",
            "Regular manager check-ins"
        ]

    else:
        return [
            "No immediate action required"
        ]


class EmployeeData(BaseModel):
    Age: int
    BusinessTravel: int
    DailyRate: int
    Department: int
    DistanceFromHome: int
    Education: int
    EducationField: int
    EnvironmentSatisfaction: int
    Gender: int
    HourlyRate: int
    JobInvolvement: int
    JobLevel: int
    JobRole: int
    JobSatisfaction: int
    MaritalStatus: int
    MonthlyIncome: int
    MonthlyRate: int
    NumCompaniesWorked: int
    OverTime: int
    PercentSalaryHike: int
    PerformanceRating: int
    RelationshipSatisfaction: int
    StockOptionLevel: int
    TotalWorkingYears: int
    TrainingTimesLastYear: int
    WorkLifeBalance: int
    YearsAtCompany: int
    YearsInCurrentRole: int
    YearsSinceLastPromotion: int
    YearsWithCurrManager: int

@app.get("/")
def home():
    return {"message": "Employee Attrition API Running"}


@app.get("/test_prediction")
def test_prediction():

    sample = [[
        41, 2, 1102, 2, 1,
        2, 1, 2, 0, 94,
        3, 2, 7, 4, 1,
        5993, 19479, 8, 1, 11,
        3, 1, 0, 8, 0,
        1, 6, 4, 0, 5
    ]]

    prediction = model.predict(sample)[0]
    probability = model.predict_proba(sample)[0][1]

    return {
        "prediction": int(prediction),
        "attrition_probability": round(float(probability), 2),
        "risk_score": risk_score(probability)
    }


@app.post("/predict_attrition")
def predict_attrition(employee: EmployeeData):

    data = [[
        employee.Age,
        employee.BusinessTravel,
        employee.DailyRate,
        employee.Department,
        employee.DistanceFromHome,
        employee.Education,
        employee.EducationField,
        employee.EnvironmentSatisfaction,
        employee.Gender,
        employee.HourlyRate,
        employee.JobInvolvement,
        employee.JobLevel,
        employee.JobRole,
        employee.JobSatisfaction,
        employee.MaritalStatus,
        employee.MonthlyIncome,
        employee.MonthlyRate,
        employee.NumCompaniesWorked,
        employee.OverTime,
        employee.PercentSalaryHike,
        employee.PerformanceRating,
        employee.RelationshipSatisfaction,
        employee.StockOptionLevel,
        employee.TotalWorkingYears,
        employee.TrainingTimesLastYear,
        employee.WorkLifeBalance,
        employee.YearsAtCompany,
        employee.YearsInCurrentRole,
        employee.YearsSinceLastPromotion,
        employee.YearsWithCurrManager
    ]]

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    return {
        "prediction": int(prediction),
        "attrition_probability": round(float(probability), 2),
        "risk_score": risk_score(probability)
    }


@app.post("/retention_recommendations")
def get_recommendations(employee: EmployeeData):

    data = [[
        employee.Age,
        employee.BusinessTravel,
        employee.DailyRate,
        employee.Department,
        employee.DistanceFromHome,
        employee.Education,
        employee.EducationField,
        employee.EnvironmentSatisfaction,
        employee.Gender,
        employee.HourlyRate,
        employee.JobInvolvement,
        employee.JobLevel,
        employee.JobRole,
        employee.JobSatisfaction,
        employee.MaritalStatus,
        employee.MonthlyIncome,
        employee.MonthlyRate,
        employee.NumCompaniesWorked,
        employee.OverTime,
        employee.PercentSalaryHike,
        employee.PerformanceRating,
        employee.RelationshipSatisfaction,
        employee.StockOptionLevel,
        employee.TotalWorkingYears,
        employee.TrainingTimesLastYear,
        employee.WorkLifeBalance,
        employee.YearsAtCompany,
        employee.YearsInCurrentRole,
        employee.YearsSinceLastPromotion,
        employee.YearsWithCurrManager
    ]]

    probability = model.predict_proba(data)[0][1]

    return {
        "attrition_probability": round(float(probability), 2),
        "risk_score": risk_score(probability),
        "recommendations": retention_recommendation(probability)
    }


@app.get("/department_insights")
def department_insights():

    return {
        "Human Resources": 19.05,
        "Research & Development": 13.84,
        "Sales": 20.63
    }


@app.get("/employee_dashboard")
def employee_dashboard():

    return {
        "total_employees": 1470,
        "total_attritions": 237,
        "retention_rate": 83.88,
        "highest_risk_department": "Sales"
    }

@app.post("/employee_risk_score")
def employee_risk(employee: EmployeeData):

    data = [[
        employee.Age,
        employee.BusinessTravel,
        employee.DailyRate,
        employee.Department,
        employee.DistanceFromHome,
        employee.Education,
        employee.EducationField,
        employee.EnvironmentSatisfaction,
        employee.Gender,
        employee.HourlyRate,
        employee.JobInvolvement,
        employee.JobLevel,
        employee.JobRole,
        employee.JobSatisfaction,
        employee.MaritalStatus,
        employee.MonthlyIncome,
        employee.MonthlyRate,
        employee.NumCompaniesWorked,
        employee.OverTime,
        employee.PercentSalaryHike,
        employee.PerformanceRating,
        employee.RelationshipSatisfaction,
        employee.StockOptionLevel,
        employee.TotalWorkingYears,
        employee.TrainingTimesLastYear,
        employee.WorkLifeBalance,
        employee.YearsAtCompany,
        employee.YearsInCurrentRole,
        employee.YearsSinceLastPromotion,
        employee.YearsWithCurrManager
    ]]

    probability = model.predict_proba(data)[0][1]

    return {
        "attrition_probability": round(float(probability), 2),
        "risk_score": risk_score(probability)
    }


@app.post("/shap_explanation")
def shap_explanation(employee: EmployeeData):

    data = [[
        employee.Age,
        employee.BusinessTravel,
        employee.DailyRate,
        employee.Department,
        employee.DistanceFromHome,
        employee.Education,
        employee.EducationField,
        employee.EnvironmentSatisfaction,
        employee.Gender,
        employee.HourlyRate,
        employee.JobInvolvement,
        employee.JobLevel,
        employee.JobRole,
        employee.JobSatisfaction,
        employee.MaritalStatus,
        employee.MonthlyIncome,
        employee.MonthlyRate,
        employee.NumCompaniesWorked,
        employee.OverTime,
        employee.PercentSalaryHike,
        employee.PerformanceRating,
        employee.RelationshipSatisfaction,
        employee.StockOptionLevel,
        employee.TotalWorkingYears,
        employee.TrainingTimesLastYear,
        employee.WorkLifeBalance,
        employee.YearsAtCompany,
        employee.YearsInCurrentRole,
        employee.YearsSinceLastPromotion,
        employee.YearsWithCurrManager
    ]]

    data = np.array(data)

    shap_values = explainer.shap_values(data)

    print("TYPE:", type(shap_values))

    try:
      print("SHAPE:", shap_values.shape)
    except:
      print("LEN:", len(shap_values))

    feature_names = [
        "Age",
        "BusinessTravel",
        "DailyRate",
        "Department",
        "DistanceFromHome",
        "Education",
        "EducationField",
        "EnvironmentSatisfaction",
        "Gender",
        "HourlyRate",
        "JobInvolvement",
        "JobLevel",
        "JobRole",
        "JobSatisfaction",
        "MaritalStatus",
        "MonthlyIncome",
        "MonthlyRate",
        "NumCompaniesWorked",
        "OverTime",
        "PercentSalaryHike",
        "PerformanceRating",
        "RelationshipSatisfaction",
        "StockOptionLevel",
        "TotalWorkingYears",
        "TrainingTimesLastYear",
        "WorkLifeBalance",
        "YearsAtCompany",
        "YearsInCurrentRole",
        "YearsSinceLastPromotion",
        "YearsWithCurrManager"
    ]


    feature_importance = np.abs(shap_values[0, :, 1])

    top_indices = np.argsort(feature_importance)[-5:][::-1]

    top_features = []

    for idx in top_indices:
        top_features.append({
            "feature": feature_names[idx],
            "impact": round(float(feature_importance[idx]), 4)
        })

    return {
        "top_factors": top_features
    }