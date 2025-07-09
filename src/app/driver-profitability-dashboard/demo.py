#!/usr/bin/env python3
"""
Demo Script for Driver Profitability Dashboard

This script demonstrates the data generation and analysis capabilities
without requiring the full Streamlit dashboard.
"""

import pandas as pd
import numpy as np
from data_generator import generate_trip_data, calculate_driver_expenses
import matplotlib.pyplot as plt
import seaborn as sns

def create_demo_visualizations(df):
    """Create basic visualizations for the demo"""
    
    # Set style
    plt.style.use('default')
    sns.set_palette("husl")
    
    # Create subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Driver Profitability Dashboard - Demo Analysis', fontsize=16, fontweight='bold')
    
    # 1. Earnings by Region
    region_earnings = df.groupby('pickup_zone')['net_earnings'].mean().sort_values(ascending=True)
    bars = ax1.barh(region_earnings.index, region_earnings.values, color='skyblue')
    ax1.set_title('Average Net Earnings by Region')
    ax1.set_xlabel('Average Net Earnings ($)')
    
    # Add value labels on bars
    for i, bar in enumerate(bars):
        width = bar.get_width()
        ax1.text(width + 0.5, bar.get_y() + bar.get_height()/2, 
                f'${width:.1f}', ha='left', va='center')
    
    # 2. Earnings by Hour
    df['hour'] = df['pickup_time'].dt.hour
    hourly_earnings = df.groupby('hour')['net_earnings'].mean()
    ax2.plot(hourly_earnings.index, hourly_earnings.values, marker='o', linewidth=2, markersize=6)
    ax2.set_title('Average Net Earnings by Hour of Day')
    ax2.set_xlabel('Hour of Day')
    ax2.set_ylabel('Average Net Earnings ($)')
    ax2.grid(True, alpha=0.3)
    
    # 3. Trip Type Comparison
    df['trip_type'] = pd.cut(df['trip_distance_km'], 
                             bins=[0, 5, 10, float('inf')], 
                             labels=['Short (<5km)', 'Medium (5-10km)', 'Long (>10km)'])
    
    trip_earnings = df.groupby('trip_type', observed=True)['net_earnings'].mean()
    colors = ['lightcoral', 'lightblue', 'lightgreen']
    bars = ax3.bar(trip_earnings.index, trip_earnings.values, color=colors)
    ax3.set_title('Net Earnings by Trip Distance')
    ax3.set_ylabel('Average Net Earnings ($)')
    ax3.tick_params(axis='x', rotation=45)
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'${height:.1f}', ha='center', va='bottom')
    
    # 4. Cost Breakdown
    avg_costs = {
        'Gas Cost': df['gas_cost'].mean(),
        'Time Cost': df['time_cost'].mean(),
        'Wait Cost': df['wait_cost'].mean()
    }
    
    wedges, texts, autotexts = ax4.pie(avg_costs.values(), labels=avg_costs.keys(), 
                                       autopct='%1.1f%%', startangle=90)
    ax4.set_title('Average Cost Breakdown per Trip')
    
    # Style adjustments
    plt.tight_layout()
    
    return fig

def print_demo_insights(df):
    """Print demo insights"""
    
    print("\n" + "="*60)
    print("🚗 DRIVER PROFITABILITY DASHBOARD - DEMO INSIGHTS")
    print("="*60)
    
    # Overall statistics
    print(f"\n📊 OVERALL STATISTICS:")
    print(f"   Total Trips: {len(df):,}")
    print(f"   Average Net Earnings: ${df['net_earnings'].mean():.2f}")
    print(f"   Profitable Trips: {(df['net_earnings'] > 0).sum():,} ({(df['net_earnings'] > 0).mean()*100:.1f}%)")
    print(f"   Average Trip Duration: {df['trip_duration_min'].mean():.1f} minutes")
    
    # Zone analysis
    print(f"\n🏢 ZONE ANALYSIS:")
    zone_earnings = df.groupby('pickup_zone')['net_earnings'].mean().sort_values(ascending=False)
    best_zone = zone_earnings.index[0]
    worst_zone = zone_earnings.index[-1]
    print(f"   Most Profitable Zone: {best_zone} (${zone_earnings.iloc[0]:.2f})")
    print(f"   Least Profitable Zone: {worst_zone} (${zone_earnings.iloc[-1]:.2f})")
    
    # Time analysis
    print(f"\n🕐 TIME ANALYSIS:")
    hourly_earnings = df.groupby(df['pickup_time'].dt.hour)['net_earnings'].mean()
    best_hour = hourly_earnings.idxmax()
    worst_hour = hourly_earnings.idxmin()
    print(f"   Best Hour: {best_hour}:00 (${hourly_earnings.max():.2f})")
    print(f"   Worst Hour: {worst_hour}:00 (${hourly_earnings.min():.2f})")
    
    # Trip distance analysis
    print(f"\n🚗 TRIP DISTANCE ANALYSIS:")
    df['trip_type'] = pd.cut(df['trip_distance_km'], 
                             bins=[0, 5, 10, float('inf')], 
                             labels=['Short', 'Medium', 'Long'])
    trip_earnings = df.groupby('trip_type', observed=True)['net_earnings'].mean()
    for trip_type, earnings in trip_earnings.items():
        print(f"   {trip_type} trips: ${earnings:.2f}")
    
    # Business insights
    print(f"\n💡 BUSINESS INSIGHTS:")
    print(f"   💡 Drivers earned the least during {worst_hour}-{worst_hour+1} PM in {worst_zone}—likely due to low demand and long wait times.")
    print(f"   🚗 {trip_earnings.idxmax()}-distance trips had the highest profitability with average earnings of ${trip_earnings.max():.2f} per trip.")
    print(f"   🏆 {best_zone} was the most profitable zone with average net earnings of ${zone_earnings.iloc[0]:.2f} per trip.")
    
    # Cost analysis
    print(f"\n💰 COST ANALYSIS:")
    print(f"   Average Gas Cost: ${df['gas_cost'].mean():.2f}")
    print(f"   Average Time Cost: ${df['time_cost'].mean():.2f}")
    print(f"   Average Wait Cost: ${df['wait_cost'].mean():.2f}")
    print(f"   Total Average Cost: ${df['total_expenses'].mean():.2f}")
    
    print("="*60)

def main():
    """Main demo function"""
    
    print("🚗 Driver Profitability Dashboard - Demo")
    print("="*50)
    
    # Generate sample data
    print("📊 Generating sample trip data...")
    df = generate_trip_data(500)  # Generate 500 trips for demo
    
    # Print insights
    print_demo_insights(df)
    
    # Create visualizations
    print("\n📈 Creating visualizations...")
    fig = create_demo_visualizations(df)
    
    # Save the plot
    output_file = "demo_analysis.png"
    fig.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"📊 Visualization saved as: {output_file}")
    
    # Show the plot
    plt.show()
    
    print("\n✅ Demo completed successfully!")
    print("💡 To run the full interactive dashboard, use: streamlit run app.py")

if __name__ == "__main__":
    main() 