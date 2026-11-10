
"""
Human Liver Context-Specific Metabolic Modelling using iMAT

Primary analysis:
    notebooks/iMAT_Human_Tissue_Project.ipynb

Dataset:
    GTEx V11 - Liver

Metabolic model:
    Human-GEM v1.19.0

Thresholds:
    10% and 15%

Optimisation:
    iMATpy with SCIP through PySCIPOpt

Note:
    The complete optimisation and flux extraction were performed
    in Google Colab. See the notebook for the executable workflow
    and the recorded solver results.
"""

from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent

NOTEBOOK = (
    PROJECT
    / "notebooks"
    / "iMAT_Human_Tissue_Project.ipynb"
)

RESULTS = PROJECT / "results"

print("Human Liver iMAT Project")
print("------------------------")
print("Project directory:", PROJECT)
print("Analysis notebook:", NOTEBOOK)
print("Results directory:", RESULTS)

if not NOTEBOOK.exists():
    print("WARNING: Analysis notebook was not found.")

if not RESULTS.exists():
    print("WARNING: Results directory was not found.")

print("\nAnalysis configuration:")
print("Tissue: Liver")
print("Model: Human-GEM v1.19.0")
print("Thresholds: 10% and 15%")
print("Optimisation solver: SCIP")

print("\nOpen the Google Colab notebook to run the")
print("complete analysis and reproduce the results.")
