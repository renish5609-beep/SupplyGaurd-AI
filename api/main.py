from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json, os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.triage_agent import triage_risk
from agents.vendor_agent import recommend_vendors

app = FastAPI(title="SupplyGuard AI", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class RiskEvent(BaseModel):
    supplier_name: str
    risk_description: str
    annual_spend: float
    category: str = "general"

class VendorRequest(BaseModel):
    supplier_name: str
    category: str
    annual_spend: float
    risk_summary: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/triage")
def triage(event: RiskEvent):
    return triage_risk(event.risk_description, event.supplier_name, event.annual_spend)

@app.post("/vendors")
def vendors(req: VendorRequest):
    return recommend_vendors(req.supplier_name, req.category, req.annual_spend, req.risk_summary)

@app.post("/full-pipeline")
def full_pipeline(event: RiskEvent):
    triage = triage_risk(event.risk_description, event.supplier_name, event.annual_spend)
    vendor_recs = recommend_vendors(
        event.supplier_name, event.category,
        event.annual_spend, triage["summary"]
    )
    return {
        "triage": triage,
        "vendors": vendor_recs,
        "requires_human_approval": triage["requires_human_approval"]
    }