# AI Platform Threat Model

## Risk 1 – Prompt Injection
Mitigation:
- Input validation
- LLM guardrails
- Logging enabled

## Risk 2 – GPU Resource Exhaustion
Mitigation:
- HPA limits
- Namespace quotas

## Risk 3 – Cost Exhaustion Attack
Mitigation:
- Budget alerts
- Per-namespace cost tracking
- Inference rate limiting

## Risk 4 – Model Artifact Tampering
Mitigation:
- Artifact signing
- Immutable storage
