"""Single source of truth for the C34 non-WSQ courseware package."""

TITLE = "Microsoft 365 Copilot for Excel"
SHORT_TITLE = "Microsoft 365 Copilot for Excel"
COURSE_CODE = "C34"
COURSE_PAGE = "tertiarycourses.com.sg/microsoft-365-copilot-for-excel.html"
VERSION = "v1.0"
VERSION_DATE = "29 July 2026"
ORG = "Tertiary Infotech Academy Pte Ltd"
UEN = "UEN: 201200696W"
TRAINER = "Assigned Tertiary Infotech Academy Trainer"
DAYS = 1
DAY_MINUTES = 480
INSTRUCTIONAL_MINUTES = 450
MODE = "Instructor-led, hands-on practical labs"
DAILY_TIMING = (
    "9:30 am - 6:30 pm (1-hour lunch; two 15-minute tea breaks; "
    "7.5 instructional hours)"
)
DARK_THEME = False

TRAINER_TEAM = [
    (
        "Ken Hiong",
        "Excel practitioner and adult educator with experience in business analysis, planning and reporting.",
    ),
    (
        "Jim Gan Chiu Liang",
        "Data automation specialist with extensive experience building practical Excel workflows.",
    ),
    (
        "Liew Sing Loon",
        "Technology and management educator with applied quantitative-analysis experience.",
    ),
    (
        "Dwight Nuwan Fonseka",
        "Data science leader and adult educator specialising in analytics, machine learning and responsible AI.",
    ),
]

ICE_BREAKER = [
    "Your name, organisation and role.",
    "One recurring spreadsheet task that takes too long today.",
    "One decision your spreadsheet should help someone make.",
    "Whether you can see Copilot in Excel and which app or web version you are using.",
]

LEARNING_OUTCOMES = [
    (
        "LO1: Explain how Copilot works in Excel, prepare an analysis-ready Excel table and "
        "write bounded prompts for workbook tasks."
    ),
    (
        "LO2: Use Copilot to highlight, sort and filter table data, then generate and verify "
        "auditable formula columns."
    ),
    (
        "LO3: Clean and enrich a business dataset, create PivotTables and charts, and interpret "
        "patterns without overstating the evidence."
    ),
    (
        "LO4: Run advanced analysis with Python-assisted Copilot, reconcile the results and "
        "produce a traceable decision summary."
    ),
]

LO_TITLES = [
    "Prepare & Prompt",
    "Transform & Calculate",
    "Summarise & Visualise",
    "Analyse & Verify",
]

TOPIC_RECAPS = {
    1: [
        (
            "LO1 - Prepare and Prompt",
            "Confirm the available Copilot experience, keep a protected source sheet, convert one-row-per-order "
            "data into a named Excel table and use Goal-Context-Data-Constraints-Output-Review prompts.",
        ),
        (
            "LO2 - Transform and Calculate",
            "Apply explicit highlight, sort and filter rules; generate structured-reference formulas; and reconcile "
            "row-level calculations to independent control totals before relying on them.",
        ),
    ],
    2: [
        (
            "LO3 - Summarise and Visualise",
            "Correct defined quality issues, build PivotTables at the intended grain, choose charts that match the "
            "question and separate observed patterns from possible explanations.",
        ),
        (
            "LO4 - Analyse and Verify",
            "State the analytical question, review Python-based logic and outputs, cross-check headline values, record "
            "limitations and communicate only decision-relevant, evidence-backed findings.",
        ),
    ],
}

