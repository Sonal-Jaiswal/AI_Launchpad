Prompt Engineering 
 
--------------------------------------------------------------
 
 
# Introduction to Prompt Engineering
 
---
 
# What is Prompt Engineering?
 
Prompt Engineering is the process of designing and optimizing instructions (prompts) given to a Large Language Model (LLM) to obtain accurate, relevant, and useful outputs.
 
Simple Definition:
 
```text
Prompt Engineering = Writing Better Instructions For AI
```
 
Examples:
 
Instead of:
 
```text
Write an email.
```
 
Use:
 
```text
Write a professional email to a manager requesting leave for 2 days due to a medical appointment.
```
 
Better Prompt → Better Response
 
---
 
# Why Prompt Engineering?
 
LLMs do not read minds.
 
They only understand:
 
```text
Prompt
      ↓
Interpretation
      ↓
Response
```
 
The quality of output depends heavily on the quality of the prompt.
 
Benefits:
 
1. More Accurate Responses
2. Reduced Hallucinations
3. Better Business Results
4. Improved Productivity
5. More Predictable Outputs
 
---
 
# What is a Prompt?
 
A Prompt is the input given to an LLM.
 
Examples:
 
Question:
 
```text
What is Python?
```
 
Instruction:
 
```text
Explain Python to a beginner.
```
 
Task:
 
```text
Summarize the following email.
```
 
---
 
# Components of a Good Prompt
 
A good prompt usually contains:
 
1. Role
2. Task
3. Context
4. Constraints
5. Output Format
 
Example:
 
```text
You are an HR Assistant.
 
Summarize the following employee feedback.
 
Keep summary under 100 words.
 
Return output in bullets.
```
 
---
 
# Prompt Engineering Fundamentals
 
## 1. Clear Instructions
 
Bad Prompt:
 
```text
Tell me about SQL.
```
 
Good Prompt:
 
```text
Explain SQL joins to a beginner with simple examples.
```
 
---
 
## 2. Provide Context
 
Bad Prompt:
 
```text
Draft an email.
```
 
Good Prompt:
 
```text
Draft an email to a trainer informing that today's Power BI session has been postponed.
```
 
---
 
## 3. Specify Output Format
 
Bad Prompt:
 
```text
Analyze sales data.
```
 
Good Prompt:
 
```text
Analyze sales data and return:
 
1. Top 3 insights
2. Risks
3. Recommendations
```
 
---
 
## 4. Define Constraints
 
Example:
 
```text
Summarize this document in less than 100 words.
```
 
---
 
# Prompt Engineering Techniques
 
---
 
# 1. Zero-Shot Prompting
 
No examples provided.
 
Prompt:
 
```text
Explain Python to a beginner.
```
 
Response generated directly.
 
---
 
# 2. One-Shot Prompting
 
One example provided.
 
Prompt:
 
```text
Example:
 
Question: Capital of India
Answer: New Delhi
 
Question: Capital of France
```
 
Output:
 
```text
Paris
```
 
---
 
# 3. Few-Shot Prompting
 
Multiple examples provided.
 
```text
Question: 2 + 2
Answer: 4
 
Question: 5 + 5
Answer: 10
 
Question: 10 + 10
```
 
Output:
 
```text
20
```
 
---
 
# 4. Role Prompting
 
Assign a role to LLM.
 
Prompt:
 
```text
You are a Senior HR Manager.
 
Draft a professional appraisal email.
```
 
---
 
# 5. Chain of Thought Prompting
 
Encourage step-by-step reasoning.
 
Bad Prompt:
 
```text
Calculate profit percentage.
```
 
Better Prompt:
 
```text
Calculate profit percentage.
 
Explain step by step.
```
 
---
 
# 6. Structured Output Prompting
 
Ask for output in a specific format.
 
Prompt:
 
```text
Analyze employee feedback.
 
Return output in JSON format.
```
 
---
 
# Business Use Cases of Prompt Engineering
 
---
 
# HR Use Case
 
Prompt:
 
```text
You are an HR Analyst.
 
Analyze the following employee feedback.
 
Return:
 
1. Positive Points
2. Negative Points
3. Suggested Actions
```
 
---
 
# Training Use Case
 
Prompt:
 
```text
You are a Learning Consultant.
 
Generate 10 SQL interview questions for freshers.
```
 
---
 
# Banking Use Case
 
Prompt:
 
```text
You are a Banking Assistant.
 
Explain home loan eligibility rules in simple language.
```
 
---
 
# Healthcare Use Case
 
Prompt:
 
```text
Summarize patient feedback into key concerns.
```
 
---
 
# Customer Support Use Case
 
Prompt:
 
```text
Classify support ticket as:
 
High
Medium
Low
```
 
---
 
# SAP Use Case
 
Prompt:
 
```text
Explain the business purpose of SAP Sales Order Processing.
```
 
---
 
# LLM Integration Architecture
 
---
 
# High Level Flow
 
```text
User
  ↓
Prompt
  ↓
LangChain
  ↓
OpenAI SDK
  ↓
OpenAI API
  ↓
Large Language Model
  ↓
Generated Response
  ↓
Python Application
  ↓
User
```
 
---
 
# What Happens Internally?
 
Step 1
 
User writes:
 
```text
Explain Python Functions.
```
 
Step 2
 
Python application sends prompt.
 
Step 3
 
LangChain formats request.
 
Step 4
 
