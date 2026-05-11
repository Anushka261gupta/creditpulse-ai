# CreditPulse AI — Finance Credit Follow-Up Email Agent

## Overview

CreditPulse AI is an AI-powered Finance Follow-Up Email Agent designed to automate overdue invoice communication workflows for finance teams.

The system detects overdue invoices, applies escalation logic based on overdue duration, generates personalized AI-powered follow-up emails, maintains audit logs, and flags high-risk accounts for manual legal review.

This project was built as part of the AI Enablement Internship Project Challenge (Task 2 — Finance Credit Follow-Up Email Agent).

---

# Problem Statement

Finance teams spend significant time manually following up on overdue payments.

Manual workflows often lead to:
- inconsistent communication
- delayed escalation
- poor tracking
- lack of auditability

CreditPulse AI automates this workflow using LLM-powered email generation and escalation logic while maintaining professional communication standards.

---

# Features

## Core Features

- CSV-based invoice ingestion
- Dynamic CSV upload support
- Overdue invoice detection
- AI-generated personalized payment reminder emails
- Tone escalation engine
- Dry-run email simulation mode
- SQLite audit logging
- Download generated emails
- Dashboard metrics
- Manual legal escalation flagging

---

# Tone Escalation Matrix

| Overdue Days | Tone |
|---|---|
| 1–7 Days | Warm & Friendly |
| 8–14 Days | Polite but Firm |
| 15–21 Days | Formal & Serious |
| 22–30 Days | Stern & Urgent |
| 30+ Days | Escalate to Legal |

---

# Tech Stack

| Layer | Technology |
|---|---|
| Frontend/UI | Streamlit |
| LLM | Groq LLM API |
| Language | Python |
| Data Processing | pandas |
| Logging | SQLite |
| Email Workflow | Dry-Run Simulation |
| Configuration | Streamlit Secrets |
| Version Control | Git + GitHub |

---

# LLM & Decision Log

## LLM Chosen

Groq LLM API was used for AI email generation because:
- fast inference speed
- cost-efficient API access
- easy Python integration
- suitable for real-time text generation tasks

---

# Agent Architecture

```text
CSV Upload
↓
Invoice Processing
↓
Overdue Detection
↓
Escalation Engine
↓
LLM Email Generation
↓
Dry Run Email Dispatch
↓
SQLite Audit Logging
↓
Dashboard Visualization
```

---

# Agent Framework

This project follows a lightweight single-agent workflow architecture implemented using Python modules and Streamlit orchestration.

Instead of using a heavy multi-agent framework, the system was designed as a modular pipeline consisting of:
- escalation_engine.py
- email_agent.py
- audit_logger.py
- Streamlit UI workflow

Architecture Type:
- Single-Agent Workflow
- Sequential Processing Pipeline
- Rule-Based Escalation + LLM Generation

This architecture was chosen because:
- lightweight execution
- simpler debugging
- faster deployment
- easier maintainability
- suitable for finance workflow automation

---

---
# Structured Output Validation

Pydantic models were implemented for validating AI-generated email responses and maintaining consistent output formatting.

Benefits:
- reduced parsing errors
- cleaner response handling
- type-safe AI outputs
- improved maintainability

---

# Prompt Design

The email generation prompt was carefully structured to ensure:
- professional finance communication
- tone consistency
- invoice-specific personalization
- controlled LLM behaviour

The prompt dynamically injects:
- client name
- invoice number
- amount due
- overdue duration
- escalation tone

Guardrails Applied:
- structured invoice input
- controlled prompt template
- no unrestricted user prompt injection
- dry-run testing mode
- human-readable output validation

---

---

# Prompt Iterations

Initial prompts generated generic reminder emails.

The prompt was later refined to:
- dynamically inject invoice details
- maintain escalation tone consistency
- avoid hallucinated payment information
- generate professional finance communication

Final prompt design focused on:
- clarity
- professionalism
- escalation control
- personalization

--- 

# Security Mitigations

## Prompt Injection
- Structured prompts used
- Limited invoice context passed to LLM

## API Key Protection
- Secrets stored using Streamlit Secrets
- API keys excluded using .gitignore

## Email Safety
- Dry-run mode used during testing
- Prevents accidental client email delivery

## Audit Logging
- SQLite logging for transparency and traceability

## Hallucination Mitigation
- LLM only generates email text
- Financial calculations handled using Python logic

## Unauthorized Access
- Local development environment used
- No public API endpoints exposed

---

# Setup Instructions

## Clone Repository

```bash
git clone https://github.com/Anushka261gupta/creditpulse-ai.git
```

---

## Navigate to Project

```bash
cd creditpulse-ai
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Secrets

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
GROQ_API_KEY="your_groq_api_key"
```

---

## Run Streamlit App

```bash
streamlit run app/streamlit_app.py
```

---

# Project Structure

```text
creditpulse-ai/
│
├── app/
│   ├── streamlit_app.py
│   ├── email_agent.py
│   ├── escalation_engine.py
│   ├── audit_logger.py
│   ├── utils.py
│
├── data/
│   └── invoices.csv
│
├── logs/
│
├── outputs/
│
├── requirements.txt
├── runtime.txt
├── .env.example
└── README.md
```

---

# Sample Outputs

The project generates:
- AI-generated finance follow-up emails
- escalation alerts
- audit history logs
- dashboard analytics

Example outputs are available in:
- outputs/
- logs/
- sample_outputs/

---

# Future Improvements

- SendGrid / Resend integration
- LangChain workflow orchestration
- Admin authentication system
- APScheduler automation
- Email analytics dashboard
- Real-time finance monitoring

---

# Demo

The application demonstrates:
- AI-powered finance automation
- escalation-based communication
- secure audit logging
- dashboard analytics
- dry-run email workflow

---

# Author

Anushka Gupta

B.Tech AIML Student  
AI Enablement Internship Project
