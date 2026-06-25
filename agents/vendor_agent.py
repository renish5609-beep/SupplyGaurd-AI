import anthropic
import json
import os
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def recommend_vendors(
    failed_supplier: str,
    category: str,
    annual_spend: float,
    risk_summary: str
) -> dict:
    prompt = f"""You are a procurement specialist. A supplier has a critical risk event.

Failed supplier: {failed_supplier}
Category: {category}
Annual spend: ${annual_spend:,.0f}
Risk: {risk_summary}

Return ONLY this JSON:
{{
  "alternative_vendors": [
    {{"name": "...", "estimated_lead_time_days": <int>, "estimated_cost_premium_pct": <int>, "notes": "..."}},
    {{"name": "...", "estimated_lead_time_days": <int>, "estimated_cost_premium_pct": <int>, "notes": "..."}}
  ],
  "draft_email": {{
    "subject": "...",
    "body": "..."
  }},
  "recommended_order_value": <integer USD>
}}"""

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )
    
    raw = response.content[0].text.strip()
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    return json.loads(raw.strip())

if __name__ == "__main__":
    result = recommend_vendors(
        "Acme Components", "electronics", 2400000,
        "Filed for Chapter 11 bankruptcy"
    )
    print(json.dumps(result, indent=2))