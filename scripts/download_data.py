
from pathlib import Path
import requests
import zipfile

# Project directories
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

# Dataset URLs
GTEX_FILENAME = (
    "GTEx_Analysis_2025-08-22_v11_RNASeQCv2.4.3_"
    "gene_median_tpm.gct.gz"
)

GTEX_URL = (
    "https://storage.googleapis.com/adult-gtex/bulk-gex/v11/"
    "rna-seq/" + GTEX_FILENAME
)

HUMAN_GEM_URL = (
    "https://zenodo.org/records/12523225/files/"
    "SysBioChalmers/Human-GEM-v1.19.0.zip?download=1"
)

def download_file(url, destination):
    print(f"\nDownloading: {destination.name}")

    response = requests.get(
        url,
        stream=True,
        timeout=180
    )
    response.raise_for_status()

    with open(destination, "wb") as file:
        for chunk in response.iter_content(
            chunk_size=1024 * 1024
        ):
            if chunk:
                file.write(chunk)

    print(f"Downloaded: {destination.name}")


# 1. Download GTEx data if missing
gtex_path = DATA_DIR / GTEX_FILENAME

if not gtex_path.exists():
    download_file(GTEX_URL, gtex_path)
else:
    print("GTEx dataset already exists.")


# 2. Download and extract Human-GEM if missing
model_path = DATA_DIR / "Human-GEM.xml"

if not model_path.exists():
    zip_path = DATA_DIR / "Human-GEM-v1.19.0.zip"

    download_file(HUMAN_GEM_URL, zip_path)

    print("\nExtracting Human-GEM model...")

    with zipfile.ZipFile(zip_path, "r") as archive:
        candidates = [
            name for name in archive.namelist()
            if Path(name).name == "Human-GEM.xml"
        ]

        if not candidates:
            raise FileNotFoundError(
                "Human-GEM.xml was not found inside the archive."
            )

        with archive.open(candidates[0]) as source:
            with open(model_path, "wb") as destination:
                destination.write(source.read())

    zip_path.unlink()
    print("Human-GEM model extracted successfully.")

else:
    print("Human-GEM model already exists.")


print("\nAll required datasets are ready!")
print("Data directory:", DATA_DIR)
v
