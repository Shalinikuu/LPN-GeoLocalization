# Notebook 05 — Robustness and Rejection

## Status

**COMPLETE**

## Model

**AdvancedEdgeGeoLPN_LOCAL_REIMPLEMENTATION**

- Provenance: `LOCAL_REIMPLEMENTATION`
- Not an official MobileGeo robustness result.

## Clean baseline limitation

The source VPS retrieval benchmark is near chance. Across 27,972 query-scale trials, only 14 were true Top-1 successes.

Therefore conventional accuracy-degradation under corruption is not used as the primary robustness claim.

## Corruption suite

- Gaussian blur: mild / strong
- Brightness reduction: mild / strong
- Contrast reduction: mild / strong
- JPEG degradation: mild / strong
- Gaussian noise: mild / strong

All five corruption families showed greater descriptor perturbation at strong severity than at mild severity.

## Descriptor stability

- Most stable condition by mean clean-to-corrupted descriptor cosine: **jpeg_mild** (0.94382)
- Least stable condition by mean clean-to-corrupted descriptor cosine: **brightness_strong** (0.24927)

## Top-1 identity stability

- Highest clean-to-corrupted Top-1 identity stability: **jpeg_mild**, 47.58%
- Lowest clean-to-corrupted Top-1 identity stability: **brightness_strong**, 2.29%

## Confidence / rejection diagnostic

- Raw Top-1 similarity produced >1x identity-stability lift at 10% coverage in only **2/10** conditions.
- Top1-Top2 margin produced >1x identity-stability lift at 10% coverage in **10/10** conditions.
- Mean Top1-Top2 margin stability lift at 10% coverage: **2.281x**.
- Minimum margin lift across conditions: **1.705x**.
- Maximum margin lift across conditions: **3.065x**.

This margin result indicates descriptive enrichment of clean-to-corrupted Top-1 identity stability only. It does not demonstrate true localization correctness.

## Rejection limitation

A validated correctness-based rejection threshold cannot be calibrated because the clean benchmark contains only 14 true Top-1 successes.

- Validated deployment rejection threshold: **No**
- Accuracy-degradation primary claim: **Not allowed**

## Reporting constraints

- CRS: **UNVERIFIED**
- WGS84: **not claimed**
- Meter-level geodetic error: **not reported**
- Retrieval output: **not verified UAV pose**
- Nominal dataset level token: not verified as AGL or MSL
- Runtime measurements: Google Colab, not Jetson Orin Nano deployment latency