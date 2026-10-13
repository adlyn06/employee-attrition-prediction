import streamlit as st
import requests

st.set_page_config(
    page_title="Employee Attrition Prediction System",
    # page_icon="📊",
    layout="wide"
)

# st.title(" Employee Attrition Prediction System")
st.markdown("""
<div style="
background-color:#1E3A8A;
padding:15px;
border-radius:8px;
margin-bottom:20px;
">
<h2 style="
color:white;
text-align:center;
margin:0;
">
 Employee Attrition Prediction System
</h2>
</div>
""", unsafe_allow_html=True)

st.markdown("""
### HR Analytics Dashboard

Predict employee resignation risk, identify high-risk employees,
and generate retention recommendations using Machine Learning.
""")

st.markdown("---")

st.header(" Employee Details")

col1, col2, col3, col4 = st.columns(4)

with col1:
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=65,
        value=30
    )

    business_travel = st.number_input(
        "Business Travel",
        value=0
    )

with col2:
    department_name = st.selectbox(
        "Department",
        [
            "Human Resources",
            "Research & Development",
            "Sales"
        ]
    )

    overtime = st.selectbox(
        "OverTime",
        ["No", "Yes"]
    )

    overtime_value = 1 if overtime == "Yes" else 0

with col3:
    monthly_income = st.number_input(
        "Monthly Income",
        min_value=1000,
        max_value=50000,
        value=6000
    )

    work_life_balance = st.slider(
        "Work Life Balance",
        min_value=1,
        max_value=4,
        value=3
    )

with col4:
    num_companies_worked = st.number_input(
        "Companies Worked",
        min_value=0,
        max_value=20,
        value=2
    )

department_map = {
    "Human Resources": 0,
    "Research & Development": 1,
    "Sales": 2
}

department = department_map[department_name]

st.markdown("")

if st.button(" Predict Attrition"):

    data = {
    "Age": age,
    "BusinessTravel": 0,
    "DailyRate": 1000,

    "Department": department,
    "DistanceFromHome": 1,
    "Education": 2,
    "EducationField": 1,
    "EnvironmentSatisfaction": 2,
    "Gender": 0,
    "HourlyRate": 94,
    "JobInvolvement": 3,
    "JobLevel": 2,
    "JobRole": 7,
    "JobSatisfaction": 4,
    "MaritalStatus": 1,

    "MonthlyIncome": monthly_income,
    "MonthlyRate": 19479,

    "NumCompaniesWorked": num_companies_worked,

    "OverTime": overtime_value,

    "PercentSalaryHike": 11,
    "PerformanceRating": 3,
    "RelationshipSatisfaction": 1,
    "StockOptionLevel": 0,
    "TotalWorkingYears": 8,
    "TrainingTimesLastYear": 0,

    "WorkLifeBalance": work_life_balance,

    "YearsAtCompany": 6,
    "YearsInCurrentRole": 4,
    "YearsSinceLastPromotion": 0,
    "YearsWithCurrManager": 5
   }
    response = requests.post(
        "http://127.0.0.1:8000/predict_attrition",
        json=data
    )

    result = response.json()

    st.markdown("### Prediction Results")

    prediction = (
    "Likely to Leave"
    if result["attrition_probability"] >= 0.5
    else "Likely to Stay"
)

    c1, c2, c3 = st.columns(3)

    c1.metric(
    "Prediction",
    prediction
)

    c2.metric(
    "Attrition Probability",
    f"{result['attrition_probability']:.2f}"
)

    c3.metric(
    "Risk Score",
    result["risk_score"]
)

    recommendation_response = requests.post(
        "http://127.0.0.1:8000/retention_recommendations",
        json=data
    )

    recommendation_result = recommendation_response.json()

    st.markdown("###  Retention Recommendations")

    for recommendation in recommendation_result["recommendations"]:
        st.write( recommendation)

st.markdown("---")

st.header(" Department Insights")

if st.button(" Show Department Insights"):

    response = requests.get(
        "http://127.0.0.1:8000/department_insights"
    )

    data = response.json()

    import pandas as pd
    import plotly.express as px

    df = pd.DataFrame(
        list(data.items()),
        columns=["Department", "Attrition Rate"]
    )

    fig = px.bar(
        df,
        x="Department",
        y="Attrition Rate",
        title="Department-wise Attrition Rate"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.markdown("---")

st.header(" HR Dashboard")

if st.button(" Show Dashboard"):

    response = requests.get(
        "http://127.0.0.1:8000/employee_dashboard"
    )

    dashboard = response.json()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Employees",
        dashboard["total_employees"]
    )

    col2.metric(
        "Attritions",
        dashboard["total_attritions"]
    )

    col3.metric(
        "Retention %",
        dashboard["retention_rate"]
    )

    col4.metric(
        "High Risk Dept",
        dashboard["highest_risk_department"]
    )