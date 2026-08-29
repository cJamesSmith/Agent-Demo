# Scoring and Sensitivity Reference

Normalize each metric across the three markets to a 0–100 range using min-max normalization: for positive metrics, `(value-min)/(max-min)*100`; for reverse metrics, `(max-value)/(max-min)*100`. If the maximum equals the minimum, assign 50 to all markets for that metric.

| Dimension | Source metrics | Combination |
|---|---|---|
| Growth Potential | Market size, three-year CAGR | 50% each |
| Profitability | Gross margin (positive), customer acquisition cost (reverse) | 50% each |
| Competitive Environment | Competition score | 100% reverse |
| Regulatory Risk | Regulatory complexity | 100% reverse |
| Execution Feasibility | Execution difficulty | 100% reverse |

The total score is the sum of each dimension score multiplied by its dimension weight, rounded to one decimal place.

| Scenario | Growth | Profitability | Competition | Regulation | Execution |
|---|---:|---:|---:|---:|---:|
| Growth-first | 40 | 20 | 15 | 10 | 15 |
| Profit-first | 15 | 40 | 10 | 15 | 20 |
| Risk-first | 10 | 20 | 10 | 35 | 25 |
| Cash-flow-first (extension) | 10 | 35 | 10 | 20 | 25 |

When one slider changes, adjust the other dimensions proportionally so the total remains 100. Mark the conclusion as sensitive when the score gap is less than 5 points. Display data confidence, but do not include it directly in the attractiveness score.
