import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import datetime
from datetime import timedelta
import random

# --- Data generation and expense calculation helpers ---
@st.cache_data
def generate_trip_data(n_trips=1000):
    zones = {
        'Downtown': {'base_fare': 15, 'demand_factor': 1.2, 'surge_multiplier': 1.3},
        'Etobicoke': {'base_fare': 12, 'demand_factor': 0.8, 'surge_multiplier': 1.1},
        'North York': {'base_fare': 14, 'demand_factor': 1.0, 'surge_multiplier': 1.2},
        'Scarborough': {'base_fare': 13, 'demand_factor': 0.9, 'surge_multiplier': 1.0},
        'Mississauga': {'base_fare': 11, 'demand_factor': 0.7, 'surge_multiplier': 0.9},
        'Brampton': {'base_fare': 10, 'demand_factor': 0.6, 'surge_multiplier': 0.8}
    }
    np.random.seed(42)
    trip_ids = [f"TRIP_{i:06d}" for i in range(1, n_trips + 1)]
    driver_ids = [f"DRIVER_{np.random.randint(1000, 9999)}" for _ in range(n_trips)]
    pickup_zones = np.random.choice(list(zones.keys()), n_trips, p=[0.3, 0.15, 0.2, 0.15, 0.1, 0.1])
    dropoff_zones = np.random.choice(list(zones.keys()), n_trips, p=[0.25, 0.2, 0.2, 0.15, 0.1, 0.1])
    trip_distances = np.random.exponential(8, n_trips) + 1
    trip_durations = trip_distances * np.random.uniform(2, 4, n_trips)
    base_time = datetime.datetime(2024, 1, 1, 6, 0, 0)
    pickup_times = [base_time + timedelta(
        days=np.random.randint(0, 7),
        hours=np.random.randint(0, 24),
        minutes=np.random.randint(0, 60)
    ) for _ in range(n_trips)]
    driver_types = np.random.choice(['Full-time', 'Part-time'], n_trips, p=[0.6, 0.4])
    ab_groups = np.random.choice(['Control', 'Treatment'], n_trips, p=[0.5, 0.5])
    fare_amounts = []
    driver_payouts = []
    for i in range(n_trips):
        pickup_zone = pickup_zones[i]
        distance = trip_distances[i]
        duration = trip_durations[i]
        base_fare = zones[pickup_zone]['base_fare']
        distance_fare = distance * 1.5
        time_fare = duration * 0.3
        surge_multiplier = zones[pickup_zone]['surge_multiplier']
        total_fare = (base_fare + distance_fare + time_fare) * surge_multiplier
        total_fare *= np.random.uniform(0.95, 1.05)
        payout_multiplier = np.random.uniform(0.7, 0.8)
        if ab_groups[i] == 'Treatment':
            payout_multiplier += 0.05
        if driver_types[i] == 'Full-time':
            payout_multiplier += 0.03
        driver_payout = total_fare * payout_multiplier
        fare_amounts.append(round(total_fare, 2))
        driver_payouts.append(round(driver_payout, 2))
    wait_times = []
    for i in range(n_trips):
        hour = pickup_times[i].hour
        zone = pickup_zones[i]
        demand_factor = zones[zone]['demand_factor']
        base_wait = np.random.exponential(3)
        time_factor = 1.5 if hour < 6 or hour > 22 else 1.0
        zone_factor = 1.5 if demand_factor < 0.9 else 1.0
        wait_time = base_wait * time_factor * zone_factor
        wait_times.append(round(wait_time, 1))
    cancellations = np.random.choice([True, False], n_trips, p=[0.05, 0.95])
    df = pd.DataFrame({
        'trip_id': trip_ids,
        'driver_id': driver_ids,
        'pickup_zone': pickup_zones,
        'dropoff_zone': dropoff_zones,
        'trip_distance_km': trip_distances,
        'trip_duration_min': trip_durations,
        'pickup_time': pickup_times,
        'fare_amount': fare_amounts,
        'driver_payout': driver_payouts,
        'wait_time_min': wait_times,
        'cancellation': cancellations,
        'driver_type': driver_types,
        'ab_group': ab_groups
    })
    return df

