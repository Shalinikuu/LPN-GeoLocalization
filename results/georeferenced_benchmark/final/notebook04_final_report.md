# Notebook 04 — Georeferenced Project Benchmark

## Status

**COMPLETE**

## Benchmark protocol

`PROJECT_DEFINED_VPS_LEAKAGE_SAFE_SCALE_CONTROLLED_RETRIEVAL`

- Core UAV queries: **2,331**
- Gallery per map scale: **2,331**
- Map scales: **700–1800 in steps of 100**
- Scale-controlled trials: **12**
- Total gallery records across trials: **27,972**
- 349 `val` samples were verified as exact duplicates of samples in the core partition and were excluded as an independent set.

## Model

**AdvancedEdgeGeoLPN_LOCAL_REIMPLEMENTATION**

- Provenance: `LOCAL_REIMPLEMENTATION`
- Descriptor dimension: 2048
- This is **not** an official MobileGeo VPS result.

## Macro retrieval results

- R@1: **0.0501%**
- R@5: **0.2109%**
- R@10: **0.4183%**
- mAP: **0.3938%**
- Mean positive rank: **1088.051**

## Random retrieval reference

- Random R@1: 0.0429%
- Random R@5: 0.2145%
- Random R@10: 0.4290%
- Random expected mAP/MRR: 0.3574%
- Random expected mean rank: 1166.000

## Diagnostic conclusion

- Descriptor collapse detected: **False**
- Positive beats random negative probability: **53.33%**

The descriptors are non-collapsed, but the zero-shot cross-domain retrieval signal is near chance. The local SUES-200-oriented reimplementation therefore does not meaningfully transfer zero-shot to this VPS retrieval domain.

## Reporting restrictions

- CRS: **UNVERIFIED**
- WGS84 is **not claimed**.
- Meter-level geodetic error is **not reported**.
- Retrieval output is **not verified UAV pose**.
- Dataset level token is not claimed as verified AGL or MSL.
- Runtime timings are Google Colab measurements, not Jetson Orin Nano deployment latency.
- Search timing measures similarity matrix + full sort only; descriptor extraction is excluded.