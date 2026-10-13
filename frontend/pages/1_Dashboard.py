# import streamlit as st
# import requests

# st.title("Dashboard")

# response = requests.get(
#     "http://127.0.0.1:8000/employee_dashboard"
# )

# dashboard = response.json()

# col1, col2, col3, col4 = st.columns(4)

# col1.metric(
#     "Employees",
#     dashboard["total_employees"]
# )

# col2.metric(
#     "Attritions",
#     dashboard["total_attritions"]
# )

# col3.metric(
#     "Retention %",
#     dashboard["retention_rate"]
# )

# col4.metric(
#     "High Risk Dept",
#     dashboard["highest_risk_department"]
# )

# import streamlit as st
# import requests
# import pandas as pd
# import plotly.express as px

# # st.title("📊 HR Analytics Dashboard")

# st.markdown("""
# <div style="
# padding:20px;
# border-radius:10px;
# background-color:#1E3A8A;
# color:white;
# margin-bottom:20px;
# ">
# <h2>📊 HR Analytics Dashboard</h2>

# </div>
# """, unsafe_allow_html=True)

# response = requests.get(
#     "http://127.0.0.1:8000/employee_dashboard"
# )

# dashboard = response.json()

# col1, col2, col3, col4 = st.columns(4)

# with col1:
#     st.metric(
#         "👥 Employees",
#         dashboard["total_employees"]
#     )

# with col2:
#     st.metric(
#         "🚪 Attritions",
#         dashboard["total_attritions"]
#     )

# with col3:
#     st.metric(
#         "📈 Retention %",
#         f"{dashboard['retention_rate']}%"
#     )

# with col4:
#     st.metric(
#         "⚠️ High Risk Dept",
#         dashboard["highest_risk_department"]
#     )

# st.markdown("---")

# chart_col1, chart_col2 = st.columns(2)

# with chart_col1:

#     pie_df = pd.DataFrame({
#         "Status": ["Retained", "Attrition"],
#         "Count": [
#             dashboard["total_employees"] - dashboard["total_attritions"],
#             dashboard["total_attritions"]
#         ]
#     })

#     pie_fig = px.pie(
#         pie_df,
#         names="Status",
#         values="Count",
#         title="Employee Distribution"
#     )

#     st.plotly_chart(
#         pie_fig,
#         use_container_width=True
#     )

# with chart_col2:

#     bar_df = pd.DataFrame({
#         "Metric": ["Employees", "Attritions"],
#         "Count": [
#             dashboard["total_employees"],
#             dashboard["total_attritions"]
#         ]
#     })

#     bar_fig = px.bar(
#         bar_df,
#         x="Metric",
#         y="Count",
#         title="Workforce Overview"
#     )

#     st.plotly_chart(
#         bar_fig,
#         use_container_width=True
#     )

import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.markdown("""
<div style="
padding:20px;
border-radius:12px;
background:linear-gradient(90deg,#1E3A8A,#2563EB);
color:white;
text-align:center;
margin-bottom:20px;
">
<h2> HR Analytics Dashboard</h2>
</div>
""", unsafe_allow_html=True)

response = requests.get(
    "http://127.0.0.1:8000/employee_dashboard"
)

dashboard = response.json()

st.markdown("""
<style>
.kpi-card {
    border: 2px solid black;
    border-radius: 10px;
    height: 180px;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    text-align: center;
}

.kpi-title {
    font-size: 22px;
    font-weight: 600;
    margin-bottom: 20px;
}

.kpi-value {
    font-size: 32px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title"> Employees</div>
        <div class="kpi-value">{dashboard["total_employees"]}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title"> Attritions</div>
        <div class="kpi-value">{dashboard["total_attritions"]}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title"> Retention %</div>
        <div class="kpi-value">{dashboard["retention_rate"]}%</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title"> High Risk Dept</div>
        <div class="kpi-value">{dashboard["highest_risk_department"]}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

chart_col1, chart_col2 = st.columns(2)

with chart_col1:

    pie_df = pd.DataFrame({
        "Status": ["Retained", "Attrition"],
        "Count": [
            dashboard["total_employees"] - dashboard["total_attritions"],
            dashboard["total_attritions"]
        ]
    })

    pie_fig = px.pie(
        pie_df,
        names="Status",
        values="Count",
        title="Employee Distribution"
    )

    st.plotly_chart(
        pie_fig,
        use_container_width=True
    )

with chart_col2:

    bar_df = pd.DataFrame({
        "Metric": ["Employees", "Attritions"],
        "Count": [
            dashboard["total_employees"],
            dashboard["total_attritions"]
        ]
    })

    bar_fig = px.bar(
        bar_df,
        x="Metric",
        y="Count",
        title="Workforce Overview"
    )

    st.plotly_chart(
        bar_fig,
        use_container_width=True
    )