TOPICS = [
    dict(
        num=1,
        code="01",
        title="Getting Started with Copilot in Excel",
        subtitle=(
            "Introduction to Microsoft 365 Copilot in Excel · preparing data as Excel tables · "
            "effective prompts · highlighting, sorting and filtering · formula columns"
        ),
        weighting="First half · 3 labs",
        concepts=[
            (
                "Copilot work modes",
                "Choose Edit for workbook changes, Plan for a proposed sequence and Chat for analysis that stays in the pane.",
            ),
            (
                "Analysis-ready tables",
                "Use one header row, one record per row, one meaning per column and consistent data types.",
            ),
            (
                "G-C-D-C-O-R prompts",
                "State Goal, Context, Data, Constraints, Output and Review criteria before Copilot acts.",
            ),
            (
                "Reversible operations",
                "Preview, apply, inspect and undo one bounded change rather than combining many opaque edits.",
            ),
            (
                "Structured-reference formulas",
                "Prefer formulas that name table columns and update as the table grows.",
            ),
            (
                "Control totals",
                "Reconcile counts, sums and edge cases independently before using a result in a decision.",
            ),
        ],
        sections=[
            dict(
                title="Introduction to Microsoft 365 Copilot in Excel",
                definition=(
                    "Copilot in Excel is a natural-language interface that can build, edit and analyse workbooks using "
                    "Excel features such as tables, formulas, PivotTables, charts, formatting and worksheet operations. "
                    "The current experience offers Edit, Plan and Chat choices. Edit can change the workbook, Plan proposes "
                    "a sequence before changes and Chat keeps the response in the conversation."
                ),
                why=(
                    "The same prompt has different consequences depending on the mode. A conversational explanation is "
                    "low-impact; a direct workbook edit changes shared evidence. Choosing the mode deliberately, saving a "
                    "protected source sheet and keeping version history available makes experimentation reversible and "
                    "keeps the human owner accountable for the final workbook."
                ),
                how=[
                    "Confirm the eligible Microsoft 365 account, current Excel version and visible Copilot entry point.",
                    "Choose Chat for questions, Plan when the intended sequence needs review and Edit for an approved change.",
                    "Inspect the proposed or completed work, save a new version and retain the ability to undo or restore.",
                ],
                example=[
                    "HarbourLight Retail has a raw order export and needs a weekly operations summary.",
                    "The analyst first asks Chat to describe the columns, then asks Plan for a safe preparation sequence.",
                    "Only after reviewing the plan does the analyst use Edit for one bounded change at a time.",
                ],
                use_when=[
                    "The workbook uses a modern supported format and the required Copilot experience is available.",
                    "The task has a clear owner who can review changes and restore an earlier version if needed.",
                ],
                avoid_when=[
                    "The prompt would expose secrets, sensitive personal information or data not approved for the service.",
                    "A high-impact financial, legal or operational decision would rely on an unchecked generated result.",
                ],
                quality=[
                    ("Mode", "Match Chat, Plan or Edit to the consequence of the task."),
                    ("Reversibility", "Protect the source, save versions and make one inspectable change at a time."),
                    ("Ownership", "A named person reviews and approves the workbook before it is shared or used."),
                ],
                sources=[
                    "https://support.microsoft.com/en-us/excel/copilot/get-started-with-copilot-in-excel",
                    "https://support.microsoft.com/en-us/excel/copilot/frequently-asked-questions-about-copilot-in-excel",
                ],
            ),
            dict(
                title="Preparing Data as Excel Tables for Copilot",
                definition=(
                    "An analysis-ready table has a single header row, one record per row, one variable per column, stable "
                    "identifiers and consistent types. Excel tables add names, filters and structured references that expand "
                    "with new rows. They make the intended data boundary clearer to people, formulas and Copilot."
                ),
                why=(
                    "Merged headings, blank rows, subtotals inside the data region, duplicate identifiers and mixed types "
                    "create ambiguous grain. If one row sometimes means an order and sometimes a subtotal, no prompt can "
                    "fully repair the analytical logic. Data structure must be corrected before asking for insight."
                ),
                how=[
                    "Identify the grain and primary identifier, then scan for blank headers, blank rows and duplicated IDs.",
                    "Convert the bounded range to a table, confirm headers and give the table a descriptive unique name.",
                    "Check date, text, count, currency and percentage columns; record known defects instead of hiding them.",
                ],
                example=[
                    "Each HarbourLight row represents one order line identified by Order_ID.",
                    "The learner converts the source range into tblOrdersRaw and freezes the header row.",
                    "A data-readiness log records inconsistent Region and Channel text for later controlled cleaning.",
                ],
                use_when=[
                    "The data can be expressed as a rectangular list with a consistent row meaning.",
                    "Headers can be made unique and each column can be assigned one stable data type.",
                ],
                avoid_when=[
                    "The range mixes several unrelated tables, presentation titles, subtotals and free-form notes.",
                    "Duplicate identifiers or missing units make the intended record grain unresolved.",
                ],
                quality=[
                    ("Grain", "Write one sentence that says exactly what a row represents."),
                    ("Schema", "Use unique headers, consistent types and stable categories."),
                    ("Controls", "Record row count, unique-ID count and source totals before transformation."),
                ],
                sources=[
                    "https://support.microsoft.com/en-us/office/create-and-format-tables-2f0ce0e7-500b-4fe1-9b5b-a16ba4b9f34a",
                    "https://support.microsoft.com/en-US/Excel/using-structured-references-with-excel-tables",
                    "https://support.microsoft.com/en-us/excel/copilot/get-started-with-copilot-in-excel",
                ],
            ),
            dict(
                title="Writing Effective Prompts for Data Tasks",
                definition=(
                    "A useful prompt is an executable specification. The C34 G-C-D-C-O-R pattern names the Goal, business "
                    "Context, exact Data boundary, Constraints, required Output and Review checks. It turns words such as "
                    "'analyse' or 'clean' into visible acceptance criteria."
                ),
                why=(
                    "Broad prompts force the model to guess which sheet, columns, period, aggregation and format matter. "
                    "Specific prompts reduce ambiguity and make the result testable. Follow-up prompts should refine one "
                    "dimension at a time and keep the original analytical question visible."
                ),
                how=[
                    "State one goal and the decision or workbook change it should support.",
                    "Name the table, fields, filters, units and exclusions; request a precise formula, table or chart output.",
                    "Require Copilot to explain its logic, flag assumptions and show the checks a human should perform.",
                ],
                example=[
                    "Goal: identify high-value returned orders that need review.",
                    "Data: tblOrdersRaw; use Returned, Units and Unit_Price; do not infer causes from Customer_Note.",
                    "Output: a filter plus a count; Review: show the exact conditions and preserve the full table.",
                ],
                use_when=[
                    "The user can name the data boundary and the expected output format.",
                    "The result has observable acceptance criteria such as a count, formula or explicit condition.",
                ],
                avoid_when=[
                    "The request is 'make this better' with no audience, boundary, rule or decision.",
                    "The prompt asks Copilot to fill unknown business facts or silently choose a high-impact threshold.",
                ],
                quality=[
                    ("Specific", "Name the table, fields, period, units and output."),
                    ("Bounded", "State exclusions, privacy limits and what must remain unchanged."),
                    ("Reviewable", "Ask for logic, assumptions, control checks and a clear success condition."),
                ],
                sources=[
                    "https://learn.microsoft.com/en-us/training/paths/craft-effective-prompts-copilot-microsoft-365/",
                    "https://support.microsoft.com/en-us/excel/copilot/data-insights-with-copilot-in-excel",
                    "https://support.microsoft.com/en-US/Excel/copilot/visualize-your-data-with-copilot-in-excel",
                ],
            ),
            dict(
                title="Highlighting, Sorting and Filtering Data with Copilot",
                definition=(
                    "Highlighting changes visual emphasis, sorting changes visible order and filtering changes which rows "
                    "are shown. None of them changes the underlying business meaning. A prompt should define the comparison "
                    "rule, tie-break order, filter conditions and whether hidden rows must remain available."
                ),
                why=(
                    "A visually persuasive sheet can still be analytically wrong. 'Highlight important orders' is undefined; "
                    "'highlight Returned=Yes and Gross_Sales at least 1000' is a reproducible rule. Filters can also hide the "
                    "denominator, so the filtered count and original row count should be recorded together."
                ),
                how=[
                    "Translate the business question into explicit Boolean conditions and a deterministic sort order.",
                    "Ask Copilot to describe the intended change, then apply it to the named table.",
                    "Count visible matches, clear the filter and confirm that the original row count returns.",
                ],
                example=[
                    "The team reviews orders where Returned is Yes and gross sales are at least S$1,000.",
                    "Rows are sorted by gross sales descending, then Order_ID ascending to break ties.",
                    "The analyst records both the flagged count and the unchanged total table count.",
                ],
                use_when=[
                    "The rule can be written using named fields, operators and values.",
                    "The workbook owner needs a reversible view, not a deletion of non-matching records.",
                ],
                avoid_when=[
                    "Colour alone would carry the only record of a business status.",
                    "Filtering would hide excluded rows from a report without disclosing the denominator.",
                ],
                quality=[
                    ("Rule", "Write the exact condition before applying any colour or filter."),
                    ("Denominator", "Record total rows and visible rows together."),
                    ("Reversible", "Clear the filter and confirm no records were deleted or overwritten."),
                ],
                sources=[
                    "https://support.microsoft.com/en-US/Excel/copilot/visualize-your-data-with-copilot-in-excel",
                    "https://support.microsoft.com/en-us/excel/copilot/get-started-with-copilot-in-excel",
                ],
            ),
            dict(
                title="Generating Formula Columns from Plain-English Requests",
                definition=(
                    "Copilot can propose native Excel formulas and add calculated columns. In a table, structured references "
                    "use names such as [@Units] and [@Unit_Price], making row logic easier to read and resilient when the "
                    "table grows. A generated formula remains a hypothesis until it is checked against the business rule."
                ),
                why=(
                    "Formula syntax can be valid while the logic is wrong: discount might be applied twice, margin might use "
                    "gross rather than net sales, or blanks might become zero without approval. Formula explanation, edge-case "
                    "tests and independent totals are therefore part of the task, not optional polish."
                ),
                how=[
                    "Write the business rule in words, including units, blank handling, rounding and error behaviour.",
                    "Ask for one structured-reference formula and an explanation before filling the calculated column.",
                    "Test representative, boundary and exceptional rows; then reconcile the column to independent totals.",
                ],
                example=[
                    "Gross_Sales equals Units multiplied by Unit_Price.",
                    "Net_Sales equals Gross_Sales less Gross_Sales times Discount_Rate.",
                    "Margin_Rate uses IFERROR(Gross_Profit divided by Net_Sales, zero), formatted as a percentage.",
                ],
                use_when=[
                    "The rule is deterministic and can be expressed using native Excel functions.",
                    "A control calculation or small hand-worked sample can verify the result.",
                ],
                avoid_when=[
                    "The requested value is a subjective classification presented as a precise calculation.",
                    "The formula would embed an unapproved business threshold or conceal missing data.",
                ],
                quality=[
                    ("Semantics", "Confirm the numerator, denominator, units, signs and timing."),
                    ("Edge cases", "Check blanks, zeros, returns, discounts and one high-value row."),
                    ("Reconciliation", "Tie column totals to an independent control before use."),
                ],
                sources=[
                    "https://support.microsoft.com/en-us/excel/copilot/data-insights-with-copilot-in-excel",
                    "https://support.microsoft.com/en-US/Excel/using-structured-references-with-excel-tables",
                    "https://support.microsoft.com/en-us/Excel/copilot/copilot-formula-suggestions-turn-on-off",
                ],
            ),
        ],
    ),
    dict(
        num=2,
        code="02",
        title="AI-Powered Data Analysis and Insights",
        subtitle=(
            "Cleaning and enriching data · PivotTables and charts from a prompt · trends, outliers and insights · "
            "advanced analysis with Python in Excel · verification and prompt best practices"
        ),
        weighting="Second half · 3 labs",
        concepts=[
            (
                "Defined cleaning rules",
                "Correct only documented text, spacing, format and missing-value issues; preserve the raw source.",
            ),
            (
                "Question-to-visual design",
                "Choose grain, dimensions, measures, aggregation and chart form from the decision question.",
            ),
            (
                "Descriptive insight",
                "Describe comparison, trend, distribution and outlier evidence before considering explanations.",
            ),
            (
                "Python-assisted analysis",
                "Review the referenced data, generated code, statistical method and returned output together.",
            ),
            (
                "Static versus refreshable output",
                "Label inserted images or tables that do not update when source data changes.",
            ),
            (
                "Evidence chain",
                "Trace every headline claim to source rows, a calculation and an independent cross-check.",
            ),
        ],
        sections=[
            dict(
                title="Cleaning and Enriching Data with Copilot",
                definition=(
                    "Cleaning makes existing values conform to a defined schema; enrichment adds a new field from a rule, "
                    "lookup or reviewed classification. The source sheet should remain unchanged. The cleaning log records "
                    "the issue, rule, affected count and verification so corrections are auditable."
                ),
                why=(
                    "Inconsistent text, number formats and extra spaces can split categories or produce wrong summaries. "
                    "Microsoft's Clean Data experience focuses on these common patterns, but availability can vary. A manual "
                    "or Copilot-assisted correction still needs a canonical value list and before/after counts."
                ),
                how=[
                    "Profile the source and compare observed values with the supplied data dictionary.",
                    "Copy the table to a working sheet; correct one issue type at a time and log the affected rows.",
                    "Add deterministic enrichment first, then review any text classification row by row against a taxonomy.",
                ],
                example=[
                    "Region values such as 'north', 'North ' and 'NORTH' become the canonical value 'North'.",
                    "Channel values map only to Store, Online or Partner according to the dictionary.",
                    "Customer_Note receives a reviewed Note_Theme; blanks remain 'No note' rather than invented feedback.",
                ],
                use_when=[
                    "The canonical schema and acceptable value set are documented.",
                    "The original data and a change log are retained for comparison.",
                ],
                avoid_when=[
                    "A correction would guess a missing business fact or overwrite an identifier.",
                    "A free-text classification will be treated as objective truth without human review.",
                ],
                quality=[
                    ("Preserve", "Keep the raw sheet unchanged and make corrections in a working table."),
                    ("Count", "Record affected rows before and after each rule."),
                    ("Taxonomy", "Use a small defined category list and retain Unknown when evidence is insufficient."),
                ],
                sources=[
                    "https://support.microsoft.com/en-us/excel/clean-data-in-excel",
                    "https://support.microsoft.com/en-us/excel/copilot/data-insights-with-copilot-in-excel",
                ],
            ),
            dict(
                title="Building PivotTables and Charts from a Prompt",
                definition=(
                    "A PivotTable aggregates measures across dimensions at a chosen grain. A chart encodes that summary "
                    "visually. A complete prompt names the source table, row and column fields, aggregation, filters, order, "
                    "chart type, title and the decision the view should support."
                ),
                why=(
                    "Copilot can build a polished result quickly, but speed does not resolve analytical design. Sum of sales, "
                    "average margin and count of orders answer different questions. A chart can also exaggerate differences "
                    "through an unsuitable scale, missing units or too many categories."
                ),
                how=[
                    "State the decision question, grain, dimensions, measures and required filters.",
                    "Generate the PivotTable first and reconcile its grand total to the cleaned table.",
                    "Choose a chart that fits comparison or time trend, then verify title, units, labels and source link.",
                ],
                example=[
                    "Question: how did monthly net sales change by canonical region?",
                    "Rows use Month, columns use Region and values use Sum of Net_Sales.",
                    "A line chart shows month on the x-axis and S$ net sales on the y-axis; the Pivot grand total must tie out.",
                ],
                use_when=[
                    "The table has a stable grain and measures have defined aggregations.",
                    "The intended comparison or trend can be shown without hiding material categories.",
                ],
                avoid_when=[
                    "The measure is a percentage that should be recomputed from totals rather than averaged row by row.",
                    "A chart is requested before the question, denominator or aggregation is agreed.",
                ],
                quality=[
                    ("Grain", "Name what one Pivot cell represents."),
                    ("Tie-out", "Reconcile the Pivot grand total to the source-table control."),
                    ("Chart truth", "Show units, full categories and an honest scale appropriate to the question."),
                ],
                sources=[
                    "https://support.microsoft.com/en-US/Excel/copilot/visualize-your-data-with-copilot-in-excel",
                    "https://support.microsoft.com/en-us/excel/overview-of-pivottables-and-pivotcharts",
                    "https://support.microsoft.com/en-us/excel/copilot/get-started-with-copilot-in-excel",
                ],
            ),
            dict(
                title="Surfacing Trends, Outliers and Insights",
                definition=(
                    "A trend describes change across an ordered period; an outlier is an observation unusually distant under "
                    "a stated rule; an insight connects a verified pattern to a relevant decision. None of these, by itself, "
                    "proves why the pattern occurred."
                ),
                why=(
                    "Prompts such as 'what is interesting?' can surface useful candidates, but they can also produce selective "
                    "or causal-sounding narratives. Start with a baseline, comparison and explicit outlier rule. Label observed "
                    "values separately from hypotheses that require more evidence."
                ),
                how=[
                    "Define the metric, period, comparison and minimum volume needed for interpretation.",
                    "Ask for descriptive results and an explicit outlier rule before requesting explanations.",
                    "Cross-check the cited rows, record limitations and convert only relevant verified patterns into actions.",
                ],
                example=[
                    "Monthly net sales are compared by region, while returned-order rate uses returned orders divided by orders.",
                    "High-value orders are flagged by a stated IQR rule and then inspected for data-quality issues.",
                    "A spike is described as observed; promotion, channel mix or data error remain hypotheses.",
                ],
                use_when=[
                    "The time order, denominator and comparison group are stable.",
                    "The output cites underlying values and states the method used to identify an outlier.",
                ],
                avoid_when=[
                    "A short or incomplete period is used to claim a persistent trend.",
                    "Correlation or a coincident change is presented as a proven cause.",
                ],
                quality=[
                    ("Baseline", "Show the comparison period, denominator and sample size."),
                    ("Method", "State the trend or outlier rule in reproducible terms."),
                    ("Language", "Use observed for evidence and hypothesis for a possible explanation."),
                ],
                sources=[
                    "https://support.microsoft.com/en-us/excel/copilot/data-insights-with-copilot-in-excel",
                    "https://support.microsoft.com/en-us/excel/get-direct-answers-to-your-data-analysis-questions",
                ],
            ),
            dict(
                title="Advanced Analysis with Python in Excel",
                definition=(
                    "Copilot can use Python-based analysis to interpret a question, compute statistics and return explanations, "
                    "tables or visuals. Direct-answer output may be static. Advanced analysis can open a new sheet and expose "
                    "Python code or a refreshable Python cell, depending on the available experience."
                ),
                why=(
                    "Python expands the range of analysis but does not remove review obligations. The analyst must verify the "
                    "referenced data, cleaning choices, grouping logic, missing-value treatment, statistical method and returned "
                    "values. Python in Excel runs in a Microsoft cloud container and has defined access and network boundaries."
                ),
                how=[
                    "Ask a precise analytical question and state the table, fields, period, grouping and expected output.",
                    "Open the generated logic or code; inspect row filters, aggregations, missing values and method assumptions.",
                    "Recompute headline results with Excel or a PivotTable, label static outputs and save the analysis notes.",
                ],
                example=[
                    "The team asks for monthly net-sales trends, return rates and an IQR review of high-value orders.",
                    "Generated Python groups only canonical rows and reports the count excluded for unresolved categories.",
                    "Excel control cells and the Pivot grand total independently confirm the headline values.",
                ],
                use_when=[
                    "The question needs deeper exploratory statistics or visuals and the available license supports the feature.",
                    "A reviewer can inspect the generated method and reproduce headline results independently.",
                ],
                avoid_when=[
                    "The analysis depends on unavailable external network calls or hidden local files.",
                    "A static inserted output will be mistaken for a refreshable result after the source changes.",
                ],
                quality=[
                    ("Inputs", "Confirm the exact table, rows, columns, filters and missing-value treatment."),
                    ("Method", "Review code and assumptions; do not accept the narrative alone."),
                    ("Reproducibility", "Tie headline values to Excel controls and label static outputs visibly."),
                ],
                sources=[
                    "https://support.microsoft.com/en-us/excel/get-direct-answers-to-your-data-analysis-questions",
                    "https://support.microsoft.com/en-US/Excel/python/introduction-to-python-in-excel",
                    "https://support.microsoft.com/en-US/Excel/python/data-security-and-python-in-excel",
                ],
            ),
            dict(
                title="Verifying Results and Prompt Best Practices",
                definition=(
                    "Verification is a chain of checks from source structure to formula, aggregation, visual and written claim. "
                    "The C34 quality gate uses protected source data, a prompt log, edge-case tests, independent control totals, "
                    "traceable claims and a named human decision."
                ),
                why=(
                    "Copilot can produce fluent explanations and valid-looking formulas that are incomplete or wrong. Microsoft "
                    "advises users to review, edit and verify generated content. A compact repeatable gate makes that advice "
                    "operational and prevents an attractive workbook from bypassing basic evidence checks."
                ),
                how=[
                    "Validate row grain, types, category values, duplicates and source control totals.",
                    "Inspect formulas, representative rows, Pivot totals, chart encodings and Python logic.",
                    "Record each claim, supporting value, limitation, owner and Share, Revise or Hold decision.",
                ],
                example=[
                    "The executive summary states a regional sales movement and cites the Pivot values behind it.",
                    "A return-rate statement shows numerator and denominator, not only the percentage.",
                    "An outlier explanation stays a hypothesis until operational evidence supports it.",
                ],
                use_when=[
                    "Any generated output will be shared, used in a decision or reused as a template.",
                    "Another reviewer needs to reproduce the conclusion without relying on the chat history.",
                ],
                avoid_when=[
                    "A fluent answer is treated as proof without checking the workbook.",
                    "A control total is copied from the same generated output it is supposed to verify.",
                ],
                quality=[
                    ("Independent", "Use a different method or source for the control check."),
                    ("Traceable", "Link every headline statement to cells, rows or a documented calculation."),
                    ("Decisive", "Choose Share, Revise or Hold and state the owner and unresolved limitation."),
                ],
                sources=[
                    "https://support.microsoft.com/en-us/excel/copilot/frequently-asked-questions-about-copilot-in-excel",
                    "https://support.microsoft.com/en-us/excel/copilot/data-insights-with-copilot-in-excel",
                    "https://support.microsoft.com/en-US/Excel/copilot/visualize-your-data-with-copilot-in-excel",
                ],
            ),
        ],
    ),
]

