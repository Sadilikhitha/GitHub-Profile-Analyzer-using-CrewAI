# 🤖 GitHub Profile Analyzer using CrewAI

> An AI-powered multi-agent web application that analyzes GitHub profiles and generates professional developer summaries and technical blog posts using **CrewAI**, **Google Gemini**, and **FastAPI**.

---

##  Overview

GitHub Profile Analyzer is a multi-agent AI application that automates GitHub profile analysis.

The project uses **CrewAI** to coordinate two specialized AI agents:

*  **GitHub Profile Analyzer Agent** – Extracts developer skills, repositories, technologies, and achievements.
*  **Technical Blog Writer Agent** – Converts the analysis into a professional blog article.

The application provides a clean web interface where users simply enter a GitHub username and receive an AI-generated profile summary.

---

##  Features

*  Analyze any public GitHub profile
*  Multi-Agent AI workflow using CrewAI
*  Extract skills and technologies
*  Analyze repositories
*  Generate professional developer summaries
*  Create AI-generated technical blogs
*  Responsive web interface
*  FastAPI backend

---

## 🏗️ Architecture

```text
User
   │
   ▼
Frontend (HTML • CSS • JavaScript)
   │
   ▼
FastAPI Backend
   │
   ▼
CrewAI
   │
   ├────────────► GitHub Profile Analyzer Agent
   │
   └────────────► Technical Blog Writer Agent
                        │
                        ▼
                AI Generated Blog
                        │
                        ▼
               Displayed on Website
```

---

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* FastAPI
* Uvicorn

### AI

* CrewAI
* Google Gemini API

### APIs

* GitHub API

### Other Libraries

* Requests
* Python Dotenv

---

## 🤖 AI Agents

### 🔍 GitHub Profile Analyzer

Responsibilities:

* Analyze GitHub profile
* Identify technologies
* Extract developer skills
* Review repositories
* Summarize achievements

---

### ✍️ Technical Blog Writer

Responsibilities:

* Read GitHub analysis
* Generate technical blog
* Improve readability
* Produce professional content

---

## 📂 Project Structure

```text
Multi_agent/
│
├── backend/
│   ├── app.py
│   ├── agent.py
│   ├── crew.py
│   ├── tasks.py
│   ├── tools.py
│   └── .env
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

## 🚀 Installation

Clone the repository

```bash
git clone <repository-url>
cd Multi_agent
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file inside the **backend** folder.

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
GITHUB_TOKEN=YOUR_GITHUB_TOKEN
```

---

## ▶️ Run the Project

```bash
cd backend
uvicorn app:app --reload
```

Open

```text
http://127.0.0.1:8000
```

Enter a GitHub username and click **Analyze GitHub Profile**.

---

# 📸 Screenshots
<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/d14828ce-5343-420a-bc4e-f81bb22bbb3e" />

## 🎥 Project Demo

<p align="center">
  <img src="images/demo.gif" width="900" alt="Project Demo">
</p>



### ⚙️ CrewAI Workflow (Optional)

> Add your architecture/workflow diagram here

```
images/workflow.png
```

---

## 📚 What I Learned

* Building Multi-Agent AI systems
* CrewAI orchestration
* FastAPI backend development
* REST API integration
* GitHub API usage
* Google Gemini API integration
* Frontend-backend communication

---

## 🚀 Future Improvements

* GitHub profile avatar
* Repository analytics
* Language usage charts
* Download as PDF
* Export as Markdown
* Dark/Light theme
* User authentication

---

## 👩‍💻 Author

**Likhitha Sadi**

GitHub: https://github.com/Sadilikhitha

---

## ⭐ If you found this project useful, consider giving it a star!
