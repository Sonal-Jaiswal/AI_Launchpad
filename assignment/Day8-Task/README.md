# Employee Skill Analyzer

A Streamlit application that uses LangChain, OpenAI, and Pydantic to identify the
skills needed to move from a current role to a target role.

## Setup

From this directory, install the dependencies:

```powershell
py -m pip install -r requirements.txt
```

Copy `.env.example` to `.env` and set `OPENAI_API_KEY`. Keep the `.env` file local.
`OPENAI_BASE_URL` can be changed when using an OpenAI-compatible endpoint.

Run the application:

```powershell
streamlit run streamlit_app.py
```

## Project structure

- `streamlit_app.py` - Streamlit page orchestration and error handling
- `components/models.py` - Pydantic response model and validation
- `components/prompts.py` - Career coach system prompt
- `components/llm_service.py` - LangChain and OpenAI integration
- `components/input_form.py` - Career transition input form
- `components/results.py` - Analysis result rendering

## Example input

> I am currently working as a Python Developer and I want to become an AI Engineer
> in the next year.

## Example output

- Current role: Python Developer
- Target role: AI Engineer
- Top skills: Python for AI, machine learning, deep learning, LLM application development, and MLOps
- Skill gap analysis: An explanation of the difference between application development experience and production AI engineering capability
- Learning roadmap: A practical sequence covering foundations, projects, deployment, and portfolio evidence