"""
Data Generator for Driver Profitability Dashboard

This script generates realistic trip data for Uber drivers and can export it to CSV
for further analysis or use in other tools.
"""

import pandas as pd
import numpy as np
import datetime
from datetime import timedelta
import argparse

def generate_trip_data(n_trips=1000, output_file=None):
    """
    Generate realistic trip data for analysis
    
    Args:
        n_trips (int): Number of trips to generate
        output_file (str): Optional CSV file path to save data
    
    Returns:
        pd.DataFrame: Generated trip data
    """
    
    # Define zones and their characteristics
    zones = {
        'Downtown': {'base_fare': 15, 'demand_factor': 1.2},
        'Etobicoke': {'base_fare': 12, 'demand_factor': 0.8},
        'North York': {'base_fare': 14, 'demand_factor': 1.0},
        'Scarborough': {'base_fare': 13, 'demand_factor': 0.9},
        'Mississauga': {'base_fare': 11, 'demand_factor': 0.7},
        'Brampton': {'base_fare': 10, 'demand_factor': 0.6}
    }
    
    # Generate trip data
    np.random.seed(42)
    
    trip_ids = [f"TRIP_{i:06d}" for i in range(1, n_trips + 1)]
    driver_ids = [f"DRIVER_{np.random.randint(1000, 9999)}" for _ in range(n_trips)]
    
    # Generate pickup and dropoff zones
    pickup_zones = np.random.choice(list(zones.keys()), n_trips, p=[0.3, 0.15, 0.2, 0.15, 0.1, 0.1])
    dropoff_zones = np.random.choice(list(zones.keys()), n_trips, p=[0.25, 0.2, 0.2, 0.15, 0.1, 0.1])
    
    # Generate trip characteristics
    trip_distances = np.random.exponential(8, n_trips) + 1  # 1-30 km range
    trip_durations = trip_distances * np.random.uniform(2, 4, n_trips)  # 2-4 min per km
    
    # Generate timestamps across a week
    base_time = datetime.datetime(2024, 1, 1, 6, 0, 0)
    pickup_times = [base_time + timedelta(
        days=np.random.randint(0, 7),
        hours=np.random.randint(0, 24),
        minutes=np.random.randint(0, 60)
    ) for _ in range(n_trips)]
    
    # Calculate fares based on zones and distance
    fare_amounts = []
    driver_payouts = []
    
    for i in range(n_trips):
        pickup_zone = pickup_zones[i]
        distance = trip_distances[i]
        duration = trip_durations[i]
        
        # Base fare calculation
        base_fare = zones[pickup_zone]['base_fare']
        distance_fare = distance * 1.5  # $1.50 per km
        time_fare = duration * 0.3  # $0.30 per minute
        
        total_fare = base_fare + distance_fare + time_fare
        total_fare *= np.random.uniform(0.9, 1.1)  # Add some variability
        
        # Driver payout (typically 70-80% of fare)
        driver_payout = total_fare * np.random.uniform(0.7, 0.8)
        
        fare_amounts.append(round(total_fare, 2))
        driver_payouts.append(round(driver_payout, 2))
    
    # Generate wait times (higher during low demand periods)
    wait_times = []
    for i in range(n_trips):
        hour = pickup_times[i].hour
        zone = pickup_zones[i]
        demand_factor = zones[zone]['demand_factor']
        
        # Higher wait times during off-peak hours and low-demand zones
        base_wait = np.random.exponential(3)
        time_factor = 1.5 if hour < 6 or hour > 22 else 1.0
        zone_factor = 1.5 if demand_factor < 0.9 else 1.0
        
        wait_time = base_wait * time_factor * zone_factor
        wait_times.append(round(wait_time, 1))
    
    # Generate cancellations (rare)
    cancellations = np.random.choice([True, False], n_trips, p=[0.05, 0.95])
    
    # Create DataFrame
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
        'cancellation': cancellations
    })
    
    # Calculate additional metrics
    df = calculate_driver_expenses(df)
    
    # Save to CSV if output file specified
    if output_file:
        df.to_csv(output_file, index=False)
        print(f"Data saved to {output_file}")
    
    return df

def calculate_driver_expenses(df):
    """
    Calculate driver expenses and net earnings
    
    Args:
        df (pd.DataFrame): Trip data
    
    Returns:
        pd.DataFrame: Data with expense calculations
    """
    
    # Gas cost: $0.12 per km
    df['gas_cost'] = df['trip_distance_km'] * 0.12
    
    # Time cost: $0.25 per minute
    df['time_cost'] = df['trip_duration_min'] * 0.25
    
    # Wait cost: $0.20 per minute
    df['wait_cost'] = df['wait_time_min'] * 0.20
    
    # Total expenses
    df['total_expenses'] = df['gas_cost'] + df['time_cost'] + df['wait_cost']
    
    # Net earnings
    df['net_earnings'] = df['driver_payout'] - df['total_expenses']
    
    # Profitability ratio
    df['profitability_ratio'] = df['net_earnings'] / df['trip_duration_min']
    
    return df

def print_summary_stats(df):
    """
    Print summary statistics for the generated data
    
    Args:
        df (pd.DataFrame): Trip data
    """
    
    print("\n" + "="*50)
    print("DRIVER PROFITABILITY DATA SUMMARY")
    print("="*50)
    
    print(f"\n📊 Total Trips: {len(df):,}")
    print(f"💰 Average Net Earnings: ${df['net_earnings'].mean():.2f}")
    print(f"📈 Profitable Trips: {(df['net_earnings'] > 0).sum():,} ({(df['net_earnings'] > 0).mean()*100:.1f}%)")
    print(f"⏱️  Average Trip Duration: {df['trip_duration_min'].mean():.1f} minutes")
    
    print(f"\n🏢 Earnings by Zone:")
    zone_earnings = df.groupby('pickup_zone')['net_earnings'].mean().sort_values(ascending=False)
    for zone, earnings in zone_earnings.items():
        print(f"   {zone}: ${earnings:.2f}")
    
    print(f"\n🕐 Best Hour: {df.groupby(df['pickup_time'].dt.hour)['net_earnings'].mean().idxmax()}:00")
    print(f"🕐 Worst Hour: {df.groupby(df['pickup_time'].dt.hour)['net_earnings'].mean().idxmin()}:00")
    
    print(f"\n🚗 Trip Distance Analysis:")
    df['trip_type'] = pd.cut(df['trip_distance_km'], bins=[0, 5, 10, float('inf')], labels=['Short', 'Medium', 'Long'])
    trip_earnings = df.groupby('trip_type', observed=True)['net_earnings'].mean()
    for trip_type, earnings in trip_earnings.items():
        print(f"   {trip_type}: ${earnings:.2f}")
    
    print("="*50)

def main():
    """Main function to run the data generator"""
    
    parser = argparse.ArgumentParser(description='Generate trip data for driver profitability analysis')
    parser.add_argument('--trips', type=int, default=1000, help='Number of trips to generate (default: 1000)')
    parser.add_argument('--output', type=str, help='Output CSV file path (optional)')
    parser.add_argument('--summary', action='store_true', help='Print summary statistics')
    
    args = parser.parse_args()
    
    print(f"Generating {args.trips:,} trip records...")
    
    # Generate data
    df = generate_trip_data(args.trips, args.output)
    
    # Print summary if requested
    if args.summary:
        print_summary_stats(df)
    
    print(f"\n✅ Generated {len(df):,} trip records successfully!")
    
    if not args.output:
        print("💡 Use --output filename.csv to save the data to a file")
        print("💡 Use --summary to see detailed statistics")

if __name__ == "__main__":
    main() 