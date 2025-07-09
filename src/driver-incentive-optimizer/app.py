import streamlit as st
import pandas as pd
import plotly.express as px
from simulate_data import simulate_driver_data
from policy_simulation import summarize_by_policy
from ab_testing import ab_test
from uplift_modeling import uplift_by_segment

st.set_page_config(page_title="Uber Toronto Driver Incentive Optimization", layout="wide")
st.title("Uber Toronto Driver Incentive Optimization Tool")
st.write("""
This internal simulation tool helps Uber’s Driver Pricing & Marketplace teams in Toronto evaluate and optimize driver incentive programs (Quest, Boost, Consecutive Trip Bonus, Guaranteed Earnings) for maximum marketplace health and cost-effectiveness.
""")

# Sidebar: Simulation controls
st.sidebar.header("Simulation Controls")
st.sidebar.markdown("Personalize incentive simulation for the Toronto marketplace.")
n_drivers = st.sidebar.slider("Number of drivers", 100, 2000, 500, 100)
n_days = st.sidebar.slider("Number of days", 1, 30, 7, 1)
random_seed = st.sidebar.number_input("Random seed", value=42, step=1)

# Simulate data
@st.cache_data(show_spinner=False)
def get_data(n_drivers, n_days, random_seed):
    return simulate_driver_data(n_drivers, n_days, random_seed)

df = get_data(n_drivers, n_days, random_seed)

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "Incentive Simulator",
    "A/B Test",
    "Uplift Analysis",
    "Toronto Summary Report"
])

# --- Incentive Simulator ---
with tab1:
    st.header("Incentive Simulator")
    st.write("Compare outcomes for Uber incentive schemes in Toronto.")
    st.markdown("""
    **Incentive Types:**
    - **Quest**: Bonus for completing a set number of rides in a time window.
    - **Boost**: Higher fares in specific zones/times (e.g., Toronto Downtown peak hours).
    - **Consecutive Trip Bonus**: Extra for completing rides back-to-back.
    - **Guaranteed Earnings**: Minimum earnings for a set period.
    """)
    summary = summarize_by_policy(df)
    st.dataframe(summary.style.format({
        'participated': '{:.2%}',
        'rides_fulfilled': '{:.2f}',
        'incentive_paid': '${:.2f}',
        'cost_per_ride': '${:.2f}'
    }), use_container_width=True)
    st.markdown("**Participation Rate by Incentive**")
    fig = px.bar(summary, x='policy', y='participated', labels={'participated':'Participation Rate'}, text_auto='.2%')
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("**Cost per Additional Ride by Incentive**")
    fig2 = px.bar(summary, x='policy', y='cost_per_ride', labels={'cost_per_ride':'Cost per Ride'}, text_auto='.2f')
    st.plotly_chart(fig2, use_container_width=True)

# --- A/B Test ---
with tab2:
    st.header("A/B Test Design & Analysis")
    st.write("Select an Uber incentive to compare against no incentive (control group) for Toronto drivers.")
    policy = st.selectbox("Incentive to test", ['Quest', 'Boost', 'Consecutive Trip Bonus', 'Guaranteed Earnings'])
    # Map display name to code name
    policy_map = {
        'Quest': 'fixed_bonus',
        'Boost': 'peak_boost',
        'Consecutive Trip Bonus': 'consecutive_bonus',
        'Guaranteed Earnings': 'guaranteed_min'
    }
    results = ab_test(df, policy_map[policy])
    st.metric("Control Participation Rate", f"{results['control_rate']:.2%}", help="No incentive group")
    st.metric("Treatment Participation Rate", f"{results['treatment_rate']:.2%}", help=f"{policy} group")
    st.metric("Control Rides", f"{results['control_rides']:.2f}")
    st.metric("Treatment Rides", f"{results['treatment_rides']:.2f}")
    st.metric("Cost per Additional Ride", f"${results['cost_per_additional_ride']:.2f}")
    st.write(f"T-test p-value: {results['pval']:.4f}")
    st.caption("If p < 0.05, the difference is statistically significant.")

# --- Uplift Analysis ---
with tab3:
    st.header("Uplift Analysis by Driver Segment")
    st.write("Estimate the treatment effect (uplift) of the selected Uber incentive by driver experience in Toronto.")
    policy2 = st.selectbox("Incentive for uplift analysis", ['Quest', 'Boost', 'Consecutive Trip Bonus', 'Guaranteed Earnings'], key='uplift')
    uplift_df = uplift_by_segment(df, policy_map[policy2], segment_col='experience')
    st.dataframe(uplift_df, use_container_width=True)
    fig3 = px.bar(uplift_df, x='segment', y='uplift', labels={'uplift':'Uplift (Rides)'}, text_auto='.2f', color='segment')
    st.plotly_chart(fig3, use_container_width=True)

# --- Toronto Summary Report ---
with tab4:
    st.header("Toronto Marketplace Summary Report")
    st.write("""
    **Key Insights for Uber Toronto:**
    - Boost incentives during peak hours in Downtown Toronto significantly increase ride fulfillment and driver engagement, especially for new drivers.
    - Guaranteed Earnings are most cost-effective for retaining experienced drivers during off-peak periods.
    - Quest programs drive high participation but may have diminishing returns on cost per additional ride.
    - Consecutive Trip Bonuses are effective for increasing ride streaks in high-density areas.

    **Business Recommendation:**
    - For Toronto, prioritize Boost and Guaranteed Earnings for new and experienced drivers, respectively, to maximize ROI and marketplace balance.
    - Use A/B testing and uplift analysis to continuously refine incentive targeting by driver segment and neighborhood.

    _This tool is inspired by Uber’s real-world incentive optimization challenges in the Toronto marketplace._
    """) 