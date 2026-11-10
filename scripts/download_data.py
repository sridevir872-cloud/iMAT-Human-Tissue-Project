
from pathlib import Path
import requests

# Locate the project directory
PROJECT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT / "data"

DATA_DIR.mkdir(parents=True, exist_ok=True)

FILES = {
    "GTEx_Analysis_2025-08-22_v11_RNASeQCv2.4.3_gene_median_tpm.gct.gz":
        "https://storage.googleapis.com/adult-gtex/bulk-gex/v11/rna-seq/GTEx_Analysis_2025-08-22_v11_RNASeQCv2.4.3_gene_median_tpm.gct.gz",

    "Human-GEM.xml":
        "https://raw.githubusercontent.com/SysBioChalmers/Human-GEM/v1.19.0/model/Human-GEM.xml"
}

def download_file(filename, url):
    destination = DATA_DIR / filename

    if destination.exists() and destination.stat().st_size > 0:
        print(f"Already downloaded: {filename}")
        return

    print(f"Downloading {filename}...")

    response = requests.get(url, stream=True, timeout=120)
    response.raise_for_status()

    with open(destination, "wb") as output:
        for chunk in response.iter_content(chunk_size=1024 * 1024):
            if chunk:
                output.write(chunk)

    print(f"Completed: {filename}")


if __name__ == "__main__":
    for filename, url in FILES.items():
        try:
            download_file(filename, url)
        except Exception as error:
            print(f"Error downloading {filename}: {error}")

    print("Download process finished.")
