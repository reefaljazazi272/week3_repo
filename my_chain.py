import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 1. تحميل الإعدادات والمفتاح
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# 2. إعداد الموديل
llm = ChatOpenAI(model_name="gpt-4o-mini", api_key=api_key)

# 3. تعريف وظائف المهام (التي سيستخدمها الـ Agent)
def get_file_data():
    with open("my_data.txt", "r") as f:
        return f.read()

# 4. محاكاة عمل الـ Agent (Task 1 & Task 2)
# طلبنا من الموديل مباشرة معالجة الملف بطريقة الـ Agent
content = get_file_data()

print("\n--- Starting Day 1 Tasks (Final) ---")

# تنفيذ المهمة الأولى: التلخيص
summary_prompt = f"Summarize this text in one short sentence: {content}"
summary = llm.invoke(summary_prompt)

# تنفيذ المهمة الثانية: عد الكلمات
words_count = len(content.split())

# طباعة النتائج النهائية
print(f"Task 1 (Summary): {summary.content}")
print(f"Task 2 (Word Count): The file contains {words_count} words.")
print("\n--- Day 1 Completed Successfully! ---")
