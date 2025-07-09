import pandas as pd
from scipy.stats import ttest_ind

def ab_test(df, policy_name):
    # Map display name to code name if needed
    policy_map = {
        'Quest': 'fixed_bonus',
        'Boost': 'peak_boost',
        'Consecutive Trip Bonus': 'consecutive_bonus',
        'Guaranteed Earnings': 'guaranteed_min'
    }
    code_name = policy_map.get(policy_name, policy_name)
    # Control: no incentive, Treatment: selected policy
    control = df[df['policy'] == 'none']
    treatment = df[df['policy'] == code_name]
    # Participation rate
    control_rate = control['participated'].mean()
    treatment_rate = treatment['participated'].mean()
    # Fulfilled rides
    control_rides = control['rides_fulfilled'].mean()
    treatment_rides = treatment['rides_fulfilled'].mean()
    # Cost per additional ride
    cost = treatment['incentive_paid'].mean()
    uplift = treatment_rides - control_rides
    cost_per_additional_ride = cost / uplift if uplift > 0 else float('inf')
    # T-test
    tstat, pval = ttest_ind(treatment['rides_fulfilled'], control['rides_fulfilled'], equal_var=False)
    return {
        'control_rate': control_rate,
        'treatment_rate': treatment_rate,
        'control_rides': control_rides,
        'treatment_rides': treatment_rides,
        'cost_per_additional_ride': cost_per_additional_ride,
        'tstat': tstat,
        'pval': pval
    } 