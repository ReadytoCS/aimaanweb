import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from datetime import datetime

# Multiple color palette options
THEME_COLORS = {
    "McKinsey (clean + formal)": ["#002F6C", "#A6192E", "#007C91", "#5C6770"],
    "Google (bright + friendly)": ["#4285F4", "#DB4437", "#F4B400", "#0F9D58"],
    "Monochrome": ["#000000", "#444444", "#777777", "#BBBBBB"],
    "Slide Pop (fun for Keynote)": ["#6A0DAD", "#FF6F61", "#20B2AA", "#FFD700"],
    "High Contrast": ["#000000", "#FF0000", "#00FF00", "#0000FF"]
}

# Legacy support for existing code
MCKINSEY_COLORS = THEME_COLORS["McKinsey (clean + formal)"]

def detect_chart_candidates(df):
    """
    Detect all possible chart types based on data structure.
    Returns a dict with chart types and their requirements.
    """
    df = df.copy()
    columns = list(df.columns)
    
    # Clean column names for display
    for col in columns:
        if col.startswith('Unnamed: 0'):
            df = df.rename(columns={col: 'Category'})
    
    # Detect categorical and numeric columns
    cat_cols = []
    num_cols = []
    
    for col in columns:
        if df[col].dtype == object or col.lower().startswith("unnamed"):
            cat_cols.append(col)
        elif pd.api.types.is_numeric_dtype(df[col]):
            num_cols.append(col)
    
    # If no categorical columns found, treat first as categorical
    if not cat_cols and columns:
        cat_cols = [columns[0]]
        num_cols = [col for col in columns[1:] if pd.api.types.is_numeric_dtype(df[col])]
    
    candidates = {}
    
    # Single metric charts (1 category + 1 numeric)
    if len(cat_cols) >= 1 and len(num_cols) >= 1:
        candidates["Pie"] = {"category": cat_cols[0], "metrics": [num_cols[0]]}
        candidates["Donut"] = {"category": cat_cols[0], "metrics": [num_cols[0]]}
        candidates["Treemap"] = {"category": cat_cols[0], "metrics": [num_cols[0]]}
        
        # Line and Area charts (if data looks temporal)
        if len(df) > 1:
            candidates["Line"] = {"category": cat_cols[0], "metrics": num_cols}
            candidates["Area"] = {"category": cat_cols[0], "metrics": num_cols}
    
    # Multi-metric charts (1 category + multiple numeric)
    if len(cat_cols) >= 1 and len(num_cols) >= 2:
        candidates["Grouped Bar"] = {"category": cat_cols[0], "metrics": num_cols}
        candidates["Stacked Bar"] = {"category": cat_cols[0], "metrics": num_cols}
        candidates["Radar"] = {"category": cat_cols[0], "metrics": num_cols}
        
        # Scatter plot (2 metrics)
        if len(num_cols) >= 2:
            candidates["Scatter"] = {"category": cat_cols[0], "metrics": num_cols[:2]}
        
        # Bubble chart (3 metrics)
        if len(num_cols) >= 3:
            candidates["Bubble"] = {"category": cat_cols[0], "metrics": num_cols[:3]}
    
    return candidates

def detect_multi_metric(df):
    """Legacy function for backward compatibility."""
    candidates = detect_chart_candidates(df)
    if "Grouped Bar" in candidates:
        return candidates["Grouped Bar"]["category"], candidates["Grouped Bar"]["metrics"]
    return None, None

def mckinsey_layout(title, x_title, y_title):
    """Returns a Plotly layout dict with McKinsey-style settings."""
    return dict(
        title=dict(text=title, font=dict(family="Inter, Arial, sans-serif", size=22, color="#222"), x=0.01, xanchor="left"),
        font=dict(family="Inter, Arial, sans-serif", size=16, color="#222"),
        plot_bgcolor="white",
        paper_bgcolor="white",
        xaxis=dict(
            title=x_title,
            showgrid=False,
            linecolor="#222",
            linewidth=1,
            ticks="outside",
            ticklen=6,
            tickcolor="#222",
            mirror=True,
            tickfont=dict(size=14),
        ),
        yaxis=dict(
            title=y_title,
            showgrid=False,
            linecolor="#222",
            linewidth=1,
            ticks="outside",
            ticklen=6,
            tickcolor="#222",
            mirror=True,
            tickfont=dict(size=14),
        ),
        margin=dict(l=60, r=30, t=60, b=60),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(size=15),
        ),
        height=600,
        width=1100,
    )

