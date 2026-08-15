# Phase 2 — Corrected SUES-200 Benchmark

## Provenance

- Model: `AdvancedEdgeGeoLPN_LOCAL_REIMPLEMENTATION`
- Provenance label: `LOCAL_REIMPLEMENTATION`
- Protocol: `PROJECT_DEFINED_LOCATION_DISJOINT_60_20_20`
- Official MobileGeo result: No
- Official SUES-200 protocol: No
- Task measured: drone-to-satellite image retrieval
- Verified geographic UAV pose: No

## Split

- Training locations: 120
- Validation locations: 40
- Test locations: 40
- Test drone queries: 8,000
- Test satellite gallery images: 40
- Train/test location overlap: 0
- Validation/test location overlap: 0

## Overall results

- Recall@1: 94.58%
- Recall@5: 99.99%
- Recall@10: 100.00%
- mAP: 96.93%
- Mean positive rank: 1.082

## Results by nominal height

| Nominal height | Queries | R@1 | R@5 | R@10 | mAP |
|---:|---:|---:|---:|---:|---:|
| 150 | 2000 | 93.35% | 99.95% | 100.00% | 96.19% |
| 200 | 2000 | 94.55% | 100.00% | 100.00% | 96.89% |
| 250 | 2000 | 95.45% | 100.00% | 100.00% | 97.33% |
| 300 | 2000 | 94.95% | 100.00% | 100.00% | 97.29% |

The height values are dataset folder labels and are not verified
as AGL or MSL altitude.

## Failure analysis

- Top-1 correct queries: 7,566
- Top-1 failures: 434
- Maximum positive rank: 6
- Weakest nominal height: 150
- Location 0071: 0% Recall@1
- Location 0007: 26.50% Recall@1

## Worst test locations

| Location | Queries | Failures | R@1 | Mean positive rank | Maximum rank |
|---|---:|---:|---:|---:|---:|
| 0071 | 200 | 200 | 0.00% | 2.000 | 2 |
| 0007 | 200 | 147 | 26.50% | 2.790 | 5 |
| 0088 | 200 | 17 | 91.50% | 1.085 | 2 |
| 0063 | 200 | 14 | 93.00% | 1.070 | 2 |
| 0155 | 200 | 12 | 94.00% | 1.060 | 2 |
| 0151 | 200 | 11 | 94.50% | 1.055 | 2 |
| 0169 | 200 | 8 | 96.00% | 1.095 | 6 |
| 0057 | 200 | 5 | 97.50% | 1.030 | 3 |
| 0027 | 200 | 4 | 98.00% | 1.020 | 2 |
| 0002 | 200 | 3 | 98.50% | 1.015 | 2 |

## Dominant confusion pairs

| Query location | Predicted location | Count | Mean margin | Maximum positive rank |
|---|---|---:|---:|---:|
| 0071 | 0058 | 200 | 0.000000 | 2 |
| 0007 | 0058 | 91 | 0.000000 | 5 |
| 0007 | 0008 | 56 | 0.051325 | 5 |
| 0088 | 0152 | 17 | 0.023337 | 2 |
| 0063 | 0056 | 14 | 0.039807 | 2 |
| 0155 | 0144 | 12 | 0.060402 | 2 |
| 0151 | 0186 | 11 | 0.067482 | 2 |
| 0057 | 0164 | 5 | 0.113171 | 3 |
| 0027 | 0140 | 4 | 0.068653 | 2 |
| 0169 | 0144 | 4 | 0.076157 | 5 |

## Confidence-margin result

Using a Top-1/Top-2 margin threshold of
`0.050`:

- Coverage: 90.79%
- Accepted Top-1 accuracy:
  99.33%
- Ambiguous queries:
  737

This is an experimental ambiguity threshold. It is not yet a
calibrated probability or an out-of-map rejection model.

## Timing interpretation

The recorded descriptor extraction used batched GPU inference.
It is not a batch-one Jetson Orin Nano deployment result.

Google Drive image decoding and loading dominated the recorded
end-to-end extraction time.

## Reporting restrictions

This result must not be described as:

- an official MobileGeo result
- an official SUES-200 benchmark result
- verified geographic positioning
- verified UAV pose
- deployment latency on Jetson Orin Nano

## Next phase

Run the common retrieval benchmark comparing reproducible
backends under one evaluator.
