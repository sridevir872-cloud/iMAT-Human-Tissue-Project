# Human Liver Metabolic Modelling Using iMAT

## 1. Project Overview

In this project, I studied how gene expression data can be used to understand the metabolic activities of the human liver.

Different tissues in our body perform different functions. Because of this, their metabolic activities are also different. The main idea of this project is to use gene-expression information to predict which metabolic reactions may be active or inactive in the liver.

For this, I used the iMAT method along with the GTEx gene-expression dataset and the Human-GEM metabolic model.

I also compared two different expression thresholds, 10% and 15%, to see how changing the threshold affects the predicted results.

## 2. Research Question

Can gene-expression information from human liver tissue be combined with a genome-scale metabolic network using iMAT to predict metabolic activity?

## 3. Objectives

- To use human liver gene-expression data for metabolic modelling.
- To connect gene-expression information with metabolic reactions.
- To use iMAT to predict the activity of metabolic reactions.
- To compare the results obtained using 10% and 15% thresholds.
- To understand how changing the threshold affects the predicted metabolic fluxes.
- To study which metabolic subsystems show changes in their reactions.

## 4. Data Used

### Gene-expression data

- Source: GTEx Portal
- Version: V11
- Data type: Gene median TPM
- Tissue selected: Liver

### Metabolic model

- Model: Human-GEM
- Version: 1.19.0
- File format: SBML (XML)

The GTEx dataset provides gene-expression values, while Human-GEM provides the metabolic reactions and their relationships with genes.

## 5. Methodology

I followed these steps to complete the project:

1. Loaded the GTEx gene-expression dataset and selected the liver tissue data.
2. Loaded the Human-GEM metabolic model.
3. Matched the gene IDs from GTEx with the gene IDs present in Human-GEM.
4. Divided the genes into low, intermediate and high expression groups.
5. Assigned weights to the genes:
   - Low expression = -1
   - Intermediate expression = 0
   - High expression = +1
6. Converted the gene weights into reaction weights using gene-protein-reaction relationships.
7. Prepared the iMAT optimisation model.
8. Used SCIP to solve the optimisation problem.
9. Extracted the predicted reaction fluxes.
10. Checked whether the predicted fluxes followed the reaction boundaries and mass-balance conditions.
11. Compared the results from the two thresholds.

### Threshold comparison

I used two different settings:

- **10% threshold:** 10th and 90th percentiles.
- **15% threshold:** 15th and 85th percentiles.

This comparison helped me understand how different expression cutoffs can change the reaction predictions.

## 6. Software and Tools Used

- Python
- Google Colab
- COBRApy
- iMATpy
- PySCIPOpt
- SCIP
- Pandas
- NumPy
- Matplotlib

## 7. Results and Observations

### Reaction classification

After converting the gene-expression values into reaction weights, the following reaction counts were obtained:

| Reaction category | 10% threshold | 15% threshold |
|---|---:|---:|
| Low (-1) | 214 | 313 |
| Intermediate (0) | 10,619 | 9,576 |
| High (+1) | 2,138 | 3,082 |
| **Total** | **12,971** | **12,971** |

From this comparison, I observed that the number of high- and low-expression reactions changed when the threshold was changed.

### Optimisation results

| Metric | 10% threshold | 15% threshold |
|---|---:|---:|
| Best objective value | 2,053 | 3,021 |
| Solver status | Optimal | Time limit |
| Feasible solutions found | 100 | 100 |
| Optimality gap | 0.0 | 0.1324% |

The 10% model reached an optimal solution. The 15% model found a feasible solution within the given time, but the solver did not prove that it was globally optimal.

### Flux comparison

The predicted fluxes from both threshold settings were compared.

- Total reactions compared: 12,971
- Reactions with changed flux: 4,628
- Reactions with direction changes: 374
- Mean absolute flux difference: 73.12

This shows that changing the gene-expression threshold can affect the predicted metabolic flux distribution.

### Flux validation

I also checked whether the predicted fluxes satisfied the model constraints.

| Validation metric | 10% threshold | 15% threshold |
|---|---:|---:|
| Bound violations | 0 | 0 |
| Maximum mass-balance residual | 7.09 × 10⁻¹² | 1.03 × 10⁻¹⁰ |
| Metabolites with residual above 10⁻⁶ | 0 | 0 |

Both models passed the flux-bound and mass-balance checks.

### Visualisations

The `results` folder contains the following visualisations:

- Flux comparison between the 10% and 15% models.
- Distribution of differences in reaction fluxes.
- Distribution of changing reactions across metabolic subsystems.

These plots help in understanding how the two threshold settings affect the model predictions.

## 8. Project Folder Structure

```text
iMAT-Human-Tissue-Project/
│
├── data/
│   ├── GTEx gene-expression dataset
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
│   └── Visualisation files
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

## 9. How to Run the Project

### Step 1: Clone the repository

```bash
git clone https://github.com/sridevir872-cloud/iMAT-Human-Tissue-Project.git
cd iMAT-Human-Tissue-Project
```

### Step 2: Install the required libraries

```bash
pip install -r requirements.txt
```

### Step 3: Download the data

```bash
python scripts/download_data.py
```

This script downloads the required input files, including the Human-GEM model, if they are not already available.

### Step 4: Run the analysis

Open the notebook:

`notebooks/iMAT_Human_Tissue_Project.ipynb`

The main analysis was performed using Google Colab. SCIP was used through PySCIPOpt to solve the optimisation problem.

The notebook contains the analysis steps and the results obtained from both threshold settings.

## 10. Limitations

There are a few limitations in this project:

- The predicted fluxes are computer-based predictions and are not actual experimental measurements.
- Changing the gene-expression threshold can change the predicted results.
- Gene expression does not always directly represent the actual activity of an enzyme.
- The 15% model reached a feasible solution, but global optimality was not proven within the time limit.
- Some reactions showed fluxes close to their allowed boundaries, so these predictions should be interpreted carefully.
- More experimental data would help in checking the predicted metabolic activities.

## 11. Reference

Shlomi, T., Cabili, M. N., Herrgård, M. J., Palsson, B. Ø., & Ruppin, E. (2008).

*Network-based prediction of human tissue-specific metabolism.*

Nature Biotechnology, 26, 1003–1010.

https://doi.org/10.1038/nbt.1487
