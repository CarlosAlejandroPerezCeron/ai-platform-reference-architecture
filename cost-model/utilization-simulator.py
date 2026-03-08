GPU_HOURLY_COST = 1.006
HOURS_PER_MONTH = 24 * 30

def simulate_utilization(utilization_percent):
    effective_cost = GPU_HOURLY_COST * HOURS_PER_MONTH
    waste_factor = 1 - (utilization_percent / 100)
    wasted_cost = effective_cost * waste_factor
    return effective_cost, wasted_cost

cost, wasted = simulate_utilization(70)

print(f"Total Monthly Cost: ${cost:.2f}")
print(f"Wasted due to underutilization: ${wasted:.2f}")
