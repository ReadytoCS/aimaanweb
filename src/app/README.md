# 📊 ExcelInsight

Transform your Excel data into interactive charts and professional PowerPoint presentations with just a few clicks!

## 🚀 Features

- **📁 File Upload**: Support for .xls and .xlsx files (up to 20 MB)
- **📋 Sheet Selection**: Choose from multiple sheets in your Excel file
- **🔍 Auto-Detection**: Smart chart candidate detection based on data types
- **📈 Interactive Charts**: Beautiful Plotly visualizations
- **📤 PowerPoint Export**: Download professional presentations with one click
- **📊 Data Profiling**: Optional comprehensive data analysis

## 📋 Supported Chart Types

- **📈 Line Charts**: Date/time + numeric columns
- **📊 Bar Charts**: Categorical + numeric columns  
- **📉 Scatter Plots**: Two numeric columns with trendlines

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- macOS/Linux (Windows support coming soon)

### Quick Setup

1. **Clone or download the project files**
   ```bash
   # If you have the files locally, navigate to the project directory
   cd path/to/excelinsight
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   # venv\Scripts\activate  # On Windows
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
   - Navigate to: `http://localhost:8501`
   - The app will open automatically in your default browser

## 📖 Usage Guide

### Step 1: Upload Your Excel File
- Click "Browse files" or drag and drop your Excel file
- Supported formats: `.xls`, `.xlsx`
- Maximum file size: 20 MB

### Step 2: Select a Sheet
- Choose from the available sheets in your Excel file
- The app will automatically analyze the data

### Step 3: Review Auto-Detected Charts
- The app will display up to 3 chart candidates
- Each chart is interactive and can be zoomed/explored

### Step 4: Download PowerPoint
- Click "Download PowerPoint Deck" to generate a presentation
- Optional: Check "Include data profiling summary" for comprehensive analysis
- The presentation will be automatically downloaded

## 🎨 Chart Detection Rules

### Line Charts
- **Trigger**: Date/time column + numeric column(s)
- **Use Case**: Time series analysis, trends over time
- **Example**: Sales data with dates

### Bar Charts
- **Trigger**: Categorical column + numeric column
- **Use Case**: Comparing categories, rankings
- **Example**: Product sales by category

### Scatter Plots
- **Trigger**: Two numeric columns (no date/time)
- **Use Case**: Correlation analysis, relationships
- **Example**: Height vs Weight data

## 📁 Project Structure

```
excelinsight/
├── app.py              # Main Streamlit application
├── chart_utils.py      # Chart detection and creation utilities
├── pptx_utils.py       # PowerPoint generation utilities
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🔧 Technical Details

### Dependencies
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **OpenPyXL**: Excel file reading
- **Plotly**: Interactive chart creation
- **Python-PPTX**: PowerPoint generation
- **Pillow**: Image processing
- **NumPy**: Numerical computing

### Architecture
- **Frontend**: Streamlit web interface
- **Backend**: Python data processing
- **Charts**: Plotly interactive visualizations
- **Export**: PowerPoint with embedded chart images

## 🎯 Screenshots

### File Upload Widget
```python
# Streamlit file uploader code
uploaded_file = st.file_uploader(
    "Choose an Excel file (.xls or .xlsx)",
    type=['xls', 'xlsx'],
    help="Maximum file size: 20 MB"
)
```

### Chart Display
```python
# Interactive Plotly chart
fig = create_chart(df, chart_info)
st.plotly_chart(fig, use_container_width=True)
```

## 🚨 Troubleshooting

### Common Issues

1. **"No sheets found" error**
   - Ensure your Excel file has at least one sheet with data
   - Check that the file isn't corrupted

2. **"No suitable chart candidates"**
   - Upload data with numeric and/or date columns
   - Ensure data is properly formatted

3. **PowerPoint generation fails**
   - Check that all dependencies are installed
   - Ensure sufficient disk space for temporary files

4. **Charts not displaying**
   - Refresh the browser page
   - Check browser console for JavaScript errors

### Performance Tips

- **Large files**: Consider splitting data into smaller sheets
- **Memory usage**: Close other applications if experiencing slowdowns
- **Browser**: Use Chrome or Firefox for best performance

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

If you encounter any issues:

1. Check the troubleshooting section above
2. Review the error messages in the Streamlit interface
3. Ensure all dependencies are correctly installed
4. Try with a smaller, simpler Excel file first

---

**Made with ❤️ for data analysts and business professionals** 