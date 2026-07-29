# Lab 1 — Prepare the Workbook and Create the Copilot Control Trail

**Course:** Microsoft 365 Copilot for Excel  
**Course Code:** C34  
**Version:** v1.0 (29 July 2026)  
**Topic 1:** Getting Started with Copilot in Excel  
**Maps to:** LO1: confirm the available Copilot experience, preserve the source data, create a named Excel table and establish prompt and verification controls  
**Duration:** 45 minutes  
**Tools:** Excel for Microsoft 365 or Excel for the web · Copilot · harbourlight-orders-raw.csv

---

## Goal

Create a reversible C34 workbook whose source boundary, row grain and baseline controls are explicit before Copilot makes any change.

## What You Will Do

You will import the synthetic HarbourLight order file, save it as a modern Excel workbook, convert the source rows into a named table and create Control and Prompt_Log sheets. You will use Copilot in Chat and Plan only to describe the data and propose a safe sequence. The raw source remains unchanged.

## What You Will Build

work-c34/C34-HarbourLight-Copilot-Analysis.xlsx with Raw_Orders, Control and Prompt_Log sheets, a tblOrdersRaw table, baseline counts and a recorded Copilot access note

## Prerequisites

- Download the repository and keep labs/assets/harbourlight-orders-raw.csv beside the other C34 assets.
- Sign in to an eligible Microsoft 365 account and open Excel or Excel for the web.
- Create a work-c34 training folder in OneDrive or SharePoint. Confirm you can save an .xlsx file there, cloud sync is complete and AutoSave is active. Use only the supplied synthetic data.

> **Data note.** Use only the supplied synthetic HarbourLight data or information you are authorised to process. Do not paste credentials, confidential business material or sensitive personal data into Copilot.

## Steps

### 1. Open labs/assets/harbourlight-orders-raw.csv in Excel. Select File > Save As and save C34-HarbourLight-Copilot-Analysis.xlsx inside your OneDrive or SharePoint work-c34 folder. Confirm the title bar shows the cloud location and AutoSave is On, then rename the first sheet Raw_Orders. Do not correct, sort or delete any source value.

```text
Expected source headers:
Order_ID | Order_Date | Region | Channel | Product | Category | Units | Unit_Price | Unit_Cost | Discount_Rate | Returned | Customer_Note
Required file state: .xlsx in OneDrive or SharePoint; cloud sync complete; AutoSave On
```

### 2. Write the grain statement above the control area in a new sheet named Control: 'One data row represents one HarbourLight order identified by Order_ID.' On Raw_Orders, click inside the data, select Home > Format as Table, confirm My table has headers and choose any accessible style. On Table Design, set Table Name to tblOrdersRaw.

```text
Required table name: tblOrdersRaw
Required grain: one row = one order
Required key: Order_ID
```

### 3. On Control, enter the labels below in A4:A9. In B4:B9 enter formulas that read tblOrdersRaw. Use ROWS for row count, COUNTA for populated Order_ID values, MIN and MAX for the date range, SUM for Units and SUMPRODUCT for gross sales. Format dates as yyyy-mm-dd and gross sales as S$.

```text
A4 Source row count
A5 Populated Order_ID count
A6 Earliest order date
A7 Latest order date
A8 Source units
A9 Source gross sales before discount

Example formulas:
=ROWS(tblOrdersRaw[Order_ID])
=COUNTA(tblOrdersRaw[Order_ID])
=MIN(tblOrdersRaw[Order_Date])
=MAX(tblOrdersRaw[Order_Date])
=SUM(tblOrdersRaw[Units])
=SUMPRODUCT(tblOrdersRaw[Units],tblOrdersRaw[Unit_Price])
```

### 4. Create a sheet named Prompt_Log. Copy the header row from labs/assets/prompt-and-verification-log-template.csv into A1:J1, format it as a table named tblPromptLog and add the first record. State the Copilot entry point you can see and whether Edit, Plan and Chat choices are available. If a label differs, record the label exactly.

```text
Lab,Timestamp,Mode,Goal,Data_Boundary,Prompt,Proposed_Logic,Workbook_Change,Verification,Decision
1,<TODAY>,Chat,Describe source structure,tblOrdersRaw,<PASTE PROMPT>,<COPILOT RESPONSE>,No change,<CHECKS>,Keep or revise
```

### 5. Open Copilot. In Chat, submit the first prompt below and compare the response with the Control sheet. Then choose Plan and submit the second prompt. Do not approve workbook edits. Record both prompts, the proposed logic and your decision in tblPromptLog.

```text
CHAT PROMPT
GOAL: Describe the structure and readiness risks in this order data.
CONTEXT: HarbourLight Retail operations review; one row should represent one order.
DATA: Use only tblOrdersRaw. Name the columns you rely on.
CONSTRAINTS: Do not change the workbook. Do not infer missing business facts.
OUTPUT: Grain, key, date range, numeric fields, category fields and five checks.
REVIEW: Compare row count, Order_ID count, date range, Units and gross sales with Control!B4:B9.

PLAN PROMPT
Propose a reversible sequence to prepare tblOrdersRaw for analysis. Preserve Raw_Orders; make one bounded change at a time; include verification after every change. Do not act.
```

## Test It

Raw_Orders must contain table tblOrdersRaw with exactly 36 data rows and 36 populated Order_ID values. Control must show earliest date 2026-01-05, latest date 2026-04-28, 36 rows, 36 populated IDs and the same Units and gross-sales controls as labs/assets/expected-controls.md. Prompt_Log must contain one Chat and one Plan record, both with 'No change' in Workbook_Change. Raw_Orders must still match the CSV.

## Checkpoint and Rejoin Point

Save and close the workbook. This file is the Lab 1 checkpoint. Lab 2 copies Raw_Orders into a working sheet. If you need to rejoin, follow the Lab 1 rebuild checklist in labs/assets/harbourlight-checkpoints.md.

## Troubleshooting

| If this happens | Fix |
|---|---|
| The Copilot button is missing. | Confirm the signed-in account, current Excel build, connected-experience settings and organisation policy. Also confirm the workbook is .xlsx in OneDrive or SharePoint, cloud sync is complete and AutoSave is On. Pair with the trainer for prompt comparison while continuing the workbook controls if access remains unavailable. |
| Copilot appears before saving but becomes unavailable in the workbook. | Use File > Save As to move the workbook into your OneDrive or SharePoint work-c34 folder, wait for sync, turn AutoSave On, close and reopen the cloud file, then retry. |
| The table includes blank rows or stops before the last order. | Select Table Design > Resize Table and set the range from the 12 headers through the final populated row. |
| The date controls show numbers instead of dates. | Keep the formulas and apply the yyyy-mm-dd number format to Control!B6:B7. |

## Challenge

Add a duplicate-ID control that returns the row count minus the unique Order_ID count. Explain why a zero result is necessary but not sufficient to prove the source is ready.

## Reflection

Which baseline control would reveal the most serious accidental change later in the workflow, and why?

---

[← Labs index](README.md) · [Lab 2 →](lab-02-apply-reproducible-highlights-sorts-and-filters.md)
