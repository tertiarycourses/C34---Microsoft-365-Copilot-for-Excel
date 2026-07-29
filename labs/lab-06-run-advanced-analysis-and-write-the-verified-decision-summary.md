# Lab 6 — Run Advanced Analysis and Write the Verified Decision Summary

**Course:** Microsoft 365 Copilot for Excel  
**Course Code:** C34  
**Version:** v1.0 (29 July 2026)  
**Topic 2:** AI-Powered Data Analysis and Insights  
**Maps to:** LO4: use Python-assisted Copilot for a bounded analytical question, inspect the generated method, reconcile headline values and produce a traceable decision summary  
**Duration:** 75 minutes  
**Tools:** Copilot direct answers · advanced analysis with Python in Excel · Excel controls · Pivot_Analysis · advanced-analysis-fallback.md

---

## Goal

Complete the HarbourLight workflow with a reviewed analysis of monthly trends, channel return rates and high-value-order outliers, followed by a Share, Revise or Hold decision.

## What You Will Do

You will ask Copilot for direct answers and advanced analysis using only tblOrdersClean. You will review the referenced fields, filters, groupings, IQR logic and generated code or explanation. You will reconcile the headline values to the Control and Pivot_Analysis sheets, then create a concise executive summary that keeps observations, hypotheses and limitations separate.

## What You Will Build

An Advanced_Analysis sheet with prompt, method, generated output and reconciliation; plus an Executive_Summary sheet with three verified findings, limitations, actions and a final decision

## Prerequisites

- Completed Lab 5 workbook with reconciled Pivot A and Pivot B.
- Open labs/assets/advanced-analysis-brief-template.md and labs/assets/expected-controls.md.
- Before class, confirm the account shows the deeper or advanced analysis entry point. If it does not, open labs/assets/advanced-analysis-fallback.md so you can inspect saved Python logic and output hands-on.
- Use only tblOrdersClean; do not connect to external data or use real organisational information.

> **Data note.** Use only the supplied synthetic HarbourLight data or information you are authorised to process. Do not paste credentials, confidential business material or sensitive personal data into Copilot.

## Steps

### 1. Create Advanced_Analysis and Executive_Summary sheets. Copy the analysis brief template to Advanced_Analysis and complete its Question, Data, Filters, Metrics, Method, Output and Review fields. Require monthly net sales by region, returned-order rate by channel and an IQR review of order Net_Sales. State that outliers are candidates for review, not errors or causes.

```text
Question: What changed across months and regions, which channel has the highest returned-order rate, and which order Net_Sales values are high under the 1.5 x IQR rule?
Data: tblOrdersClean only
Filters: none; report missing or excluded rows
Review: reconcile with Control and Pivot_Analysis
```

### 2. Ask Copilot the direct-answer prompt below. Save the response, cited source fields and any inserted static table or image on Advanced_Analysis. If an inserted output will not refresh, place a visible 'STATIC - rerun after source change' label above it. Review every changed sheet, range and object, use Undo for unrelated changes and record the accepted or rejected scope.

```text
Using only tblOrdersClean, report:
1. Monthly Net_Sales by Region and the grand total.
2. Returned-order count, order count and Return_Rate by Channel.
3. Q1, Q3, IQR, upper fence and Order_ID values above the upper fence for Net_Sales.
Show the fields and filters used. Do not claim causes. Label inserted non-refreshing output as static.
```

### 3. Choose the follow-up for deeper or advanced analysis, or ask 'Enter advanced analysis mode'. Review the generated Python code or expanded logic. Confirm it selects tblOrdersClean, groups by canonical Month/Region or Channel, computes rate as sum(Return_Flag)/count(Order_ID), uses the 1.5 x IQR upper fence and does not silently drop rows. If the feature is unavailable, inspect the saved code and output in labs/assets/advanced-analysis-fallback.md line by line and paste the reviewed method plus your notes into Advanced_Analysis. In either route, record the inspected code lines or logic in Prompt_Log.

```text
Review checklist:
[ ] source is tblOrdersClean
[ ] no hidden filter
[ ] monthly grouping uses Month and Region
[ ] rate denominator is Order_ID count
[ ] Q1/Q3/IQR and upper fence are reported
[ ] excluded or missing rows are counted
[ ] output type is labelled static or refreshable
```

### 4. On Advanced_Analysis, create a reconciliation table with Metric, Advanced_Result, Independent_Result, Difference, Source and Status. Reconcile total Net_Sales, each channel order count and return count, the overall return rate, the highest monthly-region value and the listed high outlier Order_ID values. Every numeric difference must be zero within S$0.01 or 0.01 percentage points.

```text
Reconciliation columns:
Metric | Advanced_Result | Independent_Result | Difference | Source | Status
Status rule: OK only when the difference is within the stated tolerance.
```

### 5. On Executive_Summary, write exactly three findings using the template below. Each finding must cite workbook evidence, distinguish OBSERVED from HYPOTHESIS and name a practical owner or next check. Add limitations and choose SHARE only if every required reconciliation is OK; otherwise choose REVISE or HOLD. Record the reason and owner.

```text
Finding | Evidence | Type | Why it matters | Next check | Owner
Types: OBSERVED or HYPOTHESIS
Final decision: SHARE | REVISE | HOLD
Required limitations: synthetic data; four-month window; returned status only; no causal evidence
```

## Test It

Advanced_Analysis must contain the completed brief, direct answer, reviewed code or method, output-type label and reconciliation table. Every required metric and outlier must match labs/assets/expected-controls.md within the stated tolerance. Executive_Summary must contain exactly three findings, evidence references, types, next checks, owners, four required limitations and a final SHARE, REVISE or HOLD decision. SHARE is allowed only when every reconciliation status is OK.

## Checkpoint and Rejoin Point

This is the final course checkpoint. Keep the workbook with Raw_Orders, Control, Prompt_Log, Orders_Working, Orders_Clean, Pivot_Analysis, Advanced_Analysis and Executive_Summary. Use it as a practice model, not as evidence about a real organisation.

## Troubleshooting

| If this happens | Fix |
|---|---|
| Advanced analysis is not available in the current account. | Open labs/assets/advanced-analysis-fallback.md, inspect the saved Python logic and output, identify the source fields, groupings, rate denominator and IQR rule, then complete the same reconciliations in your own workbook. Pair with the trainer only for the interface demonstration. |
| The analysis reports a different return rate. | Check that the numerator is Sum of Return_Flag and the denominator is Count of Order_ID at the same channel grain. |
| The generated narrative claims a cause. | Relabel the statement HYPOTHESIS, remove causal language and name the additional operational evidence needed. |

## Challenge

Ask for a sensitivity check using a 3 x IQR upper fence. Compare the flagged orders with the 1.5 x IQR result and explain how the threshold changes the review workload without proving which orders are wrong.

## Reflection

What evidence would make the final summary trustworthy to a reviewer who never saw the Copilot chat?

---

[← Lab 5](lab-05-build-reconciled-pivottables-and-charts.md) · [Labs index →](README.md)
