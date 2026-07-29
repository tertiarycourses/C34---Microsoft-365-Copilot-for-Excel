# Formula and Verification Rules

Apply these rules to `tblOrdersWorking`. Use native Excel formulas with structured references.

| Output field | Business rule | Required formula |
|---|---|---|
| Gross_Sales | Units multiplied by Unit_Price | `=[@Units]*[@Unit_Price]` |
| Discount_Amount | Gross_Sales multiplied by Discount_Rate | `=[@Gross_Sales]*[@Discount_Rate]` |
| Net_Sales | Gross_Sales less Discount_Amount | `=[@Gross_Sales]-[@Discount_Amount]` |
| Cost_Amount | Units multiplied by Unit_Cost | `=[@Units]*[@Unit_Cost]` |
| Gross_Profit | Net_Sales less Cost_Amount | `=[@Net_Sales]-[@Cost_Amount]` |
| Margin_Rate | Gross_Profit divided by Net_Sales; zero if the denominator is zero | `=IFERROR([@Gross_Profit]/[@Net_Sales],0)` |

## Required formats

- Gross_Sales, Discount_Amount, Net_Sales, Cost_Amount and Gross_Profit: S$ with two decimals.
- Margin_Rate: percentage with one decimal.
- Do not round inside the formulas. Apply display formatting instead.

## Verification sequence

1. Inspect the formula text in the first, middle and last table row.
2. Hand-calculate one row with no discount and one with a 20% discount.
3. Confirm all 36 rows contain formulas and no formula-error values.
4. Reconcile the five monetary totals with `expected-controls.md`.
5. Calculate overall margin as total Gross_Profit divided by total Net_Sales. Do not average row margin percentages.

Use the `COPILOT` worksheet function only for suitable text tasks where it is available. Do not use it for these deterministic numeric calculations.
