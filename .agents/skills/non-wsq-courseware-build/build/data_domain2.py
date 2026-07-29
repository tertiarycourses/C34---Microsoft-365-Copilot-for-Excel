"""Topic 2 labs for C34: clean, visualise, analyse and verify."""

DOMAIN2 = [
    dict(
        num=4,
        topic=2,
        title="Clean and Enrich the Analysis Table",
        duration=60,
        objective=(
            "LO3: apply documented cleaning rules to a copy of the working table, add deterministic analysis fields "
            "and verify categories, row counts and formula totals"
        ),
        goal=(
            "Create a clean analysis table with canonical Region and Channel values, a Month field, a numeric return "
            "flag and a reviewed note-theme classification while preserving the raw source."
        ),
        workflow=["Copy the working table", "Profile categories", "Clean one rule", "Add analysis fields", "Tie out"],
        desc=(
            "You will copy the formula-complete working table to Orders_Clean, profile observed category values and apply "
            "the supplied canonical rules one issue at a time. You will add Month, Return_Flag and Note_Theme fields, "
            "retain Unknown when a note is ambiguous and prove that cleaning did not change row-level monetary results."
        ),
        build=(
            "An Orders_Clean sheet with tblOrdersClean, canonical categories, Month, Return_Flag and Note_Theme fields, "
            "plus a cleaning log and before/after control checks"
        ),
        services="Excel · Copilot · Clean Data when available · harbourlight-data-dictionary.md",
        prerequisites=[
            "Completed Lab 3 workbook with tblOrdersWorking and reconciled formula totals.",
            "Open labs/assets/harbourlight-data-dictionary.md and use only its canonical values and note taxonomy.",
            "Raw_Orders remains unchanged and is the comparison source.",
        ],
        steps=[
            (
                "Copy Orders_Working to the end, rename it Orders_Clean and set the copied table name to "
                "tblOrdersClean. On Control, create a Cleaning_Log table with Issue, Rule, Before_Count, After_Count, "
                "Affected_Rows, Verification and Decision. Record the 36-row baseline and the five Lab 3 monetary totals.",
                "Required working sheet: Orders_Clean\n"
                "Required table: tblOrdersClean\n"
                "Required log columns: Issue | Rule | Before_Count | After_Count | Affected_Rows | Verification | Decision",
            ),
            (
                "Ask Copilot in Chat to list distinct Region, Channel, Product and Category values with counts from "
                "tblOrdersClean. Compare the response with Data > Filter for each column. Record every value that differs "
                "from the canonical dictionary by case or surrounding spaces. Do not clean yet.",
                "List the distinct values and counts in Region, Channel, Product and Category from tblOrdersClean. "
                "Do not change the workbook. Preserve exact spaces and case in the displayed values. Flag only values "
                "that do not match the supplied canonical dictionary.",
            ),
            (
                "Clean Region and Channel one field at a time using the dictionary. If Clean Data is available, review "
                "each suggestion before applying it; otherwise ask Copilot to propose exact replacements and apply only "
                "the approved mapping. After each action, review every changed sheet, range and object; confirm only the "
                "named text cells in tblOrdersClean changed and use Undo if the scope differs. Confirm that Region contains "
                "North, South and Central only, while Channel contains Store, Online and Partner only. Record affected "
                "counts and the accepted or rejected scope.",
                "Canonical Region values: North | South | Central\n"
                "Canonical Channel values: Store | Online | Partner\n"
                "Allowed operations: trim surrounding spaces and standardise case\n"
                "Do not infer or replace a value outside the mapping.",
            ),
            (
                "Add Month and Return_Flag calculated columns. Month must be yyyy-mm text derived from Order_Date. "
                "Return_Flag must equal 1 only when Returned exactly equals Yes and 0 otherwise. Fill all rows, record "
                "the sum of Return_Flag and compare it with the returned-order count from Lab 2.",
                "Month: =TEXT([@Order_Date],\"yyyy-mm\")\n"
                "Return_Flag: =--([@Returned]=\"Yes\")",
            ),
            (
                "Add Note_Theme using only Delivery, Product, Return, No note and Unknown. Ask Copilot to propose a "
                "classification with a short reason, but review every row against the dictionary. Blank or whitespace-only "
                "notes become No note. A note that does not match one defined cue remains Unknown. Review all changed sheets, "
                "ranges and objects, use Undo if anything outside Note_Theme changed and record the accepted or rejected "
                "scope. Finish by reconciling row count, populated IDs and all five monetary totals to Lab 3.",
                "Classify Customer_Note using only the supplied taxonomy. Return Order_ID | Note_Theme | cue used. "
                "Do not invent a reason. Blank text becomes No note; ambiguous text becomes Unknown. "
                "I will review every proposed label before applying it.",
            ),
        ],
        test=(
            "tblOrdersClean must contain 36 rows and 36 populated Order_ID values. Region must have exactly three canonical "
            "values and Channel exactly three. Month must contain only 2026-01 through 2026-04. Sum of Return_Flag, the "
            "five monetary totals and all Note_Theme counts must match labs/assets/expected-controls.md. Raw_Orders and "
            "Orders_Working must remain unchanged."
        ),
        checkpoint=(
            "Save the workbook with tblOrdersClean fully reconciled. Labs 5 and 6 use only this clean table for summaries. "
            "To rejoin, follow the Lab 4 mapping and field checklist in labs/assets/harbourlight-checkpoints.md."
        ),
        troubleshooting=[
            (
                "Clean Data shows no suggestions.",
                "Use the exact distinct-value list and the supplied canonical mapping. Feature availability varies, and the "
                "verification controls are the same for a reviewed manual or Copilot-assisted correction.",
            ),
            (
                "A note receives a category outside the taxonomy.",
                "Reject the output, restate the five allowed values and require Unknown for all unmatched cues.",
            ),
            (
                "Monetary totals change after cleaning text fields.",
                "Undo the last action and inspect whether a formula or numeric field was included in the changed range.",
            ),
        ],
        challenge=(
            "Create a data-validation list for Region and Channel using the canonical values, then explain how validation "
            "prevents new defects without proving that existing records are correct."
        ),
        reflection="Which cleaning decision required human judgment rather than a mechanical text correction?",
    ),
    dict(
        num=5,
        topic=2,
        title="Build Reconciled PivotTables and Charts",
        duration=55,
        objective=(
            "LO3: translate business questions into PivotTable grain, dimensions, measures and charts, then reconcile "
            "every grand total and denominator to the clean table"
        ),
        goal=(
            "Create an editable operations summary that shows monthly net sales by region and return rate by channel "
            "without hiding the underlying counts or overstating visual differences."
        ),
        workflow=["State the questions", "Build the Pivot", "Tie the total", "Create the chart", "Inspect the visual"],
        desc=(
            "You will define two decision questions before asking Copilot to build anything. The first PivotTable and line "
            "chart show monthly net sales by canonical region. The second summary shows returned orders, order count and "
            "return rate by channel. You will verify grand totals, denominators, titles, units and source linkage."
        ),
        build=(
            "A Pivot_Analysis sheet with two PivotTables, a monthly regional net-sales line chart, a channel return-rate "
            "chart, tie-out cells and a Prompt_Log record for each object"
        ),
        services="Excel PivotTables · Excel charts · Copilot · tblOrdersClean · expected-controls.md",
        prerequisites=[
            "Completed Lab 4 workbook with tblOrdersClean and reconciled clean-table controls.",
            "Month contains 2026-01 through 2026-04 and Return_Flag contains only 0 and 1.",
            "No active filter is applied to tblOrdersClean.",
        ],
        steps=[
            (
                "Create a sheet named Pivot_Analysis. At the top, write two questions and their intended grain. "
                "Question A: 'How did monthly net sales change by region?' Grain: one Pivot cell equals the sum of "
                "Net_Sales for one Month-Region combination. Question B: 'Which channel has the highest returned-order "
                "rate?' Grain: one row equals one canonical Channel.",
                "Question A fields:\n"
                "Rows = Month | Columns = Region | Values = Sum of Net_Sales\n\n"
                "Question B fields:\n"
                "Rows = Channel | Values = Sum of Return_Flag and Count of Order_ID\n"
                "Return rate = returned orders / order count",
            ),
            (
                "Ask Copilot to create PivotTable A from tblOrdersClean on Pivot_Analysis. If direct creation is "
                "unavailable, select Insert > PivotTable, choose tblOrdersClean and use the exact field layout. Format "
                "Net_Sales as S$ with two decimals, show grand totals and sort Month ascending. Review every changed sheet, "
                "range and object; confirm only the requested PivotTable was added and use Undo if the scope differs. "
                "Record the accepted or rejected scope in Prompt_Log.",
                "Create an editable PivotTable from tblOrdersClean on Pivot_Analysis. Put Month in Rows, Region in "
                "Columns and Sum of Net_Sales in Values. Show grand totals, sort Month ascending and format values as "
                "S$ with two decimals. Do not create a static pasted table.",
            ),
            (
                "Below Pivot A, add a tie-out cell that subtracts the Pivot grand total from "
                "SUM(tblOrdersClean[Net_Sales]). It must equal 0.00. Create a line chart from Pivot A with title "
                "'Monthly Net Sales by Region', Month on the x-axis, S$ Net Sales on the y-axis and a visible legend "
                "for North, South and Central. Review the changed sheets, ranges and objects; confirm the chart is linked "
                "only to Pivot A and use Undo for any unrelated change.",
                "Required tie-out:\n"
                "=SUM(tblOrdersClean[Net_Sales])-<PIVOT_A_GRAND_TOTAL_CELL>\n"
                "Expected result: 0.00",
            ),
            (
                "Create PivotTable B using Channel as rows, Sum of Return_Flag and Count of Order_ID as values. "
                "Beside the Pivot, calculate Return_Rate for each channel as returned orders divided by order count, "
                "format as 0.0% and add a total row that uses the grand totals rather than averaging channel percentages. "
                "Review every changed sheet, range and object; confirm only Pivot B and its adjacent formulas changed and "
                "use Undo if the scope differs.",
                "Return_Rate formula: =<RETURNED_ORDERS_CELL>/<ORDER_COUNT_CELL>\n"
                "Overall return rate: =<SUM_RETURN_FLAG_GRAND_TOTAL>/<COUNT_ORDER_ID_GRAND_TOTAL>",
            ),
            (
                "Create a clustered column chart using Channel and Return_Rate with title 'Returned-Order Rate by "
                "Channel'. Set the y-axis to percentage, start at zero and show data labels. Compare both PivotTables "
                "with labs/assets/expected-controls.md. Review all changed sheets, ranges and objects and record the accepted "
                "or rejected scope, exact totals, visual checks and any manual steps in Prompt_Log.",
                "Visual checks:\n"
                "[ ] chart title names the metric and dimension\n"
                "[ ] axis units match S$ or percentage\n"
                "[ ] every canonical category is visible\n"
                "[ ] line chart months are chronological\n"
                "[ ] return-rate axis starts at zero\n"
                "[ ] both source ranges remain linked and editable",
            ),
        ],
        test=(
            "Pivot A must contain four months, three regions and a grand total equal to tblOrdersClean Net_Sales with a "
            "0.00 tie-out. Pivot B must show three channels, returned-order count, order count and rates that match "
            "labs/assets/expected-controls.md; the overall rate must use grand-total numerator and denominator. Both "
            "charts must be editable, linked, fully titled and use the correct units."
        ),
        checkpoint=(
            "Save the workbook with Pivot_Analysis visible and both tie-outs complete. Lab 6 references these values as "
            "independent checks. To rejoin, use the Pivot field layouts in labs/assets/harbourlight-checkpoints.md."
        ),
        troubleshooting=[
            (
                "Net_Sales is counted instead of summed.",
                "Open Value Field Settings, choose Sum and verify that Net_Sales contains numeric values in all rows.",
            ),
            (
                "Months sort alphabetically in the wrong order.",
                "Confirm Month uses yyyy-mm text or place the real Order_Date in rows and group it by Months and Years.",
            ),
            (
                "The chart omits a region or channel.",
                "Inspect the Pivot filters and source categories, clear filters and refresh the PivotTable.",
            ),
        ],
        challenge=(
            "Add a Product gross-profit PivotTable and choose a chart. State why Sum of Gross_Profit is meaningful while "
            "a simple average of row Margin_Rate may not be the right product-level margin."
        ),
        reflection="Which tie-out proves the Pivot aggregation is complete, and what analytical error can it still miss?",
    ),
    dict(
        num=6,
        topic=2,
        title="Run Advanced Analysis and Write the Verified Decision Summary",
        duration=75,
        objective=(
            "LO4: use Python-assisted Copilot for a bounded analytical question, inspect the generated method, "
            "reconcile headline values and produce a traceable decision summary"
        ),
        goal=(
            "Complete the HarbourLight workflow with a reviewed analysis of monthly trends, channel return rates and "
            "high-value-order outliers, followed by a Share, Revise or Hold decision."
        ),
        workflow=["Write the brief", "Run advanced analysis", "Inspect the logic", "Reconcile headlines", "Decide"],
        desc=(
            "You will ask Copilot for direct answers and advanced analysis using only tblOrdersClean. You will review the "
            "referenced fields, filters, groupings, IQR logic and generated code or explanation. You will reconcile the "
            "headline values to the Control and Pivot_Analysis sheets, then create a concise executive summary that keeps "
            "observations, hypotheses and limitations separate."
        ),
        build=(
            "An Advanced_Analysis sheet with prompt, method, generated output and reconciliation; plus an "
            "Executive_Summary sheet with three verified findings, limitations, actions and a final decision"
        ),
        services=(
            "Copilot direct answers · advanced analysis with Python in Excel · Excel controls · Pivot_Analysis · "
            "advanced-analysis-fallback.md"
        ),
        prerequisites=[
            "Completed Lab 5 workbook with reconciled Pivot A and Pivot B.",
            "Open labs/assets/advanced-analysis-brief-template.md and labs/assets/expected-controls.md.",
            "Before class, confirm the account shows the deeper or advanced analysis entry point. If it does not, open "
            "labs/assets/advanced-analysis-fallback.md so you can inspect saved Python logic and output hands-on.",
            "Use only tblOrdersClean; do not connect to external data or use real organisational information.",
        ],
        steps=[
            (
                "Create Advanced_Analysis and Executive_Summary sheets. Copy the analysis brief template to "
                "Advanced_Analysis and complete its Question, Data, Filters, Metrics, Method, Output and Review fields. "
                "Require monthly net sales by region, returned-order rate by channel and an IQR review of order Net_Sales. "
                "State that outliers are candidates for review, not errors or causes.",
                "Question: What changed across months and regions, which channel has the highest returned-order rate, "
                "and which order Net_Sales values are high under the 1.5 x IQR rule?\n"
                "Data: tblOrdersClean only\n"
                "Filters: none; report missing or excluded rows\n"
                "Review: reconcile with Control and Pivot_Analysis",
            ),
            (
                "Ask Copilot the direct-answer prompt below. Save the response, cited source fields and any inserted "
                "static table or image on Advanced_Analysis. If an inserted output will not refresh, place a visible "
                "'STATIC - rerun after source change' label above it. Review every changed sheet, range and object, use "
                "Undo for unrelated changes and record the accepted or rejected scope.",
                "Using only tblOrdersClean, report:\n"
                "1. Monthly Net_Sales by Region and the grand total.\n"
                "2. Returned-order count, order count and Return_Rate by Channel.\n"
                "3. Q1, Q3, IQR, upper fence and Order_ID values above the upper fence for Net_Sales.\n"
                "Show the fields and filters used. Do not claim causes. Label inserted non-refreshing output as static.",
            ),
            (
                "Choose the follow-up for deeper or advanced analysis, or ask 'Enter advanced analysis mode'. Review "
                "the generated Python code or expanded logic. Confirm it selects tblOrdersClean, groups by canonical "
                "Month/Region or Channel, computes rate as sum(Return_Flag)/count(Order_ID), uses the 1.5 x IQR upper "
                "fence and does not silently drop rows. If the feature is unavailable, inspect the saved code and output "
                "in labs/assets/advanced-analysis-fallback.md line by line and paste the reviewed method plus your notes "
                "into Advanced_Analysis. In either route, record the inspected code lines or logic in Prompt_Log.",
                "Review checklist:\n"
                "[ ] source is tblOrdersClean\n"
                "[ ] no hidden filter\n"
                "[ ] monthly grouping uses Month and Region\n"
                "[ ] rate denominator is Order_ID count\n"
                "[ ] Q1/Q3/IQR and upper fence are reported\n"
                "[ ] excluded or missing rows are counted\n"
                "[ ] output type is labelled static or refreshable",
            ),
            (
                "On Advanced_Analysis, create a reconciliation table with Metric, Advanced_Result, Independent_Result, "
                "Difference, Source and Status. Reconcile total Net_Sales, each channel order count and return count, "
                "the overall return rate, the highest monthly-region value and the listed high outlier Order_ID values. "
                "Every numeric difference must be zero within S$0.01 or 0.01 percentage points.",
                "Reconciliation columns:\n"
                "Metric | Advanced_Result | Independent_Result | Difference | Source | Status\n"
                "Status rule: OK only when the difference is within the stated tolerance.",
            ),
            (
                "On Executive_Summary, write exactly three findings using the template below. Each finding must cite "
                "workbook evidence, distinguish OBSERVED from HYPOTHESIS and name a practical owner or next check. Add "
                "limitations and choose SHARE only if every required reconciliation is OK; otherwise choose REVISE or HOLD. "
                "Record the reason and owner.",
                "Finding | Evidence | Type | Why it matters | Next check | Owner\n"
                "Types: OBSERVED or HYPOTHESIS\n"
                "Final decision: SHARE | REVISE | HOLD\n"
                "Required limitations: synthetic data; four-month window; returned status only; no causal evidence",
            ),
        ],
        test=(
            "Advanced_Analysis must contain the completed brief, direct answer, reviewed code or method, output-type label "
            "and reconciliation table. Every required metric and outlier must match labs/assets/expected-controls.md "
            "within the stated tolerance. Executive_Summary must contain exactly three findings, evidence references, "
            "types, next checks, owners, four required limitations and a final SHARE, REVISE or HOLD decision. SHARE is "
            "allowed only when every reconciliation status is OK."
        ),
        checkpoint=(
            "This is the final course checkpoint. Keep the workbook with Raw_Orders, Control, Prompt_Log, Orders_Working, "
            "Orders_Clean, Pivot_Analysis, Advanced_Analysis and Executive_Summary. Use it as a practice model, not as "
            "evidence about a real organisation."
        ),
        troubleshooting=[
            (
                "Advanced analysis is not available in the current account.",
                "Open labs/assets/advanced-analysis-fallback.md, inspect the saved Python logic and output, identify the "
                "source fields, groupings, rate denominator and IQR rule, then complete the same reconciliations in your "
                "own workbook. Pair with the trainer only for the interface demonstration.",
            ),
            (
                "The analysis reports a different return rate.",
                "Check that the numerator is Sum of Return_Flag and the denominator is Count of Order_ID at the same channel grain.",
            ),
            (
                "The generated narrative claims a cause.",
                "Relabel the statement HYPOTHESIS, remove causal language and name the additional operational evidence needed.",
            ),
        ],
        challenge=(
            "Ask for a sensitivity check using a 3 x IQR upper fence. Compare the flagged orders with the 1.5 x IQR result "
            "and explain how the threshold changes the review workload without proving which orders are wrong."
        ),
        reflection="What evidence would make the final summary trustworthy to a reviewer who never saw the Copilot chat?",
    ),
]
