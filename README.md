# 🧠 PhysioMio Dataset

<div align="center">

![Dataset](https://img.shields.io/badge/Dataset-HD--sEMG-blue)
![Subjects](https://img.shields.io/badge/Subjects-48_Stroke_Patients-green)
![Gestures](https://img.shields.io/badge/Gestures-16_Hand_Movements-orange)
![License](https://img.shields.io/badge/License-DUA-yellow)

**PhysioMio: Bilateral and Longitudinal HD-sEMG Dataset of 16 Hand Gestures from
48 Stroke Patients**

[📄 Paper](#-paper) •
[📊 Download Data](#-download) •
[🚀 Getting Started](#-getting-started) •
[📖 Documentation](#-documentation)

</div>

---

## 🔬 Overview

The **PhysioMio dataset** provides comprehensive longitudinal and bilateral high-density
surface electromyography (HD-sEMG) recordings from stroke patients with
arm paresis. This unique dataset captures the neuromuscular patterns of both
healthy and impaired forearms during rehabilitation, offering unprecedented
insights into post-stroke motor recovery.

### ✨ Key Features

- 🏥 **48 stroke patients** with arm paresis
- 🤲 **16 distinct hand gestures** recorded per session
- 📅 **Longitudinal recordings** made during patients' stays in rehabilitation clinics
- 🔌 **64-electrode HD-sEMG array** for high-resolution muscle activity
- ⚖️ **Bilateral comparison** between healthy and impaired arms
- 📈 **Recovery progression** tracking across rehabilitation stages

---

## 📊 Dataset Statistics

| Metric | Value |
|--------|-------|
| **Participants** | 48 stroke patients |
| **Recording Sessions** | 1-2 healthy + 1-12 impaired per patient |
| **Gestures per Session** | 16 hand movements |
| **Electrodes** | 64-channel HD-sEMG array |
| **File Format** | Apache Parquet (.parquet) |
| **Comparison Data** | Healthy arm baseline |

---

## 🎯 Applications

This dataset is ideal for research in:

- 🧠 **Neuromuscular deficit analysis** in stroke patients
- 🔄 **Motor recovery pattern identification**
- 🤖 **Assistive technology development**
- 📊 **Personalized rehabilitation strategies**
- 🔬 **Comparative healthy vs. impaired arm studies**
- 🎯 **Machine learning for gesture recognition**

---

## 🚀 Getting Started

### Quick Start

```bash
pip install -r requirements.txt
jupyter-lab
```

Then open and run `technical_analysis.ipynb`.

### 📋 Prerequisites

- Tested with Python 3.11
- See `requirements.txt` for all Python dependencies to run the technical analysis

```bash
pip install -r requirements.txt
```

---

## 📖 Documentation

### 📁 Data Structure

```text
physiomio/
├── patient1/
│   ├── healthy_arm/      # Baseline recordings from healthy arm
│   │   ├── 01.parquet    # Session 1
│   │   └── 02.parquet    # Session 2
│   └── impaired_arm/     # Recordings from affected arm during rehabilitation
│       ├── 01.parquet    # Session 1
│       ├── 02.parquet    # Session 2
│       ├── ...           # Additional sessions
│       └── 12.parquet    # Session 12 (varies by patient)
├── patient2/
│   ├── healthy_arm/
│   └── impaired_arm/
└── ...                   # Additional patients (up to patient48)
```

The total number of files is 329. The dataset size is 4.4GB.

### 🔍 Data Format

- **File format**: `.parquet` (Apache Parquet)
- **Sampling rate**: 2048 Hz
- **Electrode layout**: 64-channel grid around forearm
- **Session structure**:
  - `healthy_arm/`: 1-2 baseline sessions from unaffected arm
  - `impaired_arm/`: Multiple sessions during rehabilitation
    (typically 1-12 sessions per patient)
  - Each session contains 16 continuous segments, i.e. recordings of a gesture,
    whereas the gesture is indicated in the column `movement_type`. The order
    of gestures is always the same. The first gesture is "Rest".

---

## 📄 Paper

> **TODO(aol-work)**: Update link once the paper has been accepted.

📖 **[Read the full paper](https://www.nature.com/sdata/)** *(Link to be updated)*

### 📝 Citation (to be updated)

> **TODO(aol-work)**: Update citation details once the paper has been accepted.

<!-- ```bibtex
@article{physiomio2025,
  title={PhysioMio: A Longitudinal HD-sEMG Dataset for Stroke Rehabilitation Research},
  author={[Julian Ilg, Alexander Oldemeier, Marie Fieweger, Luca Deuschel, Peter Rieckmann, Peter Young, Sabine Krause, Tim C. Lueth ]},
  journal={[Nature Datasets]},
  year={2025},
  doi={[DOI]}
}
``` -->

---

## 📊 Download

### 🤗 Hugging Face

[![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-Dataset-yellow)](https://huggingface.co/datasets/formove-ai/physiomio)

## 🤝 Contributing

- 🐛 **Bug reports**: [Open an issue](../../issues)

---

## 📜 License

This dataset is released under a [custom data usage agreement (LICENSE)](LICENSE.md).
Please cite our paper if you use this dataset in your research.

---

## 🏆 Acknowledgments

- 🏥 **Medical Team**:
  - InnKlinikum Altötting und Mühldorf, Germany
  - Medical Park Loipl, Bischofswiesen, Germany
  - Medical Park Bad Feilnbach Reithofpark, Bad Feilnbach, Germany
- 💰 **Funding**: This research was conducted in the context of the
  [START-interaktiv"physiomio"](https://www.interaktive-technologien.de/projekte/physiomio).
  The authors gratefully acknowledge the received funding from the German Federal
  Ministry of Education and Research for project 16SV9068 and from the German Federal
  Ministry for Economic Affairs and Energy for project 03EFBY0337, in which the
  presented study played a central role.
- 👥 **Participants**: All are indebted to all stroke patients who contributed
  to this research over the course of their rehabilitation stay

---

<div align="center">

[⭐ Star this repo](../../stargazers) •
[🍴 Fork it](../../fork) •

</div>
