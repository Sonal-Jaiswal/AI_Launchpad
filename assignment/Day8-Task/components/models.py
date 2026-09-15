"""Pydantic models used by the Employee Skill Analyzer."""

from typing import List

from pydantic import BaseModel, Field, field_validator


class SkillAnalysis(BaseModel):
    """Validated career analysis returned by the language model."""

    current_role: str = Field(description="The employee's current role")
    target_role: str = Field(description="The role the employee wants to reach")
    top_5_skills: List[str] = Field(
        min_length=5,
        max_length=5,
        description="Exactly five important skills for the target role",
    )
    skill_gap: str = Field(description="A practical explanation of the skill gap")
    learning_roadmap: str = Field(
        description="A step-by-step roadmap for closing the skill gap"
    )

    @field_validator("learning_roadmap", mode="before")
    @classmethod
    def normalize_learning_roadmap(cls, roadmap: object) -> str:
        """Accept either a formatted string or a list of roadmap steps."""
        if isinstance(roadmap, list):
            return "\n".join(
                f"{index}. {step}" for index, step in enumerate(roadmap, start=1)
            )
        if isinstance(roadmap, str):
            return roadmap.strip()
        raise ValueError("The learning roadmap must be text or a list of steps.")

    @field_validator("top_5_skills")
    @classmethod
    def validate_skill_count(cls, skills: List[str]) -> List[str]:
        """Keep the output contract strict even if the model over-generates."""
        cleaned_skills = [skill.strip() for skill in skills if skill.strip()]
        if len(cleaned_skills) != 5:
            raise ValueError("The analysis must contain exactly five skills.")
        return cleaned_skills
