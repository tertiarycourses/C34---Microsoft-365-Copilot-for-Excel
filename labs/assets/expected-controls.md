# Expected Controls

This file is generated from the synthetic source and the documented C34 rules. Use it as an independent comparison, not as a value to paste over a mismatched result.

## Source controls

| Control | Expected |
|---|---:|
| Data rows | 36 |
| Populated Order_ID values | 36 |
| Unique Order_ID values | 36 |
| Earliest Order_Date | 2026-01-05 |
| Latest Order_Date | 2026-04-28 |
| Sum of Units | 594 |
| Gross sales before discount | S$44,366.00 |

## Lab 2 view controls

| Control | Expected |
|---|---:|
| Returned = Yes | 8 rows |
| Discount_Rate >= 0.15 | 11 rows |
| Maximum Units | 30 |
| Maximum-Units Order_ID values | HL-1018, HL-1036 |

After sorting Units descending and Order_ID ascending, the first five pairs must be:

1. HL-1018 - 30
2. HL-1036 - 30
3. HL-1032 - 28
4. HL-1031 - 27
5. HL-1015 - 26

## Formula totals

| Field | Expected total |
|---|---:|
| Gross_Sales | S$44,366.00 |
| Discount_Amount | S$3,817.30 |
| Net_Sales | S$40,548.70 |
| Cost_Amount | S$23,313.00 |
| Gross_Profit | S$17,235.70 |
| Overall Margin_Rate | 42.5062% |

The overall margin is total Gross_Profit divided by total Net_Sales.

## Representative row checks

| Order_ID | Gross_Sales | Discount_Amount | Net_Sales | Cost_Amount | Gross_Profit | Margin_Rate |
|---|---:|---:|---:|---:|---:|---:|
| HL-1001 | S$1,032.00 | S$51.60 | S$980.40 | S$600.00 | S$380.40 | 38.8005% |
| HL-1003 | S$795.00 | S$0.00 | S$795.00 | S$460.00 | S$335.00 | 42.1384% |
| HL-1007 | S$1,602.00 | S$320.40 | S$1,281.60 | S$864.00 | S$417.60 | 32.5843% |
| HL-1018 | S$4,770.00 | S$238.50 | S$4,531.50 | S$2,760.00 | S$1,771.50 | 39.0930% |
| HL-1032 | S$3,612.00 | S$361.20 | S$3,250.80 | S$2,100.00 | S$1,150.80 | 35.4005% |

## Cleaning and enrichment controls

| Control | Expected |
|---|---:|
| Region values requiring trim or case correction | 13 |
| Channel values requiring trim or case correction | 7 |
| Canonical Region counts | North 12; South 12; Central 12 |
| Canonical Channel counts | Store 14; Online 12; Partner 10 |
| Returned-order count / Sum of Return_Flag | 8 |
| Month values | 2026-01, 2026-02, 2026-03, 2026-04 |

### Note_Theme counts

| Note_Theme | Expected count |
|---|---:|
| Delivery | 10 |
| Product | 14 |
| Return | 4 |
| No note | 8 |
| Unknown | 0 |

## Monthly Net_Sales by Region

| Month | Central | North | South | Month total |
|---|---:|---:|---:|---:|
| 2026-01 | S$2,007.60 | S$2,755.00 | S$2,425.60 | S$7,188.20 |
| 2026-02 | S$6,411.80 | S$2,330.25 | S$3,680.45 | S$12,422.50 |
| 2026-03 | S$2,901.30 | S$3,189.65 | S$2,579.10 | S$8,670.05 |
| 2026-04 | S$3,456.85 | S$2,704.95 | S$6,106.15 | S$12,267.95 |
| Grand total | S$14,777.55 | S$10,979.85 | S$14,791.30 | S$40,548.70 |

The highest Month-Region value is Central in 2026-02 at S$6,411.80.

## Returned-order rate by Channel

| Channel | Returned orders | Order count | Return_Rate |
|---|---:|---:|---:|
| Online | 2 | 12 | 16.6667% |
| Partner | 1 | 10 | 10.0000% |
| Store | 5 | 14 | 35.7143% |
| Overall | 8 | 36 | 22.2222% |

## IQR review of Net_Sales

Use inclusive quartiles with linear interpolation and the upper-fence rule `Q3 + 1.5 × IQR`.

| Statistic | Expected |
|---|---:|
| Q1 | S$739.1375 |
| Q3 | S$1,204.2000 |
| IQR | S$465.0625 |
| Upper fence | S$1,901.79375 |

Orders above the upper fence:

| Order_ID | Net_Sales |
|---|---:|
| HL-1029 | S$2,064.00 |
| HL-1032 | S$3,250.80 |
| HL-1018 | S$4,531.50 |

These are review candidates under the stated rule. They are not automatically errors and the rule does not explain why the values are high.
