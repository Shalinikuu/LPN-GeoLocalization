# Local Model vs Sample4Geo

## Protocol

- Queries: 8,000
- Gallery images: 40
- Split: `PROJECT_DEFINED_LOCATION_DISJOINT_60_20_20`
- Retrieval: exact cosine similarity

## Overall results

| Metric | Local reimplementation | Sample4Geo | Difference |
|---|---:|---:|---:|
| Recall@1 | 94.58% | 85.90% | 8.67 |
| Recall@5 | 99.99% | 98.74% | 1.25 |
| Recall@10 | 100.00% | 99.78% | 0.22 |
| mAP | 96.93% | 91.79% | 5.14 |

## Nominal-height comparison

| Height | Local R@1 | Sample4Geo R@1 | Difference | Local mAP | Sample4Geo mAP |
|---:|---:|---:|---:|---:|---:|
| 150 | 93.35% | 78.55% | 14.80 | 96.19% | 86.61% |
| 200 | 94.55% | 85.85% | 8.70 | 96.89% | 91.75% |
| 250 | 95.45% | 88.35% | 7.10 | 97.33% | 93.54% |
| 300 | 94.95% | 90.85% | 4.10 | 97.29% | 95.25% |

## Paired Top-1 outcomes

- Both correct: 6671
- Local only correct: 895
- Sample4Geo only correct: 201
- Both wrong: 233
- McNemar exact p-value: 6.077425559161068e-105

## Interpretation

The local reimplementation performs better on this particular
project-defined test split. This does not isolate architecture because
the checkpoints have different training datasets and training regimes.

Sample4Geo is evaluated as zero-shot transfer from University-1652.
The local model is not an official MobileGeo implementation.