DAY_THEMES = {
    1: "Prepare, transform, analyse and verify one Copilot-assisted Excel workflow",
}


def SCHEDULE(lab_titles):
    return {
        1: (
            DAY_THEMES[1],
            [
                (
                    "9:30",
                    "9:45",
                    15,
                    "admin",
                    "Welcome, course introduction, learning outcomes, setup check and safe workbook practices",
                ),
                (
                    "9:45",
                    "10:35",
                    50,
                    "topic",
                    "Topic 1 - Copilot modes, analysis-ready Excel tables and the G-C-D-C-O-R prompt method",
                ),
                ("10:35", "11:20", 45, "lab", "Hands-on: " + lab_titles([1])),
                ("11:20", "11:35", 15, "break", "Tea break"),
                (
                    "11:35",
                    "12:15",
                    40,
                    "lab",
                    "Hands-on: " + lab_titles([2]),
                ),
                (
                    "12:15",
                    "13:00",
                    45,
                    "lab",
                    "Hands-on: " + lab_titles([3]),
                ),
                ("13:00", "14:00", 60, "lunch", "Lunch break"),
                (
                    "14:00",
                    "14:55",
                    55,
                    "topic",
                    "Topic 2 - Data quality, PivotTables, chart design, descriptive insight and Python-assisted analysis",
                ),
                ("14:55", "15:55", 60, "lab", "Hands-on: " + lab_titles([4])),
                ("15:55", "16:10", 15, "break", "Tea break"),
                ("16:10", "17:05", 55, "lab", "Hands-on: " + lab_titles([5])),
                ("17:05", "18:20", 75, "lab", "Hands-on: " + lab_titles([6])),
                (
                    "18:20",
                    "18:30",
                    10,
                    "recap",
                    "Topic recaps mapped to LO1-LO4, continuing-practice plan and questions",
                ),
            ],
        ),
    }


