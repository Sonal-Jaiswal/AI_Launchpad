"""Result rendering components for the Streamlit page."""

import streamlit as st

from components.models import SkillAnalysis


def render_analysis(analysis: SkillAnalysis) -> None:
    """Render the validated analysis in a readable Streamlit layout."""
    st.success("✅ Analysis complete. Your transition plan is ready.")

    role_columns = st.columns(2)
    with role_columns[0]:
        st.metric("Current role", analysis.current_role)
    with role_columns[1]:
        st.metric("Target role", analysis.target_role)

    st.subheader("🎯 Top 5 skills")
    with st.container(border=True):
        for skill in analysis.top_5_skills:
            st.markdown(f"- {skill}")

    st.subheader("🧩 Skill gap analysis")
    with st.container(border=True):
        st.write(analysis.skill_gap)

    st.subheader("🗺️ Learning roadmap")
    with st.container(border=True):
        st.markdown(analysis.learning_roadmap)
