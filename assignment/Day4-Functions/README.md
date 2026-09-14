# Day 4: Functions

This folder converts repeated logic into reusable functions and builds a shopping-bill workflow from smaller steps.

## Learning Goals

- Define and call functions.
- Pass positional and keyword arguments.
- Return values instead of printing from every function.
- Use local scope and default parameters.
- Break a larger program into testable units.

## Basic Function

```python
def calculate_total(price, quantity):
    return price * quantity

amount = calculate_total(250, 3)
```

A function should usually do one clear job. Returning a value makes the function reusable by a CLI, Streamlit app, test, or API.

## Parameters and Arguments

```python
def greet(name, message="Welcome"):
    return f"{message}, {name}!"

greet("Sonal")
greet(name="Sonal", message="Hello")
```

Default parameters make optional behavior explicit. Avoid mutable defaults such as `items=[]`.

## Scope

Variables created inside a function are local by default:

```python
def add_tax(amount, rate):
    tax = amount * rate
    return amount + tax
```

Prefer passing data into functions rather than depending on global variables.

## File Guide

| File | Practice |
| --- | --- |
| `day1_functions.py` | Dictionary access and reusable calculation ideas |
| `shopping_bill_functions.py` | Input, item collection, GST, rewards, and JSON-ready bill data |

## The Shopping-Bill Flow

```text
collect customer -> collect items -> calculate subtotal -> add GST -> calculate reward -> print bill
```

The bill program uses a dictionary for the bill and nested dictionaries for item details. `sum()` with a generator expression calculates the subtotal.

## Important Differences

- `print()` displays a result; `return` makes a result available to the caller.
- A parameter is the name in a function definition; an argument is the value passed to it.
- Local variables belong to a function call; global variables belong to the module.
- A pure function depends only on its inputs and has no side effects; `input()` and `print()` are side effects.

## Better Design Exercise

Refactor the shopping bill into:

```python
def collect_items(): ...
def calculate_subtotal(items): ...
def calculate_reward(total): ...
def build_bill(customer, items, gst_rate): ...
def display_bill(bill): ...
```

This makes each rule easier to test and change.

## Exercises

1. Add a reusable `calculate_gst(amount, rate)` function.
2. Return the bill dictionary instead of printing inside the calculation code.
3. Validate that price and quantity are not negative.
4. Write tests for reward thresholds.
5. Export the final bill as JSON.

## Interview Check

**Why use functions?** They reduce duplication, isolate logic, improve readability, and make testing easier.

**What is a side effect?** A change outside a function's returned value, such as printing, reading input, writing a file, or changing global state.
