# Appendix B: Extended Results

**Supplementary material for:** "Benchmarking Large Language Models for Geolocating Colonial Virginia Land Grants"

**Repository:** [https://github.com/ryanmio/colonial-virginia-llm-geolocation](https://github.com/ryanmio/colonial-virginia-llm-geolocation)

---

## B.1 Detailed Accuracy Metrics

Table B.1 provides comprehensive error statistics for each evaluated method, including confidence intervals derived from bootstrap resampling (10,000 iterations). The best-performing automated approach, M-2 (o3-2025-04-16), achieves a mean error of 23.39 km with a 95% confidence interval of [17.57, 29.54] km.

| Method | Model | n | Mean km | 95% CI |
|---|---|---|---|---|
| E-1 | o3-2025-04-16 (ensemble) | 43 | 19.24 | [13.60, 24.97] |
| E-2 | ensemble name-redacted | 43 | 20.57 | [15.08, 26.83] |
| H-1 | GIS analyst baseline | 43 | 71.40 | [59.14, 85.11] |
| H-2 | Stanford NER (GeoTxt) | 43 | 79.02 | [56.32, 109.38] |
| H-3 | Mordecai-3 | 43 | 94.28 | [68.81, 124.61] |
| H-4 | County Centroid | 43 | 80.33 | [65.96, 95.88] |
| M-1 | o4-mini-2025-04-16 | 43 | 41.65 | [33.77, 50.11] |
| M-2 | o3-2025-04-16 | 43 | 23.39 | [17.37, 29.25] |
| M-3 | o3-mini-2025-01-31 | 43 | 50.25 | [43.02, 58.63] |
| M-4 | gpt-4.1-2025-04-14 | 43 | 28.51 | [22.68, 35.10] |
| M-5 | gpt-4o-2024-08-06 | 43 | 27.93 | [22.31, 33.85] |
| M-6 | gpt-3.5-turbo | 43 | 43.05 | [33.78, 53.98] |
| T-1 | o4-mini-2025-04-16 + tools | 43 | 37.65 | [30.86, 44.99] |
| T-4 | gpt-4.1-2025-04-14 + tools | 43 | 37.23 | [30.11, 45.03] |

**Table B.1:** Mean error with 95% bootstrap CIs by method.

## B.2 Performance by Method

Table B.2 provides the complete performance statistics for each method, including variance measures and accuracy bands. The "≤X km" columns show the percentage of predictions within X kilometers of ground truth.

| Method | n | mean | median | sd | min | Q1 | Q3 | max | ≤10 km | ≤25 km | ≤50 km |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E-1 | 43 | 18.71 | 12.45 | 19.36 | 1.77 | 5.60 | 23.87 | 100.90 | 39.5% | 76.7% | 95.3% |
| E-2 | 43 | 20.44 | 13.75 | 18.87 | 1.11 | 7.41 | 24.05 | 95.34 | 34.9% | 76.7% | 95.3% |
| H-1 | 43 | 71.40 | 60.20 | 45.65 | 5.98 | 30.63 | 117.50 | 170.95 | 4.7% | 18.6% | 41.9% |
| H-2 | 43 | 79.02 | 59.45 | 88.32 | 2.29 | 29.05 | 94.67 | 448.66 | 7.0% | 23.3% | 41.9% |
| H-3 | 43 | 94.28 | 55.45 | 91.73 | 5.20 | 30.63 | 123.12 | 383.18 | 7.0% | 20.9% | 41.9% |
| H-4 | 43 | 80.33 | 70.49 | 51.46 | 2.46 | 36.82 | 125.61 | 187.61 | 4.7% | 11.6% | 37.2% |
| M-1 | 43 | 41.65 | 27.39 | 27.32 | 7.59 | 18.45 | 70.04 | 103.49 | 7.0% | 37.2% | 62.8% |
| M-2 | 43 | 23.39 | 14.27 | 19.86 | 2.67 | 8.17 | 36.85 | 87.35 | 30.2% | 60.5% | 93.0% |
| M-3 | 43 | 50.25 | 48.40 | 24.93 | 6.29 | 27.36 | 69.53 | 123.04 | 4.7% | 16.3% | 53.5% |
| M-4 | 43 | 28.51 | 25.42 | 20.77 | 2.14 | 12.09 | 40.49 | 98.72 | 20.9% | 48.8% | 86.0% |
| M-5 | 43 | 27.93 | 24.97 | 19.46 | 3.03 | 14.66 | 37.25 | 98.86 | 16.3% | 51.2% | 90.7% |
| M-6 | 43 | 43.05 | 34.02 | 36.07 | 5.17 | 17.11 | 49.74 | 176.33 | 4.7% | 34.9% | 76.7% |
| T-1 | 43 | 37.65 | 33.61 | 24.54 | 0.59 | 18.57 | 62.30 | 110.19 | 14.0% | 32.6% | 69.8% |
| T-4 | 43 | 37.23 | 34.22 | 23.94 | 0.59 | 21.78 | 53.35 | 101.85 | 16.3% | 32.6% | 74.4% |

**Table B.2:** Full performance profile per method (dispersion and ≤10/25/50 km bands).

## B.3 Cost-Accuracy Trade-off

Table B.3 examines the cost-accuracy relationship, emphasizing the economic efficiency of gpt-4o-2024-08-06, which achieves near-top performance at just $1.05 per 1,000 grants processed.  "Cost per +1% ≤10 km hit" indicates the marginal cost of improving high-precision prediction rate by one percentage point.

| Model | Mean error km | ≤10 km hit-rate | Cost per 1k located (USD) | Cost per +1% ≤10 km hit (USD) |
|--------|---|---|---|---|
| o3-2025-04-16 (Ensemble) | 18.71 | 39.5% | $195.65 | $4.95 |
| o3-2025-04-16 | 23.39 | 30.2% | $127.46 | $4.22 |
| gpt-4o-2024-08-06 | 27.93 | 16.3% | $1.05 | $0.06 |
| gpt-4.1-2025-04-14 | 32.87 | 18.6% | $3.49 | $0.19 |
| o4-mini-2025-04-16 | 39.65 | 10.5% | $10.69 | $1.02 |
| gpt-3.5-turbo | 43.05 | 4.7% | $0.10 | $0.02 |
| o3-mini-2025-01-31 | 50.25 | 4.7% | $14.15 | $3.04 |
| human-gis | 71.40 | 4.7% | $3,255.81 | $700.00 |

**Table B.3:** Cost–accuracy summary by model family.

## B.4 Processing Time Analysis

Table B.4 quantifies the latency advantage of automated methods over traditional GIS workflows. "Speedup" shows relative improvement over the traditional GIS baseline.

| Model | Hours per located | Hours per 1k located | Speedup vs. baseline |
|---|---|---|---|
| o3-2025-04-16 (Ensemble) | 0.0128 | 12.819 | 17× |
| gpt-4o-2024-08-06 | 0.0002 | 0.178 | 1,219× |
| gpt-3.5-turbo | 0.0002 | 0.225 | 964× |
| gpt-4.1-2025-04-14 | 0.0003 | 0.295 | 736× |
| o3-2025-04-16 | 0.0121 | 12.060 | 18× |
| o3-mini-2025-01-31 | 0.0085 | 8.523 | 25× |
| o4-mini-2025-04-16 | 0.0091 | 9.145 | 24× |
| human-gis | 0.2170 | 216.977 | 1× |

**Table B.4:** Processing time by model.

## B.5 Token Usage Statistics

Table B.5 provides detailed token consumption data across all models, offering insight into computational efficiency.

| Model | Input tokens | Output tokens | Tokens per 1k located |
|---|---|---|---|
| o3-2025-04-16 (Ensemble) | 33,265 | 210,681 | 10,441,907 |
| gpt-4o-2024-08-06 | 6,698 | 900 | 176,698 |
| gpt-3.5-turbo | 6,773 | 820 | 176,581 |
| gpt-4.1-2025-04-14 | 142,258 | 4,193 | 1,702,919 |
| o3-2025-04-16 | 6,653 | 146,085 | 6,923,209 |
| o3-mini-2025-01-31 | 6,653 | 142,020 | 6,739,372 |
| o4-mini-2025-04-16 | 274,903 | 146,590 | 6,340,337 |

**Table B.5:** Token consumption by model.

Tool-augmented methods consumed on average 1.49× more tokens than pure-prompt counterparts (4,985,953 vs. 3,355,078 tokens per 1,000 located grants). However, this effect varied dramatically by model architecture: adding tools to gpt-4.1-2025-04-14 increased token usage by 18.3× (176,698 → 3,229,140), while o4-mini showed only a 1.14× increase (5,937,907 → 6,742,767).

## B.6 Professional GIS Benchmark Analysis

Table B.6 provides a more detailed analysis of the professional GIS benchmark (H-1) results, categorized by precision level. This breakdown reveals that even with expert domain knowledge and access to specialized historical gazetteers, more than 41.9% of the human-geocoded grants were located at only state-level precision. "High" indicates grants where both county boundaries and specific landmarks were used; "Medium" indicates county-centroid placement; "Low" indicates state-level precision only.

| Accuracy Category | N | Share (%) | Mean Error (km) | Median Error (km) |
|-------|---|---|---|---|
| Overall | 43 | 100.0 | 71.40 | 60.20 |
| High (County + Landmarks) | 19 | 44.2 | 68.88 | 48.09 |
| Medium (County centroid) | 6 | 14.0 | 87.95 | 82.11 |
| Low (State-level) | 18 | 41.9 | 68.55 | 63.26 |

**Table B.6:** Professional GIS benchmark by placement precision.

Notably, even the "High" precision category (where both county boundaries and specific landmarks were identified) still resulted in a mean error of 68.88 km—substantially higher than all the automated methods except gpt-3.5-turbo (M-6). This underscores the inherent difficulty of the task and further highlights the significance of the accuracy improvements achieved by the LLM approaches.

