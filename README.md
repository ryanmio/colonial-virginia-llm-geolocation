# Virginia Land Grants LLM Geolocation

This repository contains code, data, and results for the paper "Benchmarking Large Language Models for Geolocating Colonial Virginia Land Grants."

## 📄 Paper & Validation

- ** Pre-print Paper:** [arXiv:2508.08266](https://arxiv.org/abs/2508.08266)
- ** Ground Truth Validation:** [OSS Validation Repository](https://github.com/ryanmio/oss-validation)

## Abstract

Virginia's seventeenth- and eighteenth-century land patents survive primarily as narrative metes-and-bounds descriptions, limiting spatial analysis. This study systematically evaluates current-generation large language models (LLMs) in converting these prose abstracts into geographically accurate latitude/longitude coordinates within a focused evaluation context. A digitized corpus of 5,471 Virginia patent abstracts (1695–1732) is released, with 43 rigorously verified test cases serving as an initial, geographically focused benchmark. Six OpenAI models across three architectures—o-series, GPT-4-class, and GPT-3.5—were tested under two paradigms: direct-to-coordinate and tool-augmented chain-of-thought invoking external geocoding APIs. Results were compared against a GIS analyst baseline, Stanford NER geoparser, Mordecai-3 neural geoparser, and a county-centroid heuristic.

The top single-call model, o3-2025-04-16, achieved a mean error of 23 km (median 14 km), outperforming the median LLM (37.4 km) by 37.5%, the weakest LLM (50.3 km) by 53.5%, and external baselines by 67% (GIS analyst) and 70% (Stanford NER). A five-call ensemble further reduced errors to 19 km (median 12 km) at minimal additional cost (~USD 0.20 per grant), outperforming the median LLM by 48.6%. A patentee-name redaction ablation slightly increased error (~9%), showing reliance on textual landmark and adjacency descriptions rather than memorization. The cost-effective gpt-4o-2024-08-06 model maintained a 28 km mean error at USD 1.09 per 1,000 grants, establishing a strong cost-accuracy benchmark. External geocoding tools offer no measurable benefit in this evaluation.

These findings demonstrate LLMs' potential for scalable, accurate, cost-effective historical georeferencing.

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
