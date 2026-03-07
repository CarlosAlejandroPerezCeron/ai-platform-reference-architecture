HOURS_PER_MONTH = 24 * 30
GPU_HOURLY_COST = 1.006  # Example g5.xlarge

monthly_gpu_cost = GPU_HOURLY_COST * HOURS_PER_MONTH
monthly_inferences = 500000

cost_per_inference = monthly_gpu_cost / monthly_inferences

print(f"Monthly GPU Cost: ${monthly_gpu_cost:.2f}")
print(f"Cost per inference: ${cost_per_inference:.6f}")
