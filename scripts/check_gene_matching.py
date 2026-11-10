# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 18:59:54 2026

@author: G Sridevi
"""


from pathlib import Path
import pandas as pd
import cobra

# Project location
PROJECT = Path.home() / "Desktop" / "iMAT_Human_Tissue_Project"

gtex_file = PROJECT / "data" / "GTEx_Analysis_2025-08-22_v11_RNASeQCv2.4.3_gene_median_tpm.gct.gz"
model_file = PROJECT / "data" / "Human-GEM.xml"

# 1. Read GTEx column names
header = pd.read_csv(
    gtex_file,
    sep="\t",
    skiprows=2,
    nrows=0
)

print("GTEx columns:")
print(header.columns.tolist())

print("\nIs Liver available?", "Liver" in header.columns)

# 2. Read GTEx gene IDs
gtex_ids = pd.read_csv(
    gtex_file,
    sep="\t",
    skiprows=2,
    usecols=["Name"],
    compression="gzip"
)["Name"]

# Remove Ensembl version suffixes
gtex_ids = set(
    gtex_ids.astype(str).str.split(".").str[0]
)

# 3. Load Human-GEM
model = cobra.io.read_sbml_model(str(model_file))

model_ids = set(
    gene.id.split(".")[0]
    for gene in model.genes
)

# 4. Compare gene identifiers
matched = gtex_ids.intersection(model_ids)

print("\nGTEx unique genes:", len(gtex_ids))
print("Human-GEM unique genes:", len(model_ids))
print("Matched genes:", len(matched))

print("\nFirst 10 matching genes:")
print(list(sorted(matched))[:10])

print("\nGene matching check completed.")
