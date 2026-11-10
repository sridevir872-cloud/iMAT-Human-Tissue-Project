# Context-Specific Metabolic Modelling of Human Liver Using iMAT

## Project Overview

This project investigates the integration of human liver gene-expression data with a genome-scale metabolic network to predict tissue-specific metabolic activity.

The iMAT (Integrative Metabolic Analysis Tool) algorithm is used to integrate gene-expression information from the GTEx dataset with the Human-GEM metabolic reconstruction.

A sensitivity analysis is performed using two gene-expression thresholds: 10% and 15%.

## Research Question

Can gene-expression information from human liver tissue be integrated with a genome-scale metabolic network using iMAT to predict tissue-specific metabolic activity?

## Objectives

- Integrate human liver gene-expression data with a genome-scale metabolic model.
- Apply the iMAT algorithm to predict metabolic reaction activity.
- Investigate the effect of different gene-expression thresholds.
- Compare predicted reaction flux distributions.
- Identify metabolic subsystems associated with major flux differences.

## Datasets

**1. GTEx V11**

- Source: Genotype-Tissue Expression (GTEx) project.
- Data: Gene median TPM expression.
- Tissue selected: Liver.

**2. Human-GEM**

- Version: 1.19.0.
- Type: Human genome-scale metabolic model.
- Format: SBML/XML.

## Methodology

1. Download and prepare GTEx liver gene-expression data.
2. Load the Human-GEM metabolic model.
3. Match Ensembl gene identifiers between the expression dataset and metabolic model.
4. Classify genes into high, low and intermediate expression categories.
5. Convert gene-expression information into reaction weights using gene-protein-reaction associations.
6. Apply the iMAT algorithm.
7. Optimise the resulting mixed-integer linear programming model using SCIP.
8. Extract reaction fluxes and validate mass balance and reaction bounds.
9. Perform sensitivity analysis using 10% and 15% expression thresholds.

## Computational Tools

- Python
- Google Colab
- COBRApy
- imatpy
- PySCIPOpt / SCIP
- Pandas
- NumPy
- Matplotlib

## Key Results

The Human-GEM model contains 12,971 reactions, 8,455 metabolites and 2,887 genes.

The 10% threshold model produced an optimal objective value of 2,053 with zero optimality gap.

The 15% threshold model produced a best feasible objective value of 3,021, with a remaining optimality gap of approximately 0.1324%.

Flux validation showed no reaction-bound violations in either solution, and both solutions satisfied steady-state mass balance to numerical precision.

The sensitivity analysis identified 4,628 reactions with changed predicted fluxes and 374 reactions with changes in flux direction between the two solutions.

These are computational predictions and should not be interpreted as experimentally measured metabolic rates.

## Repository Structure

```text
iMAT_Human_Tissue_Project/
│
├── data/
├── results/
├── scripts/
├── notebooks/
├── README.md
└── requirements.txt
```

## Primary Research Paper

Shlomi, T., Cabili, M. N., Herrgård, M. J., Palsson, B. Ø., & Ruppin, E. (2008).

Network-based prediction of human tissue-specific metabolism.

Nature Biotechnology, 26, 1003–1010.

https://doi.org/10.1038/nbt.1487

## Project Scope

This project demonstrates the use of gene-expression information to constrain a genome-scale metabolic model and investigate predicted tissue-specific metabolic activity in human liver.
