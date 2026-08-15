# Notebook 06 — Keyframes and Ordered-Sequence Consensus

## Status

**COMPLETE**

## Model

**AdvancedEdgeGeoLPN_LOCAL_REIMPLEMENTATION**

- Provenance: `LOCAL_REIMPLEMENTATION`
- Not an official MobileGeo result.

## Ordered sequence structure

- Queries: 2,331
- Ordered groups: 12
- Adjacent ordered pairs: 2,319
- Exact +1 sequence pairs: 2,319 (100%)
- Sequence gaps: 0
- Duplicate sequence tokens: 0

The ordering is supported by dataset sample-name structure only. It is not verified timestamp or video-frame timing.

## Keyframe subsampling

- Stride 1: 2331 queries, processing fraction 100.00%
- Stride 2: 1167 queries, processing fraction 50.06%
- Stride 5: 468 queries, processing fraction 20.08%
- Stride 10: 234 queries, processing fraction 10.04%

Processing fractions are count-based only. No subsampled deployment latency was measured.

## L=1 reproduction audit

- Exact Top-k success counts preserved at every scale.
- Maximum metric difference: 6.831e-10
- Maximum equivalent rank-sum difference: 2.000000 positions per 2,331-query scale.
- Tie-aware baseline reproduction: **PASS**

## Ordered-window consensus

- L=1: mAP 0.3938%, normalized rank gain 6.69%
- L=3: mAP 0.4063%, normalized rank gain 7.84%
- L=5: mAP 0.4153%, normalized rank gain 8.05%
- L=9: mAP 0.4018%, normalized rank gain 7.71%

**Best tested multi-sample window: L=5**, for both mAP excess over chance and normalized rank gain.

This is descriptive ordered-sequence retrieval improvement only. The single-query clean baseline remains near chance.

## Reporting constraints

- Verified timestamps: **No**
- Verified FPS: **No**
- Verified fixed sample interval: **No**
- Verified temporal velocity: **No**
- CRS: **UNVERIFIED**
- WGS84: **not claimed**
- Meter-level motion/error: **not reported**
- Retrieval output: **not verified UAV pose**
- Nominal level token: **not verified AGL/MSL**
- Colab timing must not be reported as Jetson Orin Nano deployment latency.