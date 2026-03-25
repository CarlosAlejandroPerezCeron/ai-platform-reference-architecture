# AI Threat Model

## Risk Scoring Model

Risk Score = Impact (1–5) × Likelihood (1–5)

---

## GPU Resource Exhaustion

Impact: 5  
Likelihood: 3  
Risk Score: 15 (High)

Mitigation:
- HPA limits
- Namespace quotas
- Rate limiting

---

## Cost Exhaustion Attack

Impact: 4  
Likelihood: 3  
Risk Score: 12 (High)

Mitigation:
- Budget alerts
- Inference throttling
- Cost anomaly detection
