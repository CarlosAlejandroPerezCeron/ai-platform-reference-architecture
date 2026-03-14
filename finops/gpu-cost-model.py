GPU_HOURLY_COST = 1.20
RESERVED_DISCOUNT = 0.30

def monthly_cost(hours_per_day):
    return GPU_HOURLY_COST * hours_per_day * 30

def reserved_monthly_cost(hours_per_day):
    return monthly_cost(hours_per_day) * (1 - RESERVED_DISCOUNT)

def cost_per_inference(total_monthly_cost, inferences):
    return total_monthly_cost / inferences

hours = 24
inferences = 500000

on_demand = monthly_cost(hours)
reserved = reserved_monthly_cost(hours)

print("Monthly On-Demand:", on_demand)
print("Monthly Reserved:", reserved)
print("Cost per Inference:", cost_per_inference(on_demand, inferences))