def grouped_bar_chart(df, cat_col, num_cols, colors=None, show_labels=False, rotate_labels=False, show_legend=True, limit_categories=None):
    if colors is None:
        colors = MCKINSEY_COLORS
    
    # Apply category limit
    if limit_categories and limit_categories != "All":
        df = df.head(int(limit_categories))
    
    fig = go.Figure()
    for i, col in enumerate(num_cols):
        fig.add_trace(
            go.Bar(
                x=df[cat_col],
                y=df[col],
                name=col,
                marker_color=colors[i % len(colors)],
                text=df[col].round(1) if show_labels else None,
                textposition='auto' if show_labels else None,
            )
        )
    
    layout = mckinsey_layout(
        f"Grouped Bar: {', '.join(num_cols)} by {cat_col}",
        cat_col,
        "Value",
    )
    
    if rotate_labels:
        layout['xaxis']['tickangle'] = -45
    
    if not show_legend:
        layout['showlegend'] = False
    
    fig.update_layout(**layout, barmode="group")
    return fig

def stacked_bar_chart(df, cat_col, num_cols, colors=None, show_labels=False, rotate_labels=False, show_legend=True, limit_categories=None):
    if colors is None:
        colors = MCKINSEY_COLORS
    
    # Apply category limit
    if limit_categories and limit_categories != "All":
        df = df.head(int(limit_categories))
    
    fig = go.Figure()
    for i, col in enumerate(num_cols):
        fig.add_trace(
            go.Bar(
                x=df[cat_col],
                y=df[col],
                name=col,
                marker_color=colors[i % len(colors)],
                text=df[col].round(1) if show_labels else None,
                textposition='auto' if show_labels else None,
            )
        )
    
    layout = mckinsey_layout(
        f"Stacked Bar: {', '.join(num_cols)} by {cat_col}",
        cat_col,
        "Value",
    )
    
    if rotate_labels:
        layout['xaxis']['tickangle'] = -45
    
    if not show_legend:
        layout['showlegend'] = False
    
    fig.update_layout(**layout, barmode="stack")
    return fig

def line_chart(df, cat_col, num_cols, colors=None, show_labels=False, show_legend=True, limit_categories=None):
    if colors is None:
        colors = MCKINSEY_COLORS
    
    # Apply category limit
    if limit_categories and limit_categories != "All":
        df = df.head(int(limit_categories))
    
    fig = go.Figure()
    for i, col in enumerate(num_cols):
        fig.add_trace(
            go.Scatter(
                x=df[cat_col],
                y=df[col],
                mode='lines+markers',
                name=col,
                line_color=colors[i % len(colors)],
                text=df[col].round(1) if show_labels else None,
                textposition='top center' if show_labels else None,
            )
        )
    
    layout = mckinsey_layout(
        f"Line Chart: {', '.join(num_cols)} by {cat_col}",
        cat_col,
        "Value",
    )
    
    if not show_legend:
        layout['showlegend'] = False
    
    fig.update_layout(**layout)
    return fig

def area_chart(df, cat_col, num_cols, colors=None, show_labels=False, show_legend=True, limit_categories=None):
    if colors is None:
        colors = MCKINSEY_COLORS
    
    # Apply category limit
    if limit_categories and limit_categories != "All":
        df = df.head(int(limit_categories))
    
    fig = go.Figure()
    for i, col in enumerate(num_cols):
        fig.add_trace(
            go.Scatter(
                x=df[cat_col],
                y=df[col],
                mode='lines',
                fill='tonexty',
                name=col,
                line_color=colors[i % len(colors)],
                text=df[col].round(1) if show_labels else None,
                textposition='top center' if show_labels else None,
            )
        )
    
    layout = mckinsey_layout(
        f"Area Chart: {', '.join(num_cols)} by {cat_col}",
        cat_col,
        "Value",
    )
    
    if not show_legend:
        layout['showlegend'] = False
    
    fig.update_layout(**layout)
    return fig

