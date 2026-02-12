# VoyageGuard

VoyageGuard is an AI-powered travel risk assessment system that evaluates environmental, weather, and contextual factors to determine potential travel risks for a given location.

---

## Problem Statement

Travelers often lack structured, data-driven risk assessments before visiting a location. VoyageGuard provides:

- Real-time environmental risk evaluation  
- Structured risk scoring  
- Contextual reasoning using LLM  
- Data logging for analysis  

---

## Core Features

- Risk scoring engine  
- Agent-based orchestration  
- Weather and external API integration  
- Gemini LLM reasoning  
- MySQL database storage  
- Streamlit-based UI  

---

## Tech Stack

- Python  
- Streamlit  
- MySQL  
- Google Gemini API  
- REST APIs  

---

## Project Structure

```
voyageguard/
│
├── main.py
├── agent.py
├── risk_engine.py
├── tools.py
├── database.py
├── gemini_helper.py
├── schema.sql
├── config.example.py
├── requirements.txt
├── LICENSE
└── README.md
```

---

## Installation

Clone the repository:

```
git clone https://github.com/aryapatel99/voyageguard.git
cd voyageguard
```

Create virtual environment:

```
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Configuration

Create a file named:

```
config.py
```

Copy content from:

```
config.example.py
```

Add your API keys and database credentials.

---

## Database Setup

Run the schema file inside MySQL:

```
SOURCE schema.sql;
```

---

## System Workflow

1. User enters a location.
2. Agent collects external data.
3. Risk engine calculates score.
4. Gemini provides reasoning.
5. Result is displayed.
6. Data is stored in database.

---

## Academic Integrity Note

This project was developed as part of academic coursework.
Official documentation and API references were used where required.
All integration and system logic were implemented by the author(s).
