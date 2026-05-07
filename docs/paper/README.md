# Paper

This directory contains the paper version of the project.

- [`Choi.J_KCC2026_260430.pdf`](Choi.J_KCC2026_260430.pdf)
- [`Choi.J_KCC2026_260430.docx`](Choi.J_KCC2026_260430.docx)

## Title

**Real-Time Nozzle Clogging Detection in 3D Printers Using Multivariate Time-Series Sensor Data**

Korean title:

**다변량 시계열 센서 데이터를 활용한 3D 프린터 실시간 노즐 막힘 탐지**

## Paper-backed summary

The paper proposes a low-cost IoT-based real-time nozzle clogging monitoring structure for FDM 3D printers. The system combines air-quality sensors, temperature/humidity sensing, printer metadata, a closed-loop enclosure structure, and 60-second multivariate time-series windows.

Reported results from the final paper:

| Metric | Value |
|---|---:|
| Dataset size | 605,622 samples |
| Normal samples | 412,418 |
| Clogging samples | 193,204 |
| Accuracy | 0.951085 |
| Precision | 0.946218 |
| Recall | 0.999913 |
| F1-score | 0.972325 |
| ROC AUC | 0.975934 |
| Early warning lead time | 472 seconds |

Important interpretation: the labels are generated from a TVOC_diff persistence rule, so the result should be read as evidence that the model can reproduce the defined abnormal emission pattern with high sensitivity. The paper explicitly notes that some normal samples are misclassified as clogging, so the current system is better framed as a conservative early-warning prototype rather than a finished balanced classifier.
