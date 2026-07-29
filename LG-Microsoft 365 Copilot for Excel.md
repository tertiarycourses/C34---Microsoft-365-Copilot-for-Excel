# Microsoft 365 Copilot for Excel — Learner Guide

**Course Code:** C34  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v1.0 · 29 July 2026**

## Contents

- [Introduction](#introduction)
- [Course Learning Outcomes](#course-learning-outcomes)
- [Before You Start — Preparation](#before-you-start--preparation)
- [Topic 01 — Getting Started with Copilot in Excel  (First half · 3 labs)](#topic-01--getting-started-with-copilot-in-excel--first-half--3-labs)
  - [Introduction to Microsoft 365 Copilot in Excel](#introduction-to-microsoft-365-copilot-in-excel)
  - [Preparing Data as Excel Tables for Copilot](#preparing-data-as-excel-tables-for-copilot)
  - [Writing Effective Prompts for Data Tasks](#writing-effective-prompts-for-data-tasks)
  - [Highlighting, Sorting and Filtering Data with Copilot](#highlighting-sorting-and-filtering-data-with-copilot)
  - [Generating Formula Columns from Plain-English Requests](#generating-formula-columns-from-plain-english-requests)
  - [Lab 1 — Prepare the Workbook and Create the Copilot Control Trail](#lab-1--prepare-the-workbook-and-create-the-copilot-control-trail)
  - [Lab 2 — Apply Reproducible Highlights, Sorts and Filters](#lab-2--apply-reproducible-highlights-sorts-and-filters)
  - [Lab 3 — Generate and Reconcile Formula Columns](#lab-3--generate-and-reconcile-formula-columns)
  - [Topic 01 Recap - Mapped to Learning Outcomes](#topic-01-recap---mapped-to-learning-outcomes)
- [Topic 02 — AI-Powered Data Analysis and Insights  (Second half · 3 labs)](#topic-02--ai-powered-data-analysis-and-insights--second-half--3-labs)
  - [Cleaning and Enriching Data with Copilot](#cleaning-and-enriching-data-with-copilot)
  - [Building PivotTables and Charts from a Prompt](#building-pivottables-and-charts-from-a-prompt)
  - [Surfacing Trends, Outliers and Insights](#surfacing-trends-outliers-and-insights)
  - [Advanced Analysis with Python in Excel](#advanced-analysis-with-python-in-excel)
  - [Verifying Results and Prompt Best Practices](#verifying-results-and-prompt-best-practices)
  - [Lab 4 — Clean and Enrich the Analysis Table](#lab-4--clean-and-enrich-the-analysis-table)
  - [Lab 5 — Build Reconciled PivotTables and Charts](#lab-5--build-reconciled-pivottables-and-charts)
  - [Lab 6 — Run Advanced Analysis and Write the Verified Decision Summary](#lab-6--run-advanced-analysis-and-write-the-verified-decision-summary)
  - [Topic 02 Recap - Mapped to Learning Outcomes](#topic-02-recap---mapped-to-learning-outcomes)
- [Wrap-Up - The Complete C34 Workflow](#wrap-up---the-complete-c34-workflow)
- [Next Steps](#next-steps)
- [Glossary](#glossary)


## Introduction

This Learner Guide accompanies Microsoft 365 Copilot for Excel (C34). It follows the same two-topic sequence, six connected labs, learning outcomes and verified HarbourLight Retail scenario as the slide deck, Lesson Plan and standalone lab files.

Use the guide as a self-contained study text before, during and after class. Each concept explains what the capability is, why it matters, how it works, a worked example and when to use or avoid it. The labs then apply those ideas to one workbook. Copilot output remains a proposal until the learner inspects the cells, formulas, PivotTables, charts or Python logic and completes the independent checks.


## Course Learning Outcomes

- LO1: Explain how Copilot works in Excel, prepare an analysis-ready Excel table and write bounded prompts for workbook tasks.
- LO2: Use Copilot to highlight, sort and filter table data, then generate and verify auditable formula columns.
- LO3: Clean and enrich a business dataset, create PivotTables and charts, and interpret patterns without overstating the evidence.
- LO4: Run advanced analysis with Python-assisted Copilot, reconcile the results and produce a traceable decision summary.


## Before You Start — Preparation

**What you need**

- A Windows or Mac laptop with a current version of Microsoft Excel or Excel for the web.
- An eligible Microsoft 365 account with the Copilot entry point enabled by your organisation or plan.
- A OneDrive or SharePoint folder where you can save the training workbook with cloud sync and AutoSave enabled.
- A downloaded copy of this repository with the labs/assets folder intact.
- Permission to use only the supplied synthetic HarbourLight data during class.

**Verify your setup**

Open labs/assets/harbourlight-orders-raw.csv in Excel. Confirm that row 1 contains the 12 expected headers and that 36 data rows are present. In OneDrive or SharePoint, create a training folder named work-c34. Save a temporary .xlsx file there, confirm cloud sync and AutoSave are active, then open Copilot and note whether Edit, Plan and Chat choices are visible; labels can vary as Microsoft updates the interface.

```bash
Expected structure:
Downloaded course files:
  C34---Microsoft-365-Copilot-for-Excel/labs/assets/
Cloud-saved working folder:
  OneDrive or SharePoint/work-c34/
```

**Conventions used in every lab**

- All HarbourLight names, orders, notes and values are synthetic training material.
- Text between <ANGLE_BRACKETS> is a placeholder to replace; never paste a password or secret.
- OBSERVED means supported by workbook evidence; HYPOTHESIS means a possible explanation; UNKNOWN remains unresolved.
- S$ is used for currency, dates use yyyy-mm-dd and percentages are stored as decimal values.
- Save the prompt, proposed logic, workbook change, verification and human decision together.
- When the trainer provides a read-only cloud checkpoint after Labs 1-5, save a personal copy and rerun the matching Test It controls before continuing.


## Topic 01 — Getting Started with Copilot in Excel  (First half · 3 labs)

Introduction to Microsoft 365 Copilot in Excel · preparing data as Excel tables · effective prompts · highlighting, sorting and filtering · formula columns

**Key concepts**

- Copilot work modes — Choose Edit for workbook changes, Plan for a proposed sequence and Chat for analysis that stays in the pane.
- Analysis-ready tables — Use one header row, one record per row, one meaning per column and consistent data types.
- G-C-D-C-O-R prompts — State Goal, Context, Data, Constraints, Output and Review criteria before Copilot acts.
- Reversible operations — Preview, apply, inspect and undo one bounded change rather than combining many opaque edits.
- Structured-reference formulas — Prefer formulas that name table columns and update as the table grows.
- Control totals — Reconcile counts, sums and edge cases independently before using a result in a decision.


### Introduction to Microsoft 365 Copilot in Excel

Copilot in Excel is a natural-language interface that can build, edit and analyse workbooks using Excel features such as tables, formulas, PivotTables, charts, formatting and worksheet operations. The current experience offers Edit, Plan and Chat choices. Edit can change the workbook, Plan proposes a sequence before changes and Chat keeps the response in the conversation.

The same prompt has different consequences depending on the mode. A conversational explanation is low-impact; a direct workbook edit changes shared evidence. Choosing the mode deliberately, saving a protected source sheet and keeping version history available makes experimentation reversible and keeps the human owner accountable for the final workbook.

**How it works**

- Confirm the eligible Microsoft 365 account, current Excel version and visible Copilot entry point.
- Choose Chat for questions, Plan when the intended sequence needs review and Edit for an approved change.
- Inspect the proposed or completed work, save a new version and retain the ability to undo or restore.

**Worked example**

- HarbourLight Retail has a raw order export and needs a weekly operations summary.
- The analyst first asks Chat to describe the columns, then asks Plan for a safe preparation sequence.
- Only after reviewing the plan does the analyst use Edit for one bounded change at a time.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The workbook uses a modern supported format and the required Copilot experience is available. | The prompt would expose secrets, sensitive personal information or data not approved for the service. |
| The task has a clear owner who can review changes and restore an earlier version if needed. | A high-impact financial, legal or operational decision would rely on an unchecked generated result. |

**Practitioner quality lens**

- Mode: Match Chat, Plan or Edit to the consequence of the task.
- Reversibility: Protect the source, save versions and make one inspectable change at a time.
- Ownership: A named person reviews and approves the workbook before it is shared or used.

**Authoritative references**

- https://support.microsoft.com/en-us/excel/copilot/get-started-with-copilot-in-excel
- https://support.microsoft.com/en-us/excel/copilot/frequently-asked-questions-about-copilot-in-excel

---


### Preparing Data as Excel Tables for Copilot

An analysis-ready table has a single header row, one record per row, one variable per column, stable identifiers and consistent types. Excel tables add names, filters and structured references that expand with new rows. They make the intended data boundary clearer to people, formulas and Copilot.

Merged headings, blank rows, subtotals inside the data region, duplicate identifiers and mixed types create ambiguous grain. If one row sometimes means an order and sometimes a subtotal, no prompt can fully repair the analytical logic. Data structure must be corrected before asking for insight.

**How it works**

- Identify the grain and primary identifier, then scan for blank headers, blank rows and duplicated IDs.
- Convert the bounded range to a table, confirm headers and give the table a descriptive unique name.
- Check date, text, count, currency and percentage columns; record known defects instead of hiding them.

**Worked example**

- Each HarbourLight row represents one order line identified by Order_ID.
- The learner converts the source range into tblOrdersRaw and freezes the header row.
- A data-readiness log records inconsistent Region and Channel text for later controlled cleaning.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The data can be expressed as a rectangular list with a consistent row meaning. | The range mixes several unrelated tables, presentation titles, subtotals and free-form notes. |
| Headers can be made unique and each column can be assigned one stable data type. | Duplicate identifiers or missing units make the intended record grain unresolved. |

**Practitioner quality lens**

- Grain: Write one sentence that says exactly what a row represents.
- Schema: Use unique headers, consistent types and stable categories.
- Controls: Record row count, unique-ID count and source totals before transformation.

**Authoritative references**

- https://support.microsoft.com/en-us/office/create-and-format-tables-2f0ce0e7-500b-4fe1-9b5b-a16ba4b9f34a
- https://support.microsoft.com/en-US/Excel/using-structured-references-with-excel-tables
- https://support.microsoft.com/en-us/excel/copilot/get-started-with-copilot-in-excel

---


### Writing Effective Prompts for Data Tasks

A useful prompt is an executable specification. The C34 G-C-D-C-O-R pattern names the Goal, business Context, exact Data boundary, Constraints, required Output and Review checks. It turns words such as 'analyse' or 'clean' into visible acceptance criteria.

Broad prompts force the model to guess which sheet, columns, period, aggregation and format matter. Specific prompts reduce ambiguity and make the result testable. Follow-up prompts should refine one dimension at a time and keep the original analytical question visible.

**How it works**

- State one goal and the decision or workbook change it should support.
- Name the table, fields, filters, units and exclusions; request a precise formula, table or chart output.
- Require Copilot to explain its logic, flag assumptions and show the checks a human should perform.

**Worked example**

- Goal: identify high-value returned orders that need review.
- Data: tblOrdersRaw; use Returned, Units and Unit_Price; do not infer causes from Customer_Note.
- Output: a filter plus a count; Review: show the exact conditions and preserve the full table.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The user can name the data boundary and the expected output format. | The request is 'make this better' with no audience, boundary, rule or decision. |
| The result has observable acceptance criteria such as a count, formula or explicit condition. | The prompt asks Copilot to fill unknown business facts or silently choose a high-impact threshold. |

**Practitioner quality lens**

- Specific: Name the table, fields, period, units and output.
- Bounded: State exclusions, privacy limits and what must remain unchanged.
- Reviewable: Ask for logic, assumptions, control checks and a clear success condition.

**Authoritative references**

- https://learn.microsoft.com/en-us/training/paths/craft-effective-prompts-copilot-microsoft-365/
- https://support.microsoft.com/en-us/excel/copilot/data-insights-with-copilot-in-excel
- https://support.microsoft.com/en-US/Excel/copilot/visualize-your-data-with-copilot-in-excel

---


### Highlighting, Sorting and Filtering Data with Copilot

Highlighting changes visual emphasis, sorting changes visible order and filtering changes which rows are shown. None of them changes the underlying business meaning. A prompt should define the comparison rule, tie-break order, filter conditions and whether hidden rows must remain available.

A visually persuasive sheet can still be analytically wrong. 'Highlight important orders' is undefined; 'highlight Returned=Yes and Gross_Sales at least 1000' is a reproducible rule. Filters can also hide the denominator, so the filtered count and original row count should be recorded together.

**How it works**

- Translate the business question into explicit Boolean conditions and a deterministic sort order.
- Ask Copilot to describe the intended change, then apply it to the named table.
- Count visible matches, clear the filter and confirm that the original row count returns.

**Worked example**

- The team reviews orders where Returned is Yes and gross sales are at least S$1,000.
- Rows are sorted by gross sales descending, then Order_ID ascending to break ties.
- The analyst records both the flagged count and the unchanged total table count.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The rule can be written using named fields, operators and values. | Colour alone would carry the only record of a business status. |
| The workbook owner needs a reversible view, not a deletion of non-matching records. | Filtering would hide excluded rows from a report without disclosing the denominator. |

**Practitioner quality lens**

- Rule: Write the exact condition before applying any colour or filter.
- Denominator: Record total rows and visible rows together.
- Reversible: Clear the filter and confirm no records were deleted or overwritten.

**Authoritative references**

- https://support.microsoft.com/en-US/Excel/copilot/visualize-your-data-with-copilot-in-excel
- https://support.microsoft.com/en-us/excel/copilot/get-started-with-copilot-in-excel

---


### Generating Formula Columns from Plain-English Requests

Copilot can propose native Excel formulas and add calculated columns. In a table, structured references use names such as [@Units] and [@Unit_Price], making row logic easier to read and resilient when the table grows. A generated formula remains a hypothesis until it is checked against the business rule.

Formula syntax can be valid while the logic is wrong: discount might be applied twice, margin might use gross rather than net sales, or blanks might become zero without approval. Formula explanation, edge-case tests and independent totals are therefore part of the task, not optional polish.

**How it works**

- Write the business rule in words, including units, blank handling, rounding and error behaviour.
- Ask for one structured-reference formula and an explanation before filling the calculated column.
- Test representative, boundary and exceptional rows; then reconcile the column to independent totals.

**Worked example**

- Gross_Sales equals Units multiplied by Unit_Price.
- Net_Sales equals Gross_Sales less Gross_Sales times Discount_Rate.
- Margin_Rate uses IFERROR(Gross_Profit divided by Net_Sales, zero), formatted as a percentage.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The rule is deterministic and can be expressed using native Excel functions. | The requested value is a subjective classification presented as a precise calculation. |
| A control calculation or small hand-worked sample can verify the result. | The formula would embed an unapproved business threshold or conceal missing data. |

**Practitioner quality lens**

- Semantics: Confirm the numerator, denominator, units, signs and timing.
- Edge cases: Check blanks, zeros, returns, discounts and one high-value row.
- Reconciliation: Tie column totals to an independent control before use.

**Authoritative references**

- https://support.microsoft.com/en-us/excel/copilot/data-insights-with-copilot-in-excel
- https://support.microsoft.com/en-US/Excel/using-structured-references-with-excel-tables
- https://support.microsoft.com/en-us/Excel/copilot/copilot-formula-suggestions-turn-on-off

---


### Lab 1 — Prepare the Workbook and Create the Copilot Control Trail

Learning outcome: LO1: confirm the available Copilot experience, preserve the source data, create a named Excel table and establish prompt and verification controls.

Goal: Create a reversible C34 workbook whose source boundary, row grain and baseline controls are explicit before Copilot makes any change.

You will import the synthetic HarbourLight order file, save it as a modern Excel workbook, convert the source rows into a named table and create Control and Prompt_Log sheets. You will use Copilot in Chat and Plan only to describe the data and propose a safe sequence. The raw source remains unchanged.

**What you'll build**

work-c34/C34-HarbourLight-Copilot-Analysis.xlsx with Raw_Orders, Control and Prompt_Log sheets, a tblOrdersRaw table, baseline counts and a recorded Copilot access note   (Tools: Excel for Microsoft 365 or Excel for the web · Copilot · harbourlight-orders-raw.csv.)

**Prerequisites**

- Download the repository and keep labs/assets/harbourlight-orders-raw.csv beside the other C34 assets.
- Sign in to an eligible Microsoft 365 account and open Excel or Excel for the web.
- Create a work-c34 training folder in OneDrive or SharePoint. Confirm you can save an .xlsx file there, cloud sync is complete and AutoSave is active. Use only the supplied synthetic data.

**Step-by-step**

1. Open labs/assets/harbourlight-orders-raw.csv in Excel. Select File > Save As and save C34-HarbourLight-Copilot-Analysis.xlsx inside your OneDrive or SharePoint work-c34 folder. Confirm the title bar shows the cloud location and AutoSave is On, then rename the first sheet Raw_Orders. Do not correct, sort or delete any source value.

   ```bash
   Expected source headers:
Order_ID | Order_Date | Region | Channel | Product | Category | Units | Unit_Price | Unit_Cost | Discount_Rate | Returned | Customer_Note
Required file state: .xlsx in OneDrive or SharePoint; cloud sync complete; AutoSave On
   ```

2. Write the grain statement above the control area in a new sheet named Control: 'One data row represents one HarbourLight order identified by Order_ID.' On Raw_Orders, click inside the data, select Home > Format as Table, confirm My table has headers and choose any accessible style. On Table Design, set Table Name to tblOrdersRaw.

   ```bash
   Required table name: tblOrdersRaw
Required grain: one row = one order
Required key: Order_ID
   ```

3. On Control, enter the labels below in A4:A9. In B4:B9 enter formulas that read tblOrdersRaw. Use ROWS for row count, COUNTA for populated Order_ID values, MIN and MAX for the date range, SUM for Units and SUMPRODUCT for gross sales. Format dates as yyyy-mm-dd and gross sales as S$.

   ```bash
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

4. Create a sheet named Prompt_Log. Copy the header row from labs/assets/prompt-and-verification-log-template.csv into A1:J1, format it as a table named tblPromptLog and add the first record. State the Copilot entry point you can see and whether Edit, Plan and Chat choices are available. If a label differs, record the label exactly.

   ```bash
   Lab,Timestamp,Mode,Goal,Data_Boundary,Prompt,Proposed_Logic,Workbook_Change,Verification,Decision
1,<TODAY>,Chat,Describe source structure,tblOrdersRaw,<PASTE PROMPT>,<COPILOT RESPONSE>,No change,<CHECKS>,Keep or revise
   ```

5. Open Copilot. In Chat, submit the first prompt below and compare the response with the Control sheet. Then choose Plan and submit the second prompt. Do not approve workbook edits. Record both prompts, the proposed logic and your decision in tblPromptLog.

   ```bash
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


**Test it**

Raw_Orders must contain table tblOrdersRaw with exactly 36 data rows and 36 populated Order_ID values. Control must show earliest date 2026-01-05, latest date 2026-04-28, 36 rows, 36 populated IDs and the same Units and gross-sales controls as labs/assets/expected-controls.md. Prompt_Log must contain one Chat and one Plan record, both with 'No change' in Workbook_Change. Raw_Orders must still match the CSV.

**Checkpoint and rejoin point**

Save and close the workbook. This file is the Lab 1 checkpoint. Lab 2 copies Raw_Orders into a working sheet. If you need to rejoin, follow the Lab 1 rebuild checklist in labs/assets/harbourlight-checkpoints.md.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| The Copilot button is missing. | Confirm the signed-in account, current Excel build, connected-experience settings and organisation policy. Also confirm the workbook is .xlsx in OneDrive or SharePoint, cloud sync is complete and AutoSave is On. Pair with the trainer for prompt comparison while continuing the workbook controls if access remains unavailable. |
| Copilot appears before saving but becomes unavailable in the workbook. | Use File > Save As to move the workbook into your OneDrive or SharePoint work-c34 folder, wait for sync, turn AutoSave On, close and reopen the cloud file, then retry. |
| The table includes blank rows or stops before the last order. | Select Table Design > Resize Table and set the range from the 12 headers through the final populated row. |
| The date controls show numbers instead of dates. | Keep the formulas and apply the yyyy-mm-dd number format to Control!B6:B7. |

**Challenge**

Add a duplicate-ID control that returns the row count minus the unique Order_ID count. Explain why a zero result is necessary but not sufficient to prove the source is ready.

**Reflection**

Which baseline control would reveal the most serious accidental change later in the workflow, and why?

> **Note:** The complete lab and its support-file references are in labs/lab-01-*.md. Use only the supplied synthetic HarbourLight data or information you are authorised to process. Do not paste credentials, confidential business material or sensitive personal data into Copilot.

---


### Lab 2 — Apply Reproducible Highlights, Sorts and Filters

Learning outcome: LO2: translate a business question into explicit highlight, sort and filter rules and verify that the resulting view is reversible.

Goal: Create a review view for returned and high-discount orders without deleting rows, hiding the denominator or changing the protected source.

You will copy the source into a working sheet, state deterministic review rules and ask Copilot to apply highlighting, sorting and filtering one operation at a time. You will record total and visible row counts, clear all filters and confirm that the source and working tables still contain the same orders.

**What you'll build**

An Orders_Working sheet with tblOrdersWorking, reversible highlighting, an explicit multi-level sort, a returned-order filter and Prompt_Log evidence for every applied change   (Tools: Excel · Copilot Edit or Plan · Control sheet · Prompt_Log.)

**Prerequisites**

- Completed Lab 1 workbook with Raw_Orders, tblOrdersRaw, Control and Prompt_Log.
- The source row count and Order_ID count both equal 36.
- Keep Raw_Orders unchanged; all direct changes in this lab go to Orders_Working.

**Step-by-step**

1. Right-click Raw_Orders, select Move or Copy > Create a copy, place it at the end and rename it Orders_Working. Click inside the copied table and set its Table Name to tblOrdersWorking. Confirm that Raw_Orders still contains tblOrdersRaw and 36 rows.

   ```bash
   Required sheet: Orders_Working
Required table: tblOrdersWorking
Protected source: Raw_Orders / tblOrdersRaw
   ```

2. On Control, create a Lab 2 rule block with the exact definitions below. Write the total row count beside it before any filter. Add a Prompt_Log row in Plan mode and ask Copilot to restate the rules as Boolean conditions without acting. Revise the wording until its conditions match exactly.

   ```bash
   Highlight rule A: Returned equals Yes
Highlight rule B: Discount_Rate is greater than or equal to 0.15
Sort rule: Units descending, then Order_ID ascending
Filter rule: Returned equals Yes
Preserve rule: do not delete rows or edit cell values
   ```

3. Switch to Edit only after the plan matches. Ask Copilot to highlight Returned=Yes rows with a pale red fill and Discount_Rate>=0.15 cells with a pale amber fill in tblOrdersWorking. Ask it to describe the ranges or rules it changed. Review every changed sheet, range and object; confirm only tblOrdersWorking formatting changed and use Undo if the scope differs. Inspect at least one matching and one non-matching row. On Control, enter =COUNTIF(tblOrdersWorking[Discount_Rate],">=0.15") and confirm 11. Record the accepted or rejected change scope, count and evidence in Prompt_Log.

   ```bash
   Apply these visual rules only to tblOrdersWorking:
1. Pale red row highlight when Returned exactly equals Yes.
2. Pale amber cell highlight when Discount_Rate >= 0.15.
Do not change values, order or visibility. After acting, state the exact rules applied.
   ```

4. Ask Copilot to sort tblOrdersWorking by Units descending and Order_ID ascending as the tie-breaker. Review the changed sheets, ranges and objects, use Undo if anything outside tblOrdersWorking changed, then check the first five Order_ID and Units pairs against the manual Data > Sort result. Record whether the tie-break order is deterministic and whether the change scope was accepted.

   ```bash
   Sort tblOrdersWorking by Units, Largest to Smallest. For equal Units, sort Order_ID, A to Z. Keep every row and all existing formats. State the first five Order_ID and Units values after sorting.
   ```

5. Ask Copilot to filter Returned to Yes. In Control, record the visible returned-order count and the unchanged total row count. Review the changed sheets, ranges and objects and use Undo if the scope differs. Then select Data > Clear. Confirm that all 36 rows return, the table still has 36 populated IDs and Raw_Orders remains unchanged. Record the accepted or rejected scope and save with no filter active.

   ```bash
   Filter tblOrdersWorking so Returned exactly equals Yes. Do not delete non-matching rows. State the visible match count and the total table row count. I will clear the filter after verification.
   ```


**Test it**

The working table must contain 36 rows before and after the filter. The returned-order filter must show the exact count in labs/assets/expected-controls.md; the high-discount rule must match the listed count; and the maximum Units value plus first tie-break order must match the control. After Data > Clear, all 36 orders must be visible. Raw_Orders values and order must remain unchanged.

**Checkpoint and rejoin point**

Save the workbook with tblOrdersWorking sorted by Units descending and no active filter. Lab 3 adds formula columns to this table. To rejoin, rebuild Orders_Working from Raw_Orders and use the Lab 2 rules in labs/assets/harbourlight-checkpoints.md.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| Copilot highlights cells but not the full returned row. | Keep the cell rule if it is clear, or select the table data range and use a conditional-format formula based on the Returned column. Record the final range and rule. |
| The filter count differs from the control. | Inspect the exact Returned values for spaces or case differences before changing anything; the supplied file uses canonical Yes and No values. |
| The sort changes Raw_Orders. | Undo immediately, confirm the active sheet and table name, then repeat only on tblOrdersWorking. |

**Challenge**

Add a second reversible filter for Discount_Rate>=0.15 and Returned=No. Record both the visible count and the full denominator, then explain why the combination answers a different question.

**Reflection**

Why is an explicit filter denominator important when a screenshot of the filtered view is shared?

> **Note:** The complete lab and its support-file references are in labs/lab-02-*.md. Use only the supplied synthetic HarbourLight data or information you are authorised to process. Do not paste credentials, confidential business material or sensitive personal data into Copilot.

---


### Lab 3 — Generate and Reconcile Formula Columns

Learning outcome: LO2: generate structured-reference formula columns from plain-language rules, inspect the logic and reconcile the calculated results to independent controls.

Goal: Extend tblOrdersWorking with six auditable calculated columns and prove that representative rows and headline totals match the supplied business rules.

You will write the calculation rules in words, ask Copilot for one structured-reference formula at a time and inspect every formula before filling it through the table. You will verify a no-discount row, a discounted row, a returned order, the zero-error path and independent totals on the Control sheet.

**What you'll build**

Six calculated columns in tblOrdersWorking - Gross_Sales, Discount_Amount, Net_Sales, Cost_Amount, Gross_Profit and Margin_Rate - plus formula checks and reconciled totals on Control   (Tools: Excel formulas · Copilot · structured references · expected-controls.md.)

**Prerequisites**

- Completed Lab 2 workbook with tblOrdersWorking and no active filter.
- Control shows 36 total rows and the source gross-sales value from Lab 1.
- Open labs/assets/formula-and-verification-rules.md before writing a formula.

**Step-by-step**

1. On Control, copy the six business rules from labs/assets/formula-and-verification-rules.md into a Lab 3 block. Include currency units, blank handling and the Margin_Rate denominator. Add a Prompt_Log row in Chat and ask Copilot to return only the proposed structured-reference formulas and explanations; do not apply them yet.

   ```bash
   Required output columns:
Gross_Sales | Discount_Amount | Net_Sales | Cost_Amount | Gross_Profit | Margin_Rate

Use native Excel formulas. Do not use the COPILOT function for numeric calculations.
   ```

2. Review the proposed Gross_Sales and Discount_Amount formulas. In tblOrdersWorking add the two headers and enter the approved formulas in the first data row so Excel fills each calculated column. Select three rows and confirm that the formula uses current-row structured references.

   ```bash
   Gross_Sales: =[@Units]*[@Unit_Price]
Discount_Amount: =[@Gross_Sales]*[@Discount_Rate]
   ```

3. Add Net_Sales, Cost_Amount and Gross_Profit one column at a time. After every column, ask Copilot to explain the sign and inputs, then compare one row with a calculator or hand-worked result. Record the selected Order_ID, inputs, expected value and observed value in Prompt_Log.

   ```bash
   Net_Sales: =[@Gross_Sales]-[@Discount_Amount]
Cost_Amount: =[@Units]*[@Unit_Cost]
Gross_Profit: =[@Net_Sales]-[@Cost_Amount]
   ```

4. Add Margin_Rate and format the entire column as 0.0%. The approved denominator is Net_Sales. Use IFERROR to return zero if Net_Sales is zero. Check that the formula is filled in all 36 data rows and that no formula-error values appear. On Control, create two scratch cells containing Gross_Profit=0 and Net_Sales=0, apply =IFERROR(<GROSS_PROFIT_CELL>/<NET_SALES_CELL>,0) and confirm the result is 0. Delete the scratch inputs after recording the check; do not add a synthetic order to the table.

   ```bash
   Margin_Rate: =IFERROR([@Gross_Profit]/[@Net_Sales],0)
Required format: 0.0%
   ```

5. On Control, calculate SUM for Gross_Sales, Discount_Amount, Net_Sales, Cost_Amount and Gross_Profit. Add a weighted overall margin formula: total Gross_Profit divided by total Net_Sales. Compare the six results with labs/assets/expected-controls.md. Explicitly test HL-1001, HL-1003, HL-1007, HL-1018 and HL-1032 against the named row controls. Review every changed sheet, range and object; confirm only the six approved calculated columns and Control checks changed, use Undo for scope creep and record the accepted or rejected scope. If a value differs, inspect formulas and inputs rather than overwriting it.

   ```bash
   Overall Margin_Rate control:
=SUM(tblOrdersWorking[Gross_Profit])/SUM(tblOrdersWorking[Net_Sales])

Do not use AVERAGE(tblOrdersWorking[Margin_Rate]) for the overall margin.
   ```


**Test it**

All six calculated columns must contain formulas for all 36 rows with no formula-error values. The formula text must use structured references and the overall margin must use total Gross_Profit divided by total Net_Sales. The six totals and the named representative Order_ID checks must exactly match labs/assets/expected-controls.md. Copilot's explanation alone does not satisfy the check.

**Checkpoint and rejoin point**

Save the workbook with all formulas present and no active filter. Lab 4 copies tblOrdersWorking to a clean analysis sheet. To rejoin, use the formula block and control totals in labs/assets/harbourlight-checkpoints.md.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| Excel creates A1 references instead of structured references. | Confirm the range is an Excel table, select the first data cell under the new header and build the formula by clicking the current-row cells; Excel should insert named column references. |
| The overall margin differs from the control while row formulas look correct. | Confirm you divided total Gross_Profit by total Net_Sales and did not average row percentages. |
| Only the first row contains the formula. | Double-click the fill handle or re-enter the formula in the table column and confirm calculated-column fill is enabled. Do not paste hardcoded values down the column. |

**Challenge**

Add a Recalculation_Check column that compares Net_Sales with Gross_Sales minus Discount_Amount and returns OK only when the absolute difference is below 0.005. Explain the tolerance.

**Reflection**

Which formula check is independent enough to catch a fluent but logically wrong Copilot suggestion?

> **Note:** The complete lab and its support-file references are in labs/lab-03-*.md. Use only the supplied synthetic HarbourLight data or information you are authorised to process. Do not paste credentials, confidential business material or sensitive personal data into Copilot.

---


### Topic 01 Recap - Mapped to Learning Outcomes

Use this checkpoint to explain what you can now do and identify any lab evidence you still need to repair.

| Learning outcome | Evidence from this topic |
|---|---|
| LO1 - Prepare and Prompt | Confirm the available Copilot experience, keep a protected source sheet, convert one-row-per-order data into a named Excel table and use Goal-Context-Data-Constraints-Output-Review prompts. |
| LO2 - Transform and Calculate | Apply explicit highlight, sort and filter rules; generate structured-reference formulas; and reconcile row-level calculations to independent control totals before relying on them. |

---


## Topic 02 — AI-Powered Data Analysis and Insights  (Second half · 3 labs)

Cleaning and enriching data · PivotTables and charts from a prompt · trends, outliers and insights · advanced analysis with Python in Excel · verification and prompt best practices

**Key concepts**

- Defined cleaning rules — Correct only documented text, spacing, format and missing-value issues; preserve the raw source.
- Question-to-visual design — Choose grain, dimensions, measures, aggregation and chart form from the decision question.
- Descriptive insight — Describe comparison, trend, distribution and outlier evidence before considering explanations.
- Python-assisted analysis — Review the referenced data, generated code, statistical method and returned output together.
- Static versus refreshable output — Label inserted images or tables that do not update when source data changes.
- Evidence chain — Trace every headline claim to source rows, a calculation and an independent cross-check.


### Cleaning and Enriching Data with Copilot

Cleaning makes existing values conform to a defined schema; enrichment adds a new field from a rule, lookup or reviewed classification. The source sheet should remain unchanged. The cleaning log records the issue, rule, affected count and verification so corrections are auditable.

Inconsistent text, number formats and extra spaces can split categories or produce wrong summaries. Microsoft's Clean Data experience focuses on these common patterns, but availability can vary. A manual or Copilot-assisted correction still needs a canonical value list and before/after counts.

**How it works**

- Profile the source and compare observed values with the supplied data dictionary.
- Copy the table to a working sheet; correct one issue type at a time and log the affected rows.
- Add deterministic enrichment first, then review any text classification row by row against a taxonomy.

**Worked example**

- Region values such as 'north', 'North ' and 'NORTH' become the canonical value 'North'.
- Channel values map only to Store, Online or Partner according to the dictionary.
- Customer_Note receives a reviewed Note_Theme; blanks remain 'No note' rather than invented feedback.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The canonical schema and acceptable value set are documented. | A correction would guess a missing business fact or overwrite an identifier. |
| The original data and a change log are retained for comparison. | A free-text classification will be treated as objective truth without human review. |

**Practitioner quality lens**

- Preserve: Keep the raw sheet unchanged and make corrections in a working table.
- Count: Record affected rows before and after each rule.
- Taxonomy: Use a small defined category list and retain Unknown when evidence is insufficient.

**Authoritative references**

- https://support.microsoft.com/en-us/excel/clean-data-in-excel
- https://support.microsoft.com/en-us/excel/copilot/data-insights-with-copilot-in-excel

---


### Building PivotTables and Charts from a Prompt

A PivotTable aggregates measures across dimensions at a chosen grain. A chart encodes that summary visually. A complete prompt names the source table, row and column fields, aggregation, filters, order, chart type, title and the decision the view should support.

Copilot can build a polished result quickly, but speed does not resolve analytical design. Sum of sales, average margin and count of orders answer different questions. A chart can also exaggerate differences through an unsuitable scale, missing units or too many categories.

**How it works**

- State the decision question, grain, dimensions, measures and required filters.
- Generate the PivotTable first and reconcile its grand total to the cleaned table.
- Choose a chart that fits comparison or time trend, then verify title, units, labels and source link.

**Worked example**

- Question: how did monthly net sales change by canonical region?
- Rows use Month, columns use Region and values use Sum of Net_Sales.
- A line chart shows month on the x-axis and S$ net sales on the y-axis; the Pivot grand total must tie out.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The table has a stable grain and measures have defined aggregations. | The measure is a percentage that should be recomputed from totals rather than averaged row by row. |
| The intended comparison or trend can be shown without hiding material categories. | A chart is requested before the question, denominator or aggregation is agreed. |

**Practitioner quality lens**

- Grain: Name what one Pivot cell represents.
- Tie-out: Reconcile the Pivot grand total to the source-table control.
- Chart truth: Show units, full categories and an honest scale appropriate to the question.

**Authoritative references**

- https://support.microsoft.com/en-US/Excel/copilot/visualize-your-data-with-copilot-in-excel
- https://support.microsoft.com/en-us/excel/overview-of-pivottables-and-pivotcharts
- https://support.microsoft.com/en-us/excel/copilot/get-started-with-copilot-in-excel

---


### Surfacing Trends, Outliers and Insights

A trend describes change across an ordered period; an outlier is an observation unusually distant under a stated rule; an insight connects a verified pattern to a relevant decision. None of these, by itself, proves why the pattern occurred.

Prompts such as 'what is interesting?' can surface useful candidates, but they can also produce selective or causal-sounding narratives. Start with a baseline, comparison and explicit outlier rule. Label observed values separately from hypotheses that require more evidence.

**How it works**

- Define the metric, period, comparison and minimum volume needed for interpretation.
- Ask for descriptive results and an explicit outlier rule before requesting explanations.
- Cross-check the cited rows, record limitations and convert only relevant verified patterns into actions.

**Worked example**

- Monthly net sales are compared by region, while returned-order rate uses returned orders divided by orders.
- High-value orders are flagged by a stated IQR rule and then inspected for data-quality issues.
- A spike is described as observed; promotion, channel mix or data error remain hypotheses.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The time order, denominator and comparison group are stable. | A short or incomplete period is used to claim a persistent trend. |
| The output cites underlying values and states the method used to identify an outlier. | Correlation or a coincident change is presented as a proven cause. |

**Practitioner quality lens**

- Baseline: Show the comparison period, denominator and sample size.
- Method: State the trend or outlier rule in reproducible terms.
- Language: Use observed for evidence and hypothesis for a possible explanation.

**Authoritative references**

- https://support.microsoft.com/en-us/excel/copilot/data-insights-with-copilot-in-excel
- https://support.microsoft.com/en-us/excel/get-direct-answers-to-your-data-analysis-questions

---


### Advanced Analysis with Python in Excel

Copilot can use Python-based analysis to interpret a question, compute statistics and return explanations, tables or visuals. Direct-answer output may be static. Advanced analysis can open a new sheet and expose Python code or a refreshable Python cell, depending on the available experience.

Python expands the range of analysis but does not remove review obligations. The analyst must verify the referenced data, cleaning choices, grouping logic, missing-value treatment, statistical method and returned values. Python in Excel runs in a Microsoft cloud container and has defined access and network boundaries.

**How it works**

- Ask a precise analytical question and state the table, fields, period, grouping and expected output.
- Open the generated logic or code; inspect row filters, aggregations, missing values and method assumptions.
- Recompute headline results with Excel or a PivotTable, label static outputs and save the analysis notes.

**Worked example**

- The team asks for monthly net-sales trends, return rates and an IQR review of high-value orders.
- Generated Python groups only canonical rows and reports the count excluded for unresolved categories.
- Excel control cells and the Pivot grand total independently confirm the headline values.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The question needs deeper exploratory statistics or visuals and the available license supports the feature. | The analysis depends on unavailable external network calls or hidden local files. |
| A reviewer can inspect the generated method and reproduce headline results independently. | A static inserted output will be mistaken for a refreshable result after the source changes. |

**Practitioner quality lens**

- Inputs: Confirm the exact table, rows, columns, filters and missing-value treatment.
- Method: Review code and assumptions; do not accept the narrative alone.
- Reproducibility: Tie headline values to Excel controls and label static outputs visibly.

**Authoritative references**

- https://support.microsoft.com/en-us/excel/get-direct-answers-to-your-data-analysis-questions
- https://support.microsoft.com/en-US/Excel/python/introduction-to-python-in-excel
- https://support.microsoft.com/en-US/Excel/python/data-security-and-python-in-excel

---


### Verifying Results and Prompt Best Practices

Verification is a chain of checks from source structure to formula, aggregation, visual and written claim. The C34 quality gate uses protected source data, a prompt log, edge-case tests, independent control totals, traceable claims and a named human decision.

Copilot can produce fluent explanations and valid-looking formulas that are incomplete or wrong. Microsoft advises users to review, edit and verify generated content. A compact repeatable gate makes that advice operational and prevents an attractive workbook from bypassing basic evidence checks.

**How it works**

- Validate row grain, types, category values, duplicates and source control totals.
- Inspect formulas, representative rows, Pivot totals, chart encodings and Python logic.
- Record each claim, supporting value, limitation, owner and Share, Revise or Hold decision.

**Worked example**

- The executive summary states a regional sales movement and cites the Pivot values behind it.
- A return-rate statement shows numerator and denominator, not only the percentage.
- An outlier explanation stays a hypothesis until operational evidence supports it.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Any generated output will be shared, used in a decision or reused as a template. | A fluent answer is treated as proof without checking the workbook. |
| Another reviewer needs to reproduce the conclusion without relying on the chat history. | A control total is copied from the same generated output it is supposed to verify. |

**Practitioner quality lens**

- Independent: Use a different method or source for the control check.
- Traceable: Link every headline statement to cells, rows or a documented calculation.
- Decisive: Choose Share, Revise or Hold and state the owner and unresolved limitation.

**Authoritative references**

- https://support.microsoft.com/en-us/excel/copilot/frequently-asked-questions-about-copilot-in-excel
- https://support.microsoft.com/en-us/excel/copilot/data-insights-with-copilot-in-excel
- https://support.microsoft.com/en-US/Excel/copilot/visualize-your-data-with-copilot-in-excel

---


### Lab 4 — Clean and Enrich the Analysis Table

Learning outcome: LO3: apply documented cleaning rules to a copy of the working table, add deterministic analysis fields and verify categories, row counts and formula totals.

Goal: Create a clean analysis table with canonical Region and Channel values, a Month field, a numeric return flag and a reviewed note-theme classification while preserving the raw source.

You will copy the formula-complete working table to Orders_Clean, profile observed category values and apply the supplied canonical rules one issue at a time. You will add Month, Return_Flag and Note_Theme fields, retain Unknown when a note is ambiguous and prove that cleaning did not change row-level monetary results.

**What you'll build**

An Orders_Clean sheet with tblOrdersClean, canonical categories, Month, Return_Flag and Note_Theme fields, plus a cleaning log and before/after control checks   (Tools: Excel · Copilot · Clean Data when available · harbourlight-data-dictionary.md.)

**Prerequisites**

- Completed Lab 3 workbook with tblOrdersWorking and reconciled formula totals.
- Open labs/assets/harbourlight-data-dictionary.md and use only its canonical values and note taxonomy.
- Raw_Orders remains unchanged and is the comparison source.

**Step-by-step**

1. Copy Orders_Working to the end, rename it Orders_Clean and set the copied table name to tblOrdersClean. On Control, create a Cleaning_Log table with Issue, Rule, Before_Count, After_Count, Affected_Rows, Verification and Decision. Record the 36-row baseline and the five Lab 3 monetary totals.

   ```bash
   Required working sheet: Orders_Clean
Required table: tblOrdersClean
Required log columns: Issue | Rule | Before_Count | After_Count | Affected_Rows | Verification | Decision
   ```

2. Ask Copilot in Chat to list distinct Region, Channel, Product and Category values with counts from tblOrdersClean. Compare the response with Data > Filter for each column. Record every value that differs from the canonical dictionary by case or surrounding spaces. Do not clean yet.

   ```bash
   List the distinct values and counts in Region, Channel, Product and Category from tblOrdersClean. Do not change the workbook. Preserve exact spaces and case in the displayed values. Flag only values that do not match the supplied canonical dictionary.
   ```

3. Clean Region and Channel one field at a time using the dictionary. If Clean Data is available, review each suggestion before applying it; otherwise ask Copilot to propose exact replacements and apply only the approved mapping. After each action, review every changed sheet, range and object; confirm only the named text cells in tblOrdersClean changed and use Undo if the scope differs. Confirm that Region contains North, South and Central only, while Channel contains Store, Online and Partner only. Record affected counts and the accepted or rejected scope.

   ```bash
   Canonical Region values: North | South | Central
Canonical Channel values: Store | Online | Partner
Allowed operations: trim surrounding spaces and standardise case
Do not infer or replace a value outside the mapping.
   ```

4. Add Month and Return_Flag calculated columns. Month must be yyyy-mm text derived from Order_Date. Return_Flag must equal 1 only when Returned exactly equals Yes and 0 otherwise. Fill all rows, record the sum of Return_Flag and compare it with the returned-order count from Lab 2.

   ```bash
   Month: =TEXT([@Order_Date],"yyyy-mm")
Return_Flag: =--([@Returned]="Yes")
   ```

5. Add Note_Theme using only Delivery, Product, Return, No note and Unknown. Ask Copilot to propose a classification with a short reason, but review every row against the dictionary. Blank or whitespace-only notes become No note. A note that does not match one defined cue remains Unknown. Review all changed sheets, ranges and objects, use Undo if anything outside Note_Theme changed and record the accepted or rejected scope. Finish by reconciling row count, populated IDs and all five monetary totals to Lab 3.

   ```bash
   Classify Customer_Note using only the supplied taxonomy. Return Order_ID | Note_Theme | cue used. Do not invent a reason. Blank text becomes No note; ambiguous text becomes Unknown. I will review every proposed label before applying it.
   ```


**Test it**

tblOrdersClean must contain 36 rows and 36 populated Order_ID values. Region must have exactly three canonical values and Channel exactly three. Month must contain only 2026-01 through 2026-04. Sum of Return_Flag, the five monetary totals and all Note_Theme counts must match labs/assets/expected-controls.md. Raw_Orders and Orders_Working must remain unchanged.

**Checkpoint and rejoin point**

Save the workbook with tblOrdersClean fully reconciled. Labs 5 and 6 use only this clean table for summaries. To rejoin, follow the Lab 4 mapping and field checklist in labs/assets/harbourlight-checkpoints.md.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| Clean Data shows no suggestions. | Use the exact distinct-value list and the supplied canonical mapping. Feature availability varies, and the verification controls are the same for a reviewed manual or Copilot-assisted correction. |
| A note receives a category outside the taxonomy. | Reject the output, restate the five allowed values and require Unknown for all unmatched cues. |
| Monetary totals change after cleaning text fields. | Undo the last action and inspect whether a formula or numeric field was included in the changed range. |

**Challenge**

Create a data-validation list for Region and Channel using the canonical values, then explain how validation prevents new defects without proving that existing records are correct.

**Reflection**

Which cleaning decision required human judgment rather than a mechanical text correction?

> **Note:** The complete lab and its support-file references are in labs/lab-04-*.md. Use only the supplied synthetic HarbourLight data or information you are authorised to process. Do not paste credentials, confidential business material or sensitive personal data into Copilot.

---


### Lab 5 — Build Reconciled PivotTables and Charts

Learning outcome: LO3: translate business questions into PivotTable grain, dimensions, measures and charts, then reconcile every grand total and denominator to the clean table.

Goal: Create an editable operations summary that shows monthly net sales by region and return rate by channel without hiding the underlying counts or overstating visual differences.

You will define two decision questions before asking Copilot to build anything. The first PivotTable and line chart show monthly net sales by canonical region. The second summary shows returned orders, order count and return rate by channel. You will verify grand totals, denominators, titles, units and source linkage.

**What you'll build**

A Pivot_Analysis sheet with two PivotTables, a monthly regional net-sales line chart, a channel return-rate chart, tie-out cells and a Prompt_Log record for each object   (Tools: Excel PivotTables · Excel charts · Copilot · tblOrdersClean · expected-controls.md.)

**Prerequisites**

- Completed Lab 4 workbook with tblOrdersClean and reconciled clean-table controls.
- Month contains 2026-01 through 2026-04 and Return_Flag contains only 0 and 1.
- No active filter is applied to tblOrdersClean.

**Step-by-step**

1. Create a sheet named Pivot_Analysis. At the top, write two questions and their intended grain. Question A: 'How did monthly net sales change by region?' Grain: one Pivot cell equals the sum of Net_Sales for one Month-Region combination. Question B: 'Which channel has the highest returned-order rate?' Grain: one row equals one canonical Channel.

   ```bash
   Question A fields:
Rows = Month | Columns = Region | Values = Sum of Net_Sales

Question B fields:
Rows = Channel | Values = Sum of Return_Flag and Count of Order_ID
Return rate = returned orders / order count
   ```

2. Ask Copilot to create PivotTable A from tblOrdersClean on Pivot_Analysis. If direct creation is unavailable, select Insert > PivotTable, choose tblOrdersClean and use the exact field layout. Format Net_Sales as S$ with two decimals, show grand totals and sort Month ascending. Review every changed sheet, range and object; confirm only the requested PivotTable was added and use Undo if the scope differs. Record the accepted or rejected scope in Prompt_Log.

   ```bash
   Create an editable PivotTable from tblOrdersClean on Pivot_Analysis. Put Month in Rows, Region in Columns and Sum of Net_Sales in Values. Show grand totals, sort Month ascending and format values as S$ with two decimals. Do not create a static pasted table.
   ```

3. Below Pivot A, add a tie-out cell that subtracts the Pivot grand total from SUM(tblOrdersClean[Net_Sales]). It must equal 0.00. Create a line chart from Pivot A with title 'Monthly Net Sales by Region', Month on the x-axis, S$ Net Sales on the y-axis and a visible legend for North, South and Central. Review the changed sheets, ranges and objects; confirm the chart is linked only to Pivot A and use Undo for any unrelated change.

   ```bash
   Required tie-out:
=SUM(tblOrdersClean[Net_Sales])-<PIVOT_A_GRAND_TOTAL_CELL>
Expected result: 0.00
   ```

4. Create PivotTable B using Channel as rows, Sum of Return_Flag and Count of Order_ID as values. Beside the Pivot, calculate Return_Rate for each channel as returned orders divided by order count, format as 0.0% and add a total row that uses the grand totals rather than averaging channel percentages. Review every changed sheet, range and object; confirm only Pivot B and its adjacent formulas changed and use Undo if the scope differs.

   ```bash
   Return_Rate formula: =<RETURNED_ORDERS_CELL>/<ORDER_COUNT_CELL>
Overall return rate: =<SUM_RETURN_FLAG_GRAND_TOTAL>/<COUNT_ORDER_ID_GRAND_TOTAL>
   ```

5. Create a clustered column chart using Channel and Return_Rate with title 'Returned-Order Rate by Channel'. Set the y-axis to percentage, start at zero and show data labels. Compare both PivotTables with labs/assets/expected-controls.md. Review all changed sheets, ranges and objects and record the accepted or rejected scope, exact totals, visual checks and any manual steps in Prompt_Log.

   ```bash
   Visual checks:
[ ] chart title names the metric and dimension
[ ] axis units match S$ or percentage
[ ] every canonical category is visible
[ ] line chart months are chronological
[ ] return-rate axis starts at zero
[ ] both source ranges remain linked and editable
   ```


**Test it**

Pivot A must contain four months, three regions and a grand total equal to tblOrdersClean Net_Sales with a 0.00 tie-out. Pivot B must show three channels, returned-order count, order count and rates that match labs/assets/expected-controls.md; the overall rate must use grand-total numerator and denominator. Both charts must be editable, linked, fully titled and use the correct units.

**Checkpoint and rejoin point**

Save the workbook with Pivot_Analysis visible and both tie-outs complete. Lab 6 references these values as independent checks. To rejoin, use the Pivot field layouts in labs/assets/harbourlight-checkpoints.md.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| Net_Sales is counted instead of summed. | Open Value Field Settings, choose Sum and verify that Net_Sales contains numeric values in all rows. |
| Months sort alphabetically in the wrong order. | Confirm Month uses yyyy-mm text or place the real Order_Date in rows and group it by Months and Years. |
| The chart omits a region or channel. | Inspect the Pivot filters and source categories, clear filters and refresh the PivotTable. |

**Challenge**

Add a Product gross-profit PivotTable and choose a chart. State why Sum of Gross_Profit is meaningful while a simple average of row Margin_Rate may not be the right product-level margin.

**Reflection**

Which tie-out proves the Pivot aggregation is complete, and what analytical error can it still miss?

> **Note:** The complete lab and its support-file references are in labs/lab-05-*.md. Use only the supplied synthetic HarbourLight data or information you are authorised to process. Do not paste credentials, confidential business material or sensitive personal data into Copilot.

---


### Lab 6 — Run Advanced Analysis and Write the Verified Decision Summary

Learning outcome: LO4: use Python-assisted Copilot for a bounded analytical question, inspect the generated method, reconcile headline values and produce a traceable decision summary.

Goal: Complete the HarbourLight workflow with a reviewed analysis of monthly trends, channel return rates and high-value-order outliers, followed by a Share, Revise or Hold decision.

You will ask Copilot for direct answers and advanced analysis using only tblOrdersClean. You will review the referenced fields, filters, groupings, IQR logic and generated code or explanation. You will reconcile the headline values to the Control and Pivot_Analysis sheets, then create a concise executive summary that keeps observations, hypotheses and limitations separate.

**What you'll build**

An Advanced_Analysis sheet with prompt, method, generated output and reconciliation; plus an Executive_Summary sheet with three verified findings, limitations, actions and a final decision   (Tools: Copilot direct answers · advanced analysis with Python in Excel · Excel controls · Pivot_Analysis · advanced-analysis-fallback.md.)

**Prerequisites**

- Completed Lab 5 workbook with reconciled Pivot A and Pivot B.
- Open labs/assets/advanced-analysis-brief-template.md and labs/assets/expected-controls.md.
- Before class, confirm the account shows the deeper or advanced analysis entry point. If it does not, open labs/assets/advanced-analysis-fallback.md so you can inspect saved Python logic and output hands-on.
- Use only tblOrdersClean; do not connect to external data or use real organisational information.

**Step-by-step**

1. Create Advanced_Analysis and Executive_Summary sheets. Copy the analysis brief template to Advanced_Analysis and complete its Question, Data, Filters, Metrics, Method, Output and Review fields. Require monthly net sales by region, returned-order rate by channel and an IQR review of order Net_Sales. State that outliers are candidates for review, not errors or causes.

   ```bash
   Question: What changed across months and regions, which channel has the highest returned-order rate, and which order Net_Sales values are high under the 1.5 x IQR rule?
Data: tblOrdersClean only
Filters: none; report missing or excluded rows
Review: reconcile with Control and Pivot_Analysis
   ```

2. Ask Copilot the direct-answer prompt below. Save the response, cited source fields and any inserted static table or image on Advanced_Analysis. If an inserted output will not refresh, place a visible 'STATIC - rerun after source change' label above it. Review every changed sheet, range and object, use Undo for unrelated changes and record the accepted or rejected scope.

   ```bash
   Using only tblOrdersClean, report:
1. Monthly Net_Sales by Region and the grand total.
2. Returned-order count, order count and Return_Rate by Channel.
3. Q1, Q3, IQR, upper fence and Order_ID values above the upper fence for Net_Sales.
Show the fields and filters used. Do not claim causes. Label inserted non-refreshing output as static.
   ```

3. Choose the follow-up for deeper or advanced analysis, or ask 'Enter advanced analysis mode'. Review the generated Python code or expanded logic. Confirm it selects tblOrdersClean, groups by canonical Month/Region or Channel, computes rate as sum(Return_Flag)/count(Order_ID), uses the 1.5 x IQR upper fence and does not silently drop rows. If the feature is unavailable, inspect the saved code and output in labs/assets/advanced-analysis-fallback.md line by line and paste the reviewed method plus your notes into Advanced_Analysis. In either route, record the inspected code lines or logic in Prompt_Log.

   ```bash
   Review checklist:
[ ] source is tblOrdersClean
[ ] no hidden filter
[ ] monthly grouping uses Month and Region
[ ] rate denominator is Order_ID count
[ ] Q1/Q3/IQR and upper fence are reported
[ ] excluded or missing rows are counted
[ ] output type is labelled static or refreshable
   ```

4. On Advanced_Analysis, create a reconciliation table with Metric, Advanced_Result, Independent_Result, Difference, Source and Status. Reconcile total Net_Sales, each channel order count and return count, the overall return rate, the highest monthly-region value and the listed high outlier Order_ID values. Every numeric difference must be zero within S$0.01 or 0.01 percentage points.

   ```bash
   Reconciliation columns:
Metric | Advanced_Result | Independent_Result | Difference | Source | Status
Status rule: OK only when the difference is within the stated tolerance.
   ```

5. On Executive_Summary, write exactly three findings using the template below. Each finding must cite workbook evidence, distinguish OBSERVED from HYPOTHESIS and name a practical owner or next check. Add limitations and choose SHARE only if every required reconciliation is OK; otherwise choose REVISE or HOLD. Record the reason and owner.

   ```bash
   Finding | Evidence | Type | Why it matters | Next check | Owner
Types: OBSERVED or HYPOTHESIS
Final decision: SHARE | REVISE | HOLD
Required limitations: synthetic data; four-month window; returned status only; no causal evidence
   ```


**Test it**

Advanced_Analysis must contain the completed brief, direct answer, reviewed code or method, output-type label and reconciliation table. Every required metric and outlier must match labs/assets/expected-controls.md within the stated tolerance. Executive_Summary must contain exactly three findings, evidence references, types, next checks, owners, four required limitations and a final SHARE, REVISE or HOLD decision. SHARE is allowed only when every reconciliation status is OK.

**Checkpoint and rejoin point**

This is the final course checkpoint. Keep the workbook with Raw_Orders, Control, Prompt_Log, Orders_Working, Orders_Clean, Pivot_Analysis, Advanced_Analysis and Executive_Summary. Use it as a practice model, not as evidence about a real organisation.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| Advanced analysis is not available in the current account. | Open labs/assets/advanced-analysis-fallback.md, inspect the saved Python logic and output, identify the source fields, groupings, rate denominator and IQR rule, then complete the same reconciliations in your own workbook. Pair with the trainer only for the interface demonstration. |
| The analysis reports a different return rate. | Check that the numerator is Sum of Return_Flag and the denominator is Count of Order_ID at the same channel grain. |
| The generated narrative claims a cause. | Relabel the statement HYPOTHESIS, remove causal language and name the additional operational evidence needed. |

**Challenge**

Ask for a sensitivity check using a 3 x IQR upper fence. Compare the flagged orders with the 1.5 x IQR result and explain how the threshold changes the review workload without proving which orders are wrong.

**Reflection**

What evidence would make the final summary trustworthy to a reviewer who never saw the Copilot chat?

> **Note:** The complete lab and its support-file references are in labs/lab-06-*.md. Use only the supplied synthetic HarbourLight data or information you are authorised to process. Do not paste credentials, confidential business material or sensitive personal data into Copilot.

---


### Topic 02 Recap - Mapped to Learning Outcomes

Use this checkpoint to explain what you can now do and identify any lab evidence you still need to repair.

| Learning outcome | Evidence from this topic |
|---|---|
| LO3 - Summarise and Visualise | Correct defined quality issues, build PivotTables at the intended grain, choose charts that match the question and separate observed patterns from possible explanations. |
| LO4 - Analyse and Verify | State the analytical question, review Python-based logic and outputs, cross-check headline values, record limitations and communicate only decision-relevant, evidence-backed findings. |

---


## Wrap-Up - The Complete C34 Workflow

The finished output is not simply a polished workbook. It is a traceable chain from source data through Copilot actions and independent checks to a named human decision.

**Prepare and transform**

- Confirm access, mode and a reversible versioning approach.
- Define row grain and convert the bounded source into a named Excel table.
- Use explicit rules for filters, sorting, highlighting and generated formula columns.

**Summarise and analyse**

- Clean against a canonical dictionary and retain the source sheet.
- Define grain, measure and aggregation before creating PivotTables and charts.
- Use Python-assisted analysis for deeper questions while reviewing generated logic.

**Verify and communicate**

- Reconcile counts, formula totals, Pivot grand totals and analytical headline values.
- Label static outputs and separate observed evidence from hypotheses.
- Choose Share, Revise or Hold with a named owner and visible limitations.

---


## Next Steps

- Re-run all six labs from the raw CSV without referring to your completed workbook.
- Adapt the G-C-D-C-O-R prompt and verification log to one authorised workbook in your role.
- Create a small reusable control panel with row counts, unique IDs and source totals.
- Review Microsoft Support before delivery because Copilot labels, availability and capabilities continue to change.


## Glossary

- **Calculated column** — A table column whose formula is filled consistently for every data row.
- **Canonical value** — The approved spelling and format used for a category after cleaning.
- **Control total** — An independently computed count or sum used to verify another output.
- **Edit mode** — The Copilot choice that can make changes directly in the workbook.
- **Grain** — What one row or one aggregated cell represents.
- **G-C-D-C-O-R** — Goal, Context, Data, Constraints, Output and Review - the C34 prompt framework.
- **IQR** — Interquartile range; the distance between the 25th and 75th percentiles.
- **Outlier** — An observation unusually distant under a stated method, not automatically an error.
- **PivotTable** — An interactive Excel object that aggregates measures across selected dimensions.
- **Plan mode** — The Copilot choice that proposes a structured sequence before workbook changes.
- **Static output** — An inserted table or image that does not automatically update with its source data.
- **Structured reference** — An Excel formula reference that uses table and column names.
- **Tie-out** — A reconciliation showing that two independently derived totals agree.
