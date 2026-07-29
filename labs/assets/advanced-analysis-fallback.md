# Advanced Analysis Fallback - Saved Method and Output

Use this file only when the deeper or advanced analysis entry point is unavailable. It preserves the hands-on review task: inspect the saved Python logic, identify the source and method, then reconcile every headline result in your own workbook.

The snapshot uses only the synthetic `tblOrdersClean` table. It does not connect to the internet or another file.

## Saved Python logic

```python
import pandas as pd

# Python in Excel reads the named table through xl().
df = xl("tblOrdersClean[#All]", headers=True)

required = [
    "Order_ID",
    "Month",
    "Region",
    "Channel",
    "Net_Sales",
    "Return_Flag",
]

# Keep missing-row handling visible.
missing_required = df[required].isna().any(axis=1)
excluded_rows = int(missing_required.sum())
analysis = df.loc[~missing_required, required].copy()

# One cell represents Sum of Net_Sales for one Month-Region pair.
monthly_region = (
    analysis.groupby(["Month", "Region"], dropna=False)["Net_Sales"]
    .sum()
    .unstack(fill_value=0)
    .sort_index()
)

# Return_Rate uses returned-order count divided by order count.
channel_returns = (
    analysis.groupby("Channel", dropna=False)
    .agg(
        Returned_Orders=("Return_Flag", "sum"),
        Order_Count=("Order_ID", "count"),
    )
    .sort_index()
)
channel_returns["Return_Rate"] = (
    channel_returns["Returned_Orders"] / channel_returns["Order_Count"]
)

# Inclusive quartiles use linear interpolation.
q1 = analysis["Net_Sales"].quantile(0.25, interpolation="linear")
q3 = analysis["Net_Sales"].quantile(0.75, interpolation="linear")
iqr = q3 - q1
upper_fence = q3 + 1.5 * iqr
high_outliers = (
    analysis.loc[
        analysis["Net_Sales"] > upper_fence,
        ["Order_ID", "Net_Sales"],
    ]
    .sort_values(["Net_Sales", "Order_ID"])
    .reset_index(drop=True)
)
```

## Method review prompts

Write your answers in `Advanced_Analysis`:

1. Which line defines the data boundary?
2. Which six fields are required and how are missing rows counted?
3. What does one `monthly_region` cell represent?
4. What are the numerator and denominator of `Return_Rate`?
5. Which quartile interpolation and outlier fence are used?
6. Which values are observations, and which possible explanations would remain hypotheses?

## Saved output

`excluded_rows = 0`

### Monthly Net_Sales by Region

| Month | Central | North | South |
|---|---:|---:|---:|
| 2026-01 | 2,007.60 | 2,755.00 | 2,425.60 |
| 2026-02 | 6,411.80 | 2,330.25 | 3,680.45 |
| 2026-03 | 2,901.30 | 3,189.65 | 2,579.10 |
| 2026-04 | 3,456.85 | 2,704.95 | 6,106.15 |

### Returned-order rate by Channel

| Channel | Returned_Orders | Order_Count | Return_Rate |
|---|---:|---:|---:|
| Online | 2 | 12 | 0.166667 |
| Partner | 1 | 10 | 0.100000 |
| Store | 5 | 14 | 0.357143 |

### IQR result

| Statistic | Value |
|---|---:|
| Q1 | 739.1375 |
| Q3 | 1,204.2000 |
| IQR | 465.0625 |
| Upper fence | 1,901.79375 |

| Order_ID | Net_Sales |
|---|---:|
| HL-1029 | 2,064.00 |
| HL-1032 | 3,250.80 |
| HL-1018 | 4,531.50 |

## Required learner evidence

- Paste the method review answers into the workbook.
- Reconcile total Net_Sales, channel counts, rates and all outliers against `Control`, `Pivot_Analysis` and `expected-controls.md`.
- Label this source `SAVED TRAINING SNAPSHOT - rerun live analysis when the feature is available`.
- Keep the same final decision rule: `SHARE` only when every reconciliation status is `OK`.
