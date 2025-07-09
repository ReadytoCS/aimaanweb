import pandas as pd

def uplift_by_segment(df, policy_name, segment_col='experience'):
    policy_map = {
        'Quest': 'fixed_bonus',
        'Boost': 'peak_boost',
        'Consecutive Trip Bonus': 'consecutive_bonus',
        'Guaranteed Earnings': 'guaranteed_min'
    }
    code_name = policy_map.get(policy_name, policy_name)
    control = df[df['policy'] == 'none']
    treatment = df[df['policy'] == code_name]
    segments = df[segment_col].unique()
    results = []
    for seg in segments:
        c = control[control[segment_col] == seg]['rides_fulfilled'].mean()
        t = treatment[treatment[segment_col] == seg]['rides_fulfilled'].mean()
        uplift = t - c
        results.append({'segment': seg, 'control': c, 'treatment': t, 'uplift': uplift})
    return pd.DataFrame(results) 