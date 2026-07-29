# Lab 3 — Generate and Reconcile Formula Columns

**Course:** Microsoft 365 Copilot for Excel  
**Course Code:** C34  
**Version:** v1.0 (29 July 2026)  
**Topic 1:** Getting Started with Copilot in Excel  
**Maps to:** LO2: generate structured-reference formula columns from plain-language rules, inspect the logic and reconcile the calculated results to independent controls  
**Duration:** 45 minutes  
**Tools:** Excel formulas · Copilot · structured references · expected-controls.md

---

## Goal

Extend tblOrdersWorking with six auditable calculated columns and prove that representative rows and headline totals match the supplied business rules.

## What You Will Do

You will write the calculation rules in words, ask Copilot for one structured-reference formula at a time and inspect every formula before filling it through the table. You will verify a no-discount row, a discounted row, a returned order, the zero-error path and independent totals on the Control sheet.

## What You Will Build

Six calculated columns in tblOrdersWorking - Gross_Sales, Discount_Amount, Net_Sales, Cost_Amount, Gross_Profit and Margin_Rate - plus formula checks and reconciled totals on Control

## Prerequisites

- Completed Lab 2 workbook with tblOrdersWorking and no active filter.
- Control shows 36 total rows and the source gross-sales value from Lab 1.
- Open labs/assets/formula-and-verification-rules.md before writing a formula.

> **Data note.** Use only the supplied synthetic HarbourLight data or information you are authorised to process. Do not paste credentials, confidential business material or sensitive personal data into Copilot.

## Steps

### 1. On Control, copy the six business rules from labs/assets/formula-and-verification-rules.md into a Lab 3 block. Include currency units, blank handling and the Margin_Rate denominator. Add a Prompt_Log row in Chat and ask Copilot to return only the proposed structured-reference formulas and explanations; do not apply them yet.

```text
Required output columns:
Gross_Sales | Discount_Amount | Net_Sales | Cost_Amount | Gross_Profit | Margin_Rate

Use native Excel formulas. Do not use the COPILOT function for numeric calculations.
```

### 2. Review the proposed Gross_Sales and Discount_Amount formulas. In tblOrdersWorking add the two headers and enter the approved formulas in the first data row so Excel fills each calculated column. Select three rows and confirm that the formula uses current-row structured references.

```text
Gross_Sales: =[@Units]*[@Unit_Price]
Discount_Amount: =[@Gross_Sales]*[@Discount_Rate]
```

### 3. Add Net_Sales, Cost_Amount and Gross_Profit one column at a time. After every column, ask Copilot to explain the sign and inputs, then compare one row with a calculator or hand-worked result. Record the selected Order_ID, inputs, expected value and observed value in Prompt_Log.

```text
Net_Sales: =[@Gross_Sales]-[@Discount_Amount]
Cost_Amount: =[@Units]*[@Unit_Cost]
Gross_Profit: =[@Net_Sales]-[@Cost_Amount]
```

### 4. Add Margin_Rate and format the entire column as 0.0%. The approved denominator is Net_Sales. Use IFERROR to return zero if Net_Sales is zero. Check that the formula is filled in all 36 data rows and that no formula-error values appear. On Control, create two scratch cells containing Gross_Profit=0 and Net_Sales=0, apply =IFERROR(<GROSS_PROFIT_CELL>/<NET_SALES_CELL>,0) and confirm the result is 0. Delete the scratch inputs after recording the check; do not add a synthetic order to the table.

```text
Margin_Rate: =IFERROR([@Gross_Profit]/[@Net_Sales],0)
Required format: 0.0%
```

### 5. On Control, calculate SUM for Gross_Sales, Discount_Amount, Net_Sales, Cost_Amount and Gross_Profit. Add a weighted overall margin formula: total Gross_Profit divided by total Net_Sales. Compare the six results with labs/assets/expected-controls.md. Explicitly test HL-1001, HL-1003, HL-1007, HL-1018 and HL-1032 against the named row controls. Review every changed sheet, range and object; confirm only the six approved calculated columns and Control checks changed, use Undo for scope creep and record the accepted or rejected scope. If a value differs, inspect formulas and inputs rather than overwriting it.

```text
Overall Margin_Rate control:
=SUM(tblOrdersWorking[Gross_Profit])/SUM(tblOrdersWorking[Net_Sales])

Do not use AVERAGE(tblOrdersWorking[Margin_Rate]) for the overall margin.
```

## Test It

All six calculated columns must contain formulas for all 36 rows with no formula-error values. The formula text must use structured references and the overall margin must use total Gross_Profit divided by total Net_Sales. The six totals and the named representative Order_ID checks must exactly match labs/assets/expected-controls.md. Copilot's explanation alone does not satisfy the check.

## Checkpoint and Rejoin Point

Save the workbook with all formulas present and no active filter. Lab 4 copies tblOrdersWorking to a clean analysis sheet. To rejoin, use the formula block and control totals in labs/assets/harbourlight-checkpoints.md.

## Troubleshooting

| If this happens | Fix |
|---|---|
| Excel creates A1 references instead of structured references. | Confirm the range is an Excel table, select the first data cell under the new header and build the formula by clicking the current-row cells; Excel should insert named column references. |
| The overall margin differs from the control while row formulas look correct. | Confirm you divided total Gross_Profit by total Net_Sales and did not average row percentages. |
| Only the first row contains the formula. | Double-click the fill handle or re-enter the formula in the table column and confirm calculated-column fill is enabled. Do not paste hardcoded values down the column. |

## Challenge

Add a Recalculation_Check column that compares Net_Sales with Gross_Sales minus Discount_Amount and returns OK only when the absolute difference is below 0.005. Explain the tolerance.

## Reflection

Which formula check is independent enough to catch a fluent but logically wrong Copilot suggestion?

---

[← Lab 2](lab-02-apply-reproducible-highlights-sorts-and-filters.md) · [Lab 4 →](lab-04-clean-and-enrich-the-analysis-table.md)
