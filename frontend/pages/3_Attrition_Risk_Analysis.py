import streamlit as st
import requests

st.markdown("""
<div style="
padding:20px;
border-radius:12px;
background:linear-gradient(90deg,#1E3A8A,#2563EB);
color:white;
text-align:center;
margin-bottom:20px;
">
<h2> Attrition Risk Analysis</h2>
</div>
""", unsafe_allow_html=True)

with st.expander("Employee Details", expanded=True):

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

    overtime = st.selectbox(
    "OverTime",
    ["No", "Yes"]
    )
    overtime_value = 1 if overtime == "Yes" else 0

    monthly_income = st.number_input(
    " Monthly Income",
    min_value=1000,
    max_value=50000,
    value=6000
   )
    
    work_life_balance = st.slider(
    " Work Life Balance",
    min_value=1,
    max_value=4,
    value=3
   )
    
    num_companies_worked = st.number_input(
    "Companies Worked",
    min_value=0,
    max_value=20,
    value=2
   )


    department_name = st.selectbox(
        "Department",
        [
            "Human Resources",
            "Research & Development",
            "Sales"
        ]
    )

department_map = {
    "Human Resources": 0,
    "Research & Development": 1,
    "Sales": 2
}

department = department_map[department_name]

if st.button(
    " Analyze Risk",
    use_container_width=True
):

    data = {
        "Age": age,
        "BusinessTravel": business_travel,
        "Department": department,
        "DailyRate": 1000,
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
        "MonthlyIncome":  monthly_income,
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
        "http://127.0.0.1:8000/employee_risk_score",
        json=data
    )

    result = response.json()

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            " Attrition Probability",
            result["attrition_probability"]
        )

    with col2:
        st.metric(
            " Risk Score",
            result["risk_score"]
        )

    risk = result["risk_score"]

    if risk == "Low":
        st.success("🟢 Employee is currently in the Low Risk category.")
    elif risk == "Medium":
        st.warning("🟠 Employee is currently in the Medium Risk category.")
    else:
        st.error("🔴 Employee is currently in the High Risk category.")