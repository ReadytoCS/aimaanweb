import numpy as np
import pandas as pd

def simulate_driver_data(n_drivers=500, n_days=7, random_seed=42):
    np.random.seed(random_seed)
    driver_ids = np.arange(1, n_drivers+1)
    experience = np.random.choice(['new', 'experienced'], size=n_drivers, p=[0.4, 0.6])
    rating = np.round(np.random.normal(4.7, 0.2, n_drivers), 2)
    zones = ['Downtown', 'North York', 'Scarborough', 'Etobicoke', 'Midtown']
    zone = np.random.choice(zones, size=n_drivers, p=[0.35, 0.2, 0.2, 0.15, 0.1])
    shift_length = np.random.choice(['part-time', 'full-time'], size=n_drivers, p=[0.6, 0.4])
    tenure_months = np.random.randint(1, 61, size=n_drivers)
    base_earnings = np.random.normal(100, 20, n_drivers)
    records = []
    for day in range(n_days):
        for i, did in enumerate(driver_ids):
            policy = np.random.choice(['none', 'fixed_bonus', 'peak_boost', 'consecutive_bonus', 'guaranteed_min'])
            p_participate = 0.3
            if policy == 'fixed_bonus':
                p_participate += 0.15
            elif policy == 'peak_boost':
                p_participate += 0.2 if day % 7 in [5,6] else 0.1
            elif policy == 'consecutive_bonus':
                p_participate += 0.12
            elif policy == 'guaranteed_min':
                p_participate += 0.18
            if experience[i] == 'new':
                p_participate += 0.05
            if zone[i] == 'Downtown':
                p_participate += 0.05
            if shift_length[i] == 'full-time':
                p_participate += 0.07
            if tenure_months[i] < 6:
                p_participate -= 0.03
            participated = np.random.rand() < p_participate
            rides = np.random.poisson(10 if participated else 2)
            incentive_paid = 0
            if policy == 'fixed_bonus' and participated:
                incentive_paid = 10 if rides >= 10 else 0
            elif policy == 'peak_boost' and participated:
                incentive_paid = rides * (3 if day % 7 in [5,6] else 1)
            elif policy == 'consecutive_bonus' and participated:
                incentive_paid = 5 if rides >= 3 else 0
            elif policy == 'guaranteed_min' and participated:
                incentive_paid = max(0, 120 - (base_earnings[i] + rides * 8))
            # Churn probability: base + less if participated or incentivized
            churn_prob = 0.08
            if participated:
                churn_prob -= 0.03
            if incentive_paid > 0:
                churn_prob -= 0.02
            if tenure_months[i] < 3:
                churn_prob += 0.04
            churned = np.random.rand() < churn_prob
            records.append({
                'driver_id': did,
                'day': day,
                'experience': experience[i],
                'rating': rating[i],
                'zone': zone[i],
                'shift_length': shift_length[i],
                'tenure_months': tenure_months[i],
                'policy': policy,
                'participated': int(participated),
                'rides_fulfilled': rides,
                'incentive_paid': incentive_paid,
                'base_earnings': base_earnings[i],
                'churned': int(churned),
                'churn_prob': churn_prob
            })
    return pd.DataFrame(records)

if __name__ == "__main__":
    df = simulate_driver_data()
    print(df.head()) 