# Lab 2 — Apply Reproducible Highlights, Sorts and Filters

**Course:** Microsoft 365 Copilot for Excel  
**Course Code:** C34  
**Version:** v1.0 (29 July 2026)  
**Topic 1:** Getting Started with Copilot in Excel  
**Maps to:** LO2: translate a business question into explicit highlight, sort and filter rules and verify that the resulting view is reversible  
**Duration:** 40 minutes  
**Tools:** Excel · Copilot Edit or Plan · Control sheet · Prompt_Log

---

## Goal

Create a review view for returned and high-discount orders without deleting rows, hiding the denominator or changing the protected source.

## What You Will Do

You will copy the source into a working sheet, state deterministic review rules and ask Copilot to apply highlighting, sorting and filtering one operation at a time. You will record total and visible row counts, clear all filters and confirm that the source and working tables still contain the same orders.

## What You Will Build

An Orders_Working sheet with tblOrdersWorking, reversible highlighting, an explicit multi-level sort, a returned-order filter and Prompt_Log evidence for every applied change

## Prerequisites

- Completed Lab 1 workbook with Raw_Orders, tblOrdersRaw, Control and Prompt_Log.
- The source row count and Order_ID count both equal 36.
- Keep Raw_Orders unchanged; all direct changes in this lab go to Orders_Working.

> **Data note.** Use only the supplied synthetic HarbourLight data or information you are authorised to process. Do not paste credentials, confidential business material or sensitive personal data into Copilot.

## Steps

### 1. Right-click Raw_Orders, select Move or Copy > Create a copy, place it at the end and rename it Orders_Working. Click inside the copied table and set its Table Name to tblOrdersWorking. Confirm that Raw_Orders still contains tblOrdersRaw and 36 rows.

```text
Required sheet: Orders_Working
Required table: tblOrdersWorking
Protected source: Raw_Orders / tblOrdersRaw
```

### 2. On Control, create a Lab 2 rule block with the exact definitions below. Write the total row count beside it before any filter. Add a Prompt_Log row in Plan mode and ask Copilot to restate the rules as Boolean conditions without acting. Revise the wording until its conditions match exactly.

```text
Highlight rule A: Returned equals Yes
Highlight rule B: Discount_Rate is greater than or equal to 0.15
Sort rule: Units descending, then Order_ID ascending
Filter rule: Returned equals Yes
Preserve rule: do not delete rows or edit cell values
```

### 3. Switch to Edit only after the plan matches. Ask Copilot to highlight Returned=Yes rows with a pale red fill and Discount_Rate>=0.15 cells with a pale amber fill in tblOrdersWorking. Ask it to describe the ranges or rules it changed. Review every changed sheet, range and object; confirm only tblOrdersWorking formatting changed and use Undo if the scope differs. Inspect at least one matching and one non-matching row. On Control, enter =COUNTIF(tblOrdersWorking[Discount_Rate],">=0.15") and confirm 11. Record the accepted or rejected change scope, count and evidence in Prompt_Log.

```text
Apply these visual rules only to tblOrdersWorking:
1. Pale red row highlight when Returned exactly equals Yes.
2. Pale amber cell highlight when Discount_Rate >= 0.15.
Do not change values, order or visibility. After acting, state the exact rules applied.
```

### 4. Ask Copilot to sort tblOrdersWorking by Units descending and Order_ID ascending as the tie-breaker. Review the changed sheets, ranges and objects, use Undo if anything outside tblOrdersWorking changed, then check the first five Order_ID and Units pairs against the manual Data > Sort result. Record whether the tie-break order is deterministic and whether the change scope was accepted.

```text
Sort tblOrdersWorking by Units, Largest to Smallest. For equal Units, sort Order_ID, A to Z. Keep every row and all existing formats. State the first five Order_ID and Units values after sorting.
```

### 5. Ask Copilot to filter Returned to Yes. In Control, record the visible returned-order count and the unchanged total row count. Review the changed sheets, ranges and objects and use Undo if the scope differs. Then select Data > Clear. Confirm that all 36 rows return, the table still has 36 populated IDs and Raw_Orders remains unchanged. Record the accepted or rejected scope and save with no filter active.

```text
Filter tblOrdersWorking so Returned exactly equals Yes. Do not delete non-matching rows. State the visible match count and the total table row count. I will clear the filter after verification.
```

## Test It

The working table must contain 36 rows before and after the filter. The returned-order filter must show the exact count in labs/assets/expected-controls.md; the high-discount rule must match the listed count; and the maximum Units value plus first tie-break order must match the control. After Data > Clear, all 36 orders must be visible. Raw_Orders values and order must remain unchanged.

## Checkpoint and Rejoin Point

Save the workbook with tblOrdersWorking sorted by Units descending and no active filter. Lab 3 adds formula columns to this table. To rejoin, rebuild Orders_Working from Raw_Orders and use the Lab 2 rules in labs/assets/harbourlight-checkpoints.md.

## Troubleshooting

| If this happens | Fix |
|---|---|
| Copilot highlights cells but not the full returned row. | Keep the cell rule if it is clear, or select the table data range and use a conditional-format formula based on the Returned column. Record the final range and rule. |
| The filter count differs from the control. | Inspect the exact Returned values for spaces or case differences before changing anything; the supplied file uses canonical Yes and No values. |
| The sort changes Raw_Orders. | Undo immediately, confirm the active sheet and table name, then repeat only on tblOrdersWorking. |

## Challenge

Add a second reversible filter for Discount_Rate>=0.15 and Returned=No. Record both the visible count and the full denominator, then explain why the combination answers a different question.

## Reflection

Why is an explicit filter denominator important when a screenshot of the filtered view is shared?

---

[← Lab 1](lab-01-prepare-the-workbook-and-create-the-copilot-control-trail.md) · [Lab 3 →](lab-03-generate-and-reconcile-formula-columns.md)
