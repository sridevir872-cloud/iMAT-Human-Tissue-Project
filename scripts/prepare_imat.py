
from pathlib import Path
import pandas as pd
import cobra
from imatpy.parse_gpr import gene_to_rxn_weights

# Project paths
PROJECT = Path.home() / "Desktop" / "iMAT_Human_Tissue_Project"

gtex_file = PROJECT / "data" / "GTEx_Analysis_2025-08-22_v11_RNASeQCv2.4.3_gene_median_tpm.gct.gz"
model_file = PROJECT / "data" / "Human-GEM.xml"

RESULTS = PROJECT / "results"
RESULTS.mkdir(exist_ok=True)

# Load GTEx liver expression
print("Loading GTEx liver expression...")

gtex = pd.read_csv(
    gtex_file,
    sep="\t",
    skiprows=2,
    usecols=["Name", "Liver"],
    compression="gzip"
)

gtex["Liver"] = pd.to_numeric(gtex["Liver"], errors="coerce")
gtex = gtex.dropna(subset=["Liver"])

# Remove Ensembl version suffixes
gtex["Gene_ID"] = (
    gtex["Name"].astype(str).str.replace(r"\.\d+$", "", regex=True)
)

# Combine duplicate gene IDs
gtex = gtex.groupby("Gene_ID")["Liver"].median()

print("GTEx unique genes:", len(gtex))

# Load Human-GEM
print("\nLoading Human-GEM...")
model = cobra.io.read_sbml_model(str(model_file))

model_genes = {
    gene.id.split(".")[0]: gene.id
    for gene in model.genes
}

# Match GTEx genes with Human-GEM
matched = {
    model_genes[gene_id]: expression
    for gene_id, expression in gtex.items()
    if gene_id in model_genes
}

expression = pd.Series(matched, dtype=float)

print("Matched genes:", len(expression))

# Prepare reaction weights for both thresholds
for percentile in [0.10, 0.15]:

    print(f"\nProcessing {percentile:.0%} threshold...")

    low_cutoff = expression.quantile(percentile)
    high_cutoff = expression.quantile(1 - percentile)

    gene_weights = pd.Series(
        0,
        index=expression.index,
        dtype=int
    )

    gene_weights[expression <= low_cutoff] = -1
    gene_weights[expression >= high_cutoff] = 1

    reaction_weights = gene_to_rxn_weights(
        model=model,
        gene_weights=gene_weights
    )

    print("Low genes:", (gene_weights == -1).sum())
    print("High genes:", (gene_weights == 1).sum())
    print("Low reactions:", (reaction_weights < 0).sum())
    print("High reactions:", (reaction_weights > 0).sum())
    print("Intermediate reactions:", (reaction_weights == 0).sum())

    # Save gene weights
    gene_weights.to_csv(
        RESULTS / f"liver_gene_weights_{int(percentile*100)}.csv"
    )

    # Save reaction weights
    reaction_weights.to_csv(
        RESULTS / f"liver_reaction_weights_{int(percentile*100)}.csv",
        header=["Weight"]
    )

print("\nBoth threshold reaction-weight files saved successfully!")
