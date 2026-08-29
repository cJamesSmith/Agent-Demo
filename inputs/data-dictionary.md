# Market Data Dictionary

> All data is fictional instructional data.

| Field | Unit/range | Meaning | Scoring direction |
|---|---|---|---|
| `market_size_usd_m` | USD millions | Current serviceable market size | Higher is better |
| `three_year_cagr_pct` | % | Compound annual growth rate over the next three years | Higher is better |
| `customer_acquisition_cost_usd` | USD | Estimated cost to acquire one paying customer | Lower is better |
| `gross_margin_pct` | % | Estimated steady-state gross margin | Higher is better |
| `competition_score` | 0–100 | Intensity of competition | Lower is better |
| `regulatory_complexity_score` | 0–100 | Complexity of regulatory entry and ongoing operations | Lower is better |
| `execution_difficulty_score` | 0–100 | Combined difficulty of localization, channels, talent, and operations | Lower is better |
| `data_confidence_pct` | % | Research team's confidence in data quality | Display only; do not include directly in the base score |

## Recommended Decision Dimensions

1. **Growth Potential**: market size and three-year growth rate.
2. **Profitability**: gross margin and customer acquisition cost.
3. **Competitive Environment**: reverse-normalized competition score.
4. **Regulatory Risk**: reverse-normalized regulatory complexity.
5. **Execution Feasibility**: reverse-normalized execution difficulty.

## Normalization Rules

Apply min-max normalization to each metric across the three markets:

- Positive metric: `(value - min) / (max - min) × 100`
- Reverse metric: `(max - value) / (max - min) × 100`
- If the maximum equals the minimum, assign 50 points to every market for that metric.

Round all calculated results to one decimal place. The dashboard must state explicitly that rankings are scenario simulations based on limited inputs, not forecasts.
