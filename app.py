import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

app = Flask(__name__)

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7,api_key=os.getenv("OPENAI_API_KEY"))

summary_prompt = PromptTemplate.from_template("Summarize these tasks: {tasks}")
class_prompt = PromptTemplate.from_template("Classify these tasks into 'Work' or 'Personal': {tasks}")
priority_prompt = PromptTemplate.from_template("Assign Priority (High/Medium/Low) for: {tasks}")

chain = summary_prompt | llm 

@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    if request.method == "POST":
        user_tasks = request.form["tasks"]
        
        summary = (summary_prompt | llm).invoke({"tasks": user_tasks}).content
        categories = (class_prompt | llm).invoke({"tasks": user_tasks}).content
        priority = (priority_prompt | llm).invoke({"tasks": user_tasks}).content
        
        results = {
            "original": user_tasks,
            "summary": summary,
            "categories": categories,
            "priority": priority
        }
        
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)

