# SupplyGaurd-AI
Agentic supply chain risk monitoring system built on UiPath Maestro BPMN. Uses Claude Sonnet to triage supplier risk events, score severity, recommend alternative vendors, and draft procurement emails. Orchestrates AI agents, human approval gates, and automated workflows end-to-end.


## Project Description

SupplyGuard AI is an enterprise supply chain risk intelligence platform that monitors 14 suppliers across $20.1M in annual spend. When a risk event occurs (supplier bankruptcy, factory explosion, ransomware attack, port strike, etc.), the platform triages the event using AI in ~9 seconds, scores severity 1–10, recommends pre-qualified alternative vendors, drafts a procurement email, and routes high-severity events (≥7) to a human procurement manager for approval.

**Business problem solved:** Mid-market manufacturers lose an average of $1.6M/year to supply chain disruptions (McKinsey 2024). Most procurement teams still manage supplier risk reactively through spreadsheets. SupplyGuard AI provides proactive, automated risk triage with human-in-the-loop oversight.

---

## UiPath Components Used

- **UiPath Maestro BPMN** — orchestrates the full risk response pipeline as a BPMN 2.0 process
- **UiPath Agent Builder** — two agents built and deployed (Triage Agent + Vendor Recommendation Agent)
- **UiPath Action Center** — human approval workflow for severity ≥7 risk events
- **UiPath Automation Cloud** — hosting environment for all agents and orchestration

---

## Agent Type

This solution utilizes **Low-code Agents** built in UiPath Agent Builder, powered by Claude Sonnet (Anthropic) via AWS Bedrock.

- **Triage Agent** — ingests supplier name, risk description, and annual spend; outputs severity score (1–10), risk category, financial impact estimate, and recommended action
- **Vendor Recommendation Agent** — ingests triage output; identifies 2 alternative vendors with lead times, cost premiums, and a draft procurement email

---

## BPMN Process Flow
---

## Setup Instructions

### Prerequisites
- Python 3.9+
- UiPath Automation Cloud account
- Anthropic API key

### 1. Clone the repository
```bash
git clone https://github.com/renish5609-beep/SupplyGaurd-AI
cd SupplyGaurd-AI
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure environment variables
Create a `.env` file in the root directory:

### 4. Start the FastAPI backend
```bash
python -m uvicorn api.main:app --port 8000
```

The API will be available at `http://localhost:8000`. Verify with:
```bash
curl http://localhost:8000/health
```

### 5. Open the dashboard
Open `dashboard.html` in your browser. No additional server required — the dashboard is a single HTML file.

### 6. UiPath Maestro BPMN (for judging)
- Tenant: `https://staging.uipath.com/hackathon26_892/DefaultTenant`
- Process: **SupplyGuard Risk Response**
- Both agents are live in Agent Builder and the BPMN process has been successfully debug-run with all steps green

### 7. Run a test analysis
1. Open the dashboard
2. Click **Monitor** tab
3. Click the **Bankruptcy** scenario card (Acme Components, $2.4M)
4. Click **Analyze**
5. The full pipeline returns severity score, vendor alternatives, and draft email in ~9 seconds

---

## Tech Stack

- UiPath Maestro BPMN, Agent Builder, Action Center
- Claude Sonnet (Anthropic) via AWS Bedrock
- FastAPI + Python
- HTML/CSS/JavaScript + Chart.js
- Built with Claude Code as primary coding agent

---

## Hackathon Track

**Track 2: UiPath Maestro BPMN** — UiPath AgentHack 2026
