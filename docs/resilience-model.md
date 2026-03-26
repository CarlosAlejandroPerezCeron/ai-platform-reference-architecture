# Resilience & SLO Model

Target Availability: 99.5%

Error Budget:
0.5% monthly downtime

Latency Target:
< 200ms p95 inference latency

Failure Scenarios:

1. GPU node crash
2. Spot interruption
3. Traffic spike

Mitigation:

- Multi-node GPU pool
- Autoscaling
- Fallback CPU inference
