
# Context-Specific Metabolic Modelling of Human Liver Using iMAT

## 1. Project Overview

This project investigates the integration of human liver gene-expression data with a genome-scale metabolic network to predict tissue-specific metabolic activity.

The iMAT (Integrative Metabolic Analysis Tool) algorithm is used to integrate gene-expression information from the GTEx dataset with the Human-GEM metabolic reconstruction.

A sensitivity analysis is performed using two gene-expression thresholds: 10% and 15%.

## 2. Research Question

Can gene-expression information from human liver tissue be integrated with a genome-scale metabolic network using iMAT to predict tissue-specific metabolic activity?

## 3. Objectives

- Integrate human liver gene-expression data with a genome-scale metabolic model.
- Apply the iMAT algorithm to predict metabolic reaction activity.
- Investigate the effect of different gene-expression thresholds.
- Compare predicted reaction flux distributions.
- Identify metabolic subsystems associated with major flux differences.

## 4. Datasets and Model

### Gene-expression dataset
- Source: GTEx Portal
- Version: V11
- Data: Gene median TPM expression
- Tissue: Liver

### Metabolic model
- Model: Human-GEM
- Version: 1.19.0
- Format: SBML (XML)

## 5. Methodology

The project follows these steps:

1. Load GTEx liver gene-expression data.
2. Remove Ensembl gene ID version suffixes.
3. Match GTEx genes with Human-GEM genes.
4. Calculate low- and high-expression thresholds.
5. Assign gene weights:
   - Low expression: -1
   - Intermediate expression: 0
   - High expression: +1
6. Convert gene weights into reaction weights using gene-protein-reaction rules.
7. Construct the iMAT optimisation model.
8. Export the optimisation model in LP format.
9. Optimise using SCIP through PySCIPOpt.
10. Extract reaction fluxes and validate the predicted flux distribution.
11. Compare the 10% and 15% threshold results.

### Sensitivity analysis

Two threshold settings were investigated:

- 10%: 10th and 90th percentiles.
- 15%: 15th and 85th percentiles.

## 6. Software and Tools

- Python
- Google Colab
- COBRApy
- iMATpy
- PySCIPOpt
- SCIP
- Pandas
- NumPy
- Matplotlib

## 7. Results

### Reaction classification

| Reaction weight | 10% threshold | 15% threshold |
|---|---:|---:|
| Low (-1) | 214 | 313 |
| Intermediate (0) | 10,619 | 9,576 |
| High (+1) | 2,138 | 3,082 |
| Total reactions | 12,971 | 12,971 |

### Optimisation results

| Metric | 10% threshold | 15% threshold |
|---|---:|---:|
| Best objective value | 2,053 | 3,021 |
| Solver status | Optimal | Time limit |
| Feasible solutions found | 100 | 100 |
| Optimality gap | 0.0 | 0.1324% |

The 10% model reached an optimal solution. The 15% model produced a feasible solution with a small remaining optimality gap; global optimality was not proven.

### Flux comparison

- Total reactions compared: 12,971
- Reactions with changed flux: 4,628
- Reactions with direction changes: 374
- Mean absolute flux difference: 73.12

### Flux validation

Both threshold models were checked for flux-bound violations and mass-balance consistency.

| Validation metric | 10% | 15% |
|---|---:|---:|
| Bound violations | 0 | 0 |
| Maximum mass-balance residual | 7.09 × 10⁻¹² | 1.03 × 10⁻¹⁰ |
| Metabolites with residual > 10⁻⁶ | 0 | 0 |

### Visualisations

The results folder contains:
- Flux comparison scatter plot.
- Distribution of flux differences.
- Metabolic subsystem distribution of changing reactions.

## 8. Project Structure

```text
iMAT-Human-Tissue-Project/
│
├── data/
│   ├── GTEx_Analysis_...gct.gz
│   └── Human-GEM.xml (download separately)
│
├── notebooks/
│   └── iMAT_Human_Tissue_Project.ipynb
│
├── results/
│   ├── liver_iMAT_fluxes_10.csv
│   ├── liver_iMAT_fluxes_15.csv
│   ├── liver_iMAT_validation_10.csv
│   ├── liver_iMAT_validation_15.csv
│   ├── iMAT_sensitivity_comparison.csv
│   ├── iMAT_flux_comparison_10_vs_15.csv
│   └── visualisation files
│
├── scripts/
│   ├── check_gene_matching.py
│   ├── download_data.py
│   ├── prepare_imat.py
│   ├── run_imat.py
│   └── test_data.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## 9. Installation and Reproducibility

### Step 1: Clone the repository

```bash
git clone https://github.com/sridevir872-cloud/iMAT-Human-Tissue-Project.git
cd iMAT-Human-Tissue-Project
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Download the datasets

```bash
python scripts/download_data.py
```

The download script retrieves any missing input datasets, including the Human-GEM model.

### Step 4: Run the analysis

Open the notebook:

`notebooks/iMAT_Human_Tissue_Project.ipynb`

The complete optimisation workflow was executed in Google Colab using SCIP through PySCIPOpt.

The Python scripts provide supporting data preparation and project utilities. Refer to the notebook for the complete recorded analysis and results.

## 10. Limitations

- Predicted reaction fluxes are computational model outputs, not experimentally measured metabolic rates.
- Results depend on gene-expression thresholds and gene-protein-reaction relationships.
- The 15% optimisation reached a feasible solution but did not prove global optimality within the time limit.
- Several predicted fluxes reached reaction bounds, so boundary-associated flux predictions require cautious interpretation.
- Gene expression does not necessarily correspond directly to enzyme abundance or metabolic activity.

## 11. Reference

Shlomi, T., Cabili, M. N., Herrgård, M. J., Palsson, B. Ø., & Ruppin, E. (2008).

Network-based prediction of human tissue-specific metabolism.

*Nature Biotechnology*, 26, 1003–1010.

https://doi.org/10.1038/nbt.1487

