# Appendix C: Supplementary Figures

**Supplementary material for:** "Benchmarking Large Language Models for Geolocating Colonial Virginia Land Grants"

**Repository:** [https://github.com/ryanmio/colonial-virginia-llm-geolocation](https://github.com/ryanmio/colonial-virginia-llm-geolocation)

---

## C.1 Error Distribution Plots

Figure C.1 shows the distribution of geolocation error for each method as a boxplot, complementing the violin plot and CDF already presented in the main text. The boxplot highlights the median error (central line), interquartile range (box), and outliers (points) for each method, providing a clear view of error distribution and central tendency.

![Error boxplots by method; complementary to violin and CDF plots.](../figures/error_boxplot.pdf)

**Figure C.1:** Error boxplots by method.

## C.2 Error Maps

![All mapped grants with ground truth (black stars) and predictions; dashed lines indicate errors.](../analysis/mapping_workflow/contact_sheet.png)

**Figure C.2:** Contact sheet showing all mapped grants with ground truth (black stars) and predictions from six methods. Error distances are shown as dashed lines connecting predictions to ground truth. For cartographic clarity the H-2, H-3, and H-4 baselines are omitted; their substantially larger positional errors would require a map extent so broad that the fine-scale patterns of interest would be lost.

## C.3 Marginal Cost of High-Precision Accuracy

Table C.1 reports how many U.S. dollars each method requires to raise the ≤10 km hit-rate by one percentage point (column "Cost per +1 % ≤10 km hit").  This marginal-cost view complements the mean-error vs. cost Pareto plot in the main text: it quantifies the price of *high-confidence* geocoding rather than average error alone.

| Model | ≤10 km hit-rate | Cost per 1 k located (USD) | Cost per +1 % ≤10 km hit (USD) |
|---|---|---|---|
| o3-2025-04-16 (Ensemble) | 39.5 % | $195.65 | $4.95 |
| o3-2025-04-16 | 30.2 % | $127.46 | $4.22 |
| gpt-4o-2024-08-06 | 16.3 % | $1.05 | $0.06 |
| gpt-4.1-2025-04-14 | 18.6 % | $3.49 | $0.19 |
| o4-mini-2025-04-16 | 10.5 % | $10.69 | $1.02 |
| gpt-3.5-turbo | 4.7 % | $0.10 | $0.02 |
| o3-mini-2025-01-31 | 4.7 % | $14.15 | $3.04 |
| human-gis | 4.7 % | $3,255.81 | $700.00 |

**Table C.1:** Marginal cost per +1 percentage point gain in ≤10 km accuracy.

The numbers reveal why **gpt-4o-2024-08-06** is so attractive in budget-constrained settings: each percentage-point gain in "high-precision" accuracy costs only six cents—roughly two orders of magnitude cheaper than even the *o3* ensemble, and over 10,000 × cheaper than a professional GIS analyst.

## C.4 Latency-Accuracy Tradeoff

Processing time presents another critical dimension for evaluation. Figure C.3 shows how each method balances computational latency against geolocation accuracy. LLM methods cluster in the bottom-left quadrant, delivering results in seconds rather than minutes, while maintaining lower error rates than the professional GIS approach.

![Latency–accuracy scatter (seconds, log x‑axis vs mean error).](../figures/pareto_latency_tradeoff.pdf)

**Figure C.3:** Latency-Accuracy Tradeoff. This figure plots mean error (km) against processing time per grant (seconds) for each evaluated method. All automatic methods produce coordinates in 0.2–13 s of computation time, compared to the GIS analyst's labor time of ≈502 s per grant. Note the logarithmic scale on the x-axis.

