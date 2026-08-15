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
├── tests/
│   └── Unit tests for project components
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
Evaluation Protocols

The repository contains several evaluation stages.

1. Official Release Audit

The MobileGeo release is examined for:

Dataset assets
Pre-computed features
Repository provenance
Released artifacts
Source-code evidence

Results are stored under:

results/mobilegeo_audit/
2. Location-Disjoint Evaluation

A location-disjoint protocol is used to reduce geographic overlap between training/reference data and evaluation locations.

The SUES-200 evaluation artifacts are available under:

results/sues200_corrected/

This includes:

Query results
Retrieval rankings
Location-level metrics
Height-wise analysis
Failure analysis
Confusion analysis
Evaluation manifests
3. Common Retrieval Benchmark

Multiple models are evaluated using a common retrieval protocol.

Results are available under:

results/common_benchmark/

The benchmark includes:

MobileGeo
Sample4Geo
UltraVPR
Local model evaluation
4. Georeferenced Evaluation

The project also evaluates visual retrieval using georeferenced imagery.

Artifacts are stored under:

results/georeferenced_benchmark/

This includes:

Geospatial metadata inspection
Gallery/query manifests
Scale-based evaluation
Retrieval rankings
Per-site metrics
Georeferencing validation
5. Robustness Analysis

The framework evaluates retrieval stability under image corruption and confidence-based rejection.

Results are available under:

results/robustness_and_rejection/

The analysis includes:

Descriptor stability
Retrieval stability
Corruption experiments
Confidence analysis
Correctness-coverage curves
Rejection analysis
6. Temporal Keyframe Consensus

For UAV image sequences, temporal information is investigated using keyframe selection and ordered-window aggregation.

Results are stored under:

results/keyframes_temporal_consensus/

The analysis includes:

Keyframe subsampling
Ordered query windows
Temporal consensus
Retrieval performance across scales
7. Edge Deployment Benchmark

Deployment-oriented evaluation is included for NVIDIA Jetson Orin Nano environments.

Relevant artifacts are available under:

results/orin_nano_benchmark/

These include:

Deployment protocols
Model validation
Environment checks
Benchmark scripts
Results Dashboard

A consolidated project dashboard is provided in:

final_results_dashboard/

It contains:

Model comparison figures
Dataset examples
Retrieval visualizations
Robustness plots
Keyframe analysis
Summary tables
Deployment status
Important artifact index

The main project summary is:

final_results_dashboard/FINAL_PROJECT_RESULTS_SUMMARY.txt
Source Code

Core implementation is organized into modular components:

src/
├── datasets/
├── deployment/
├── evaluation/
├── models/
├── reporting/
├── retrieval/
└── utils/
Model Adapters
src/models/

contains the model-specific adapters used by the evaluation framework.

Evaluation
src/evaluation/

contains evaluation metrics and latency-related utilities.

Retrieval
src/retrieval/

contains retrieval and ranking utilities.

Dataset Utilities
src/datasets/

contains dataset manifest and split-validation utilities.

Installation

Clone the repository:

git clone https://github.com/Shalinikuu/LPN-GeoLocalization.git
cd LPN-GeoLocalization

Create a Python environment:

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt
Running the Application

The repository contains an application entry point:

app.py

Run it using:

python app.py
Reproducibility

The project maintains reproducibility through:

Configuration files
Dataset manifests
Environment snapshots
Evaluation protocols
Artifact hashes
Provenance records
Structured result directories
Benchmark completion manifests

These artifacts allow experiments and evaluation stages to be traced and reviewed systematically.

Dataset

The repository contains dataset-related manifests and selected project assets.

Large datasets, pretrained checkpoints, and other large binary artifacts are not included in the repository unless explicitly provided.

Dataset paths should be configured through the files under:

configs/
Model Checkpoints

Large model checkpoints are intentionally excluded from Git tracking.

For example:

*.pth
*.pt

are ignored through .gitignore.

Users should provide the required checkpoints locally and configure their paths using the appropriate files under:

configs/
Important Notes

This repository is primarily intended for:

Research evaluation
Reproducible experimentation
UAV-to-satellite retrieval research
Visual geo-localization benchmarking
Deployment-oriented investigation

Results should be interpreted according to the evaluation protocol associated with each experiment.

Project Status

The repository contains evaluation artifacts, benchmark results, analysis notebooks, source modules, and deployment-oriented evaluation components.

Further work can include:

Improved UAV-to-satellite retrieval models
Larger-scale evaluation
Additional datasets
Improved temporal aggregation
Real-world GPS-denied flight experiments
Further edge-device optimization
License

Please refer to the repository and individual third-party model implementations for their respective licensing and usage requirements.

Acknowledgements

This project builds upon research and publicly available resources in the field of visual geo-localization, UAV navigation, image retrieval, and satellite imagery.

All third-party models, datasets, and repositories should be used according to their respective licenses and attribution requirements.

Author

Shalini Kushwaha

GitHub: https://github.com/Shalinikuu

