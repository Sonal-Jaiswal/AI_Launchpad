"""Input form component for the Streamlit page."""

import streamlit as st


def render_input_form() -> tuple[str, bool]:
    """Render the career transition form and return its input and submit state."""
    with st.form("skill_analysis_form", border=True):
        st.subheader("Describe your career transition")
        employee_context = st.text_area(
            "Employee context",
            placeholder=(
                "Example: I am currently working as a Python Developer and I want to "
                "become an AI Engineer in the next year."
            ),
            height=150,
            label_visibility="collapsed",
        )
        submitted = st.form_submit_button(
            "Analyze Skills",
            type="primary",
            icon=":material/analytics:",
            width="stretch",
        )
    return employee_context, submitted
