from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL"),
    model="gemini-3.5-flash",
    temperature=0
)

while True:
    prompt = input("\nEnter your prompt (type 'exit' to quit): ")

    if prompt.lower() == "exit":
        print("Exiting...")
        break

    response = llm.invoke(prompt)

    print("\nResponse:")
    print(response.content)