COURSE_OVERVIEW = dict(
    section_title="The Verified Copilot-in-Excel Workflow",
    concepts_title="Keep Four Layers Visible",
    concepts=[
        ("Source data", "Protected raw rows, documented grain, types, identifiers and control totals."),
        ("Copilot action", "The prompt, selected mode, proposed logic and exact workbook change."),
        ("Verification evidence", "Formula checks, reconciliations, Pivot tie-outs and cited source rows."),
        ("Human decision", "Approved wording, limitations, owner and Share, Revise or Hold outcome."),
    ],
    framework_title="G-C-D-C-O-R Prompt Framework",
    framework=[
        ("Goal", "One task and the decision or workbook change it supports."),
        ("Context", "Audience, business situation, units and time period."),
        ("Data", "Named table, sheets, fields, grain and filters."),
        ("Constraints", "What must remain unchanged, privacy limits and exclusions."),
        ("Output", "Formula, table, chart, explanation or exact schema."),
        ("Review", "Logic, assumptions, edge cases, controls and acceptance criteria."),
    ],
    statement=dict(
        headline="Copilot accelerates workbook work; verification determines whether the result is usable.",
        body="Protect the source, specify the task, inspect every change and reconcile every headline number.",
        kicker="C34 OPERATING PRINCIPLE",
    ),
    pillars_title="What You Will Build",
    pillars=[
        ("Prepared workbook", ["named Excel table", "readiness log", "prompt-and-change trail"]),
        ("Analysis workbook", ["formula columns", "clean table", "PivotTables and charts"]),
        ("Decision pack", ["Python-assisted analysis", "reconciliation", "verified executive summary"]),
    ],
    arc_title="The Learning Arc in Every Lab",
    arc=[
        "Open the supplied checkpoint and state the exact question.",
        "Prompt Copilot with a named data boundary and review criteria.",
        "Inspect the workbook change, formula, Pivot or generated code.",
        "Run the Test It controls and keep the checkpoint for the next lab.",
    ],
    deep_dives=[
        dict(
            title="The C34 Verification Gate",
            kicker="BEFORE YOU RELY ON A RESULT",
            items=[
                ("Structure", "Does each row have one meaning and do types and categories match the dictionary?"),
                ("Logic", "Do formula, aggregation, denominator, filter and missing-value rules match the question?"),
                ("Reconciliation", "Do independent counts and totals tie to the generated output?"),
                ("Visual", "Are title, units, scale, categories and source linkage accurate?"),
                ("Claim", "Does each sentence distinguish observed evidence from a hypothesis?"),
                ("Decision", "Share, Revise or Hold - with an owner, reason and unresolved limitation."),
            ],
        ),
    ],
)

