import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="📊",
    layout="wide"
)

@st.cache_data
def load_data():
    df = pd.read_csv("online_vs_offline_learning_dataset.csv")
    return df

df = load_data()

col1, col2, col3, col4, col5, col6 = st.columns(6)

col1.metric("📊 Total Students", len(df))
col2.metric("📘 Subjects", df["Subject"].nunique())
col3.metric("🧠 Avg Study Hours", round(df["Study_Hours"].mean(), 2))
col4.metric("🎯 Avg Exam Score", round(df["Exam_Score"].mean(), 2))
col5.metric("🧩 Avg Focus", round(df["Focus_Level"].mean(), 2))
col6.metric("📈 Avg Retention", round(df["Retention_Score"].mean(), 2))

st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📚 Study Hours vs Exam Score")
    fig, ax = plt.subplots()
    ax.scatter(df["Study_Hours"], df["Exam_Score"])
    ax.set_xlabel("Study Hours")
    ax.set_ylabel("Exam Score")
    st.pyplot(fig)

with col2:
    st.subheader("🎓 Learning Mode Performance")
    mode_score = df.groupby("Learning_Mode")["Exam_Score"].mean()
    fig, ax = plt.subplots()
    mode_score.plot(kind="bar", ax=ax)
    ax.set_ylabel("Avg Exam Score")
    st.pyplot(fig)

with col3:
    st.subheader("📘 Subject-wise Performance")
    subject_score = df.groupby("Subject")["Exam_Score"].mean().sort_values()
    fig, ax = plt.subplots()
    subject_score.plot(kind="barh", ax=ax)
    st.pyplot(fig)

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🧠 Focus vs Exam Score")
    fig, ax = plt.subplots()
    ax.scatter(df["Focus_Level"], df["Exam_Score"])
    ax.set_xlabel("Focus Level")
    ax.set_ylabel("Exam Score")
    st.pyplot(fig)

with col2:
    st.subheader("📈 Retention vs Exam Score")
    fig, ax = plt.subplots()
    ax.scatter(df["Retention_Score"], df["Exam_Score"])
    ax.set_xlabel("Retention Score")
    ax.set_ylabel("Exam Score")
    st.pyplot(fig)

with col3:
    st.subheader("📊 Learning Mode Distribution")
    mode_count = df["Learning_Mode"].value_counts()
    fig, ax = plt.subplots()
    ax.pie(mode_count, labels=mode_count.index, autopct="%1.1f%%")
    st.pyplot(fig)

with st.expander("📄 View Dataset"):
    st.dataframe(df)

st.markdown("✅ Student Performance Analytics Dashboard using Streamlit")