import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model_name="gpt-4o-mini", api_key=api_key)

def get_file_data():
    with open("my_data.txt", "r") as f:
        return f.read()

content = get_file_data()

print("\n--- Starting Day 1 Tasks (Final) ---")

summary_prompt = f"Summarize this text in one short sentence: {content}"
summary = llm.invoke(summary_prompt)

words_count = len(content.split())

print(f"Task 1 (Summary): {summary.content}")
print(f"Task 2 (Word Count): The file contains {words_count} words.")
print("\n--- Day 1 Completed Successfully! ---")