OpenAI SDK calls OpenAI API.
 
Step 5
 
Prompt reaches LLM.
 
Step 6
 
Model predicts next tokens.
 
Step 7
 
Response generated.
 
Step 8
 
LangChain receives response.
 
Step 9
 
Python displays response.
 
---
 
# Installing Required Libraries
 
```python
pip install langchain
pip install langchain-openai
pip install openai
pip install python-dotenv
```
 
---
 
# Setting OpenAI API Key
 
Create:
 
```text
.env
```
 
File:
 
```text
OPENAI_API_KEY=YOUR_API_KEY
```
 
---
 
# First OpenAI Connection Using LangChain
 
```python
from dotenv import load_dotenv
 
from langchain_openai import ChatOpenAI
 
load_dotenv()
 
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)
 
response = llm.invoke(
    "Explain Python Functions."
)
 
print(response.content)
```
 
---
 
# Execution Flow of This Code
 
Step 1
 
```python
load_dotenv()
```
 
Loads API Key.
 
---
 
Step 2
 
```python
ChatOpenAI()
```
 
Creates LLM object.
 
---
 
Step 3
 
```python
llm.invoke()
```
 
Sends prompt.
 
---
 
Step 4
 
LangChain converts prompt into API request.
 
---
 
Step 5
 
OpenAI API receives request.
 
---
 
Step 6
 
LLM processes prompt.
 
---
 
Step 7
 
Response generated.
 
---
 
Step 8
 
Response returned to LangChain.
 
---
 
Step 9
 
Response displayed.
 
---
 
# Example 2 : Role Prompting
 
```python
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
 
load_dotenv()
 
llm = ChatOpenAI(
    model="gpt-4o-mini"
)
 
prompt = """
You are a Senior HR Manager.
 
Draft a professional leave approval email.
"""
 
response = llm.invoke(prompt)
 
print(response.content)
```
 
---
 
# Example 3 : Structured Output Prompt
 
```python
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
 
load_dotenv()
 
llm = ChatOpenAI(
    model="gpt-4o-mini"
)
 
prompt = """
Analyze the feedback:
 
"The trainer explained concepts very clearly but session timing was too long."
 
Return:
 
1. Positives
2. Negatives
3. Recommendations
"""
 
response = llm.invoke(prompt)
 
print(response.content)
```
 
---
 
# Example 4 : Few-Shot Prompting
 
```python
prompt = """
Question: 2 + 2
Answer: 4
 
Question: 5 + 5
Answer: 10
 
Question: 20 + 20
"""
```
 
---
 
# Example 5 : Chain of Thought Prompting
 
```python
prompt = """
A company earns 15000 and spends 10000.
 
Calculate profit.
 
Explain step by step.
"""
```
 
---
 
# Real Business Example
 
## Employee Travel Expense Claim Assistant
 
Prompt:
 
```text
You are an Expense Claim Auditor.
 
Validate the following travel claim.
 
Check:
 
1. Missing Receipt
2. Policy Violation
3. Duplicate Claim
4. Eligible Amount
 
Return findings in table format.
```
 
This is a real use case where Prompt Engineering directly affects business outcomes.
 
---
 
# Common Mistakes in Prompt Engineering
 
Bad Prompt:
 
```text
Explain.
```
 
Good Prompt:
 
```text
Explain Python Functions to freshers with 3 examples.
```
 
---
 
Bad Prompt:
 
```text
Analyze feedback.
```
 
Good Prompt:
 
```text
Analyze employee feedback and return strengths, concerns and recommendations.
```
 
---
 
# Practice Prompts
 
## Practice 1
 
```text
Explain Python Lists to a beginner.
```
 
---
 
## Practice 2
 
```text
You are a SQL Trainer.
 
Generate 10 beginner-level SQL questions.
```
 
---
 
## Practice 3
 
```text
Summarize the following meeting notes in 5 bullets.
```
 
---
 
## Practice 4
 
```text
Return employee feedback analysis in JSON format.
```
 
---
 
## Practice 5
 
```text
Explain the difference between Python List and Tuple with examples.
```
 
---
 
# Quick Revision
 
Prompt
 
```text
Instruction Given To LLM
```
 
Prompt Engineering
 
```text
Designing Better Prompts
```
 
Zero Shot
 
```text
No Example
```
 
One Shot
 
```text
One Example
```
 
Few Shot
 
```text
Multiple Examples
```
 
Role Prompting
 
```text
Assign Role To AI
```
 
Chain Of Thought
 
```text
Step By Step Reasoning
```
 
Structured Output
 
```text
JSON
Table
Bullets
```
 
LangChain LLM Call
 
```python
response = llm.invoke(prompt)
```
 
---
 
# Summary
 
1. Prompt Engineering is the art of writing effective prompts for AI systems.
2. Better prompts produce better outputs.
3. Good prompts include role, task, context, constraints and output format.
4. Common techniques include Zero-Shot, One-Shot, Few-Shot, Role Prompting and Chain of Thought.
5. LangChain simplifies interaction with LLMs.
6. OpenAI provides the underlying Large Language Model.
7. Prompts are passed through LangChain to OpenAI APIs.
8. The LLM predicts tokens and generates responses.
9. Prompt Engineering is critical for HR, Banking, Healthcare, SAP and AI applications.
10. Prompt Engineering is the first foundational skill before learning LangChain, RAG, AI Agents and Agentic AI.