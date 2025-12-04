# 🤖 AI Bias Classifier

The **AI Bias Classifier** is a fully implemented web application designed to **compare and evaluate the responses of multiple AI models** (OpenAI, Anthropic, and others) by analyzing their **bias levels**.

The project provides a modern, polished frontend, a robust backend, and a complete bias-analysis pipeline.

---

## 🎯 Purpose

The application allows a user to:

1. Submit any question (e.g., *“What do you think about nuclear energy?”*).
2. Retrieve responses from several AI models.
3. Automatically analyze each response for bias:
   - assign a **bias score**,
   - extract qualitative labels,
   - compare models side-by-side.
4. Visualize everything through a clean and intuitive dashboard.

The goal is to offer an objective, educational tool to compare AI behavior on sensitive topics (politics, ethics, society, etc.).

---

## 🏗️ Project Architecture

The system consists of two fully functional layers:  
a **FastAPI backend** and a **Next.js frontend**.

---

## 🧩 Backend — FastAPI (fully implemented)

The backend, built with Python and FastAPI, handles:

- querying multiple LLM providers,
- storing questions and responses,
- bias analysis,
- exposing a complete REST API for the frontend.

### Current Structure

```bash
backend/
├── main.py                  # FastAPI application entrypoint
├── services/
│   ├── llm_client.py        # OpenAI/Anthropic API calls via httpx
│   └── bias_analyzer.py     # Bias detection and scoring logic
├── models/
│   ├── schemas.py           # Pydantic request/response schemas
│   └── db_models.py         # Database models
└── database/
    └── db.py                # SQLite initialization and connection

```
🔌 OpenAI & Anthropic Integration

The backend no longer relies on the official openai SDK (which caused freezing issues).
➡️ Instead, all API communication uses httpx.AsyncClient, ensuring:

no import freezes,

complete API compatibility,

clean asynchronous performance.

Anthropic integration follows the same pattern.

🧠 Bias Analysis

The bias_analyzer.py module implements a full bias-evaluation pipeline:

LLM-as-a-Judge architecture
A neutral model evaluates the responses produced by other models.

Extraction of indicators:

political leaning,

emotional tone,

subjectivity,

argumentative direction.

Standardized output score from 0 to 1.

Everything is already integrated and functional.

🎨 Frontend — Next.js + TailwindCSS (fully implemented)

The frontend is built in TypeScript using Next.js and TailwindCSS.
It offers a clean, premium-style UI with a strong focus on comparative analysis.

Current Structure

```bash
frontend/
├── app/ (or pages/)         # Next.js routing
├── components/
│   ├── QuestionForm.tsx     # Main input component
│   ├── ResponsesList.tsx    # Display of AI responses
│   └── BiasDashboard.tsx    # Bias score charts & visualizations
└── styles/
    └── globals.css          # Tailwind + global styles

```
Implemented Features
User input form

Real-time backend requests

Side-by-side display of AI responses

Interactive bias-score visualizations

Responsive and polished UI

🗂️ Database — SQLite (fully implemented)
SQLite stores:

user questions,

model responses,

computed bias scores,

metadata (model type, timestamp, etc.).

Prepared for future migration to PostgreSQL if needed.

🧪 Testing & Verification
Automated Tests (backend)
Using pytest, the backend includes unit tests for:

API endpoints,

the LLM client,

the bias analysis module.

Manual Verification
Start the backend

```bash
cd backend
source venv/bin/activate
uvicorn main:app --reload
```
Start the frontend

```bash
cd frontend
npm install
npm run dev
Visit:
http://localhost:3000

Submit a question (e.g., “What do you think about nuclear energy?”).
```

Confirm:

multiple AI responses appear,

bias scores are computed,

dashboard visualizations update correctly.

📦 Project Status
The application is fully functional, and all components defined in the initial design have been implemented successfully.

🔮 Future Improvements
Potential extensions include:

Support for additional models (LLaMA, Mistral, etc.)

Advanced multidimensional bias visualization

PDF/CSV export

Edge/Client-side analysis

