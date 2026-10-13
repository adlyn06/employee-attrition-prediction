import streamlit as st
import requests
import pandas as pd

st.markdown("""
<div style="
padding:20px;
border-radius:12px;
background:linear-gradient(90deg,#7C3AED,#A855F7);
color:white;
text-align:center;
margin-bottom:20px;
">
<h2> HR Report </h2>
</div>
""", unsafe_allow_html=True)

dashboard_response = requests.get(
    "http://127.0.0.1:8000/employee_dashboard"
)

department_response = requests.get(
    "http://127.0.0.1:8000/department_insights"
)

dashboard = dashboard_response.json()
department_data = department_response.json()

st.info(
    f" Organization currently has {dashboard['total_employees']} employees with "
    f"{dashboard['total_attritions']} attritions recorded."
)

st.markdown("###  Key HR Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        " Employees",
        dashboard["total_employees"]
    )

with col2:
    st.metric(
        " Attritions",
        dashboard["total_attritions"]
    )

with col3:
    st.metric(
        " Retention %",
        f"{dashboard['retention_rate']}%"
    )

with col4:
    st.metric(
        " High Risk Dept",
        dashboard["highest_risk_department"]
    )

st.markdown("---")

st.subheader(" Organization Summary")

report_df = pd.DataFrame({
    "Metric": [
        "Total Employees",
        "Total Attritions",
        "Retention Rate (%)",
        "Highest Risk Department"
    ],
    "Value": [
        dashboard["total_employees"],
        dashboard["total_attritions"],
        dashboard["retention_rate"],
        dashboard["highest_risk_department"]
    ]
})

st.table(report_df)

st.markdown("---")

st.subheader(" Department Attrition Report")

dept_df = pd.DataFrame(
    list(department_data.items()),
    columns=["Department", "Attrition Rate"]
)

st.dataframe(
    dept_df,
    use_container_width=True
)

st.download_button(
    label=" Download Department Report",
    data=dept_df.to_csv(index=False),
    file_name="department_attrition_report.csv",
    mime="text/csv"
)

