# LPN-GeoLocalization

### UAV-to-Satellite Image Geo-Localization for GPS-Denied Environments

A research-oriented framework for **UAV/drone image geo-localization** using visual matching between aerial queries and satellite imagery.

This project evaluates multiple visual geo-localization approaches under controlled and reproducible benchmark protocols, including location-disjoint evaluation, robustness analysis, temporal keyframe consensus, georeferenced evaluation, and deployment-oriented benchmarking.

---

## Overview

GPS-denied UAV navigation requires reliable visual localization when conventional GPS signals are unavailable or unreliable.

This project investigates **image-based geo-localization**, where a UAV image is matched against a satellite-image gallery to identify the most likely geographic location.

The repository contains the implementation, evaluation pipelines, benchmark results, analysis artifacts, notebooks, and deployment-oriented components developed during the project.

---

## Research Objectives

1. Evaluate visual geo-localization models under a common retrieval protocol.
2. Perform location-disjoint evaluation to reduce geographic leakage.
3. Compare different geo-localization approaches using consistent evaluation metrics.
4. Analyze model robustness under image corruptions and varying conditions.
5. Investigate temporal keyframe aggregation for UAV image sequences.
6. Evaluate performance across different satellite-gallery scales.
7. Study deployment considerations for edge hardware.
8. Maintain reproducible evaluation and provenance artifacts.

---

## Models Evaluated

- **MobileGeo**
- **Sample4Geo**
- **UltraVPR**
- **Advanced Edge GeoLPN**

Model-specific implementations are organized under:

```text
src/models/
```

Available adapters include:

```text
src/models/mobilegeo_adapter.py
src/models/sample4geo_adapter.py
src/models/ultravpr_adapter.py
src/models/advanced_edge_geolpn_adapter.py
```

---

## Key Features

- UAV-to-satellite image retrieval
- Location-disjoint benchmarking
- Common retrieval evaluation
- Georeferenced evaluation
- Multi-scale satellite-gallery evaluation
- Robustness and corruption analysis
- Rejection and confidence analysis
- Temporal keyframe subsampling
- Ordered-window temporal consensus
- Model comparison
- Result visualization
- Reproducibility and provenance tracking
- Edge deployment benchmarking
- Automated evaluation reports

---

## Project Structure

```text
LPN-GeoLocalization/
│
├── baseline_v1/
├── configs/
├── environment/
├── final_results_dashboard/
├── manifests/
├── notebooks/
├── rankings/
├── reports/
├── results/
├── src/
├── tests/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

### Main Directories

| Directory | Description |
|---|---|
| `src/` | Core source code and model adapters |
| `notebooks/` | Research and evaluation notebooks |
| `configs/` | Project and checkpoint configuration |
| `manifests/` | Dataset and evaluation manifests |
| `results/` | Benchmark results and analysis |
| `reports/` | Summaries and evaluation reports |
| `final_results_dashboard/` | Figures, tables and final result summaries |
| `environment/` | Environment and dependency snapshots |
| `baseline_v1/` | Baseline evaluation artifacts |
| `tests/` | Validation and testing utilities |

---

## Evaluation Pipeline

```text
UAV Images
    │
    ▼
Dataset Preparation
    │
    ▼
Feature Extraction
    │
    ▼
Satellite Gallery Construction
    │
    ▼
Visual Retrieval
    │
    ▼
Ranking Generation
    │
    ├── Location-Disjoint Benchmark
    ├── Georeferenced Benchmark
    ├── Robustness Analysis
    ├── Temporal Consensus
    └── Edge Deployment Evaluation
    │
    ▼
