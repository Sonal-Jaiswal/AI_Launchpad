import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Student Result Management System",
    page_icon="🎓",
    layout="wide"
)

# -------------------------------------------------
# CSS
# -------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.title {
    text-align:center;
    padding:20px;
    border-radius:15px;
    color:white;
    background: linear-gradient(90deg,#4A00E0,#8E2DE2);
    margin-bottom:20px;
}

.metric-box{
    background:linear-gradient(135deg,#11998e,#38ef7d);
    color:white;
    padding:20px;
    border-radius:15px;
    text-align:center;
    font-size:20px;
    font-weight:bold;
}

.stButton>button{
    width:100%;
    background:#4A00E0;
    color:white;
    border-radius:10px;
}

.stButton>button:hover{
    background:#8E2DE2;
    transition:0.4s;
    transform:scale(1.03);
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Title
# -------------------------------------------------

st.markdown("""
<div class='title'>
<h1>🎓 Student Result Management System</h1>
<p>Python | SQL | Power BI Performance Dashboard</p>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Session State
# -------------------------------------------------

if "students" not in st.session_state:
    st.session_state.students = []

# -------------------------------------------------
# Sidebar Input
# -------------------------------------------------

st.sidebar.header("➕ Add Student")

name = st.sidebar.text_input("Student Name")

python_marks = st.sidebar.number_input(
    "Python Marks",
    min_value=0.0,
    max_value=100.0
)

sql_marks = st.sidebar.number_input(
    "SQL Marks",
    min_value=0.0,
    max_value=100.0
)

powerbi_marks = st.sidebar.number_input(
    "Power BI Marks",
    min_value=0.0,
    max_value=100.0
)

attendance = st.sidebar.number_input(
    "Attendance %",
    min_value=0.0,
    max_value=100.0
)

# -------------------------------------------------
# Add Student
# -------------------------------------------------

if st.sidebar.button("Add Student"):

    total = python_marks + sql_marks + powerbi_marks
    average = total / 3

    passed = (
        python_marks >= 40 and
        sql_marks >= 40 and
        powerbi_marks >= 40 and
        attendance >= 75
    )

    if not passed:
        grade = "F"
    elif average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "D"

    scholarship = (
        passed and
        average >= 85 and
        attendance >= 90
    )

    st.session_state.students.append({
        "Name": name,
        "Python": python_marks,
        "SQL": sql_marks,
        "Power BI": powerbi_marks,
        "Attendance": attendance,
        "Total": total,
        "Average": round(average, 2),
        "Result": "Pass" if passed else "Fail",
        "Grade": grade,
        "Scholarship": "Yes" if scholarship else "No"
    })

    st.success("Student Added Successfully ✅")

# -------------------------------------------------
# Report
# -------------------------------------------------

if st.session_state.students:

    df = pd.DataFrame(st.session_state.students)

    st.subheader("📋 Student Result Report")

    st.dataframe(df, use_container_width=True)

    total_students = len(df)
    passed_count = len(df[df["Result"] == "Pass"])
    failed_count = len(df[df["Result"] == "Fail"])

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"<div class='metric-box'>👨‍🎓 Students<br>{total_students}</div>",
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"<div class='metric-box'>✅ Passed<br>{passed_count}</div>",
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"<div class='metric-box'>❌ Failed<br>{failed_count}</div>",
            unsafe_allow_html=True
        )

    # ---------------------------------------------
    # List Comprehensions
    # ---------------------------------------------

    passed_students = [
        s["Name"]
        for s in st.session_state.students
        if s["Result"] == "Pass"
    ]

    failed_students = [
        s["Name"]
        for s in st.session_state.students
        if s["Result"] == "Fail"
    ]

    scholarship_students = [
        s["Name"]
        for s in st.session_state.students
        if s["Scholarship"] == "Yes"
    ]

    st.subheader("📌 Student Lists")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.success(f"Passed Students\n\n{passed_students}")

    with c2:
        st.error(f"Failed Students\n\n{failed_students}")

    with c3:
        st.info(f"Scholarship Students\n\n{scholarship_students}")

    # ---------------------------------------------
    # Charts
    # ---------------------------------------------

    st.subheader("📊 Result Analysis")

    result_counts = df["Result"].value_counts()

    st.bar_chart(result_counts)

    st.subheader("🎯 Grade Distribution")

    grade_counts = df["Grade"].value_counts()

    st.bar_chart(grade_counts)

    st.subheader("📚 Subject Performance")

    subject_df = df[["Python", "SQL", "Power BI"]]

    st.line_chart(subject_df)

else:
    st.info("Add student records from the sidebar to generate report.")