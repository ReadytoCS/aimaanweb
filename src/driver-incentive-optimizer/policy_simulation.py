import pandas as pd

def summarize_by_policy(df):
    policy_names = {
        'none': 'No Incentive',
        'fixed_bonus': 'Quest',
        'peak_boost': 'Boost',
        'consecutive_bonus': 'Consecutive Trip Bonus',
        'guaranteed_min': 'Guaranteed Earnings'
    }
    summary = df.groupby('policy').agg({
        'participated': 'mean',
        'rides_fulfilled': 'mean',
        'incentive_paid': 'mean',
        'driver_id': 'count'
    }).rename(columns={'driver_id': 'n_observations'}).reset_index()
    summary['cost_per_ride'] = summary['incentive_paid'] / summary['rides_fulfilled']
    summary['policy'] = summary['policy'].map(policy_names)
    return summary 