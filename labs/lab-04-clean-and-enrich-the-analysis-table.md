# Lab 4 — Clean and Enrich the Analysis Table

**Course:** Microsoft 365 Copilot for Excel  
**Course Code:** C34  
**Version:** v1.0 (29 July 2026)  
**Topic 2:** AI-Powered Data Analysis and Insights  
**Maps to:** LO3: apply documented cleaning rules to a copy of the working table, add deterministic analysis fields and verify categories, row counts and formula totals  
**Duration:** 60 minutes  
**Tools:** Excel · Copilot · Clean Data when available · harbourlight-data-dictionary.md

---

## Goal

Create a clean analysis table with canonical Region and Channel values, a Month field, a numeric return flag and a reviewed note-theme classification while preserving the raw source.

## What You Will Do

You will copy the formula-complete working table to Orders_Clean, profile observed category values and apply the supplied canonical rules one issue at a time. You will add Month, Return_Flag and Note_Theme fields, retain Unknown when a note is ambiguous and prove that cleaning did not change row-level monetary results.

## What You Will Build

An Orders_Clean sheet with tblOrdersClean, canonical categories, Month, Return_Flag and Note_Theme fields, plus a cleaning log and before/after control checks

## Prerequisites

- Completed Lab 3 workbook with tblOrdersWorking and reconciled formula totals.
- Open labs/assets/harbourlight-data-dictionary.md and use only its canonical values and note taxonomy.
- Raw_Orders remains unchanged and is the comparison source.

> **Data note.** Use only the supplied synthetic HarbourLight data or information you are authorised to process. Do not paste credentials, confidential business material or sensitive personal data into Copilot.

## Steps

### 1. Copy Orders_Working to the end, rename it Orders_Clean and set the copied table name to tblOrdersClean. On Control, create a Cleaning_Log table with Issue, Rule, Before_Count, After_Count, Affected_Rows, Verification and Decision. Record the 36-row baseline and the five Lab 3 monetary totals.

```text
Required working sheet: Orders_Clean
Required table: tblOrdersClean
Required log columns: Issue | Rule | Before_Count | After_Count | Affected_Rows | Verification | Decision
```

### 2. Ask Copilot in Chat to list distinct Region, Channel, Product and Category values with counts from tblOrdersClean. Compare the response with Data > Filter for each column. Record every value that differs from the canonical dictionary by case or surrounding spaces. Do not clean yet.

```text
List the distinct values and counts in Region, Channel, Product and Category from tblOrdersClean. Do not change the workbook. Preserve exact spaces and case in the displayed values. Flag only values that do not match the supplied canonical dictionary.
```

### 3. Clean Region and Channel one field at a time using the dictionary. If Clean Data is available, review each suggestion before applying it; otherwise ask Copilot to propose exact replacements and apply only the approved mapping. After each action, review every changed sheet, range and object; confirm only the named text cells in tblOrdersClean changed and use Undo if the scope differs. Confirm that Region contains North, South and Central only, while Channel contains Store, Online and Partner only. Record affected counts and the accepted or rejected scope.

```text
Canonical Region values: North | South | Central
Canonical Channel values: Store | Online | Partner
Allowed operations: trim surrounding spaces and standardise case
Do not infer or replace a value outside the mapping.
```

### 4. Add Month and Return_Flag calculated columns. Month must be yyyy-mm text derived from Order_Date. Return_Flag must equal 1 only when Returned exactly equals Yes and 0 otherwise. Fill all rows, record the sum of Return_Flag and compare it with the returned-order count from Lab 2.

```text
Month: =TEXT([@Order_Date],"yyyy-mm")
Return_Flag: =--([@Returned]="Yes")
```

### 5. Add Note_Theme using only Delivery, Product, Return, No note and Unknown. Ask Copilot to propose a classification with a short reason, but review every row against the dictionary. Blank or whitespace-only notes become No note. A note that does not match one defined cue remains Unknown. Review all changed sheets, ranges and objects, use Undo if anything outside Note_Theme changed and record the accepted or rejected scope. Finish by reconciling row count, populated IDs and all five monetary totals to Lab 3.

```text
Classify Customer_Note using only the supplied taxonomy. Return Order_ID | Note_Theme | cue used. Do not invent a reason. Blank text becomes No note; ambiguous text becomes Unknown. I will review every proposed label before applying it.
```

## Test It

tblOrdersClean must contain 36 rows and 36 populated Order_ID values. Region must have exactly three canonical values and Channel exactly three. Month must contain only 2026-01 through 2026-04. Sum of Return_Flag, the five monetary totals and all Note_Theme counts must match labs/assets/expected-controls.md. Raw_Orders and Orders_Working must remain unchanged.

## Checkpoint and Rejoin Point

Save the workbook with tblOrdersClean fully reconciled. Labs 5 and 6 use only this clean table for summaries. To rejoin, follow the Lab 4 mapping and field checklist in labs/assets/harbourlight-checkpoints.md.

## Troubleshooting

| If this happens | Fix |
|---|---|
| Clean Data shows no suggestions. | Use the exact distinct-value list and the supplied canonical mapping. Feature availability varies, and the verification controls are the same for a reviewed manual or Copilot-assisted correction. |
| A note receives a category outside the taxonomy. | Reject the output, restate the five allowed values and require Unknown for all unmatched cues. |
| Monetary totals change after cleaning text fields. | Undo the last action and inspect whether a formula or numeric field was included in the changed range. |

## Challenge

Create a data-validation list for Region and Channel using the canonical values, then explain how validation prevents new defects without proving that existing records are correct.

## Reflection

Which cleaning decision required human judgment rather than a mechanical text correction?

---

[← Lab 3](lab-03-generate-and-reconcile-formula-columns.md) · [Lab 5 →](lab-05-build-reconciled-pivottables-and-charts.md)
