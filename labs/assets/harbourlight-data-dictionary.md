# HarbourLight Retail Data Dictionary

Use this dictionary for the synthetic C34 scenario. Do not invent values outside it.

## Row grain and key

- One data row represents one HarbourLight order.
- `Order_ID` is the expected unique identifier.
- The source contains 36 rows covering 2026-01-05 through 2026-04-28.

## Field definitions

| Field | Type | Definition | Rule |
|---|---|---|---|
| Order_ID | Text | Synthetic order identifier | Required; unique; format `HL-####` |
| Order_Date | Date | Order transaction date | Valid date; display `yyyy-mm-dd` |
| Region | Text category | Operating region | Canonical: `North`, `South`, `Central` |
| Channel | Text category | Order channel | Canonical: `Store`, `Online`, `Partner` |
| Product | Text category | Product sold | `Trail Pack`, `City Tote`, `Weekender`, `Bottle`, `Travel Pouch`, `Laptop Sleeve` |
| Category | Text category | Product family | `Bags`, `Accessories` |
| Units | Whole number | Units in the order | Positive integer |
| Unit_Price | Currency | Selling price per unit before discount | S$; non-negative |
| Unit_Cost | Currency | Cost per unit | S$; non-negative |
| Discount_Rate | Percentage | Proportion deducted from gross sales | Decimal from 0 to 1 |
| Returned | Text category | Whether the order was returned | `Yes` or `No` |
| Customer_Note | Text | Optional synthetic note | Blank is permitted |

## Canonical cleaning rules

1. Preserve `Raw_Orders` unchanged.
2. Trim surrounding spaces in Region and Channel.
3. Standardise Region and Channel case to the canonical values above.
4. Do not change Order_ID, numeric inputs or formula columns while cleaning categories.
5. Retain the before/after count for every replacement rule.

## Enrichment rules

### Month

Derive text in `yyyy-mm` format from `Order_Date`.

### Return_Flag

- `1` when `Returned` exactly equals `Yes`.
- `0` otherwise.

### Note_Theme

Use the first matching cue below. Do not invent a reason.

| Theme | Approved cues |
|---|---|
| No note | Blank or whitespace-only Customer_Note |
| Return | Contains `return` or `refund` |
| Delivery | Contains `deliver`, `delay` or `package` |
| Product | Contains `product`, `zipper`, `strap`, `handle`, `colour`, `fit` or `quality` |
| Unknown | No approved cue matches |

The theme is a reviewed training classification, not an objective fact about customer intent.
