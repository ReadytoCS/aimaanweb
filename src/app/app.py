import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import tempfile
import os
import pyperclip

from chart_utils import (
    detect_chart_candidates,
    grouped_bar_chart,
    stacked_bar_chart,
    line_chart,
    area_chart,
    pie_chart,
    donut_chart,
    scatter_chart,
    bubble_chart,
    radar_chart,
    treemap_chart,
    THEME_COLORS,
)
from insight_utils import generate_insights
from export_utils import export_chart_as_png, copy_chart_text_to_clipboard

st.set_page_config(
    page_title="ExcelInsight Pro",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Remove sidebar entirely ---
# All controls, help, and onboarding are now in the main workflow area.

# --- Subtle branding in header ---
st.markdown('<h1 class="main-header">ExcelInsight Pro</h1>', unsafe_allow_html=True)
st.markdown("<div style='text-align:center;color:#1255b5;font-weight:600;margin-bottom:1.5em;'>By Aimaan Shergill</div>", unsafe_allow_html=True)

# --- Floating help button (bottom right) ---
help_button_style = '''
<style>
.fab-help {
  position: fixed;
  bottom: 32px;
  right: 32px;
  z-index: 9999;
  background: linear-gradient(90deg,#1255b5 0%,#007C91 100%);
  color: #fff;
  border: none;
  border-radius: 50%;
  width: 60px;
  height: 60px;
  font-size: 2em;
  box-shadow: 0 2px 8px rgba(18,85,181,0.12);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.2s;
}
.fab-help:hover {
  background: linear-gradient(90deg,#007C91 0%,#1255b5 100%);
}
</style>
'''
st.markdown(help_button_style, unsafe_allow_html=True)

if 'show_help' not in st.session_state:
    st.session_state['show_help'] = False

help_btn = st.button("Help", key="fab_help", help="Help & Onboarding", use_container_width=False)
if help_btn:
    st.session_state['show_help'] = not st.session_state['show_help']

# --- Onboarding/FAQ modal (shown when help button is clicked) ---
if st.session_state['show_help']:
    with st.expander("Welcome to ExcelInsight Pro (Click to close)", expanded=True):
        st.markdown("""
        **How to use ExcelInsight Pro:**
        1. Upload your Excel file (max 20 MB)
        2. Select a sheet and review your data
        3. Choose a chart type and customize
        4. Use Slide Frame for export-ready visuals
        5. Download or copy insights instantly
        
        _Tip: All controls are in the main area. Use this button anytime for help._
        """)
        st.markdown("---")
        st.markdown("**FAQ**")
        st.markdown("- **How do I export?** Use the export buttons below the chart.\n- **How do I get insights?** Insights are generated automatically after chart creation.\n- **How do I swap axes?** Use the 'Swap Axes' toggle in chart settings.")
        st.markdown("---")
        st.markdown("<div style='text-align:center;color:#888;font-size:1em;margin-top:2em;'>Made with love by Aimaan Shergill | <a href='mailto:amaan.shergill@gmail.com'>Contact</a> | <a href='https://www.linkedin.com/in/aimaanshergill/' target='_blank'>LinkedIn</a></div>", unsafe_allow_html=True)

# 3. Section dividers, card-style sections, and clear headings
st.markdown('<div style="height:2em"></div>', unsafe_allow_html=True)
st.markdown('<hr style="border:0;border-top:2px solid #e5e5e5;margin:2em 0;">', unsafe_allow_html=True)

# 4. Use more whitespace, card-style containers, and subtle shadows
st.markdown('''
<style>
.card-section {
    background: #fff;
    border-radius: 18px;
    box-shadow: 0 2px 16px rgba(0,0,0,0.06);
    padding: 2.5em 2em 2em 2em;
    margin-bottom: 2.5em;
}
.cta-btn {
    background: linear-gradient(90deg,#1255b5 0%,#007C91 100%);
    color: #fff !important;
    font-weight: 600;
    border-radius: 999px;
    padding: 0.75em 2em;
    font-size: 1.1em;
    border: none;
    box-shadow: 0 2px 8px rgba(18,85,181,0.08);
    transition: background 0.2s;
}
.cta-btn:hover {
    background: linear-gradient(90deg,#007C91 0%,#1255b5 100%);
}
.section-title {
    font-size: 2.2rem;
    font-weight: 800;
    color: #1255b5;
    margin-bottom: 1.2em;
    letter-spacing: -1px;
}
hr {
    border:0;
    border-top:2px solid #e5e5e5;
    margin:2em 0;
}
input, select, textarea {
    border-radius: 8px !important;
    border: 1.5px solid #d1d5db !important;
    font-size: 1.08em !important;
    padding: 0.5em 1em !important;
}
</style>
''', unsafe_allow_html=True)

# 5. Footer with credits and contact
st.markdown('<hr style="border:0;border-top:2px solid #e5e5e5;margin:2em 0;">', unsafe_allow_html=True)
st.markdown("<div style='text-align:center;color:#888;font-size:1em;margin-top:2em;'>Made with love by Aimaan Shergill | <a href='mailto:amaan.shergill@gmail.com'>Contact</a> | <a href='https://www.linkedin.com/in/aimaanshergill/' target='_blank'>LinkedIn</a></div>", unsafe_allow_html=True)

st.markdown("""
<style>
    .main-header {
        color: #1255b5;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
    }
    .deck-preview {
        background: #f8f9fa;
        border-radius: 16px;
        width: 1280px;
        height: 720px;
        margin: 0 auto;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        box-shadow: 0 2px 16px rgba(0,0,0,0.04);
        padding: 32px 0;
    }
    .slide-caption {
        color: #888;
        font-size: 1.1rem;
        text-align: center;
        margin-top: 0.5rem;
    }
    .insight-bullet {
        font-size: 1.25rem;
        margin-bottom: 0.5rem;
        color: #666;
    }
    .insight-toggle {
        background: #f0f2f6;
        border-radius: 8px;
        padding: 12px;
        margin: 16px 0;
    }
    .export-dropdown {
        margin: 16px 0;
    }
    .chart-container {
        margin: 24px 0;
    }
    .chart-settings {
        background: #f8f9fa;
        border-radius: 8px;
        padding: 16px;
        margin: 16px 0;
    }
    .chart-type-tooltip {
        font-size: 0.9rem;
        color: #666;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

# Add custom CSS for section headings and responsive layout
st.markdown('''
<style>
.section-title {
    font-size: 2rem;
    font-weight: 700;
    margin: 2em 0 1em 0;
    color: var(--text-color, #1255b5);
}
@media (min-width: 900px) {
    .responsive-row {display: flex; gap: 2em; align-items: flex-start;}
    .responsive-col {flex: 1; min-width: 0;}
}
@media (max-width: 899px) {
    .responsive-row {display: block;}
    .responsive-col {width: 100%;}
}
</style>
''', unsafe_allow_html=True)

# Detect Streamlit theme (dark/light)
def get_theme():
    try:
        bg = st.get_option("theme.backgroundColor")
        if bg and (bg.lower() == '#0e1117' or 'dark' in bg.lower()):
            return 'dark'
    except Exception:
        pass
    return 'light'
THEME_MODE = get_theme()

# Chart type descriptions for tooltips
CHART_DESCRIPTIONS = {
    "Grouped Bar": "Best for comparing multiple metrics across categories",
    "Stacked Bar": "Shows composition and total values",
    "Line": "Ideal for trends over time or continuous data",
    "Area": "Shows volume and trends with filled areas",
    "Pie": "Use for part-to-whole relationships",
    "Donut": "Modern alternative to pie charts",
    "Scatter": "Shows correlation between two variables",
    "Bubble": "Scatter plot with size representing a third variable",
    "Radar": "Compare multiple metrics on polar axes",
    "Treemap": "Hierarchical data visualization"
}

# --- Custom chart animation: fade-in and scale-up ---
import time
chart_anim_style = '''
<style>
@keyframes fadeInScale {
  0% { opacity: 0; transform: scale(0.96); }
  100% { opacity: 1; transform: scale(1); }
}
.animated-chart {
  animation: fadeInScale 0.7s cubic-bezier(.4,1.4,.6,1) 1;
}
</style>
'''
st.markdown(chart_anim_style, unsafe_allow_html=True)

def main():
    st.markdown('<h1 class="main-header">ExcelInsight Pro</h1>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:1.2em;margin-bottom:1.5em;color:#444;">Upload Excel. Customize your chart. Export insights in seconds.</div>', unsafe_allow_html=True)

    # Sticky deck preview mode at top
    deck_preview = st.checkbox("Show in Slide Frame", value=False, key="deck_preview")

    # Section: Upload Excel File
    st.markdown('<div class="section-title">📁 Upload Excel File</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "Choose an Excel file (.xls or .xlsx)",
        type=['xls', 'xlsx'],
        help="Maximum file size: 20 MB"
    )
    
    if uploaded_file is not None:
        file_size = len(uploaded_file.getvalue())
        if file_size > 20 * 1024 * 1024:
            st.error("❌ File size exceeds 20 MB limit. Please upload a smaller file.")
            return
            
        try:
            excel_file = pd.ExcelFile(uploaded_file)
            sheet_names = excel_file.sheet_names
            if not sheet_names:
                st.error("❌ No sheets found in the Excel file.")
                return
                
            st.success(f"✅ File uploaded. Data looks good!")
            
            # Section: Select Sheet
            st.markdown('<div class="section-title">📄 Select Sheet</div>', unsafe_allow_html=True)
            selected_sheet = st.selectbox(
                "Choose a sheet to analyze:",
                sheet_names,
                index=0
            )
            
            with st.spinner("Loading data..."):
                try:
                    df = pd.read_excel(uploaded_file, sheet_name=selected_sheet)
                except Exception as e:
                    st.error(f"❌ Error loading sheet '{selected_sheet}': {str(e)}")
                    return
            # Data upload clarity: auto-rename and prompt for NaN/empty headers
            renamed_cols = []
            for col in df.columns:
                # Defensive: ensure col is always a string
                col_str = str(col) if not isinstance(col, str) else col
                # Fix: use explicit checks, never use Series in boolean context
                is_ambiguous = False
                if isinstance(col, str):
                    if col.startswith('Unnamed: 0') or col.strip() == '':
                        is_ambiguous = True
                else:
                    # If col is not a string, check if it's NaN or empty string
                    if pd.isna(col) or col_str.strip() == '':
                        is_ambiguous = True
                if is_ambiguous:
                    old_col = col
                    guess = 'Category' if (isinstance(col, str) and col.startswith('Unnamed')) or pd.isna(col) else 'Label'
                    new_col = st.text_input(f"Column '{old_col}' is ambiguous. Please name it:", value=guess, key=f"fixcol_{old_col}")
                    df = df.rename(columns={col: new_col})
                    renamed_cols.append((old_col, new_col))
            # End fix
            if renamed_cols:
                msg = "<br>".join([f"Renamed '{o}' → '{n}'" for o, n in renamed_cols])
                st.info(f"{msg}", icon="ℹ️")
            display_df = df.copy()
            
            # Section: Data Overview
            st.markdown('<div class="section-title">📊 Data Overview</div>', unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Rows", len(df))
            with col2:
                st.metric("Columns", len(df.columns))
            with col3:
                st.metric("Memory Usage", f"{df.memory_usage(deep=True).sum() / 1024:.1f} KB")
                
            st.markdown("#### Preview of Data")
            st.dataframe(display_df.head(10), use_container_width=True)

            # Auto-detect chart candidates
            chart_candidates = detect_chart_candidates(df)
            
            if chart_candidates:
                # Color palette selection
                st.markdown("### 🎨 Chart Customization")
                selected_theme = st.selectbox(
                    "🎨 Select Chart Theme",
                    list(THEME_COLORS.keys()),
                    index=st.session_state.get('last_theme', 0),
                    key="theme_selector"
                )
                selected_colors = THEME_COLORS[selected_theme]
                st.session_state['last_theme'] = list(THEME_COLORS.keys()).index(selected_theme)
                
                # Chart type selection with tooltips
                available_charts = list(chart_candidates.keys())
                
                # Auto-select if only one chart type is viable
                if len(available_charts) == 1:
                    selected_chart = available_charts[0]
                    st.info(f"💡 Auto-detected: {selected_chart} chart")
                else:
                    selected_chart = st.selectbox(
                        "📊 Chart Type",
                        available_charts,
                        index=st.session_state.get('last_chart_type', 0),
                        help="Choose a chart style to preview.",
                        key="chart_type_selector"
                    )
                    st.markdown(f"<div class='chart-type-tooltip'>{CHART_DESCRIPTIONS.get(selected_chart, '')}</div>", unsafe_allow_html=True)
                    st.session_state['last_chart_type'] = available_charts.index(selected_chart)
                
                # Get chart configuration
                chart_config = chart_candidates[selected_chart]
                cat_col = chart_config["category"]
                num_cols = chart_config["metrics"]

                # --- Guidance and relabels ---
                st.markdown("<b>Category (X-Axis)</b> <span title='This is the main grouping, like Product or Region.' style='cursor: help;'>ℹ️</span>:", unsafe_allow_html=True)
                st.markdown(f"<span style='font-size:1.1em;font-weight:500'>{cat_col}</span>", unsafe_allow_html=True)
                st.markdown("<b>Metrics (Y-Axis)</b> <span title='These are the numbers you want to compare, like Revenue or Units.' style='cursor: help;'>ℹ️</span>:", unsafe_allow_html=True)
                st.markdown(f"<span style='font-size:1.1em;font-weight:500'>{', '.join(num_cols)}</span>", unsafe_allow_html=True)

                # Chart Settings (collapsed by default)
                with st.expander("🛠 Chart Appearance", expanded=False):
                    st.markdown('<div class="chart-settings">', unsafe_allow_html=True)
                    col1, col2 = st.columns(2)
                    with col1:
                        show_labels = st.checkbox("Show Value Labels", value=True, key="show_labels")
                        show_legend = st.checkbox("Show Legend", value=True, key="show_legend")
                        rotate_labels = st.checkbox("Rotate X-Axis Labels", value=False, key="rotate_labels")
                    with col2:
                        if selected_chart in ["Pie", "Donut"]:
                            show_percentage = st.checkbox("Show Percentage Labels", value=True, key="show_percentage")
                        else:
                            show_percentage = False
                        limit_categories = st.selectbox(
                            "Limit Top N Categories",
                            ["All", "5", "10", "15"],
                            index=0,
                            key="limit_categories"
                        )
                    st.markdown('</div>', unsafe_allow_html=True)

                # --- Quick Templates with emoji, tooltips, and highlight ---
                templates = {
                    "📊 Professional Bar Chart (for presentations)": {
                        "desc": "Professional grouped bar chart for client deliverables.",
                        "chart_type": "Grouped Bar",
                        "theme": "McKinsey (clean + formal)",
                        "show_labels": True,
                        "show_legend": True,
                        "rotate_labels": False
                    },
                    "🎯 Executive summary slide": {
                        "desc": "Pie chart for high-level takeaways.",
                        "chart_type": "Pie",
                        "theme": "Google (bright + friendly)",
                        "show_labels": True,
                        "show_legend": True,
                        "rotate_labels": False
                    },
                    "📈 Time trend for presentation": {
                        "desc": "Line chart for time series or trends.",
                        "chart_type": "Line",
                        "theme": "Slide Pop (fun for Keynote)",
                        "show_labels": True,
                        "show_legend": True,
                        "rotate_labels": False
                    }
                }
                template_names = list(templates.keys())
                selected_template = st.selectbox(
                    "📊 Layout Presets",
                    ["None"] + template_names,
                    index=0,
                    help="Apply a preset for common use cases."
                )
                if selected_template != "None":
                    preset = templates[selected_template]
                    st.info(f"{selected_template}: {preset['desc']}")
                    if preset["chart_type"] in chart_candidates:
                        selected_chart = preset["chart_type"]
                        st.session_state['last_chart_type'] = list(chart_candidates.keys()).index(selected_chart)
                    if preset["theme"] in THEME_COLORS:
                        selected_theme = preset["theme"]
                        st.session_state['last_theme'] = list(THEME_COLORS.keys()).index(selected_theme)
                    show_labels = preset["show_labels"]
                    show_legend = preset["show_legend"]
                    rotate_labels = preset["rotate_labels"]

                # --- Live label editing with placeholders, reset, and fallback ---
                def smart_default(val, fallback):
                    return val if val.strip() else fallback

                def reset_label(label_key, default):
                    st.session_state[label_key] = default

                col_title, col_x, col_y = st.columns([2,1,1])
                def_title = f"{selected_chart} of {', '.join(num_cols)} by {cat_col}"
                def_x = cat_col
                def_y = ", ".join(num_cols)
                with col_title:
                    chart_title = st.text_input(
                        "Chart Title",
                        value=st.session_state.get("chart_title", def_title),
                        placeholder="e.g. Category Breakdown by Value",
                        key="chart_title"
                    )
                    if st.button("↻ Reset", key="reset_title"): reset_label("chart_title", def_title)
                with col_x:
                    x_axis_label = st.text_input(
                        "X-Axis Label",
                        value=st.session_state.get("x_axis_label", def_x),
                        placeholder="e.g. Region",
                        key="x_axis_label"
                    )
                    if st.button("↻ Reset", key="reset_x"): reset_label("x_axis_label", def_x)
                with col_y:
                    y_axis_label = st.text_input(
                        "Y-Axis Label",
                        value=st.session_state.get("y_axis_label", def_y),
                        placeholder="e.g. Revenue, Units",
                        key="y_axis_label"
                    )
                    if st.button("↻ Reset", key="reset_y"): reset_label("y_axis_label", def_y)
                chart_title = smart_default(chart_title, def_title)
                x_axis_label = smart_default(x_axis_label, def_x)
                y_axis_label = smart_default(y_axis_label, def_y)

                # Section: Chart Controls & Preview (responsive)
                st.markdown('<div class="section-title">📈 Chart & Settings</div>', unsafe_allow_html=True)
                st.markdown('<div class="responsive-row">', unsafe_allow_html=True)
                with st.container():
                    st.markdown('<div class="responsive-col">', unsafe_allow_html=True)
                    # ... chart controls (template, type, settings, labels) ...
                    st.markdown('</div>', unsafe_allow_html=True)
                with st.container():
                    st.markdown('<div class="responsive-col">', unsafe_allow_html=True)
                    # ... chart preview ...
                    st.markdown('</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

                # --- Axis Swap Option ---
                swap_axes_enabled = selected_chart in ["Grouped Bar", "Stacked Bar", "Line", "Area"]
                swap_axes = False
                if swap_axes_enabled:
                    swap_axes = st.checkbox("Swap Axes: Show Metrics on X-Axis", value=False, key="swap_axes")

                # --- Prepare data for chart based on axis swap ---
                chart_cat_col = cat_col
                chart_num_cols = num_cols
                chart_df = df.copy()
                chart_x_label = x_axis_label
                chart_y_label = y_axis_label
                chart_title_final = chart_title
                if swap_axes:
                    # Transpose: metrics become x-axis, categories become series
                    chart_cat_col = "Metric"
                    chart_num_cols = list(df[cat_col].unique())
                    chart_df = pd.DataFrame({
                        "Metric": num_cols
                    })
                    for cat in chart_num_cols:
                        chart_df[cat] = [df[df[cat_col] == cat][metric].values[0] if not df[df[cat_col] == cat][metric].empty else None for metric in num_cols]
                    chart_x_label = y_axis_label  # Swap labels
                    chart_y_label = x_axis_label
                    chart_title_final = f"{selected_chart} of {', '.join(chart_num_cols)} by Metric"

                # --- Chart Preview (only one location at a time, with advanced visual polish) ---
                with st.container():
                    st.markdown('<div class="chart-container" style="margin-bottom:2em;">', unsafe_allow_html=True)
                    fig = None
                    if selected_chart == "Grouped Bar":
                        fig = grouped_bar_chart(chart_df, chart_cat_col, chart_num_cols, selected_colors, show_labels, rotate_labels, show_legend, limit_categories)
                    elif selected_chart == "Stacked Bar":
                        fig = stacked_bar_chart(chart_df, chart_cat_col, chart_num_cols, selected_colors, show_labels, rotate_labels, show_legend, limit_categories)
                    elif selected_chart == "Line":
                        fig = line_chart(chart_df, chart_cat_col, chart_num_cols, selected_colors, show_labels, show_legend, limit_categories)
                    elif selected_chart == "Area":
                        fig = area_chart(chart_df, chart_cat_col, chart_num_cols, selected_colors, show_labels, show_legend, limit_categories)
                    elif selected_chart == "Pie":
                        fig = pie_chart(chart_df, chart_cat_col, chart_num_cols, selected_colors, show_labels, show_percentage, limit_categories)
                    elif selected_chart == "Donut":
                        fig = donut_chart(chart_df, chart_cat_col, chart_num_cols, selected_colors, show_labels, show_percentage, limit_categories)
                    elif selected_chart == "Scatter":
                        fig = scatter_chart(chart_df, chart_cat_col, chart_num_cols, selected_colors, show_labels, show_legend, limit_categories)
                    elif selected_chart == "Bubble":
                        fig = bubble_chart(chart_df, chart_cat_col, chart_num_cols, selected_colors, show_labels, show_legend, limit_categories)
                    elif selected_chart == "Radar":
                        fig = radar_chart(chart_df, chart_cat_col, chart_num_cols, selected_colors, show_labels, show_legend, limit_categories)
                    elif selected_chart == "Treemap":
                        fig = treemap_chart(chart_df, chart_cat_col, chart_num_cols, selected_colors, show_labels, limit_categories)
                    # --- Advanced visual polish ---
                    if fig is not None:
                        # Universal layout polish
                        fig.update_layout(
                            font=dict(family="Inter, Arial, sans-serif", size=18, color="#222"),
                            title=dict(font=dict(size=28, color="#1a1a1a", family="Inter, Arial, sans-serif"), x=0.01, xanchor="left"),
                            plot_bgcolor="white",
                            paper_bgcolor="white",
                            margin=dict(l=80, r=40, t=80, b=80),
                            legend=dict(
                                orientation="h",
                                yanchor="bottom",
                                y=1.02,
                                xanchor="right",
                                x=1,
                                font=dict(size=17, color="#222"),
                                bgcolor="rgba(0,0,0,0)",
                                borderwidth=0
                            ),
                            xaxis=dict(
                                showgrid=True,
                                gridcolor="#e5e5e5",
                                linecolor="#222",
                                linewidth=1.2,
                                ticks="outside",
                                ticklen=6,
                                tickcolor="#222",
                                mirror=True,
                                tickfont=dict(size=16),
                                title_font=dict(size=20, color="#222"),
                                automargin=True
                            ),
                            yaxis=dict(
                                showgrid=True,
                                gridcolor="#e5e5e5",
                                linecolor="#222",
                                linewidth=1.2,
                                ticks="outside",
                                ticklen=6,
                                tickcolor="#222",
                                mirror=True,
                                tickfont=dict(size=16),
                                title_font=dict(size=20, color="#222"),
                                automargin=True
                            ),
                            hovermode="x unified"
                        )
                        # Slide mode: boost font and chart size
                        if deck_preview:
                            fig.update_layout(
                                width=1280,
                                height=720,
                                font=dict(size=22),
                                title=dict(font=dict(size=36)),
                                legend=dict(font=dict(size=20)),
                                xaxis=dict(tickfont=dict(size=20), title_font=dict(size=24)),
                                yaxis=dict(tickfont=dict(size=20), title_font=dict(size=24)),
                            )
                        # Add note for best export quality
                        st.caption("For best export quality, use Slide Frame mode and PNG download.")
                    # Only show in one place: slide frame or normal
                    if deck_preview:
                        st.markdown('<div class="deck-preview animated-chart">', unsafe_allow_html=True)
                        if fig is not None:
                            st.plotly_chart(fig, use_container_width=False)
                        st.markdown('<div class="slide-caption">Slide Preview Mode</div>', unsafe_allow_html=True)
                        st.markdown('</div>', unsafe_allow_html=True)
                    else:
                        if fig is not None:
                            st.markdown('<div class="animated-chart">', unsafe_allow_html=True)
                            st.plotly_chart(fig, use_container_width=True)
                            st.markdown('</div>', unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)
                    # --- Download Chart as PNG button ---
                    if fig is not None:
                        img_bytes = export_chart_as_png(fig, deck_mode=deck_preview)
                        st.download_button(
                            "📸 Download Chart as PNG",
                            data=img_bytes,
                            file_name=f"{selected_chart.replace(' ', '_').lower()}_chart.png",
                            mime="image/png",
                            help="Download this chart as a high-res PNG for your slides."
                        )
                        st.success("Chart image ready for download!")
                
                # Section: Export
                st.markdown('<div class="section-title">📤 Export</div>', unsafe_allow_html=True)
                export_col1, export_col2, export_col3 = st.columns(3)
                
                with export_col1:
                    # PNG Export
                    if st.button("📷 Download PNG", help="Download chart for use in slides"):
                        try:
                            img_bytes = export_chart_as_png(fig, deck_mode=deck_preview)
                            st.download_button(
                                label="💾 Save PNG",
                                data=img_bytes,
                                file_name=f"{selected_chart.replace(' ', '_').lower()}_chart.png",
                                mime="image/png",
                            )
                        except Exception as e:
                            st.error(f"Error generating PNG: {str(e)}")
                
                with export_col2:
                    # Copy to clipboard
                    if st.button("📋 Copy Chart + Insights"):
                        try:
                            insights = generate_insights(df, cat_col, num_cols)
                            slide_text = copy_chart_text_to_clipboard(selected_chart, cat_col, num_cols, insights)
                            pyperclip.copy(slide_text)
                            st.success("✅ Copied to clipboard!")
                        except Exception as e:
                            st.warning("Copying to clipboard is not supported in this environment.")
                
                with export_col3:
                    # PPTX Export (placeholder)
                    if st.button("📊 Export to PPTX", help="Download chart with auto-insights in PowerPoint format"):
                        st.info("PPTX export feature coming soon!")
                
                # Section: Insights
                st.markdown('<div class="section-title">📌 Strategic Takeaways</div>', unsafe_allow_html=True)
                auto_insights = generate_insights(df, cat_col, num_cols)
                
                # Only show insights if they're meaningful
                if auto_insights and len(auto_insights) > 0:
                    st.markdown("### 📌 Strategic Takeaways")
                    show_insights = st.checkbox("🧠 Show Strategic Takeaways", value=False, key="show_insights")
                    
                    if show_insights:
                        with st.container():
                            st.markdown('<div class="insight-toggle">', unsafe_allow_html=True)
                            
                            # Initialize session state for edited insights
                            if 'edited_insights' not in st.session_state:
                                st.session_state['edited_insights'] = auto_insights.copy()
                            
                            # If number of insights changed, reset
                            if len(st.session_state['edited_insights']) != len(auto_insights):
                                st.session_state['edited_insights'] = auto_insights.copy()
                            
                            # Display insights with editing capability
                            for i, insight in enumerate(auto_insights):
                                edited = st.text_area(
                                    f"Edit insight {i+1}", 
                                    value=st.session_state['edited_insights'][i], 
                                    key=f"insight_edit_{i}",
                                    height=80
                                )
                                st.session_state['edited_insights'][i] = edited
                                st.markdown(f"<div class='insight-bullet'>• {edited}</div>", unsafe_allow_html=True)
                            
                            st.markdown('</div>', unsafe_allow_html=True)
                            
                            # Copy insights button
                            if st.button("📋 Copy All Insights"):
                                try:
                                    insights_text = "\n".join(st.session_state['edited_insights'])
                                    pyperclip.copy(insights_text)
                                    st.success("✅ Insights copied to clipboard!")
                                except Exception as e:
                                    st.warning("Copying to clipboard is not supported in this environment.")
            else:
                st.warning("⚠️ No suitable chart pattern detected. Try uploading a file with one categorical and multiple numeric columns.")
                
        except Exception as e:
            st.error(f"❌ Error processing file: {str(e)}")
    else:
        st.markdown("""
        ### 🚀 How to Use ExcelInsight Pro
        1. **Upload** your Excel file (.xls or .xlsx) - max 20 MB
        2. **Select** a sheet to analyze
        3. **Choose** from 10+ chart types
        4. **Customize** with themes and settings
        5. **Export** charts as PNG or copy insights
        ---
        **Supported Chart Types:**
        - 📊 **Bar Charts**: Grouped, Stacked
        - 📈 **Trend Charts**: Line, Area
        - 🥧 **Part-to-Whole**: Pie, Donut, Treemap
        - 📊 **Correlation**: Scatter, Bubble
        - 🎯 **Multi-Metric**: Radar
        """)

if __name__ == "__main__":
    main() 