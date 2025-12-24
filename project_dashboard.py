



import streamlit as st
import matplotlib.pyplot as plt
from project_dashboard import Project, Task, Risk, Resource

st.set_page_config(page_title="PM Dashboard", layout="wide")

st.title("📊 Project Management Dashboard")

# Create Project
project = Project("African Arab Bank System")

# Sample Data
project.add_task(Task("Requirements", "Ahmed", "2025-03-20", "Completed"))
project.add_task(Task("Development", "Sara", "2025-04-10", "Pending"))

project.add_risk(Risk("Delay Risk", 4, 3, "Add buffer time"))
project.add_risk(Risk("Budget Risk", 3, 2, "Weekly monitoring"))

project.add_resource(Resource("Ahmed", "Analyst", 40))
project.add_resource(Resource("Sara", "Developer", 35))

# KPIs
col1, col2, col3 = st.columns(3)

col1.metric("Completed Tasks", project.completed_tasks_count())
col2.metric("Pending Tasks", project.pending_tasks_count())
col3.metric("Overall Risk Score", round(project.overall_risk_score(), 2))

# Tasks Chart
st.subheader("📌 Tasks Status")
fig1 = plt.figure()
plt.bar(
    ["Completed", "Pending"],
    [project.completed_tasks_count(), project.pending_tasks_count()]
)
plt.ylabel("Count")
st.pyplot(fig1)

# Risks Chart
st.subheader("⚠️ Risk Levels")
fig2 = plt.figure()
risk_names = [r.name for r in project.risks]
risk_scores = [r.risk_score() for r in project.risks]
plt.bar(risk_names, risk_scores, color="red")
plt.ylabel("Risk Score")
st.pyplot(fig2)

st.success("Dashboard Loaded Successfully 🚀")