Reports & Visualizations
```

---

## Benchmarking

### Location-Disjoint Benchmark

Location-disjoint evaluation is used to reduce geographic overlap between reference and evaluation locations.

Related notebook:

```text
notebooks/02_sues200_location_disjoint_benchmark.ipynb
```

Results:

```text
results/sues200_corrected/
```

### Common Retrieval Benchmark

Different models are evaluated using a common retrieval protocol to enable consistent comparison.

Related notebook:

```text
notebooks/03_common_retrieval_benchmark.ipynb
```

Results:

```text
results/common_benchmark/
```

### Georeferenced Benchmark

The georeferenced evaluation investigates UAV-to-satellite retrieval using spatial metadata and multiple satellite-gallery scales.

Related notebook:

```text
notebooks/04_georeferenced_project_benchmark.ipynb
```

Results:

```text
results/georeferenced_benchmark/
```

### Robustness and Rejection Analysis

The project evaluates retrieval stability under image corruptions and analyzes confidence and rejection behavior.

Related notebook:

```text
notebooks/05_robustness_and_rejection.ipynb
```

Results:

```text
results/robustness_and_rejection/
```

### Temporal Keyframe Consensus

For UAV sequences, the project investigates temporal aggregation using keyframe subsampling and ordered query windows.

Related notebook:

```text
notebooks/06_keyframes_temporal_consensus.ipynb
```

Results:

```text
results/keyframes_temporal_consensus/
```

### Edge Deployment Benchmark

Deployment-oriented evaluation investigates running the localization pipeline on edge hardware, including an NVIDIA Jetson Orin Nano-oriented workflow.

Related notebook:

```text
notebooks/07_orin_nano_benchmark.ipynb
```

Results:

```text
results/orin_nano_benchmark/
```

---

## Results and Analysis

The repository contains a consolidated results dashboard with:

- Model comparison figures
- Retrieval performance tables
- Height-wise analysis
- Gallery-scale analysis
- Robustness analysis
- Temporal consensus results
- Example UAV and satellite images
- Deployment status
- Artifact indexes

Main dashboard:

```text
final_results_dashboard/
```

Project-level summary:

```text
final_results_dashboard/FINAL_PROJECT_RESULTS_SUMMARY.txt
```

---

## Research Notebooks

| Notebook | Purpose |
|---|---|
| `01_mobilegeo_official_release_audit.ipynb` | MobileGeo release and artifact audit |
| `02_sues200_location_disjoint_benchmark.ipynb` | Location-disjoint benchmark |
| `03_common_retrieval_benchmark.ipynb` | Common model retrieval evaluation |
| `04_georeferenced_project_benchmark.ipynb` | Georeferenced evaluation |
| `05_robustness_and_rejection.ipynb` | Robustness and rejection analysis |
| `06_keyframes_temporal_consensus.ipynb` | Temporal keyframe and consensus evaluation |
| `07_orin_nano_benchmark.ipynb` | Edge deployment benchmarking |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Shalinikuu/LPN-GeoLocalization.git
cd LPN-GeoLocalization
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Project configuration files are stored under:

```text
configs/
```

Before running experiments, update local dataset and checkpoint paths according to your environment.

Large datasets and model checkpoints are intentionally excluded from Git version control where appropriate.

---

## Running the Project

For notebook-based experiments:

```bash
jupyter notebook
```

Then open the required notebook from:

```text
notebooks/
```

The main application entry point is:

```text
app.py
```

---

## Source Code

Core reusable components are organized under:

```text
src/
```

### Dataset Utilities

```text
src/datasets/
```

Dataset manifests and split-validation utilities.

### Evaluation

```text
src/evaluation/
```

Retrieval metrics and evaluation utilities.

### Models

```text
src/models/
```

Model adapters for the evaluated geo-localization approaches.

### Retrieval

```text
src/retrieval/
```

Retrieval and ranking utilities.

### Reporting

```text
src/reporting/
```

Provenance and reporting utilities.

### Utilities

```text
src/utils/
```

Supporting utilities such as hashing.

---

## Reproducibility

The repository maintains:

- Environment snapshots
- Configuration files
- Dataset manifests
- Evaluation protocols
- Artifact hashes
- Audit reports
- Benchmark definitions
- Completion manifests
- Result tables

Relevant directories include:

```text
baseline_v1/
environment/
manifests/
reports/
results/
```

---

## Data and Checkpoints

Large datasets and trained model checkpoints are not stored in the repository when they are unsuitable for Git version control.

The `.gitignore` configuration excludes files such as:

```text
*.pth
*.pt
*.onnx
*.engine
*.npy
*.npz
*.zip
```

Datasets and large checkpoints should therefore be obtained separately and configured locally.

---

## Applications

The framework is relevant to:

- GPS-denied UAV navigation
- Drone localization
- Visual localization
- UAV-to-satellite image matching
- Aerial robotics
- Autonomous navigation
- Remote sensing
- Computer vision
- Visual place recognition

---

## Future Work

Potential future extensions include:

- Improved UAV-to-satellite domain adaptation
- More robust cross-view feature learning
- Sensor fusion with IMU information
- Visual-inertial localization
- Real-time UAV localization
- Larger-scale geographic evaluation
- Improved temporal aggregation
- Further edge-device optimization
- Lightweight deployment models

---

## Project Status

The repository contains the current implementation and evaluation artifacts for the research workflow, including benchmark notebooks, source modules, evaluation results, reports, visualizations, and deployment-oriented components.

Further experiments and improvements can be added as the research progresses.

---

## Citation

If this repository is used in academic or research work, please cite the corresponding project or paper when available.

```text
LPN-GeoLocalization
UAV-to-Satellite Image Geo-Localization for GPS-Denied Environments
```

---

## Acknowledgements

This project builds upon research in:

- Visual Geo-Localization
- Cross-View Image Retrieval
- UAV Navigation
- Visual Place Recognition
- Deep Learning
- Computer Vision
- Remote Sensing

The repository includes evaluation and comparison components based on existing geo-localization approaches and publicly available research resources.

---

## Author

**Shalini Kushwaha**

B.Tech Computer Science & Engineering — Artificial Intelligence & Machine Learning

GitHub:  
https://github.com/Shalinikuu

---

## Repository

**LPN-GeoLocalization**

```text
UAV Image
   ↓
Visual Feature Extraction
   ↓
Satellite Gallery
   ↓
Cross-View Retrieval
   ↓
Geographic Localization
```

A research-oriented framework for evaluating visual geo-localization approaches for UAV navigation in GPS-denied environments.
