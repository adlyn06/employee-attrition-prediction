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
<h2> Department Analytics</h2>
</div>
""", unsafe_allow_html=True)

response = requests.get(
    "http://127.0.0.1:8000/department_insights"
)

data = response.json()

df = pd.DataFrame(
    list(data.items()),
    columns=["Department", "Attrition Rate"]
)

st.markdown("###  Department Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Departments",
        len(df)
    )

with col2:
    st.metric(
        "Highest Attrition",
        round(df["Attrition Rate"].max(), 2)
    )

with col3:
    st.metric(
        "Average Attrition",
        round(df["Attrition Rate"].mean(), 2)
    )

st.markdown("---")

chart_col1, chart_col2 = st.columns(2)

with chart_col1:

    fig_bar = px.bar(
        df,
        x="Department",
        y="Attrition Rate",
        title="Department-wise Attrition Rate"
    )

    st.plotly_chart(
        fig_bar,
        use_container_width=True
    )

with chart_col2:

    fig_pie = px.pie(
        df,
        names="Department",
        values="Attrition Rate",
        title="Attrition Distribution"
    )

    st.plotly_chart(
        fig_pie,
        use_container_width=True
    )

st.markdown("---")

st.subheader(" Department Data")

st.dataframe(
    df,
    use_container_width=True
)