def calculate_driver_expenses(df):
    df['gas_cost'] = df['trip_distance_km'] * 0.12
    df['time_cost'] = df['trip_duration_min'] * 0.25
    df['wait_cost'] = df['wait_time_min'] * 0.20
    df['total_expenses'] = df['gas_cost'] + df['time_cost'] + df['wait_cost']
    df['net_earnings'] = df['driver_payout'] - df['total_expenses']
    df['profitability_ratio'] = df['net_earnings'] / df['trip_duration_min']
    n_unprofitable = max(1, int(0.02 * len(df)))
    unprofitable_indices = np.random.choice(df.index, n_unprofitable, replace=False)
    df.loc[unprofitable_indices, 'net_earnings'] = -np.abs(np.random.uniform(1, 10, n_unprofitable))
    df.loc[unprofitable_indices, 'profitability_ratio'] = df.loc[unprofitable_indices, 'net_earnings'] / df.loc[unprofitable_indices, 'trip_duration_min']
    return df

# --- Helper for plain-language insights ---
def generate_plain_insights(df):
    insights = []
    # Earnings by region
    region_earnings = df.groupby('pickup_zone')['net_earnings'].mean().sort_values(ascending=False)
    best_zone = region_earnings.index[0]
    worst_zone = region_earnings.index[-1]
    pct_diff = (region_earnings[best_zone] - region_earnings[worst_zone]) / region_earnings[worst_zone] * 100
    insights.append(f"{best_zone} drivers earn {pct_diff:.0f}% more per trip than {worst_zone}.")
    # Earnings by hour
    hourly = df.groupby(df['pickup_time'].dt.hour)['net_earnings'].mean()
    best_hour = hourly.idxmax()
    worst_hour = hourly.idxmin()
    insights.append(f"Best hour: {best_hour}:00, Worst hour: {worst_hour}:00.")
    # Earnings by trip length
    df['trip_bucket'] = pd.cut(df['trip_distance_km'], [0,5,10,100], labels=['Short','Medium','Long'])
    trip_earn = df.groupby('trip_bucket')['net_earnings'].mean()
    best_bucket = trip_earn.idxmax()
    insights.append(f"{best_bucket} trips are most profitable.")
    return insights

# --- Helper for A/B badge ---
def ab_test_badge(df):
    control = df[df['ab_group']=='Control']['net_earnings']
    treat = df[df['ab_group']=='Treatment']['net_earnings']
    lift = (treat.mean() - control.mean()) / control.mean() * 100
    # Use a simple t-test for p-value
    from scipy.stats import ttest_ind
    tstat, pval = ttest_ind(treat, control)
    badge = f"{'✅' if pval<0.05 else '⚠️'} Treatment group outperformed control by {lift:+.1f}% in net earnings. p = {pval:.3f}"
    sub = "Suggest further testing across more regions."
    return badge, sub

# --- Helper for business recs ---
def business_recs(df):
    recs = []
    # Find lowest zone/hour
    hourly = df.groupby([df['pickup_time'].dt.hour, 'pickup_zone'])['net_earnings'].mean()
    if not hourly.empty:
        idx = hourly.idxmin()
        recs.append(f"📉 Drivers earned least in {idx[1]} {idx[0]}–{idx[0]+1}h – consider higher wait-time bonus.")
    # Find low trip bucket
    df['trip_bucket'] = pd.cut(df['trip_distance_km'], [0,5,10,100], labels=['Short','Medium','Long'])
    trip_earn = df.groupby('trip_bucket')['net_earnings'].mean()
    if not trip_earn.empty:
        low_bucket = trip_earn.idxmin()
        recs.append(f"🛣️ {low_bucket} trips are least profitable – review pricing or incentives.")
    return recs

# --- Cost breakdown card ---
def cost_breakdown_card(df):
    avg_gas = df['gas_cost'].mean()
    avg_time = df['time_cost'].mean()
    avg_wait = df['wait_cost'].mean()
    st.markdown("""
    <div style='background:#fffbe7;padding:1rem;border-radius:0.5rem;border-left:5px solid #ffb300;margin-bottom:1rem;'>
    <b>Where does the money go?</b><br>
    <ul style='margin:0;padding-left:1.2em;'>
      <li>⛽ Gas: ${:.2f}</li>
      <li>⏰ Time: ${:.2f}</li>
      <li>🕒 Wait: ${:.2f}</li>
    </ul>
    </div>
    """.format(avg_gas, avg_time, avg_wait), unsafe_allow_html=True)

