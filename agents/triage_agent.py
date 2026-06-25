import anthropic
import json
import os
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def triage_risk(risk_description: str, supplier_name: str, spend: float) -> dict:
    prompt = f"""You are a supply chain risk analyst. Analyze this risk and return ONLY valid JSON.

Supplier: {supplier_name}
Annual spend: ${spend:,.0f}
Risk event: {risk_description}

Return this exact JSON structure:
{{
  "severity": <integer 1-10>,
  "category": "<one of: supplier_financial, logistics, geopolitical, quality, capacity>",
  "summary": "<one sentence summary>",
  "recommended_action": "<specific action to take>",
  "requires_human_approval": <true if severity >= 7 else false>,
  "estimated_impact_usd": <estimated dollar impact as integer>
}}"""

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}]
    )
    
    raw = response.content[0].text.strip()
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    return json.loads(raw.strip())

if __name__ == "__main__":
    result = triage_risk(
        "Acme Components has filed for Chapter 11 bankruptcy",
        "Acme Components",
        2400000
    )
    print(json.dumps(result, indent=2))