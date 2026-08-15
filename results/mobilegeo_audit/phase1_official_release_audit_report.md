# MobileGeo Phase 1 Official Release Audit

## Final supported provenance

`PUBLISHED_PRECOMPUTED_FEATURE_EVALUATION`

## What was reproduced

The released MobileGeo `.mat` descriptor files were validated
and evaluated using direct dot-product retrieval consistent with
the released `Tools/evaluate_norm.py` evaluator.

## Evaluated assets

| Asset | Queries | Gallery | Descriptor dimension | R@1 | R@5 | R@10 | mAP |
|---|---:|---:|---:|---:|---:|---:|---:|
| second_D2S.mat | 37854 | 951 | 768 | 93.95% | 98.02% | 98.57% | 95.83% |
| second_S2D.mat | 701 | 51354 | 768 | 95.72% | 97.15% | 97.43% | 92.63% |

## What was not reproduced

- Raw-image MobileGeo inference
- An official trained MobileGeo checkpoint
- A complete query/gallery image-preprocessing pipeline
- MobileGeo training
- AGX Orin runtime results
- Jetson Orin Nano runtime results

## Repository findings

- Two valid evaluator-compatible `.mat` files were released.
- The evaluator requires `query_f`, `query_label`,
  `gallery_f`, and `gallery_label`.
- The released descriptors have dimension 768.
- The MobileGeo weights link in the current README is empty.
- Generic ConvNeXt pretrained backbone URLs are not
  MobileGeo model checkpoints.
- No repository licence file was verified.
- `README.md~` contains older PFED documentation and was
  treated only as repository-history evidence.

## Reporting restriction

These metrics must be labelled:

`PUBLISHED_PRECOMPUTED_FEATURE_EVALUATION`

They must not be labelled:

- `OFFICIAL_CHECKPOINT_REPRODUCTION`
- raw-image inference
- verified GPS-denied positioning
- verified global UAV pose

## Phase 1 decision

Phase 1 is complete at the strongest provenance supported by
the released evidence.

## Next phase

Create and validate the corrected SUES-200 location-disjoint
benchmark in:

`02_sues200_location_disjoint_benchmark.ipynb`
