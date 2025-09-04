from typing import List
import pandas as pd
import re

def _metric_phrase(metric: str) -> str:
    m = metric.lower()
    if re.search(r"revenue|sales|total", m):
        return "drives topline value"
    if re.search(r"incidents|failures|issues|errors", m):
        return "dominates reported counts"
    if re.search(r"share|%|percent|ratio", m):
        return "commands the largest share"
    return "has the highest total value"

def generate_insights(df: pd.DataFrame, category_col: str, metric_cols: List[str]) -> List[str]:
    insights = []
    # 1. Which metric has the highest total value across all segments?
    metric_totals = df[metric_cols].sum()
    max_metric = metric_totals.idxmax()
    phrase = _metric_phrase(max_metric)
    insights.append(f"{max_metric} {phrase} across all segments.")

    # 2. Which segment has the highest value for each metric?
    for col in metric_cols:
        idx = df[col].idxmax()
        seg = df.loc[idx, category_col]
        val = df.loc[idx, col]
        phrase = _metric_phrase(col)
        insights.append(f"{seg} has the highest {col} value ({val:,}) and {phrase}.")
        if len(insights) >= 2:
            break

    # 3. % contribution of each metric to total
    total_sum = metric_totals.sum()
    if total_sum > 0:
        pct_contrib = (metric_totals / total_sum * 100).round(1)
        top_metric = pct_contrib.idxmax()
        pct = pct_contrib.max()
        phrase = _metric_phrase(top_metric)
        if pct > 50:
            insights.append(f"{top_metric} {phrase}, contributing {pct:.0f}% of the total.")

    # 4. Detect if any metric is 2x another within same category
    for i, row in df.iterrows():
        vals = row[metric_cols]
        for a in metric_cols:
            for b in metric_cols:
                if a != b and vals[a] >= 2 * vals[b] and vals[b] > 0:
                    insights.append(f"{row[category_col]}'s {a} is double that of {b}.")
                    break
            if len(insights) >= 3:
                break
        if len(insights) >= 3:
            break

    # 5. Flag if any segment is dominant across multiple metrics
    segment_wins = {}
    for col in metric_cols:
        idx = df[col].idxmax()
        seg = df.loc[idx, category_col]
        segment_wins[seg] = segment_wins.get(seg, 0) + 1
    dominant = [seg for seg, count in segment_wins.items() if count > 1]
    if dominant:
        insights.append(f"{dominant[0]} is dominant across multiple metrics.")

    # Return only 2-3 unique insights
    seen = set()
    result = []
    for ins in insights:
        if ins not in seen:
            result.append(ins)
            seen.add(ins)
        if len(result) >= 3:
            break
    return result

# --- Test cases ---
if __name__ == "__main__":
    data = {
        "Segment": ["A", "B", "C"],
        "Revenue": [100, 200, 50],
        "Incidents": [300, 100, 50],
        "Share %": [50, 400, 100],
        "Y4": [500, 100, 50],
    }
    df = pd.DataFrame(data)
    insights = generate_insights(df, "Segment", ["Revenue", "Incidents", "Share %", "Y4"])
    print("\n".join(insights)) 