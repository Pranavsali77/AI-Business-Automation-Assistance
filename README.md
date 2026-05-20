🤖 AI-Powered Business Automation Assistant

📌 Project Overview

AI-Powered Business Automation Assistant is an intelligent automation platform developed using Streamlit, Python, OpenRouter API, and SQLite.

The system is designed to automate business workflows, manage user leads, generate intelligent AI responses, and provide analytics through an admin dashboard.

This project demonstrates:
- AI/LLM integration
- Business automation workflows
- Lead management systems
- Analytics dashboard
- Email automation
- Intelligent chatbot systems

---

🚀 Features

 ✅ AI Chatbot
- AI-powered conversational assistant
- OpenRouter LLM integration
- Intelligent response generation
- Multilingual support

 ✅ Lead Capture System
- User inquiry form
- Customer lead management
- Business inquiry handling

 ✅ Database Management
- SQLite database integration
- Lead storage and retrieval
- CRUD operations

 ✅ Automation Workflow
- Automated email notifications
- Follow-up campaign system
- Admin lead alerts

 ✅ Admin Dashboard
- Lead viewing interface
- Analytics dashboard
- Data visualization
- Record deletion system

---

 🛠 Technology Stack

- Python
- Streamlit
- OpenRouter API
- SQLite
- Pandas
- SMTP Email Automation

---

 📊 Analytics Features

- Total lead tracking
- Bar charts
- Line charts
- Lead analytics dashboard

---

 📂 Project Structure

```bash
AI-Powered-Business-Automation-Assistant/
│
├── app.py
├── chatbot.py
├── database.py
├── automation.py
├── requirements.txt
├── README.md
├── .env
│
├── data/
│   └── leads.db
```

---

 ⚙ Installation

 1️⃣ Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

---

 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

 3️⃣ Activate Virtual Environment

 Windows

```bash
venv\Scripts\activate
```

 Mac/Linux

```bash
source venv/bin/activate
```

---

 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

 🔐 Environment Variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key

EMAIL_ADDRESS=your_email@gmail.com

EMAIL_PASSWORD=your_app_password
```

---

 ▶ Run Application

```bash
streamlit run app.py
```

---

 🏗 Project Architecture Diagram

```text
                    ┌─────────────────────┐
                    │      User UI        │
                    │   (Streamlit App)   │
                    └─────────┬───────────┘
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
          ▼                   ▼                   ▼

 ┌────────────────┐  ┌────────────────┐  ┌────────────────┐
 │  AI Chatbot    │  │ Lead Capture   │  │ Admin Dashboard│
 │  Module        │  │ Module         │  │ Module         │
 └────────┬───────┘  └────────┬───────┘  └────────┬───────┘
          │                   │                   │
          ▼                   ▼                   ▼

 ┌────────────────────────────────────────────────────────┐
 │                Backend Logic (Python)                  │
 │ chatbot.py     automation.py     database.py           │
 └───────────────────────┬────────────────────────────────┘
                         │
         ┌───────────────┼────────────────┐
         │                                │
         ▼                                ▼

┌───────────────────┐          ┌─────────────────────┐
│ OpenRouter API    │          │ SQLite Database     │
│ (LLM Integration) │          │ Lead Management     │
└───────────────────┘          └─────────────────────┘
         │
         ▼

┌────────────────────┐
│ Email Automation   │
│ SMTP / Gmail API   │
└────────────────────┘

---

 🌐 Deployment
 🚀 Live Demo

Try the deployed AI-Powered Business Automation Assistant here:

👉 https://ai-business-automation-assistance.streamlit.app/

 🔗 GitHub Repository

👉 https://github.com/Pranavsali77/AI-Business-Automation-Assistance

---

📌 Future Improvements

- AI-generated email campaigns
- PDF chatbot (RAG)
- User authentication
- Sentiment analysis
- Cloud database integration

---

 📄 License

This project is developed for educational purposes.
