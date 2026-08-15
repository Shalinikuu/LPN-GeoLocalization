# MobileGeo Retrieval Project

Project: GPS-Denied UAV Visual Positioning System

## Current baseline

The existing custom checkpoint and model are labelled:

`AdvancedEdgeGeoLPN_LOCAL_REIMPLEMENTATION`

The existing SUES-200 result remains a smoke test until the
location-disjoint protocol is verified.

## Notebook order

1. Official MobileGeo release audit
2. Corrected SUES-200 location-disjoint benchmark
3. Common retrieval benchmark
4. Georeferenced project benchmark
5. Robustness and rejection experiments
6. Retrieval-aware keyframes and temporal consensus
7. Jetson Orin Nano deployment benchmark

## Important limitation

The retrieval subsystem returns Top-K map candidates for downstream
geometric verification. It must not publish a retrieved tile centre
as a verified UAV pose.
