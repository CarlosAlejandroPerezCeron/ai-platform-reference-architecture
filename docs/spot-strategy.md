# GPU Spot Strategy

Objective:
Reduce GPU baseline cost while maintaining SLA.

Strategy:
- Use spot instances for non-critical training workloads.
- Keep on-demand nodes for inference critical path.

Risk:
Spot interruption can affect training stability.

Mitigation:
- Checkpointing enabled.
- Fallback node group available.
