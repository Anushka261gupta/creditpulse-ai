# CreditPulse AI — Finance Credit Follow-Up Email Agent

## Overview

CreditPulse AI is an AI-powered Finance Follow-Up Agent designed to automate overdue invoice communication workflows for finance teams.

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
