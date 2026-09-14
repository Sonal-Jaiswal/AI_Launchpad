# Day 7: LangChain and Prompt Engineering

This folder introduces the building blocks used to create applications with Large Language Models (LLMs). It starts with a direct model call, adds a Streamlit chat interface, and then develops the prompt-engineering concepts needed to make model responses more useful and reliable.

## What You Will Learn

By the end of this lesson, you should be able to:

- Explain what an LLM, prompt, model, chain, tool, agent, memory, and RAG system are.
- Call a chat model from Python using LangChain.
- Build a simple chatbot with Streamlit session state.
- Write prompts with roles, context, constraints, examples, and output formats.
- Choose between a direct SDK call, LangChain, LangGraph, and a hosted application framework.
- Recognize common reliability, security, cost, and privacy problems in LLM applications.

## Folder Guide

| File | Purpose |
| --- | --- |
| `llm_api_calls.py` | Minimal terminal chatbot. Reads prompts with `input()` and calls a chat model. |
| `llm_streamlit_app.py` | Browser chatbot built with Streamlit. Uses `st.session_state` to retain messages during a session. |
| `system_prompt.py` | Prompt templates and system instructions for tutor, LinkedIn, resume, interview, and prompt-reviewer roles. |
| `notes.md` | Prompt-engineering notes covering prompt components and zero-shot, one-shot, and few-shot prompting. |
| `roles.md` | Reusable role-based prompts and output formats. |
| `.env` | Local credentials and endpoint configuration. Never commit this file. |

## What Is an LLM?

A Large Language Model predicts and generates text from a sequence of tokens. It can summarize, classify, translate, explain, write code, and transform text, but it does not automatically have current knowledge, private data, reliable memory, or permission to perform real-world actions.

A useful mental model is:

```text
User input + instructions + available context -> model -> generated output
```

The output is generated, not guaranteed to be true. Production applications need validation, observability, access controls, and tests around the model.

## What Is LangChain?

LangChain is a framework for connecting language models to application code, prompts, data sources, tools, and workflows. It provides common interfaces so that an application can switch models or compose multiple steps without rewriting every integration.

LangChain is not itself an LLM. It is application plumbing around an LLM.

```text
Your application
      |
      +-- prompts and messages
      +-- model provider
      +-- parsers and structured output
      +-- retrievers and vector stores
      +-- tools and external APIs
      +-- chains or workflows
```

## The Core Concepts

### 1. Model

The model generates a response. A chat model receives messages rather than one unstructured string.

```python
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
)

response = model.invoke("Explain lists in Python to a beginner.")
print(response.content)
```

This repository uses `ChatOpenAI` with a configurable `OPENAI_BASE_URL`. That allows an OpenAI-compatible endpoint to be used with the same LangChain integration. The model name and endpoint must be supported by the provider configured in `.env`.

### 2. Messages

Chat applications normally separate instructions by role:

- `system`: application rules and behavior.
- `human`: the user's request.
- `ai`: a previous assistant response.

```python
from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="You are a patient Python tutor."),
    HumanMessage(content="Explain dictionaries with one example."),
]
response = model.invoke(messages)
```

A system message is an instruction, not a security boundary. Treat user input as untrusted even when a system message says otherwise.

### 3. Prompt Templates

A prompt template separates reusable instructions from changing data.

```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You teach {audience} using simple language."),
    ("human", "Explain {topic} with one short code example."),
])

messages = prompt.invoke({
    "audience": "Python beginners",
    "topic": "sets",
})
response = model.invoke(messages)
```

This is better than repeatedly building long strings because the structure is visible, reusable, and testable.

### 4. Output Parsers and Structured Output

A model normally returns text. An output parser converts that text into a useful application type. Structured output is preferable when the application needs fields rather than prose.

```python
from pydantic import BaseModel, Field

class Sentiment(BaseModel):
    label: str = Field(description="positive, neutral, or negative")
    confidence: float = Field(ge=0, le=1)

structured_model = model.with_structured_output(Sentiment)
result = structured_model.invoke("The product arrived early and works well.")
print(result.label, result.confidence)
```

Always validate model output. A type annotation alone does not make an answer correct.

### 5. Chains and LCEL

A chain passes the result of one step into the next. Modern LangChain commonly composes steps with the pipe operator, called LCEL (LangChain Expression Language).

```python
chain = prompt | model
response = chain.invoke({
    "audience": "Python beginners",
    "topic": "tuples",
})
print(response.content)
```

A parser can be added as another step:

```python
from langchain_core.output_parsers import StrOutputParser

chain = prompt | model | StrOutputParser()
answer = chain.invoke({"audience": "students", "topic": "functions"})
```

A chain is a predictable sequence. It is not automatically an autonomous agent.

### 6. Memory and Conversation History