LAB_SHOTS = {}

LG_INTRO = (
    "This Learner Guide accompanies Microsoft 365 Copilot for Excel (C34). It follows the same "
    "two-topic sequence, six connected labs, learning outcomes and verified HarbourLight Retail "
    "scenario as the slide deck, Lesson Plan and standalone lab files."
)

LG_INTRO2 = (
    "Use the guide as a self-contained study text before, during and after class. Each concept "
    "explains what the capability is, why it matters, how it works, a worked example and when to "
    "use or avoid it. The labs then apply those ideas to one workbook. Copilot output remains a "
    "proposal until the learner inspects the cells, formulas, PivotTables, charts or Python logic "
    "and completes the independent checks."
)

LG_SETUP = dict(
    needs=[
        "A Windows or Mac laptop with a current version of Microsoft Excel or Excel for the web.",
        "An eligible Microsoft 365 account with the Copilot entry point enabled by your organisation or plan.",
        "A OneDrive or SharePoint folder where you can save the training workbook with cloud sync and AutoSave enabled.",
        "A downloaded copy of this repository with the labs/assets folder intact.",
        "Permission to use only the supplied synthetic HarbourLight data during class.",
    ],
    verify_text=(
        "Open labs/assets/harbourlight-orders-raw.csv in Excel. Confirm that row 1 contains the "
        "12 expected headers and that 36 data rows are present. In OneDrive or SharePoint, create a "
        "training folder named work-c34. Save a temporary .xlsx file there, confirm cloud sync and "
        "AutoSave are active, then open Copilot and note whether Edit, Plan and Chat choices are "
        "visible; labels can vary as Microsoft updates the interface."
    ),
    verify_code=(
        "Expected structure:\n"
        "Downloaded course files:\n"
        "  C34---Microsoft-365-Copilot-for-Excel/labs/assets/\n"
        "Cloud-saved working folder:\n"
        "  OneDrive or SharePoint/work-c34/"
    ),
    conventions=[
        "All HarbourLight names, orders, notes and values are synthetic training material.",
        "Text between <ANGLE_BRACKETS> is a placeholder to replace; never paste a password or secret.",
        "OBSERVED means supported by workbook evidence; HYPOTHESIS means a possible explanation; UNKNOWN remains unresolved.",
        "S$ is used for currency, dates use yyyy-mm-dd and percentages are stored as decimal values.",
        "Save the prompt, proposed logic, workbook change, verification and human decision together.",
        "When the trainer provides a read-only cloud checkpoint after Labs 1-5, save a personal copy and rerun the "
        "matching Test It controls before continuing.",
    ],
)

