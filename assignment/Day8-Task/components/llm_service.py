"""LangChain service for generating employee skill analyses."""

import os
from typing import Any

import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from components.models import SkillAnalysis
from components.prompts import SYSTEM_PROMPT


load_dotenv()


@st.cache_resource
def get_analysis_chain() -> Any:
    """Create and cache the structured-output LLM chain."""
    api_key = os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("OPENAI_BASE_URL")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is missing. Add it to a .env file before analyzing."
        )

    model_kwargs: dict[str, Any] = {
        "model": os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        "temperature": 0.2,
        "api_key": api_key,
    }
    if base_url:
        model_kwargs["base_url"] = base_url

    llm = ChatOpenAI(**model_kwargs)
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM_PROMPT),
            ("human", "Employee context:\n{employee_context}"),
        ]
    )
    return prompt | llm.with_structured_output(SkillAnalysis, method="json_mode")


def analyze_skills(employee_context: str) -> SkillAnalysis:
    """Run the career analysis and return a validated Pydantic object."""
    analysis = get_analysis_chain().invoke({"employee_context": employee_context})

    if not isinstance(analysis, SkillAnalysis):
        analysis = SkillAnalysis.model_validate(analysis)
    return analysis
