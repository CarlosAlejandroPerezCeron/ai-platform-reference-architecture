GPU_HOURLY_COST = 1.20
RESERVED_DISCOUNT = 0.30
SPOT_DISCOUNT = 0.65

HOURS_MONTH = 24 * 30

def monthly_cost(rate):
    return rate * HOURS_MONTH

def cost_per_inference(total_cost, inferences):
    return total_cost / inferences

def simulate():
    inferences = 500000

    on_demand = monthly_cost(GPU_HOURLY_COST)
    reserved = monthly_cost(GPU_HOURLY_COST * (1 - RESERVED_DISCOUNT))
    spot = monthly_cost(GPU_HOURLY_COST * (1 - SPOT_DISCOUNT))

    print("=== GPU Cost Modeling ===")
    print(f"On-Demand Monthly: ${on_demand:.2f}")
    print(f"Reserved Monthly: ${reserved:.2f}")
    print(f"Spot Monthly: ${spot:.2f}")
    print(f"Cost per inference (On-Demand): ${cost_per_inference(on_demand, inferences):.6f}")

if __name__ == "__main__":
    simulate()