def pie_chart(df, cat_col, num_cols, colors=None, show_labels=False, show_percentage=False, limit_categories=None):
    if colors is None:
        colors = MCKINSEY_COLORS
    
    # Apply category limit
    if limit_categories and limit_categories != "All":
        df = df.head(int(limit_categories))
    
    # Calculate percentages if requested
    if show_percentage:
        total = df[num_cols[0]].sum()
        df = df.copy()
        df['percentage'] = (df[num_cols[0]] / total * 100).round(1)
        text_values = df['percentage'].astype(str) + '%'
    elif show_labels:
        text_values = df[num_cols[0]].round(1)
    else:
        text_values = None
    
    fig = go.Figure(data=[go.Pie(
        labels=df[cat_col],
        values=df[num_cols[0]],
        text=text_values,
        textinfo='text+label' if text_values else 'label',
        marker_colors=colors[:len(df)]
    )])
    
    fig.update_layout(
        title=f"Pie Chart: {num_cols[0]} by {cat_col}",
        height=600,
        width=1100,
        showlegend=True
    )
    return fig

def donut_chart(df, cat_col, num_cols, colors=None, show_labels=False, show_percentage=False, limit_categories=None):
    if colors is None:
        colors = MCKINSEY_COLORS
    
    # Apply category limit
    if limit_categories and limit_categories != "All":
        df = df.head(int(limit_categories))
    
    # Calculate percentages if requested
    if show_percentage:
        total = df[num_cols[0]].sum()
        df = df.copy()
        df['percentage'] = (df[num_cols[0]] / total * 100).round(1)
        text_values = df['percentage'].astype(str) + '%'
    elif show_labels:
        text_values = df[num_cols[0]].round(1)
    else:
        text_values = None
    
    fig = go.Figure(data=[go.Pie(
        labels=df[cat_col],
        values=df[num_cols[0]],
        text=text_values,
        textinfo='text+label' if text_values else 'label',
        marker_colors=colors[:len(df)],
        hole=0.4
    )])
    
    fig.update_layout(
        title=f"Donut Chart: {num_cols[0]} by {cat_col}",
        height=600,
        width=1100,
        showlegend=True
    )
    return fig

def scatter_chart(df, cat_col, num_cols, colors=None, show_labels=False, show_legend=True, limit_categories=None):
    if colors is None:
        colors = MCKINSEY_COLORS
    
    # Apply category limit
    if limit_categories and limit_categories != "All":
        df = df.head(int(limit_categories))
    
    fig = go.Figure()
    
    # Color by category if we have multiple categories
    if len(df[cat_col].unique()) > 1:
        for i, category in enumerate(df[cat_col].unique()):
            subset = df[df[cat_col] == category]
            fig.add_trace(
                go.Scatter(
                    x=subset[num_cols[0]],
                    y=subset[num_cols[1]],
                    mode='markers',
                    name=category,
                    marker_color=colors[i % len(colors)],
                    text=subset[num_cols[0]].round(1).astype(str) + ', ' + subset[num_cols[1]].round(1).astype(str) if show_labels else None,
                    textposition='top center' if show_labels else None,
                )
            )
    else:
        fig.add_trace(
            go.Scatter(
                x=df[num_cols[0]],
                y=df[num_cols[1]],
                mode='markers',
                marker_color=colors[0],
                text=df[num_cols[0]].round(1).astype(str) + ', ' + df[num_cols[1]].round(1).astype(str) if show_labels else None,
                textposition='top center' if show_labels else None,
            )
        )
    
    layout = mckinsey_layout(
        f"Scatter Plot: {num_cols[1]} vs {num_cols[0]}",
        num_cols[0],
        num_cols[1],
    )
    
    if not show_legend:
        layout['showlegend'] = False
    
    fig.update_layout(**layout)
    return fig