Models do not remember previous requests by themselves. An application must send relevant history again on each request.

The Streamlit app does this with session state:

```python
if "messages" not in st.session_state:
    st.session_state.messages = []

st.session_state.messages.append({
    "role": "user",
    "content": prompt,
})
```

The example currently stores and displays the conversation, but it sends only the newest `prompt` to the model. Therefore the user interface shows history while the model does not necessarily receive that history. To give the model conversational context, invoke it with the full message list or use a history-aware workflow.

```python
from langchain_core.messages import HumanMessage, AIMessage

history = [
    HumanMessage(content="My name is Sonal."),
    AIMessage(content="Nice to meet you, Sonal."),
    HumanMessage(content="What is my name?"),
]
response = model.invoke(history)
```

For long conversations, summarize or retrieve relevant history instead of sending everything forever. This reduces token cost and context-window pressure.

### 7. Documents and RAG

RAG means Retrieval-Augmented Generation. Instead of asking the model to invent an answer from its training data, the application retrieves relevant source text and includes it in the prompt.

Typical RAG flow:

```text
Documents
  -> load
  -> split into chunks
  -> create embeddings
  -> store vectors
  -> retrieve relevant chunks for a question
  -> add chunks to prompt
  -> generate answer with citations
```

Conceptual example:

```python
from langchain_core.prompts import ChatPromptTemplate

rag_prompt = ChatPromptTemplate.from_template("""
Answer only from the context below.
If the answer is not present, say that you do not know.

Context:
{context}

Question: {question}
""")

chain = rag_prompt | model
answer = chain.invoke({
    "context": "Python sets store unique values.",
    "question": "What does a set store?",
})
```

RAG is different from fine-tuning. RAG supplies changing knowledge at request time; fine-tuning changes model behavior by training on examples. RAG is usually the first choice for private documents that change frequently.

### 8. Tools

A tool is a controlled function the model can request, such as a calculator, database lookup, or weather API.

```python
from langchain_core.tools import tool

@tool
def add_numbers(first: int, second: int) -> int:
    """Add two integers."""
    return first + second
```

The tool description helps the model decide when it is appropriate. The application must still validate arguments, authorize access, handle errors, and log usage.

### 9. Agents

An agent uses a model to decide which available tool to call and what to do next. A simple chain follows a known path; an agent chooses a path at runtime.

```text
Chain:  input -> step A -> step B -> output
Agent:  input -> decide -> tool -> observe -> decide -> output
```

Agents are useful for open-ended tasks, but they are harder to test and control. Prefer a deterministic chain when the steps are known in advance.

### 10. Streaming and Callbacks

Normal invocation waits for the complete response. Streaming displays chunks as they arrive, which improves perceived responsiveness for chat interfaces.

```python
for chunk in model.stream("Explain functions in Python."):
    print(chunk.content, end="", flush=True)
```

Callbacks and tracing can record tokens, latency, tool calls, errors, and intermediate steps. In production, observability is essential because model failures are often probabilistic rather than simple exceptions.

## Prompt Engineering

Prompt engineering is the deliberate design of instructions and context to make model output more accurate, consistent, and useful.

A strong prompt commonly includes:

1. **Role**: Who should the model act as?
2. **Task**: What should it do?
3. **Context**: What information does it need?
4. **Constraints**: What must it avoid or limit?
5. **Output format**: How should the answer be shaped?
6. **Quality criteria**: What makes the result good?
7. **Examples**: What input/output pattern should it follow?

Weak prompt:

```text
Write an email.
```

Improved prompt:

```text
Role: You are a professional workplace communication assistant.
Task: Write an email requesting two days of leave.
Context: The employee has a medical appointment next week.
Constraints: Use a respectful tone and keep it under 120 words.
Output: Return a subject line followed by the email body.
```

### Prompting Techniques

| Technique | Meaning | Example use |
| --- | --- | --- |
| Zero-shot | Give an instruction without examples. | Classify a support ticket. |
| One-shot | Give one example of the expected pattern. | Show one correctly formatted answer. |
| Few-shot | Give several examples. | Classify unusual labels consistently. |
| Role prompting | Define the model's perspective and audience. | Act as a Python tutor for beginners. |
| Chain-of-thought request | Ask for reasoning support when appropriate. | Ask for a concise rationale, not hidden private reasoning. |
| Structured prompting | Define fields, sections, or JSON output. | Extract name, date, and issue from an email. |
| Grounded prompting | Supply trusted context and require it to be used. | Answer from a company policy document. |

Do not rely on prompting alone for high-stakes correctness. Use code validation, retrieval, permissions, and human review where needed.

## The Example Application

`llm_api_calls.py` is the smallest learning step:

```text
read input -> invoke model -> print response -> repeat
```

`llm_streamlit_app.py` adds a user interface:

```text
render chat input -> save user message -> invoke model -> save answer -> render history
```

The important Streamlit concepts are:

- `st.title()` renders a heading.
- `st.chat_input()` collects a user message.
- `st.chat_message()` renders a role-specific message.
- `st.session_state` keeps values across Streamlit reruns.

Run it from this folder with:

```powershell
streamlit run llm_streamlit_app.py
```

The current scripts use:

```python
load_dotenv()
os.getenv("OPENAI_API_KEY")
os.getenv("OPENAI_BASE_URL")
```

A compatible local `.env` might look like this:

```text
OPENAI_API_KEY=your-api-key
OPENAI_BASE_URL=https://your-openai-compatible-endpoint/v1
```

Do not place real keys in source code, notebooks, screenshots, or Git history. If a key is exposed, revoke it and create a replacement.

## Important Differences

### LLM vs Chat Model

An LLM may expose a text-in/text-out interface. A chat model is designed around role-based messages. Chat models are usually the natural fit for assistants and multi-turn conversations.

### Prompt vs System Prompt

A prompt is any input instruction or context. A system prompt is the high-priority application instruction that defines behavior. Neither guarantees truth or prevents malicious user input.

### Chain vs Agent

A chain follows a planned sequence. An agent chooses tools and steps dynamically. Chains are easier to test; agents are more flexible but need stronger controls.

### Memory vs RAG

Memory supplies conversation or user-specific history. RAG retrieves external knowledge such as documents. They solve different problems and can be used together.

### RAG vs Fine-Tuning

RAG adds information at request time and can reflect updated documents. Fine-tuning changes behavior or style through training and is less convenient for frequently changing facts.

### Tool vs Agent

A tool is a callable capability. An agent is a decision-making loop that may choose among tools. A tool can be used directly without an agent.

### LangChain vs LangGraph

LangChain provides model, prompt, tool, retriever, and chain abstractions. LangGraph is designed for stateful, multi-step, branching, and durable agent workflows. Start with a chain; use a graph when explicit state and control are needed.

### LangChain vs Direct Provider SDK

A provider SDK is often simpler for one model call and exposes provider-specific features first. LangChain adds common interfaces and composition across models, prompts, tools, parsers, and retrievers. The extra abstraction is useful when the application has multiple steps or integrations.

### LangChain vs LlamaIndex

LangChain is broad workflow and tool orchestration. LlamaIndex is especially focused on data ingestion, indexing, and retrieval. The two can overlap and can also be used together.

## Reliability and Security Checklist

Before calling an LLM application complete, check:

- Secrets are stored in environment variables and excluded from Git.
- User input is treated as untrusted data.
- Tool calls have authentication, authorization, validation, and timeouts.
- Retrieved documents are treated as data, not trusted instructions.
- Outputs are validated before they reach a database, shell, email system, or user.
- The application handles provider errors, rate limits, timeouts, and empty responses.
- Logs do not expose API keys, private documents, or unnecessary personal data.
- Token usage, latency, model version, and cost are observable.
- Important answers include sources or a clear statement of uncertainty.
- Prompts and model behavior have repeatable evaluation examples.

## Suggested Exercises

1. Add a system message that makes the chatbot a Python tutor.
2. Change the app so the model receives the complete conversation history.
3. Add a clear `exit` command and error handling to `llm_api_calls.py`.
4. Create a prompt template for resume review using a fixed output format.
5. Add structured output for a support-ticket classifier.
6. Replace the hard-coded context in the RAG example with a local text document.
7. Add a calculator tool and compare direct tool use with an agent.
8. Add streaming output to the Streamlit chatbot.
9. Record three evaluation questions and compare two prompts or models.

## Interview Preparation

### What is LangChain?

LangChain is a framework for building LLM applications by composing models with prompts, parsers, tools, retrievers, and workflows.

### Why use a prompt template?

It keeps reusable instructions separate from variable input, improves consistency, and makes prompts easier to test and maintain.

### What is RAG?

RAG retrieves relevant external context and supplies it to the model before generation, helping answer questions about current or private information without retraining the model.

### What is an agent?

An agent is a model-driven workflow that chooses actions or tools dynamically. It is more flexible than a fixed chain but requires more safety and testing.

### How do you reduce hallucinations?

Ground the model with trusted context, require it to say when information is missing, use structured output and validation, retrieve sources, lower unnecessary randomness, and evaluate representative questions.

### How do you manage conversation history?

Store messages in application state, send the relevant history to the model, and summarize or retrieve older turns when the context becomes too large.

## Summary

LangChain does not replace Python fundamentals or model knowledge. It helps connect those pieces into an application:

```text
prompt + model + parser + data + tools + state + validation = LLM application
```

Start with the smallest working chain. Add memory, retrieval, tools, agents, and observability only when the application actually needs them.
