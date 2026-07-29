# HarbourLight Lab Checkpoints and Rejoin Guide

Use these compact rebuild steps only if you need to rejoin after falling behind. Do not skip the matching lab's `Test It` controls.

## After Lab 1

- Workbook: `C34-HarbourLight-Copilot-Analysis.xlsx` in the learner's OneDrive or SharePoint `work-c34` folder
- File state: `.xlsx`, cloud sync complete, AutoSave On
- Sheets: `Raw_Orders`, `Control`, `Prompt_Log`
- Raw table: `tblOrdersRaw`
- Controls: 36 rows, 36 populated IDs, date range, Units and gross sales
- Prompt_Log: one Chat record and one Plan record; neither changed the workbook

## After Lab 2

- Copy `Raw_Orders` to `Orders_Working`
- Working table: `tblOrdersWorking`
- Apply returned-row and high-discount highlights
- Sort Units descending, then Order_ID ascending
- Clear every filter before saving

## After Lab 3

Add these calculated columns in order:

1. Gross_Sales
2. Discount_Amount
3. Net_Sales
4. Cost_Amount
5. Gross_Profit
6. Margin_Rate

Use the exact formulas in `formula-and-verification-rules.md`, then match every total in `expected-controls.md`.

## After Lab 4

- Copy `Orders_Working` to `Orders_Clean`
- Clean table: `tblOrdersClean`
- Canonical Region: `North`, `South`, `Central`
- Canonical Channel: `Store`, `Online`, `Partner`
- Add `Month`, `Return_Flag` and reviewed `Note_Theme`
- Reconcile row count and all monetary totals before continuing

## After Lab 5

On `Pivot_Analysis`:

- Pivot A: Month rows, Region columns, Sum of Net_Sales values
- Line chart: Monthly Net Sales by Region
- Pivot B: Channel rows, Sum of Return_Flag and Count of Order_ID values
- Return-rate chart: Returned-Order Rate by Channel
- Both source totals tie to `tblOrdersClean`

## After Lab 6

Required sheets:

- `Advanced_Analysis`: completed brief, output, reviewed logic or code, output label and reconciliation
- `Executive_Summary`: exactly three findings, limitations, actions, owners and final decision

Keep all eight workbook sheets together so another person can trace the final claims back to the source.

If deeper or advanced analysis is unavailable, use `advanced-analysis-fallback.md`. Inspect its saved method and output in the same way, complete the workbook reconciliations yourself and label the source as a saved training snapshot.

## Trainer rejoin preparation

Before class, the trainer should complete the six labs once in the current Excel tenant and retain cloud-saved copies after Labs 1-5. Name them `C34-checkpoint-after-lab-01.xlsx` through `C34-checkpoint-after-lab-05.xlsx`. Each copy must:

- contain only the synthetic HarbourLight data;
- show its checkpoint number and creation date on Control;
- pass the matching `Test It` checks;
- be shared read-only so each learner saves a personal copy;
- require the learner to rerun the checkpoint controls before continuing.

The repository summaries remain the rebuild route when a live checkpoint copy is unavailable.