# --- Comparison tool ---
def comparison_tool(df, compare_type, compare_options):
    st.markdown("<b>Compare any two:</b>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        left = st.selectbox("First", compare_options, key="comp1")
    with c2:
        right = st.selectbox("Second", compare_options, key="comp2")
    if left == right:
        st.info("Select two different options.")
        return
    if compare_type == 'zone':
        left_df = df[df['pickup_zone']==left]
        right_df = df[df['pickup_zone']==right]
    else:
        left_df = df[df['driver_type']==left]
        right_df = df[df['driver_type']==right]
    # Net Earnings
    left_net = left_df['net_earnings'].mean()
    right_net = right_df['net_earnings'].mean()
    net_diff = left_net - right_net
    net_pct = 100 * net_diff / right_net if right_net != 0 else 0
    st.markdown(f"Net Earnings: {left}: <b>{left_net:.2f}</b>, {right}: <b>{right_net:.2f}</b>", unsafe_allow_html=True)
    if abs(net_pct) > 1:
        if net_pct > 0:
            st.caption(f"{left} drivers earn {abs(net_pct):.1f}% more per trip than {right}, suggesting higher efficiency or better trip choices.")
        else:
            st.caption(f"{right} drivers earn {abs(net_pct):.1f}% more per trip than {left}, suggesting higher efficiency or better trip choices.")
    else:
        st.caption("No meaningful difference in net earnings per trip.")
    # Driver Payout
    left_payout = left_df['driver_payout'].mean()
    right_payout = right_df['driver_payout'].mean()
    payout_diff = left_payout - right_payout
    payout_pct = 100 * payout_diff / right_payout if right_payout != 0 else 0
    st.markdown(f"Driver Payout: {left}: <b>{left_payout:.2f}</b>, {right}: <b>{right_payout:.2f}</b>", unsafe_allow_html=True)
    if abs(payout_pct) > 1:
        if payout_pct > 0:
            st.caption(f"{left} drivers receive higher payouts, possibly due to more premium trips or better timing.")
        else:
            st.caption(f"{right} drivers receive higher payouts, possibly due to more premium trips or better timing.")
    else:
        st.caption("No meaningful difference in driver payout per trip.")
    # Trip Distance
    left_dist = left_df['trip_distance_km'].mean()
    right_dist = right_df['trip_distance_km'].mean()
    dist_diff = left_dist - right_dist
    dist_pct = 100 * dist_diff / right_dist if right_dist != 0 else 0
    st.markdown(f"Trip Distance Km: {left}: <b>{left_dist:.2f}</b>, {right}: <b>{right_dist:.2f}</b>", unsafe_allow_html=True)
    if abs(dist_pct) > 1:
        if dist_pct > 0:
            st.caption(f"{left} drivers take longer trips on average, which may impact their earnings or trip strategy.")
        else:
            st.caption(f"{right} drivers take longer trips on average, which may impact their earnings or trip strategy.")
    else:
        st.caption("No meaningful difference in trip distance per trip.")

# --- Main app ---
def main():
    st.set_page_config(page_title="Uber Driver Profitability", layout="wide")
    st.title("🚗 Driver Profitability Dashboard")
    st.info(
        "This dashboard shows how much Uber drivers earn after expenses, and where they earn the most. "
        "It's designed for Uber's Driver Pricing Team to quickly spot ways to help drivers earn more.  \n"
        "_Hypothetical case study by Aimaan._\n"
        "\n"
        "**About A/B Groups**\n"
        "We use 'Treatment' and 'Control' groups to test different incentive or pricing strategies. This helps us see what works best for drivers.\n"
        "- For example, the Treatment group might receive a higher per-trip bonus than the Control group."
    )
    df = generate_trip_data(1000)
    df = calculate_driver_expenses(df)
    st.sidebar.header("Filters")
    zones = list(df['pickup_zone'].unique())
    types = list(df['driver_type'].unique())
    df['trip_bucket'] = pd.cut(df['trip_distance_km'], [0,5,10,100], labels=['Short','Medium','Long'])
    buckets = list(df['trip_bucket'].unique())
    ab_opts = list(df['ab_group'].unique())

    # --- RESET LOGIC ---
    if 'reset_filters' not in st.session_state:
        st.session_state['reset_filters'] = False

    if st.sidebar.button("Reset Filters"):
        st.session_state['reset_filters'] = True
        st.rerun()

    if st.session_state.get('reset_filters', False):
        # Only reset before widgets are rendered
        st.session_state['zone_sel'] = zones.copy()
        st.session_state['type_sel'] = types.copy()
        st.session_state['bucket_sel'] = buckets.copy()
        st.session_state['ab_sel'] = ab_opts.copy()
        st.session_state['reset_filters'] = False
        st.rerun()

    # --- FILTERS ---
    if 'zone_sel' not in st.session_state:
        st.session_state['zone_sel'] = zones.copy()
    if 'type_sel' not in st.session_state:
        st.session_state['type_sel'] = types.copy()
    if 'bucket_sel' not in st.session_state:
        st.session_state['bucket_sel'] = buckets.copy()
    if 'ab_sel' not in st.session_state:
        st.session_state['ab_sel'] = ab_opts.copy()

    zone_sel = st.sidebar.multiselect("Pickup Zone", zones, default=st.session_state['zone_sel'], key='zone_sel')
    type_sel = st.sidebar.multiselect("Driver Type", types, default=st.session_state['type_sel'], key='type_sel')
    bucket_sel = st.sidebar.multiselect("Trip Length", buckets, default=st.session_state['bucket_sel'], key='bucket_sel')
    ab_sel = st.sidebar.multiselect("A/B Group", ab_opts, default=st.session_state['ab_sel'], key='ab_sel')

    # Apply filters
    filtered = df[
        df['pickup_zone'].isin(st.session_state['zone_sel']) &
        df['driver_type'].isin(st.session_state['type_sel']) &
        df['trip_bucket'].isin(st.session_state['bucket_sel']) &
        df['ab_group'].isin(st.session_state['ab_sel'])
    ]
    # --- Top metrics ---
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("💰 Avg Net Earnings", f"${filtered['net_earnings'].mean():.2f}")
    with col2:
        best_zone = filtered.groupby('pickup_zone')['net_earnings'].mean().idxmax()
        st.metric("📍 Best Zone", best_zone)
    with col3:
        best_bucket = filtered.groupby('trip_bucket')['net_earnings'].mean().idxmax()
        st.metric("🛣️ Best Trip Length", str(best_bucket))
    # --- Plain-language insights ---
    st.markdown("### Key Insights")
    for insight in generate_plain_insights(filtered):
        st.info(insight)
    # --- A/B Test Badge ---
    badge, ab_sub = ab_test_badge(filtered)
    st.markdown(f"<div style='background:#e3f2fd;padding:0.7rem 1rem;border-radius:0.5rem;display:inline-block;font-weight:bold;'>{badge}</div>", unsafe_allow_html=True)
    st.caption(ab_sub)
    # --- Visuals ---
    st.markdown("---")
    st.subheader("Earnings by Region")
    st.caption("Which pickup zones are most profitable for drivers? Use this to prioritize incentive programs and resource allocation.")
    reg = filtered.groupby('pickup_zone')['net_earnings'].mean().sort_values()
    fig1 = px.bar(reg, x=reg.values, y=reg.index, orientation='h', color=reg.values, color_continuous_scale='Blues', labels={'x':'Net Earnings','y':'Zone'})
    st.plotly_chart(fig1, use_container_width=True)
    st.subheader("Earnings by Trip Length")
    st.caption("Compare short, medium, and long trips. Use this to inform trip pricing and bonus strategies.")
    tb = filtered.groupby('trip_bucket')['net_earnings'].mean()
    fig3 = px.bar(tb, x=tb.index, y=tb.values, color=tb.values, color_continuous_scale='Greens', labels={'x':'Trip Length','y':'Net Earnings'})
    st.plotly_chart(fig3, use_container_width=True)
    # --- Cost breakdown card ---
    with st.sidebar:
        cost_breakdown_card(filtered)
    # --- Business Recommendations ---
    st.markdown("### Business Recommendations")
    for rec in business_recs(filtered):
        st.warning(rec)
    # --- Comparison Tool ---
    st.markdown("---")
    st.markdown("### Compare Zones or Driver Types")
    st.caption("Quickly compare two zones or driver types to see where Uber can make the biggest impact for drivers.")
    comp_type = st.radio("Compare by", ['zone','driver_type'], horizontal=True)
    options = list(filtered['pickup_zone'].unique()) if comp_type=='zone' else list(filtered['driver_type'].unique())
    comparison_tool(filtered, comp_type, options)

if __name__ == "__main__":
    main() 