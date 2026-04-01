def survivability_index(cost_risk, security_risk, availability_score):
    """
    Lower cost_risk and security_risk improve survivability.
    Higher availability improves survivability.
    """
    return (availability_score * 0.4) + ((5 - cost_risk) * 0.3) + ((5 - security_risk) * 0.3)

def simulate():
    cost_risk = 3          # 1–5
    security_risk = 2      # 1–5
    availability = 4.5     # 1–5

    index = survivability_index(cost_risk, security_risk, availability)
    print("AI Survivability Index:", round(index, 2))

if __name__ == "__main__":
    simulate()
