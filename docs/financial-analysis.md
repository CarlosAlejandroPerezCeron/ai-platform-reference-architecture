# Financial Exposure Analysis

Primary Cost Driver: GPU compute

Baseline:
g5.xlarge ≈ $1.20/hour

Monthly On-Demand:
$864

Reserved Savings:
~30%

Spot Savings:
~65%

Risk:

- Underutilization below 70% increases effective cost per inference.
- Spot interruptions affect training stability.

Mitigation:

- HPA tuning
- Reserved baseline + Spot overflow
- Inference batching
