# Lab 5 — Build Reconciled PivotTables and Charts

**Course:** Microsoft 365 Copilot for Excel  
**Course Code:** C34  
**Version:** v1.0 (29 July 2026)  
**Topic 2:** AI-Powered Data Analysis and Insights  
**Maps to:** LO3: translate business questions into PivotTable grain, dimensions, measures and charts, then reconcile every grand total and denominator to the clean table  
**Duration:** 55 minutes  
**Tools:** Excel PivotTables · Excel charts · Copilot · tblOrdersClean · expected-controls.md

---

## Goal

Create an editable operations summary that shows monthly net sales by region and return rate by channel without hiding the underlying counts or overstating visual differences.

## What You Will Do

You will define two decision questions before asking Copilot to build anything. The first PivotTable and line chart show monthly net sales by canonical region. The second summary shows returned orders, order count and return rate by channel. You will verify grand totals, denominators, titles, units and source linkage.

## What You Will Build

A Pivot_Analysis sheet with two PivotTables, a monthly regional net-sales line chart, a channel return-rate chart, tie-out cells and a Prompt_Log record for each object

## Prerequisites

- Completed Lab 4 workbook with tblOrdersClean and reconciled clean-table controls.
- Month contains 2026-01 through 2026-04 and Return_Flag contains only 0 and 1.
- No active filter is applied to tblOrdersClean.

> **Data note.** Use only the supplied synthetic HarbourLight data or information you are authorised to process. Do not paste credentials, confidential business material or sensitive personal data into Copilot.

## Steps

### 1. Create a sheet named Pivot_Analysis. At the top, write two questions and their intended grain. Question A: 'How did monthly net sales change by region?' Grain: one Pivot cell equals the sum of Net_Sales for one Month-Region combination. Question B: 'Which channel has the highest returned-order rate?' Grain: one row equals one canonical Channel.

```text
Question A fields:
Rows = Month | Columns = Region | Values = Sum of Net_Sales

Question B fields:
Rows = Channel | Values = Sum of Return_Flag and Count of Order_ID
Return rate = returned orders / order count
```

### 2. Ask Copilot to create PivotTable A from tblOrdersClean on Pivot_Analysis. If direct creation is unavailable, select Insert > PivotTable, choose tblOrdersClean and use the exact field layout. Format Net_Sales as S$ with two decimals, show grand totals and sort Month ascending. Review every changed sheet, range and object; confirm only the requested PivotTable was added and use Undo if the scope differs. Record the accepted or rejected scope in Prompt_Log.

```text
Create an editable PivotTable from tblOrdersClean on Pivot_Analysis. Put Month in Rows, Region in Columns and Sum of Net_Sales in Values. Show grand totals, sort Month ascending and format values as S$ with two decimals. Do not create a static pasted table.
```

### 3. Below Pivot A, add a tie-out cell that subtracts the Pivot grand total from SUM(tblOrdersClean[Net_Sales]). It must equal 0.00. Create a line chart from Pivot A with title 'Monthly Net Sales by Region', Month on the x-axis, S$ Net Sales on the y-axis and a visible legend for North, South and Central. Review the changed sheets, ranges and objects; confirm the chart is linked only to Pivot A and use Undo for any unrelated change.

```text
Required tie-out:
=SUM(tblOrdersClean[Net_Sales])-<PIVOT_A_GRAND_TOTAL_CELL>
Expected result: 0.00
```

### 4. Create PivotTable B using Channel as rows, Sum of Return_Flag and Count of Order_ID as values. Beside the Pivot, calculate Return_Rate for each channel as returned orders divided by order count, format as 0.0% and add a total row that uses the grand totals rather than averaging channel percentages. Review every changed sheet, range and object; confirm only Pivot B and its adjacent formulas changed and use Undo if the scope differs.

```text
Return_Rate formula: =<RETURNED_ORDERS_CELL>/<ORDER_COUNT_CELL>
Overall return rate: =<SUM_RETURN_FLAG_GRAND_TOTAL>/<COUNT_ORDER_ID_GRAND_TOTAL>
```

### 5. Create a clustered column chart using Channel and Return_Rate with title 'Returned-Order Rate by Channel'. Set the y-axis to percentage, start at zero and show data labels. Compare both PivotTables with labs/assets/expected-controls.md. Review all changed sheets, ranges and objects and record the accepted or rejected scope, exact totals, visual checks and any manual steps in Prompt_Log.

```text
Visual checks:
[ ] chart title names the metric and dimension
[ ] axis units match S$ or percentage
[ ] every canonical category is visible
[ ] line chart months are chronological
[ ] return-rate axis starts at zero
[ ] both source ranges remain linked and editable
```

## Test It

Pivot A must contain four months, three regions and a grand total equal to tblOrdersClean Net_Sales with a 0.00 tie-out. Pivot B must show three channels, returned-order count, order count and rates that match labs/assets/expected-controls.md; the overall rate must use grand-total numerator and denominator. Both charts must be editable, linked, fully titled and use the correct units.

## Checkpoint and Rejoin Point

Save the workbook with Pivot_Analysis visible and both tie-outs complete. Lab 6 references these values as independent checks. To rejoin, use the Pivot field layouts in labs/assets/harbourlight-checkpoints.md.

## Troubleshooting

| If this happens | Fix |
|---|---|
| Net_Sales is counted instead of summed. | Open Value Field Settings, choose Sum and verify that Net_Sales contains numeric values in all rows. |
| Months sort alphabetically in the wrong order. | Confirm Month uses yyyy-mm text or place the real Order_Date in rows and group it by Months and Years. |
| The chart omits a region or channel. | Inspect the Pivot filters and source categories, clear filters and refresh the PivotTable. |

## Challenge

Add a Product gross-profit PivotTable and choose a chart. State why Sum of Gross_Profit is meaningful while a simple average of row Margin_Rate may not be the right product-level margin.

## Reflection

Which tie-out proves the Pivot aggregation is complete, and what analytical error can it still miss?

---

[← Lab 4](lab-04-clean-and-enrich-the-analysis-table.md) · [Lab 6 →](lab-06-run-advanced-analysis-and-write-the-verified-decision-summary.md)
