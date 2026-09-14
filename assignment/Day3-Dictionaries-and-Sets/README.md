# Day 3: Dictionaries, Sets, and Streamlit Applications

This folder applies dictionaries and sets to interactive Streamlit programs for students, inventory, expenses, and ration-card benefits.

## Learning Goals

- Store key-value data with dictionaries.
- Use nested dictionaries for real-world records.
- Use sets for uniqueness and membership checks.
- Build simple Streamlit interfaces.
- Separate user input, calculation, and display.

## Dictionaries

A dictionary maps a key to a value:

```python
student = {"name": "Sonal", "marks": 88}
student["grade"] = "A"
print(student.get("name"))
```

Useful operations include `keys()`, `values()`, `items()`, `get()`, `update()`, and `pop()`.

Nested data models a record:

```python
inventory = {
    "laptop": {"price": 65000, "stock": 4},
    "mouse": {"price": 800, "stock": 20},
}
```

## Sets

A set stores unique values and supports fast membership checks:

```python
skills = {"Python", "SQL", "Python"}
print(skills)  # Python appears once
print("SQL" in skills)
```

Set operators include union `|`, intersection `&`, difference `-`, and symmetric difference `^`.

## Streamlit Basics

The application files use common Streamlit building blocks:

```python
import streamlit as st

st.title("Inventory")
name = st.text_input("Product name")
if st.button("Save"):
    st.success(f"Saved {name}")
```

Run an application from this folder:

```powershell
streamlit run student_result_app.py
```

The browser interface reruns the Python script when a widget changes. Use `st.session_state` when values must survive reruns.

## File Guide

| File | Practice |
| --- | --- |
| `student_result_app.py` | Student results and interactive display |
| `inventory_app.py` | Stock and inventory management |
| `expense_app.py` | Expense tracking and totals |
| `ration_card_app.py` | Benefit eligibility and records |

## Important Differences

- Dictionary: key-value lookup; keys must be unique.
- Set: unique values without reliable positional indexing.
- List: ordered values that may repeat.
- `st.write()` displays general values; `st.table()` displays tabular data; `st.metric()` highlights a number.

## Exercises

1. Add a search box to the inventory application.
2. Show expenses grouped by category.
3. Add validation for empty names and negative amounts.
4. Use a set to show unique student subjects.
5. Store form submissions in `st.session_state`.

## Interview Check

**When should you use a dictionary?** When values are naturally accessed by meaningful keys.

**Why does Streamlit rerun?** Its simple execution model reruns the script after interaction so the UI reflects current widget values.
