import plotly.graph_objects as go
import io
import base64
import copy

def export_chart_as_png(fig, width=1280, height=720, deck_mode=False):
    """
    Export a Plotly chart as PNG with proper background settings.
    
    Args:
        fig: Plotly figure object
        width: Image width in pixels
        height: Image height in pixels
        deck_mode: Whether to use white background for deck mode
    
    Returns:
        bytes: PNG image data
    """
    # Create a copy to avoid modifying the original
    fig_copy = copy.deepcopy(fig)
    
    # Set background based on deck mode
    if deck_mode:
        fig_copy.update_layout(
            plot_bgcolor="white",
            paper_bgcolor="white"
        )
    
    # Generate PNG with high quality
    img_bytes = fig_copy.to_image(
        format="png", 
        width=width, 
        height=height,
        scale=2  # Higher resolution
    )
    
    return img_bytes

def get_chart_base64(fig, width=1280, height=720, deck_mode=False):
    """
    Get base64 encoded string of chart for embedding.
    
    Args:
        fig: Plotly figure object
        width: Image width in pixels
        height: Image height in pixels
        deck_mode: Whether to use white background for deck mode
    
    Returns:
        str: Base64 encoded image string
    """
    img_bytes = export_chart_as_png(fig, width, height, deck_mode)
    return base64.b64encode(img_bytes).decode()

def copy_chart_text_to_clipboard(chart_type, category_col, metric_cols, insights):
    """
    Generate and copy chart text to clipboard.
    
    Args:
        chart_type: Type of chart (e.g., "Grouped Bar")
        category_col: Category column name
        metric_cols: List of metric column names
        insights: List of insight strings
    
    Returns:
        str: Generated text for clipboard
    """
    text = f"{chart_type} Chart: {category_col} vs {', '.join(metric_cols)}\n\n"
    text += "\n".join(insights)
    return text

def create_powerpoint_slide(chart_fig, title, insights, deck_mode=False):
    """
    Create a PowerPoint slide with the chart and insights.
    This is a placeholder for future PPTX export functionality.
    
    Args:
        chart_fig: Plotly figure object
        title: Slide title
        insights: List of insight strings
        deck_mode: Whether to use white background
    
    Returns:
        bytes: PPTX file data (placeholder)
    """
    # Placeholder for PPTX export
    # In a real implementation, this would use python-pptx
    return b"PPTX export coming soon!"

def export_all_charts(charts_data, deck_mode=False):
    """
    Export multiple charts as a combined file.
    
    Args:
        charts_data: List of dicts with 'fig', 'title', 'insights' keys
        deck_mode: Whether to use white background
    
    Returns:
        bytes: Combined export data
    """
    # Placeholder for multi-chart export
    return b"Multi-chart export coming soon!" 