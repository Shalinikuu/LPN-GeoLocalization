# Phase 3 — Common Retrieval Benchmark

## Protocol

- Test queries: 8,000
- Gallery images: 40
- Held-out test locations: 40
- Nominal dataset height labels: 150, 200, 250, 300
- Retrieval: exact cosine similarity
- Descriptor normalization: L2
- Benchmark: `PROJECT_DEFINED_LOCATION_DISJOINT_60_20_20`

## Direct common benchmark

| Method | Descriptor dim | R@1 | R@5 | R@10 | mAP | Mean positive rank |
|---|---:|---:|---:|---:|---:|---:|
| AdvancedEdgeGeoLPN_LOCAL_REIMPLEMENTATION | 2048 | 94.58% | 99.99% | 100.00% | 96.93% | 1.082 |
| Sample4Geo | 1024 | 85.90% | 98.74% | 99.78% | 91.79% | 1.274 |
| UltraVPR | 256 | 81.94% | 95.22% | 98.47% | 87.83% | 1.667 |

Best Recall@1 on this project-defined protocol:
**AdvancedEdgeGeoLPN_LOCAL_REIMPLEMENTATION — 94.58%**

## Recall@1 by nominal height

| Height | Local reimplementation | Sample4Geo | UltraVPR |
|---:|---:|---:|---:|
| 150 | 93.35% | 78.55% | 56.35% |
| 200 | 94.55% | 85.85% | 83.15% |
| 250 | 95.45% | 88.35% | 93.85% |
| 300 | 94.95% | 90.85% | 94.40% |

The height values are dataset folder labels and are not verified
as AGL or MSL altitude.

## Pairwise differences

- Local minus Sample4Geo R@1:
  8.67 percentage points
- Local minus UltraVPR R@1:
  12.64 percentage points
- Sample4Geo minus UltraVPR R@1:
  3.96 percentage points

## Three-method paired query analysis

- All three correct:
  5735
- All three wrong:
  216
- Local only correct:
  273
- Sample4Geo only correct:
  20
- UltraVPR only correct:
  17
- At least one method correct:
  7784
- All three produced the same Top-1 prediction:
  5873

## Provenance

### AdvancedEdgeGeoLPN local reimplementation

`LOCAL_REIMPLEMENTATION`

This method must not be described as official MobileGeo.

### Sample4Geo

Official Sample4Geo University-1652 checkpoint evaluated as zero-shot
transfer on the project-defined SUES-200 test split.

This is not an official Sample4Geo SUES-200 result.

### UltraVPR

Official UltraVPR checkpoint evaluated as zero-shot transfer on the
project-defined SUES-200 test split.

This is not an official UltraVPR SUES-200 result.

## MobileGeo release status

MobileGeo is not included in the direct common accuracy ranking.

The released MobileGeo artifacts support published precomputed-feature
evaluation with 768-D MAT descriptors, but a verified official checkpoint
and complete raw-image-to-descriptor pipeline were not available for
generating descriptors on the exact same 8,000-query / 40-gallery split.

Therefore the MobileGeo published MAT results must remain a separate
provenance result and must not be ranked directly against the three
methods above.

## Interpretation restriction

The three directly compared methods use the same test queries, gallery
and evaluator, but their checkpoints have different training regimes.
The observed accuracy differences therefore do not isolate architecture
alone.

Image retrieval performance is not equivalent to verified geographic
UAV pose estimation.
