"""Employee Skill Analyzer Streamlit entry point."""

import streamlit as st

from components.input_form import render_input_form
from components.llm_service import analyze_skills
from components.results import render_analysis


st.set_page_config(
    page_title="Employee Skill Analyzer",
    page_icon="🎯",
    layout="centered",
)

st.title("Employee Skill Analyzer 🎯")
st.write(
    "Turn your career goal into a focused skill plan with an AI career coach."
)

employee_context, submitted = render_input_form()

if submitted:
    if not employee_context.strip():
        st.warning("⚠️ Add a description of your current and target role first.")
    else:
        with st.spinner("Analyzing your career transition..."):
            try:
                result = analyze_skills(employee_context.strip())
            except Exception as error:
                st.error(
                    "❌ The analysis could not be completed. "
                    "Check your API settings and try again."
                )
                st.caption(f"Technical detail: {error}")
            else:
                render_analysis(result)
