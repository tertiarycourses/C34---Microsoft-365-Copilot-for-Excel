"""Topic 1 labs for C34: prepare, prompt, transform and calculate."""

DOMAIN1 = [
    dict(
        num=1,
        topic=1,
        title="Prepare the Workbook and Create the Copilot Control Trail",
        duration=45,
        objective=(
            "LO1: confirm the available Copilot experience, preserve the source data, create a named Excel "
            "table and establish prompt and verification controls"
        ),
        goal=(
            "Create a reversible C34 workbook whose source boundary, row grain and baseline controls are explicit "
            "before Copilot makes any change."
        ),
        workflow=[
            "Save the source",
            "Define the grain",
            "Create the table",
            "Record controls",
            "Confirm Copilot",
        ],
        desc=(
            "You will import the synthetic HarbourLight order file, save it as a modern Excel workbook, convert the "
            "source rows into a named table and create Control and Prompt_Log sheets. You will use Copilot in Chat and "
            "Plan only to describe the data and propose a safe sequence. The raw source remains unchanged."
        ),
        build=(
            "work-c34/C34-HarbourLight-Copilot-Analysis.xlsx with Raw_Orders, Control and Prompt_Log sheets, "
            "a tblOrdersRaw table, baseline counts and a recorded Copilot access note"
        ),
        services="Excel for Microsoft 365 or Excel for the web · Copilot · harbourlight-orders-raw.csv",
        prerequisites=[
            "Download the repository and keep labs/assets/harbourlight-orders-raw.csv beside the other C34 assets.",
            "Sign in to an eligible Microsoft 365 account and open Excel or Excel for the web.",
            "Create a work-c34 training folder in OneDrive or SharePoint. Confirm you can save an .xlsx file there, "
            "cloud sync is complete and AutoSave is active. Use only the supplied synthetic data.",
        ],
        steps=[
            (
                "Open labs/assets/harbourlight-orders-raw.csv in Excel. Select File > Save As and save "
                "C34-HarbourLight-Copilot-Analysis.xlsx inside your OneDrive or SharePoint work-c34 folder. "
                "Confirm the title bar shows the cloud location and AutoSave is On, then rename the first sheet "
                "Raw_Orders. Do not correct, sort or delete any source value.",
                "Expected source headers:\n"
                "Order_ID | Order_Date | Region | Channel | Product | Category | Units | Unit_Price | "
                "Unit_Cost | Discount_Rate | Returned | Customer_Note\n"
                "Required file state: .xlsx in OneDrive or SharePoint; cloud sync complete; AutoSave On",
            ),
            (
                "Write the grain statement above the control area in a new sheet named Control: 'One data row "
                "represents one HarbourLight order identified by Order_ID.' On Raw_Orders, click inside the data, "
                "select Home > Format as Table, confirm My table has headers and choose any accessible style. On "
                "Table Design, set Table Name to tblOrdersRaw.",
                "Required table name: tblOrdersRaw\n"
                "Required grain: one row = one order\n"
                "Required key: Order_ID",
            ),
            (
                "On Control, enter the labels below in A4:A9. In B4:B9 enter formulas that read tblOrdersRaw. "
                "Use ROWS for row count, COUNTA for populated Order_ID values, MIN and MAX for the date range, "
                "SUM for Units and SUMPRODUCT for gross sales. Format dates as yyyy-mm-dd and gross sales as S$.",
                "A4 Source row count\n"
                "A5 Populated Order_ID count\n"
                "A6 Earliest order date\n"
                "A7 Latest order date\n"
                "A8 Source units\n"
                "A9 Source gross sales before discount\n\n"
                "Example formulas:\n"
                "=ROWS(tblOrdersRaw[Order_ID])\n"
                "=COUNTA(tblOrdersRaw[Order_ID])\n"
                "=MIN(tblOrdersRaw[Order_Date])\n"
                "=MAX(tblOrdersRaw[Order_Date])\n"
                "=SUM(tblOrdersRaw[Units])\n"
                "=SUMPRODUCT(tblOrdersRaw[Units],tblOrdersRaw[Unit_Price])",
            ),
            (
                "Create a sheet named Prompt_Log. Copy the header row from "
                "labs/assets/prompt-and-verification-log-template.csv into A1:J1, format it as a table named "
                "tblPromptLog and add the first record. State the Copilot entry point you can see and whether "
                "Edit, Plan and Chat choices are available. If a label differs, record the label exactly.",
                "Lab,Timestamp,Mode,Goal,Data_Boundary,Prompt,Proposed_Logic,Workbook_Change,Verification,Decision\n"
                "1,<TODAY>,Chat,Describe source structure,tblOrdersRaw,<PASTE PROMPT>,<COPILOT RESPONSE>,"
                "No change,<CHECKS>,Keep or revise",
            ),
            (
                "Open Copilot. In Chat, submit the first prompt below and compare the response with the Control "
                "sheet. Then choose Plan and submit the second prompt. Do not approve workbook edits. Record both "
                "prompts, the proposed logic and your decision in tblPromptLog.",
                "CHAT PROMPT\n"
                "GOAL: Describe the structure and readiness risks in this order data.\n"
                "CONTEXT: HarbourLight Retail operations review; one row should represent one order.\n"
                "DATA: Use only tblOrdersRaw. Name the columns you rely on.\n"
                "CONSTRAINTS: Do not change the workbook. Do not infer missing business facts.\n"
                "OUTPUT: Grain, key, date range, numeric fields, category fields and five checks.\n"
                "REVIEW: Compare row count, Order_ID count, date range, Units and gross sales with Control!B4:B9.\n\n"
                "PLAN PROMPT\n"
                "Propose a reversible sequence to prepare tblOrdersRaw for analysis. Preserve Raw_Orders; "
                "make one bounded change at a time; include verification after every change. Do not act.",
            ),
        ],
        test=(
            "Raw_Orders must contain table tblOrdersRaw with exactly 36 data rows and 36 populated Order_ID values. "
            "Control must show earliest date 2026-01-05, latest date 2026-04-28, 36 rows, 36 populated IDs and the "
            "same Units and gross-sales controls as labs/assets/expected-controls.md. Prompt_Log must contain one "
            "Chat and one Plan record, both with 'No change' in Workbook_Change. Raw_Orders must still match the CSV."
        ),
        checkpoint=(
            "Save and close the workbook. This file is the Lab 1 checkpoint. Lab 2 copies Raw_Orders into a working "
            "sheet. If you need to rejoin, follow the Lab 1 rebuild checklist in labs/assets/harbourlight-checkpoints.md."
        ),
        troubleshooting=[
            (
                "The Copilot button is missing.",
                "Confirm the signed-in account, current Excel build, connected-experience settings and organisation policy. "
                "Also confirm the workbook is .xlsx in OneDrive or SharePoint, cloud sync is complete and AutoSave is On. "
                "Pair with the trainer for prompt comparison while continuing the workbook controls if access remains unavailable.",
            ),
            (
                "Copilot appears before saving but becomes unavailable in the workbook.",
                "Use File > Save As to move the workbook into your OneDrive or SharePoint work-c34 folder, wait for sync, "
                "turn AutoSave On, close and reopen the cloud file, then retry.",
            ),
            (
                "The table includes blank rows or stops before the last order.",
                "Select Table Design > Resize Table and set the range from the 12 headers through the final populated row.",
            ),
            (
                "The date controls show numbers instead of dates.",
                "Keep the formulas and apply the yyyy-mm-dd number format to Control!B6:B7.",
            ),
        ],
        challenge=(
            "Add a duplicate-ID control that returns the row count minus the unique Order_ID count. Explain why a zero "
            "result is necessary but not sufficient to prove the source is ready."
        ),
        reflection="Which baseline control would reveal the most serious accidental change later in the workflow, and why?",
    ),
    dict(
        num=2,
        topic=1,
        title="Apply Reproducible Highlights, Sorts and Filters",
        duration=40,
        objective=(
            "LO2: translate a business question into explicit highlight, sort and filter rules and verify that "
            "the resulting view is reversible"
        ),
        goal=(
            "Create a review view for returned and high-discount orders without deleting rows, hiding the denominator "
            "or changing the protected source."
        ),
        workflow=["Copy the source", "Write the rules", "Apply one change", "Count matches", "Restore the view"],
        desc=(
            "You will copy the source into a working sheet, state deterministic review rules and ask Copilot to apply "
            "highlighting, sorting and filtering one operation at a time. You will record total and visible row counts, "
            "clear all filters and confirm that the source and working tables still contain the same orders."
        ),
        build=(
            "An Orders_Working sheet with tblOrdersWorking, reversible highlighting, an explicit multi-level sort, "
            "a returned-order filter and Prompt_Log evidence for every applied change"
        ),
        services="Excel · Copilot Edit or Plan · Control sheet · Prompt_Log",
        prerequisites=[
            "Completed Lab 1 workbook with Raw_Orders, tblOrdersRaw, Control and Prompt_Log.",
            "The source row count and Order_ID count both equal 36.",
            "Keep Raw_Orders unchanged; all direct changes in this lab go to Orders_Working.",
        ],
        steps=[
            (
                "Right-click Raw_Orders, select Move or Copy > Create a copy, place it at the end and rename it "
                "Orders_Working. Click inside the copied table and set its Table Name to tblOrdersWorking. Confirm "
                "that Raw_Orders still contains tblOrdersRaw and 36 rows.",
                "Required sheet: Orders_Working\n"
                "Required table: tblOrdersWorking\n"
                "Protected source: Raw_Orders / tblOrdersRaw",
            ),
            (
                "On Control, create a Lab 2 rule block with the exact definitions below. Write the total row count "
                "beside it before any filter. Add a Prompt_Log row in Plan mode and ask Copilot to restate the rules "
                "as Boolean conditions without acting. Revise the wording until its conditions match exactly.",
                "Highlight rule A: Returned equals Yes\n"
                "Highlight rule B: Discount_Rate is greater than or equal to 0.15\n"
                "Sort rule: Units descending, then Order_ID ascending\n"
                "Filter rule: Returned equals Yes\n"
                "Preserve rule: do not delete rows or edit cell values",
            ),
            (
                "Switch to Edit only after the plan matches. Ask Copilot to highlight Returned=Yes rows with a pale "
                "red fill and Discount_Rate>=0.15 cells with a pale amber fill in tblOrdersWorking. Ask it to describe "
                "the ranges or rules it changed. Review every changed sheet, range and object; confirm only "
                "tblOrdersWorking formatting changed and use Undo if the scope differs. Inspect at least one matching "
                "and one non-matching row. On Control, enter "
                '=COUNTIF(tblOrdersWorking[Discount_Rate],">=0.15") and confirm 11. Record the accepted or rejected '
                "change scope, count and evidence in Prompt_Log.",
                "Apply these visual rules only to tblOrdersWorking:\n"
                "1. Pale red row highlight when Returned exactly equals Yes.\n"
                "2. Pale amber cell highlight when Discount_Rate >= 0.15.\n"
                "Do not change values, order or visibility. After acting, state the exact rules applied.",
            ),
            (
                "Ask Copilot to sort tblOrdersWorking by Units descending and Order_ID ascending as the tie-breaker. "
                "Review the changed sheets, ranges and objects, use Undo if anything outside tblOrdersWorking changed, "
                "then check the first five Order_ID and Units pairs against the manual Data > Sort result. Record whether "
                "the tie-break order is deterministic and whether the change scope was accepted.",
                "Sort tblOrdersWorking by Units, Largest to Smallest. For equal Units, sort Order_ID, A to Z. "
                "Keep every row and all existing formats. State the first five Order_ID and Units values after sorting.",
            ),
            (
                "Ask Copilot to filter Returned to Yes. In Control, record the visible returned-order count and the "
                "unchanged total row count. Review the changed sheets, ranges and objects and use Undo if the scope "
                "differs. Then select Data > Clear. Confirm that all 36 rows return, the table still has 36 populated "
                "IDs and Raw_Orders remains unchanged. Record the accepted or rejected scope and save with no filter active.",
                "Filter tblOrdersWorking so Returned exactly equals Yes. Do not delete non-matching rows. "
                "State the visible match count and the total table row count. I will clear the filter after verification.",
            ),
        ],
        test=(
            "The working table must contain 36 rows before and after the filter. The returned-order filter must show "
            "the exact count in labs/assets/expected-controls.md; the high-discount rule must match the listed count; "
            "and the maximum Units value plus first tie-break order must match the control. After Data > Clear, all 36 "
            "orders must be visible. Raw_Orders values and order must remain unchanged."
        ),
        checkpoint=(
            "Save the workbook with tblOrdersWorking sorted by Units descending and no active filter. Lab 3 adds formula "
            "columns to this table. To rejoin, rebuild Orders_Working from Raw_Orders and use the Lab 2 rules in "
            "labs/assets/harbourlight-checkpoints.md."
        ),
        troubleshooting=[
            (
                "Copilot highlights cells but not the full returned row.",
                "Keep the cell rule if it is clear, or select the table data range and use a conditional-format formula "
                "based on the Returned column. Record the final range and rule.",
            ),
            (
                "The filter count differs from the control.",
                "Inspect the exact Returned values for spaces or case differences before changing anything; the supplied "
                "file uses canonical Yes and No values.",
            ),
            (
                "The sort changes Raw_Orders.",
                "Undo immediately, confirm the active sheet and table name, then repeat only on tblOrdersWorking.",
            ),
        ],
        challenge=(
            "Add a second reversible filter for Discount_Rate>=0.15 and Returned=No. Record both the visible count and "
            "the full denominator, then explain why the combination answers a different question."
        ),
        reflection="Why is an explicit filter denominator important when a screenshot of the filtered view is shared?",
    ),
    dict(
        num=3,
        topic=1,
        title="Generate and Reconcile Formula Columns",
        duration=45,
        objective=(
            "LO2: generate structured-reference formula columns from plain-language rules, inspect the logic and "
            "reconcile the calculated results to independent controls"
        ),
        goal=(
            "Extend tblOrdersWorking with six auditable calculated columns and prove that representative rows and "
            "headline totals match the supplied business rules."
        ),
        workflow=["Define the rules", "Generate one formula", "Inspect the fill", "Test edge cases", "Reconcile totals"],
        desc=(
            "You will write the calculation rules in words, ask Copilot for one structured-reference formula at a time "
            "and inspect every formula before filling it through the table. You will verify a no-discount row, a discounted "
            "row, a returned order, the zero-error path and independent totals on the Control sheet."
        ),
        build=(
            "Six calculated columns in tblOrdersWorking - Gross_Sales, Discount_Amount, Net_Sales, Cost_Amount, "
            "Gross_Profit and Margin_Rate - plus formula checks and reconciled totals on Control"
        ),
        services="Excel formulas · Copilot · structured references · expected-controls.md",
        prerequisites=[
            "Completed Lab 2 workbook with tblOrdersWorking and no active filter.",
            "Control shows 36 total rows and the source gross-sales value from Lab 1.",
            "Open labs/assets/formula-and-verification-rules.md before writing a formula.",
        ],
        steps=[
            (
                "On Control, copy the six business rules from labs/assets/formula-and-verification-rules.md into a "
                "Lab 3 block. Include currency units, blank handling and the Margin_Rate denominator. Add a Prompt_Log "
                "row in Chat and ask Copilot to return only the proposed structured-reference formulas and explanations; "
                "do not apply them yet.",
                "Required output columns:\n"
                "Gross_Sales | Discount_Amount | Net_Sales | Cost_Amount | Gross_Profit | Margin_Rate\n\n"
                "Use native Excel formulas. Do not use the COPILOT function for numeric calculations.",
            ),
            (
                "Review the proposed Gross_Sales and Discount_Amount formulas. In tblOrdersWorking add the two headers "
                "and enter the approved formulas in the first data row so Excel fills each calculated column. Select "
                "three rows and confirm that the formula uses current-row structured references.",
                "Gross_Sales: =[@Units]*[@Unit_Price]\n"
                "Discount_Amount: =[@Gross_Sales]*[@Discount_Rate]",
            ),
            (
                "Add Net_Sales, Cost_Amount and Gross_Profit one column at a time. After every column, ask Copilot to "
                "explain the sign and inputs, then compare one row with a calculator or hand-worked result. Record the "
                "selected Order_ID, inputs, expected value and observed value in Prompt_Log.",
                "Net_Sales: =[@Gross_Sales]-[@Discount_Amount]\n"
                "Cost_Amount: =[@Units]*[@Unit_Cost]\n"
                "Gross_Profit: =[@Net_Sales]-[@Cost_Amount]",
            ),
            (
                "Add Margin_Rate and format the entire column as 0.0%. The approved denominator is Net_Sales. Use "
                "IFERROR to return zero if Net_Sales is zero. Check that the formula is filled in all 36 data rows and "
                "that no formula-error values appear. On Control, create two scratch cells containing Gross_Profit=0 "
                "and Net_Sales=0, apply =IFERROR(<GROSS_PROFIT_CELL>/<NET_SALES_CELL>,0) and confirm the result is 0. "
                "Delete the scratch inputs after recording the check; do not add a synthetic order to the table.",
                "Margin_Rate: =IFERROR([@Gross_Profit]/[@Net_Sales],0)\n"
                "Required format: 0.0%",
            ),
            (
                "On Control, calculate SUM for Gross_Sales, Discount_Amount, Net_Sales, Cost_Amount and Gross_Profit. "
                "Add a weighted overall margin formula: total Gross_Profit divided by total Net_Sales. Compare the six "
                "results with labs/assets/expected-controls.md. Explicitly test HL-1001, HL-1003, HL-1007, HL-1018 "
                "and HL-1032 against the named row controls. Review every changed sheet, range and object; confirm only "
                "the six approved calculated columns and Control checks changed, use Undo for scope creep and record "
                "the accepted or rejected scope. If a value differs, inspect formulas and inputs rather than overwriting it.",
                "Overall Margin_Rate control:\n"
                "=SUM(tblOrdersWorking[Gross_Profit])/SUM(tblOrdersWorking[Net_Sales])\n\n"
                "Do not use AVERAGE(tblOrdersWorking[Margin_Rate]) for the overall margin.",
            ),
        ],
        test=(
            "All six calculated columns must contain formulas for all 36 rows with no formula-error values. The formula "
            "text must use structured references and the overall margin must use total Gross_Profit divided by total "
            "Net_Sales. The six totals and the named representative Order_ID checks must exactly match "
            "labs/assets/expected-controls.md. Copilot's explanation alone does not satisfy the check."
        ),
        checkpoint=(
            "Save the workbook with all formulas present and no active filter. Lab 4 copies tblOrdersWorking to a clean "
            "analysis sheet. To rejoin, use the formula block and control totals in "
            "labs/assets/harbourlight-checkpoints.md."
        ),
        troubleshooting=[
            (
                "Excel creates A1 references instead of structured references.",
                "Confirm the range is an Excel table, select the first data cell under the new header and build the formula "
                "by clicking the current-row cells; Excel should insert named column references.",
            ),
            (
                "The overall margin differs from the control while row formulas look correct.",
                "Confirm you divided total Gross_Profit by total Net_Sales and did not average row percentages.",
            ),
            (
                "Only the first row contains the formula.",
                "Double-click the fill handle or re-enter the formula in the table column and confirm calculated-column fill "
                "is enabled. Do not paste hardcoded values down the column.",
            ),
        ],
        challenge=(
            "Add a Recalculation_Check column that compares Net_Sales with Gross_Sales minus Discount_Amount and returns "
            "OK only when the absolute difference is below 0.005. Explain the tolerance."
        ),
        reflection="Which formula check is independent enough to catch a fluent but logically wrong Copilot suggestion?",
    ),
]
