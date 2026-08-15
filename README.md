# LPN-GeoLocalization

### UAV-to-Satellite Image Geo-Localization for GPS-Denied Environments

A research-oriented framework for UAV/drone image geo-localization using visual matching between aerial queries and satellite imagery.

This project evaluates multiple visual geo-localization approaches under controlled and reproducible benchmark protocols, including location-disjoint evaluation, robustness analysis, temporal keyframe consensus, georeferenced evaluation, and deployment-oriented benchmarking.

---

## Overview

GPS-denied UAV navigation requires reliable visual localization when conventional GPS signals are unavailable or unreliable.

This project investigates image-based geo-localization, where a UAV image is matched against a satellite-image gallery to identify the most likely geographic location.

The repository provides:

- Reproducible evaluation protocols
- Multiple geo-localization model adapters
- UAV-to-satellite retrieval pipelines
- Location-disjoint benchmarking
- Robustness and rejection analysis
- Temporal keyframe consensus
- Georeferenced evaluation
- Deployment-oriented benchmarking
- Result analysis and visualization
- Provenance and audit artifacts

---

## Research Objectives

The main objectives of this project are:

1. Evaluate visual geo-localization models under a common retrieval protocol.
2. Perform location-disjoint evaluation to reduce geographic leakage.
3. Compare different geo-localization approaches using consistent metrics.
4. Analyze model robustness under image corruptions and varying conditions.
5. Investigate temporal keyframe aggregation for UAV sequences.
6. Evaluate performance across different satellite-gallery scales.
7. Study deployment considerations for edge hardware.
8. Maintain reproducible evaluation and provenance artifacts.

---

## Models Evaluated

The project provides adapters and evaluation support for multiple visual geo-localization approaches:

- **MobileGeo**
- **Sample4Geo**
- **UltraVPR**
- **Advanced Edge GeoLPN**

Model-specific implementations are organized under:

src/models/

- advanced_edge_geolpn_adapter.py
- base_adapter.py
- mobilegeo_adapter.py
- sample4geo_adapter.py
- ultravpr_adapter.py

---

## Repository Structure

```text
LPN-GeoLocalization/
│
├── baseline_v1/
│   └── Baseline evaluation artifacts
│
├── configs/
│   └── Project and model configuration files
│
├── environment/
│   └── Environment and dependency information
│
├── final_results_dashboard/
│   ├── figures/
│   ├── sample_images/
│   ├── tables/
│   └── video_index/
│
├── manifests/
│   └── Dataset and evaluation manifests
│
├── notebooks/
│   ├── 01_mobilegeo_official_release_audit.ipynb
│   ├── 02_sues200_location_disjoint_benchmark.ipynb
│   ├── 03_common_retrieval_benchmark.ipynb
│   ├── 04_georeferenced_project_benchmark.ipynb
│   ├── 05_robustness_and_rejection.ipynb
│   ├── 06_keyframes_temporal_consensus.ipynb
│   └── 07_orin_nano_benchmark.ipynb
│
├── rankings/
│   └── Ranking templates and retrieval outputs
│
├── reports/
│   └── Evaluation reports and provenance records
│
├── results/
│   ├── common_benchmark/
│   ├── georeferenced_benchmark/
│   ├── keyframes_temporal_consensus/
│   ├── mobilegeo_audit/
│   ├── orin_nano_benchmark/
│   ├── robustness_and_rejection/
│   └── sues200_corrected/
│
├── src/
│   ├── datasets/
│   ├── deployment/
│   ├── evaluation/
│   ├── models/
│   ├── reporting/
│   ├── retrieval/
│   └── utils/
│
├── tests/
│   └── Unit tests for project components
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
