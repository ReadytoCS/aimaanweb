# 🚗 Driver Profitability Dashboard

A comprehensive dashboard that helps Uber analyze **driver earnings after expenses** to ensure sustainable payout structures across trip types, regions, and time windows.

## 🎯 Objective

This dashboard simulates trip-level data and clearly shows how profitable driving is for different driver profiles and situations. It answers the critical business question:

> **"Where and when are drivers actually making money?"**

## 📊 Features

### Data Generation
- **Realistic Trip Data**: 1000+ simulated trips with realistic parameters
- **Multiple Zones**: Downtown, Etobicoke, North York, Scarborough, Mississauga, Brampton
- **Time-based Analysis**: Trips across different hours and days
- **Cost Modeling**: Gas, time, and wait costs per trip

### Key Metrics
- **Total Trips**: Number of completed trips
- **Average Net Earnings**: Driver earnings after all expenses
- **Profitable Trips Percentage**: Ratio of profitable to total trips
- **Average Trip Duration**: Time spent per trip

### Visualizations
1. **Earnings by Region**: Bar chart showing average net earnings by pickup zone
2. **Earnings by Time**: Line chart showing earnings patterns throughout the day
3. **Trip Type Comparison**: Box plots comparing short, medium, and long trips
4. **Cost Breakdown**: Pie chart showing the split of gas, time, and wait costs

### Business Insights
- Automated generation of plain-English insights
- Identification of worst and best performing zones/times
- Profitability analysis by trip distance
- Overall profitability statistics

### Interactive Filters
- **Zone Selection**: Filter by specific pickup zones
- **Time Range**: Select custom time periods for analysis
- **Real-time Updates**: All visualizations update based on filters

## 🧮 Calculations

### Driver Expenses (per trip):
- **Gas Cost**: `trip_distance_km × $0.12/km`
- **Time Cost**: `trip_duration_min × $0.25/min`
- **Wait Cost**: `wait_time_min × $0.20/min`

### Driver Net Earnings:
- `driver_payout - (gas + time + wait cost)`

### Profitability Ratio:
- `Net Earnings / trip_duration_min`

## 🛠 Technology Stack

- **Python**: Core programming language
- **Streamlit**: Interactive web application framework
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Plotly**: Interactive visualizations

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone or navigate to the project directory**
   ```bash
   cd driver-profitability-dashboard
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - If not, manually navigate to the URL shown in the terminal

## 📈 Data Structure

Each trip record contains:

| Column | Description | Type |
|--------|-------------|------|
| `trip_id` | Unique trip identifier | String |
| `driver_id` | Driver identifier | String |
| `pickup_zone` | Pickup location zone | String |
| `dropoff_zone` | Dropoff location zone | String |
| `trip_distance_km` | Trip distance in kilometers | Float |
| `trip_duration_min` | Trip duration in minutes | Float |
| `pickup_time` | Trip pickup timestamp | DateTime |
| `fare_amount` | Total fare paid to Uber | Float |
| `driver_payout` | Amount paid to driver | Float |
| `wait_time_min` | Driver wait time in minutes | Float |
| `cancellation` | Whether trip was cancelled | Boolean |

## 🎨 Dashboard Layout

### Header Section
- Main title and description
- Key performance metrics in cards

### Visualization Section
- **Top Row**: Earnings by Region & Earnings by Time
- **Bottom Row**: Trip Type Comparison & Cost Breakdown

### Business Insights Section
- Automated insights with emojis and clear explanations
- Data-driven recommendations

### Data Table Section
- Sample trip data for verification
- Key columns for quick analysis

## 🔧 Customization

### Modifying Cost Parameters
Edit the `calculate_driver_expenses()` function to adjust:
- Gas cost per kilometer
- Time cost per minute
- Wait cost per minute

### Adding New Zones
Modify the `zones` dictionary in `generate_trip_data()` to add new zones with their base fares and demand factors.

### Changing Data Volume
Adjust the `n_trips` parameter in the `generate_trip_data()` function call to generate more or fewer trips.

## 📊 Business Use Cases

### For Product Managers
- Identify unprofitable zones and time periods
- Optimize driver incentives and pricing
- Understand driver behavior patterns

### For Operations Teams
- Plan driver allocation strategies
- Optimize service coverage areas
- Monitor driver satisfaction through earnings

### For Finance Teams
- Analyze cost structures and profitability
- Model different pricing scenarios
- Track financial performance by region

## 🎯 Key Insights Generated

The dashboard automatically generates insights like:
- "💡 Drivers earned the least during 1–3 PM in Etobicoke—likely due to low demand and long wait times."
- "🚗 Short-distance trips in Downtown had the highest profitability due to low costs and high volume."
- "🏆 Downtown was the most profitable zone with average net earnings of $X.XX per trip."

## 🔮 Future Enhancements

### Potential Additions
- **Driver Type Filtering**: Full-time vs part-time drivers
- **Gas Price Sensitivity**: Slider to adjust gas prices
- **Uber's Cut Analysis**: Show Uber's revenue per trip
- **Export Functionality**: Download filtered data as CSV
- **Historical Trends**: Time-series analysis over weeks/months
- **Driver Satisfaction Metrics**: Correlation with earnings

### Advanced Analytics
- **Predictive Modeling**: Forecast earnings based on conditions
- **A/B Testing**: Compare different pricing strategies
- **Geographic Heatmaps**: Visual earnings by exact location
- **Driver Cohort Analysis**: Compare different driver segments

## 🤝 Contributing

Feel free to contribute to this project by:
- Adding new visualizations
- Improving the data generation logic
- Enhancing the business insights algorithm
- Adding new filtering options

## 📄 License

This project is open source and available under the MIT License.

---

**Built with ❤️ for data-driven decision making in the gig economy** 