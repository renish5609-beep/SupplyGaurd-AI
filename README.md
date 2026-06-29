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
