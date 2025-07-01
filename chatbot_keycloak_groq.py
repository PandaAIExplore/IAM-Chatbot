
import gradio as gr
import requests


GROQ_API_KEY = ''
GROQ_API_URL = 'https://api.groq.com/openai/v1/chat/completions'
MODEL_NAME = 'llama3-70b-8192'

# Load the current access report (use fresh data when needed)
with open('keycloak_access_review.csv', 'r') as f:
    access_report = f.read()

SYSTEM_PROMPT = """
You are a security analyst assistant for Keycloak IAM.
The following CSV contains users, their emails, groups, and roles.
Answer questions about access, risks, and user permissions using only the info provided.
Be accurate and concise.
"""

def ask_groq(question,history):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"Here is the current Keycloak access report CSV:\n{access_report}\n\nNow, answer this question: {question}"}
    ]
    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "max_tokens": 800,
        "temperature": 0.2
    }
    response = requests.post(GROQ_API_URL, headers=headers, json=payload, verify=False)
    print(response.status_code)
    print(response.text)
    response.raise_for_status()
    if response.status_code ==200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error {response.status_code}:{response.text}"


chatbot = gr.ChatInterface(fn=ask_groq,title='IAM-Bot',theme='monochrome')

if __name__ == '__main__':
    chatbot.launch()