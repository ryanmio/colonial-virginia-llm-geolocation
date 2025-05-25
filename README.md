# Virginia Land Grants LLM Geolocation

This repository contains code, data, and results for the paper "Benchmarking Large Language Models for Geolocating Colonial Virginia Land Grants."

## Abstract

This study evaluates whether state-of-the-art large language models (LLMs) can convert narrative metes-and-bounds descriptions from Virginia's seventeenth- and eighteenth-century land patent abstracts into usable latitude/longitude coordinates. We digitized 5,471 Virginia patent abstracts (1695–1732) from *Cavaliers and Pioneers* Vol. 3, with a rigorously annotated ground-truth dataset of 45 georeferenced test cases.

We benchmark six OpenAI models spanning three architecture families under two prompting paradigms: (i) one-shot "direct-to-coordinate" and (ii) tool-augmented chain-of-thought that invokes external geocoding APIs. The best purely textual model (OpenAI o3-2025-04-16) achieves a mean great-circle error of 23.4 km (median 14.3 km), a 67% improvement over a professional GIS baseline (71.4 km), while cutting cost and latency by roughly two and three orders of magnitude, respectively.

## Installation

### Option 1: Standard Python Setup

```bash
# Clone the repository
git clone https://github.com/ryanmio/virginia-land-grants-llm.git
cd virginia-land-grants-llm

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Option 2: Docker Setup (Recommended for Reproducibility)

For guaranteed reproducible results across different machines, use the provided Docker container:

```bash
# Clone the repository
git clone https://github.com/ryanmio/virginia-land-grants-llm.git
cd virginia-land-grants-llm

# Set your API keys
export OPENAI_API_KEY="your-openai-key-here"
export GOOGLE_MAPS_API_KEY="your-google-maps-key-here"

# Build and run with docker-compose
docker-compose -f docker/docker-compose.yml up --build
```

**Manual Docker commands:**

```bash
# Build the image
docker build -f docker/Dockerfile -t llm-geolocation .

# Run experiments with public data (45 ground-truth cases)
docker run -e OPENAI_API_KEY=$OPENAI_API_KEY \
           -v $(pwd)/results:/app/results \
           llm-geolocation \
           python3 code/run_experiment.py --evalset data/processed/validation.csv

# Interactive shell for development
docker run -it -e OPENAI_API_KEY=$OPENAI_API_KEY llm-geolocation /bin/bash
```

**Docker Data Access:**
- The Docker container includes all **public data** (`data/raw/limited_excerpts_45_abstracts.csv`, `data/raw/metadata_with_hashes.csv`, `data/processed/validation.csv`)
- For **full corpus analysis**, mount your private dataset: `-v /path/to/your/raw_cavaliers_extract.csv:/app/data/raw/raw_cavaliers_extract.csv`
- The `.gitignore` ensures private data never gets committed to the container image

**Reproducibility benefits:**
- Locks in Python 3.11 and exact package versions
- Preserves OpenAI API endpoints as of April 2025  
- Ensures identical results across different operating systems
- Simplifies dependency management
- Respects copyright compliance automatically

## Data

### Copyright-Compliant Data Organization

This repository implements a copyright protection protocol for the *Cavaliers and Pioneers* Vol. 3 dataset while maintaining research reproducibility. See [`docs/COPYRIGHT_COMPLIANCE.md`](docs/COPYRIGHT_COMPLIANCE.md) for full details.

#### Public Data (Included in Repository)

**`data/raw/` - Copyright-Compliant Research Data:**
- **`limited_excerpts_45_abstracts.csv`** (19KB) - Up to 200 words each from 45 abstracts with ground-truth coordinates
- **`metadata_with_hashes.csv`** (446KB) - Row identifiers, word counts, and SHA-256 hashes for all 5,470 abstracts

**`data/processed/` - Validation and Evaluation Data:**
- **`validation.csv`** (36KB) - Ground-truth coordinates and metadata for 45 test cases used for benchmarking

#### Private Data (Excluded from Repository)
- **`data/raw/raw_cavaliers_extract.csv`** - Complete OCR corpus (excluded via .gitignore)
  - Available privately under vetted, non-commercial data-use agreement
  - Contact repository maintainer for access
  - Verify integrity using SHA-256 hashes in `metadata_with_hashes.csv`

### Usage Notes

**For reproducing paper results:** Use `data/processed/validation.csv` for evaluation. The 45 ground-truth abstracts are available as limited excerpts in `data/raw/limited_excerpts_45_abstracts.csv`.

**For full corpus analysis:** Contact the maintainer for access to the complete dataset under appropriate data-use agreement.

**For verification:** All data can be verified using SHA-256 hashes provided in the metadata file.

### Data Verification

Data integrity verification tools are available for researchers with access to the complete dataset. Contact the repository maintainer for access to verification utilities.

## Usage

### Running Experiments

To run the main experiment with default settings:

```bash
python code/run_experiment.py --evalset data/processed/validation.csv
```

Options:
- `--evalset`: Path to evaluation dataset CSV
- `--methods-file`: Path to YAML defining models and methods (default: config/methods.yaml)
- `--prompts-file`: Path to YAML defining prompts (default: config/prompts.yaml)
- `--dry-run`: Skip OpenAI API calls and generate mock predictions
- `--max-rows`: Process at most N rows (for quick tests)
- `--verbose`: Print detailed progress info

### Creating Maps

To generate maps for individual grants:

```bash
python code/mapping/map_one_grant.py --grant_id 1
```

For batch mapping:

```bash
python code/mapping/batch_map.py --input results/full_results.csv
```

### Generating Plots

The `code/analysis/` directory contains scripts for generating all figures from the paper:

```bash
python code/analysis/plot_accuracy_bar.py
python code/analysis/plot_violin_methods.py
python code/analysis/plot_pareto.py
# etc.
```

## Key Findings

1. State-of-the-art LLMs can georeference colonial land grants with greater accuracy than traditional GIS workflows (23.4 km vs 71.4 km mean error).

2. One-shot "direct-to-coordinate" prompting outperforms tool-augmented approaches that use external geocoding APIs.

3. Cost-per-1000-grants ranges from $1.09 (GPT-4o) to $137.44 (o3), compared to $3,255.81 for professional GIS methods.

4. Processing time is reduced from hours (432s per grant) to seconds (0.7-48s per grant).

5. LLMs demonstrate robust performance across different abstract lengths and parameter settings.

## Citation

If you use this code or data in your research, please cite:

```
@article{mioduski2025benchmarking,
  title={Benchmarking Large Language Models for Geolocating Colonial Virginia Land Grants},
  author={Mioduski, Ryan},
  journal={},
  year={2025}
}
```

## AI Use Disclosure

This research employed artificial intelligence tools for specific technical and documentation tasks while maintaining full researcher control over all scientific content and conclusions. A comprehensive disclosure of AI usage is available in [`docs/AI_USE_DISCLOSURE.md`](docs/AI_USE_DISCLOSURE.md), detailing where AI tools were and were not used throughout the research process.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

This work builds upon the meticulous archival research of Nell Marion Nugent, whose *Cavaliers and Pioneers* abstracts have preserved Virginia's colonial land records for generations of scholars. Special thanks to Bimbola Bashorun for providing the professional GIS benchmark, and to the Library of Virginia and Virginia Surveyor's Office for access to their digital archives and land patent collections.
