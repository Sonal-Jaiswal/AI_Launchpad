# Day 5: Object-Oriented Programming

This folder introduces object-oriented programming (OOP): modeling data and behavior together in classes and objects.

## Learning Goals

- Define classes and create objects.
- Initialize object state with `__init__`.
- Write instance methods using `self`.
- Understand encapsulation, inheritance, polymorphism, and composition.
- Choose OOP when it makes a domain easier to model.

## Class and Object

A class is a blueprint; an object is an instance of that blueprint:

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

account = BankAccount("Sonal", 1000)
account.deposit(250)
```

`self` refers to the current object. Each object has its own instance attributes.

## Encapsulation

Keep state changes behind methods that enforce rules:

```python
class InventoryItem:
    def __init__(self, stock):
        self._stock = stock

    def sell(self, quantity):
        if quantity > self._stock:
            raise ValueError("Not enough stock")
        self._stock -= quantity
```

A leading underscore communicates that an attribute is internal. It is a convention, not strict privacy.

## Inheritance and Polymorphism

Inheritance creates a specialized class from a base class:

```python
class Employee:
    def calculate_bonus(self):
        return 0

class Manager(Employee):
    def calculate_bonus(self):
        return 10000
```

Both objects respond to `calculate_bonus`, but their behavior differs. This is polymorphism.

## Composition

Composition means one object contains another object. It is often easier to change than a deep inheritance tree:

```python
class Engine:
    def start(self):
        return "started"

class Car:
    def __init__(self):
        self.engine = Engine()
```

## File Guide

| File | Practice |
| --- | --- |
| `oop_examples.py` | Classes, attributes, methods, and object behavior |

## Important Differences

- Class: definition or blueprint; object: concrete instance.
- Instance attribute: belongs to one object; class attribute: shared by the class.
- Inheritance models an “is-a” relationship; composition models a “has-a” relationship.
- Encapsulation protects rules around state; abstraction hides unnecessary implementation detail.

## Design Checklist

Create a class when the program has entities with both state and behavior. Keep methods small, validate state changes, and avoid classes that only group unrelated functions.

## Exercises

1. Add `withdraw()` with insufficient-balance validation.
2. Create `Student` and `Course` classes.
3. Use a class property to count created objects.
4. Compare an inheritance solution with a composition solution.
5. Add `__str__` for readable object output.

## Interview Check

**What is `__init__`?** An initializer called when an object is created; it commonly sets instance attributes.

**What is polymorphism?** Different object types responding to the same operation according to their own implementation.

**Why prefer composition sometimes?** It reduces tight coupling and allows behavior to be assembled from smaller objects.
