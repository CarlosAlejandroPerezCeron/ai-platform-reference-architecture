import pandas as pd
import numpy as np

THRESHOLD = 2  # standard deviations

def detect_anomalies(cost_series):
    mean = cost_series.mean()
    std = cost_series.std()
    anomalies = cost_series[np.abs(cost_series - mean) > THRESHOLD * std]
    return anomalies

def simulate():
    # Simulated 30-day GPU spend
    np.random.seed(42)
    daily_cost = np.random.normal(1000, 50, 30)
    daily_cost[15] = 1400  # anomaly spike

    df = pd.Series(daily_cost)
    anomalies = detect_anomalies(df)

    print("=== Cost Anomaly Detection ===")
    print("Mean daily cost:", df.mean())
    print("Detected anomalies:")
    print(anomalies)

if __name__ == "__main__":
    simulate()
