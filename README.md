# 🤖 IAM-Chat-Bot

A Q&A chatbot for Identity & Access Management (IAM), leveraging **Keycloak** as the IAM backend and **Groq Cloud-powered LLM** for natural language query resolution. The bot can answer questions about users and groups within your IAM system.



## 🌟 Features

- **Conversational Q&A**: Ask real-time questions about users and groups via chat.
- **Keycloak Integration**: Connects to a Keycloak IAM instance with pre-loaded (dummy) users and groups.
- **LLM Intelligence**: Uses Groq Cloud’s large language model for understanding and responding to queries.
- **Customizable Dataset**: Easy to swap in your own user/group data for experimentation.
- **API-first & Extensible**: Ready for integration with Teams, Slack, or your browser.



## 🛠️ Tech Stack

- **Identity Platform**: [Keycloak](https://www.keycloak.org/) (users & groups management)
- **Large Language Model**: [Groq Cloud](https://groq.com/) LLM API
- **Backend**: Python (FastAPI)
- **Frontend**: Simple chat UI (React or Streamlit, optional)
- **Authentication**: OAuth2 (via Keycloak)
- **Data Loading**: Custom scripts for dummy users/groups
- **Containerization**: Docker


## 🚀 Getting Started

### 1. **Clone the Repository**
```bash
git clone https://github.com/PandaAIExplore/IAM-Chatbot.git
cd IAM-Chat-Bot
```

### 2. **Set Up Keycloak**

- Install Keycloak (locally or Docker).
- Create a realm, dummy users, and groups (sample JSON/data provided in `/keycloak-setup`).
- Note the Keycloak server URL, client ID, secret.

### 3. **Configure Groq LLM**

- Sign up for [Groq Cloud](https://groq.com/) and obtain your API key.
- Configure the `.env` or `config.py` file:
  ```
  KEYCLOAK_URL=https://localhost:8080
  KEYCLOAK_CLIENT_ID=your-client-id
  KEYCLOAK_SECRET=your-client-secret
  GROQ_API_KEY=your-groq-api-key
  ```

### 4. **Run the Bot**

- Backend:

  python chatbot_keycloak_groq.py

## 💬 Usage

- Start the chatbot web interface or use the provided API endpoint.
- Example questions you can ask:
  - “Who is in the Admin group?”
  - “List all users”
  - “What groups does user alice belong to?”


**Happy chatting with your IAM!**
