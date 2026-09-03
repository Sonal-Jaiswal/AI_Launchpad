# Python Foundations

A day-by-day Python learning repository covering core Python, data structures, application exercises, validation, and LLM application foundations.

## Learning path

| Day | Topic | Folder |
| --- | --- | --- |
| 1 | Python Basics | `assignment/Day1-Python-Basics` |
| 2 | Lists and Tuples | `assignment/Day2-Lists-and-Tuples` |
| 3 | Dictionaries and Sets | `assignment/Day3-Dictionaries-and-Sets` |
| 4 | Functions | `assignment/Day4-Functions` |
| 5 | OOP | `assignment/Day5-OOP` |
| 6 | Pydantic | `assignment/Day6-Pydantic` |
| 7 | LangChain | `assignment/Day7-LangChain` |

The Day 3 folder also contains Streamlit exercises that apply Python data structures in small interactive applications.

## Setup

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
```

Run a Streamlit exercise with:

```powershell
streamlit run assignment\Day3-Dictionaries-and-Sets\student_result_app.py
```

Keep API keys and other local configuration in `.env`; environment files and virtual environments are intentionally ignored by Git.

## Commit history

The repository includes `commit-learning-days.ps1`, which creates one dated commit for each learning day and pushes the result to `origin`.