LAB_NOTE = (
    "Use only the supplied synthetic HarbourLight data or information you are authorised to process. "
    "Do not paste credentials, confidential business material or sensitive personal data into Copilot."
)

LG_WRAPUP = dict(
    title="Wrap-Up - The Complete C34 Workflow",
    intro=(
        "The finished output is not simply a polished workbook. It is a traceable chain from source "
        "data through Copilot actions and independent checks to a named human decision."
    ),
    sections=[
        dict(
            title="Prepare and transform",
            bullets=[
                "Confirm access, mode and a reversible versioning approach.",
                "Define row grain and convert the bounded source into a named Excel table.",
                "Use explicit rules for filters, sorting, highlighting and generated formula columns.",
            ],
        ),
        dict(
            title="Summarise and analyse",
            bullets=[
                "Clean against a canonical dictionary and retain the source sheet.",
                "Define grain, measure and aggregation before creating PivotTables and charts.",
                "Use Python-assisted analysis for deeper questions while reviewing generated logic.",
            ],
        ),
        dict(
            title="Verify and communicate",
            bullets=[
                "Reconcile counts, formula totals, Pivot grand totals and analytical headline values.",
                "Label static outputs and separate observed evidence from hypotheses.",
                "Choose Share, Revise or Hold with a named owner and visible limitations.",
            ],
        ),
    ],
)

