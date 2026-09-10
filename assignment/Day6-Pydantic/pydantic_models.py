"""Small Pydantic model example for the Day 6 exercises."""

from pydantic import BaseModel, EmailStr


class Learner(BaseModel):
    name: str
    email: EmailStr
    age: int


if __name__ == "__main__":
    learner = Learner(name="Sonal", email="sonal@example.com", age=25)
    print(learner.model_dump())
