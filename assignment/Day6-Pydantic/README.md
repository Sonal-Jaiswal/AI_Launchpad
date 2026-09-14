# Day 6: Pydantic

This folder is prepared for data validation with Pydantic. Pydantic models turn untrusted input, such as form data or API payloads, into validated Python objects.

## Learning Goals

- Define schemas with `BaseModel`.
- Validate required fields and types.
- Use field constraints and custom validators.
- Understand the difference between parsing and business validation.
- Serialize validated models for APIs and storage.

## Basic Model

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str
    age: int = Field(ge=0, le=120)
    email: str

user = User(name="Sonal", age=25, email="sonal@example.com")
print(user.model_dump())
```

Pydantic validates the input when the model is created. Invalid data raises a `ValidationError` with details that an API or form can display.

## Nested Models

```python
class Address(BaseModel):
    city: str

class Customer(BaseModel):
    name: str
    address: Address
```

Nested models make the expected shape of structured data explicit.

## Field and Model Validation

Use field constraints for one value and a model validator when multiple fields must agree:

```python
from pydantic import BaseModel, model_validator

class PasswordForm(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def passwords_match(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self
```

Prefer `mode="after"` when you want to compare already parsed fields. Use `mode="before"` when the raw input shape must be normalized first.

## Serialization

```python
payload = user.model_dump()
json_text = user.model_dump_json()
```

Use `model_dump()` for a Python dictionary and `model_dump_json()` for JSON text.

## Why Validation Matters

Input can come from users, files, APIs, databases, or LLM responses. Type hints document intent but do not validate runtime data. Pydantic creates an executable boundary between untrusted input and application logic.

## Common Differences

- Type hint: documentation and static analysis; Pydantic model: runtime validation.
- Parsing: converting input into expected types; validation: rejecting values that violate rules.
- Field validator: validates one field; model validator: validates relationships between fields.
- `model_dump()`: Python dictionary; `model_dump_json()`: JSON string.

## Exercises

1. Create a `Product` model with positive price and non-negative stock.
2. Validate an email and a phone number.
3. Create an `Order` containing a list of products.
4. Add a model validator that checks total price.
5. Validate a chatbot response using a structured Pydantic model.

## Interview Check

**Why use Pydantic?** It validates and parses external data while producing clear, structured errors.

**Does Pydantic replace business logic?** No. It validates data shape and rules; larger workflows still need explicit application logic.

**What happens on invalid input?** Model creation raises `ValidationError`, which includes the failing field and reason.
