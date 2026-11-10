# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 18:57:50 2026

@author: G Sridevi
"""


from pathlib import Path
import pandas as pd
import cobra

# Project folder
PROJECT = Path.home() / "Desktop" / "iMAT_Human_Tissue_Project"

# File locations
gtex_file = PROJECT / "data" / "GTEx_Analysis_2025-08-22_v11_RNASeQCv2.4.3_gene_median_tpm.gct.gz"

model_file = PROJECT / "data" / "Human-GEM.xml"

# Check files
print("GTEx file exists:", gtex_file.exists())
print("Human-GEM file exists:", model_file.exists())

# Read GTEx data
gtex = pd.read_csv(
    gtex_file,
    sep="\t",
    skiprows=2,
    compression="gzip",
    nrows=5
)

print("\nGTEx dataset preview:")
print(gtex.head())

# Read metabolic model
model = cobra.io.read_sbml_model(str(model_file))

print("\nHuman-GEM loaded successfully!")
print("Reactions:", len(model.reactions))
print("Metabolites:", len(model.metabolites))
print("Genes:", len(model.genes))