LG_NEXT_STEPS = [
    "Re-run all six labs from the raw CSV without referring to your completed workbook.",
    "Adapt the G-C-D-C-O-R prompt and verification log to one authorised workbook in your role.",
    "Create a small reusable control panel with row counts, unique IDs and source totals.",
    "Review Microsoft Support before delivery because Copilot labels, availability and capabilities continue to change.",
]

LG_GLOSSARY = [
    ("Calculated column", "A table column whose formula is filled consistently for every data row."),
    ("Canonical value", "The approved spelling and format used for a category after cleaning."),
    ("Control total", "An independently computed count or sum used to verify another output."),
    ("Edit mode", "The Copilot choice that can make changes directly in the workbook."),
    ("Grain", "What one row or one aggregated cell represents."),
    ("G-C-D-C-O-R", "Goal, Context, Data, Constraints, Output and Review - the C34 prompt framework."),
    ("IQR", "Interquartile range; the distance between the 25th and 75th percentiles."),
    ("Outlier", "An observation unusually distant under a stated method, not automatically an error."),
    ("PivotTable", "An interactive Excel object that aggregates measures across selected dimensions."),
    ("Plan mode", "The Copilot choice that proposes a structured sequence before workbook changes."),
    ("Static output", "An inserted table or image that does not automatically update with its source data."),
    ("Structured reference", "An Excel formula reference that uses table and column names."),
    ("Tie-out", "A reconciliation showing that two independently derived totals agree."),
]

NEXT_STEPS = dict(
    title="Continue the Verified Workflow",
    items=[
        "Reuse the prepared prompt and verification templates on an authorised workbook.",
        "Keep a protected source sheet and visible controls in every Copilot-assisted model.",
        "Refresh PivotTables and rerun checks whenever the source data changes.",
        "Review generated code, formulas and claims before sharing a decision summary.",
    ],
)

THANK_YOU = dict(
    body=(
        "You can now prepare, transform, analyse and verify Excel work with Copilot while keeping "
        "source evidence, formula logic and human judgment in control."
    ),
    kicker="MICROSOFT 365 COPILOT FOR EXCEL · C34",
)

VERSION_HISTORY = [
    (
        "1.0",
        VERSION_DATE,
        "Initial aligned release of PPT, Learner Guide, Lesson Plan and six connected labs.",
        TRAINER,
    ),
]
