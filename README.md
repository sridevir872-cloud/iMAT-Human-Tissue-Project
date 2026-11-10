# Human Liver Metabolic Modelling Using iMAT

## 1. Project Overview

This project focuses on predicting human liver-specific metabolic activity by combining gene-expression data with a genome-scale metabolic model.

The **iMAT (Integrative Metabolic Analysis Tool)** method is used to integrate gene-expression information into a metabolic network and predict which metabolic reactions are likely to be active or inactive.

## 2. Research Question

Can gene-expression information from human liver tissue be integrated with a genome-scale metabolic network using iMAT to predict tissue-specific metabolic activity?

## 3. Dataset and Tools

### Datasets
- **GTEx V11:** Human liver gene-expression data (median TPM values).
- **Human-GEM v1.19.0:** Human genome-scale metabolic model.

### Tools and Libraries
- Python 3.11
- iMATpy
- COBRApy
- PySCIPOpt / SCIP
- Pandas
- NumPy
- Matplotlib

## 4. Methodology

The project follows these main steps:

1. **Data preparation:** GTEx liver gene-expression data is loaded and processed. Version numbers are removed from Ensembl gene IDs to allow matching with the metabolic model.
2. **Gene matching:** GTEx gene IDs are matched with the genes present in Human-GEM.
3. **Gene classification:** Genes are classified into high, low, and intermediate expression groups using 10% and 15% expression thresholds.
4. **Reaction mapping:** Gene-expression information is mapped to metabolic reactions using the gene-reaction rules in Human-GEM.
5. **iMAT optimisation:** The iMAT method integrates gene-expression information with the metabolic network to predict reaction activity.
6. **Flux analysis:** Predicted reaction fluxes are extracted and compared between the two threshold settings.
7. **Validation:** Flux bounds and mass-balance constraints are checked to assess the validity of the predicted solutions.

## 5. Results

### Gene Matching

- Total unique GTEx genes: 74,628
- Total Human-GEM genes: 2,887
- Matched genes: 2,877
- Unmatched genes: 10
- Gene matching percentage: 99.65%

### Reaction Classification

A total of 12,971 reactions were analysed.

| Reaction classification | 10% threshold | 15% threshold |
|---|---:|---:|
| Low expression (-1) | 214 | 313 |
| Intermediate (0) | 10,619 | 9,576 |
| High expression (+1) | 2,138 | 3,082 |
| **Total** | **12,971** | **12,971** |

### Optimisation Results

| Parameter | 10% threshold | 15% threshold |
|---|---:|---:|
| Best objective value | 2,053 | 3,021 |
| Solver status | Optimal | Time limit reached |
| Feasible solutions | 100 | 100 |
| Optimality gap | 0% | 0.1324% |

The 10% model reached an optimal solution. The 15% model reached a feasible solution with a small optimality gap, but optimality was not proven within the time limit.

### Flux Comparison

The flux distributions from the two threshold settings were compared.

- Total reactions compared: 12,971
- Reactions with changed flux: 4,628
- Reactions with direction changes: 374
- Mean absolute flux difference: 73.12

### Model Validation

Both models passed the flux-bound and mass-balance checks.

- No flux-bound violations were detected.
- Maximum mass-balance residual for the 10% model: 7.09 × 10⁻¹²
- Maximum mass-balance residual for the 15% model: 1.03 × 10⁻¹⁰

## 6. Conclusion

The results demonstrate how liver gene-expression information can be integrated with a genome-scale metabolic model using iMAT. The comparison between 10% and 15% thresholds shows that the choice of expression threshold affects reaction classification and predicted flux distributions.

The analysis provides a computational prediction of liver-specific metabolic activity. These predictions should not be treated as direct measurements of actual metabolic rates.

## 7. Limitations

- Gene expression does not always directly represent enzyme activity.
- The predicted flux values are computational estimates, not experimentally measured rates.
- Different expression thresholds can produce different metabolic predictions.
- The 15% optimisation reached the time limit before proving optimality.
- Experimental data would be required for further biological validation.

## 8. Reference

Shlomi, T., et al. (2008). Network-based prediction of human tissue-specific metabolism. *Nature Biotechnology*, 26, 1003–1010.

https://doi.org/10.1038/nbt.1487