def bubble_chart(df, cat_col, num_cols, colors=None, show_labels=False, show_legend=True, limit_categories=None):
    if colors is None:
        colors = MCKINSEY_COLORS
    
    # Apply category limit
    if limit_categories and limit_categories != "All":
        df = df.head(int(limit_categories))
    
    fig = go.Figure()
    
    # Color by category if we have multiple categories
    if len(df[cat_col].unique()) > 1:
        for i, category in enumerate(df[cat_col].unique()):
            subset = df[df[cat_col] == category]
            fig.add_trace(
                go.Scatter(
                    x=subset[num_cols[0]],
                    y=subset[num_cols[1]],
                    mode='markers',
                    name=category,
                    marker=dict(
                        size=subset[num_cols[2]],
                        color=colors[i % len(colors)],
                        sizemode='area',
                        sizeref=2.*max(df[num_cols[2]])/(40.**2),
                        sizemin=4
                    ),
                    text=subset[num_cols[0]].round(1).astype(str) + ', ' + subset[num_cols[1]].round(1).astype(str) + ', ' + subset[num_cols[2]].round(1).astype(str) if show_labels else None,
                    textposition='top center' if show_labels else None,
                )
            )
    else:
        fig.add_trace(
            go.Scatter(
                x=df[num_cols[0]],
                y=df[num_cols[1]],
                mode='markers',
                marker=dict(
                    size=df[num_cols[2]],
                    color=colors[0],
                    sizemode='area',
                    sizeref=2.*max(df[num_cols[2]])/(40.**2),
                    sizemin=4
                ),
                text=df[num_cols[0]].round(1).astype(str) + ', ' + df[num_cols[1]].round(1).astype(str) + ', ' + df[num_cols[2]].round(1).astype(str) if show_labels else None,
                textposition='top center' if show_labels else None,
            )
        )
    
    layout = mckinsey_layout(
        f"Bubble Chart: {num_cols[1]} vs {num_cols[0]} (size: {num_cols[2]})",
        num_cols[0],
        num_cols[1],
    )
    
    if not show_legend:
        layout['showlegend'] = False
    
    fig.update_layout(**layout)
    return fig

def radar_chart(df, cat_col, num_cols, colors=None, show_labels=False, show_legend=True, limit_categories=None):
    if colors is None:
        colors = MCKINSEY_COLORS
    
    # Apply category limit
    if limit_categories and limit_categories != "All":
        df = df.head(int(limit_categories))
    
    fig = go.Figure()
    for i, col in enumerate(num_cols):
        fig.add_trace(
            go.Scatterpolar(
                r=df[col],
                theta=df[cat_col],
                fill="toself",
                name=col,
                line_color=colors[i % len(colors)],
            )
        )
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                showgrid=False,
                showline=True,
                linewidth=1,
                linecolor="#222",
                tickfont=dict(size=13),
            ),
            angularaxis=dict(
                tickfont=dict(size=13),
                rotation=90,
                direction="clockwise",
            ),
        ),
        showlegend=show_legend,
        **mckinsey_layout(
            f"Radar Chart: {', '.join(num_cols)} by {cat_col}",
            "",
            "",
        ),
    )
    return fig

def treemap_chart(df, cat_col, num_cols, colors=None, show_labels=False, limit_categories=None):
    if colors is None:
        colors = MCKINSEY_COLORS
    
    # Apply category limit
    if limit_categories and limit_categories != "All":
        df = df.head(int(limit_categories))
    
    fig = px.treemap(
        df, 
        path=[cat_col], 
        values=num_cols[0],
        color_discrete_sequence=colors
    )
    
    fig.update_layout(
        title=f"Treemap: {num_cols[0]} by {cat_col}",
        height=600,
        width=1100
    )
    return fig

def generate_insights(df, cat_col, num_cols):
    """Returns 1-3 simple bullet points as insights."""
    insights = []
    # 1. Which segment has the highest value for each metric?
    for col in num_cols:
        idx = df[col].idxmax()
        seg = df.loc[idx, cat_col]
        val = df.loc[idx, col]
        insights.append(f"• {seg} has the highest {col} value ({val:,}).")
        if len(insights) >= 2:
            break
    # 2. Which metric contributes most to the total in any segment?
    if len(num_cols) > 1:
        for i, row in df.iterrows():
            total = row[num_cols].sum()
            if total == 0:
                continue
            max_col = max(num_cols, key=lambda c: row[c])
            pct = 100 * row[max_col] / total
            if pct > 60:
                insights.append(f"• {max_col} contributes over {pct:.0f}% of total in {row[cat_col]}.")
                break
    return insights[:3]

def suggest_chart_types(df, category_col, metric_cols):
    """
    Suggest valid chart types based on the data structure.
    Returns a list of chart type strings.
    """
    n_metrics = len(metric_cols)
    if n_metrics >= 3:
        return ["Grouped Bar", "Stacked Bar", "Line", "Area", "Radar", "Scatter", "Bubble"]
    elif n_metrics == 2:
        return ["Grouped Bar", "Stacked Bar", "Line", "Area", "Radar", "Scatter"]
    elif n_metrics == 1:
        return ["Pie", "Donut", "Treemap", "Line", "Area"]
    else:
        return [] 