
# Virginia Land Grants LLM Geolocation

This repository contains code, data, and results for the paper "Benchmarking Large Language Models for Geolocating Colonial Virginia Land Grants."

## Abstract

This study evaluates whether state-of-the-art large language models (LLMs) can convert narrative metes-and-bounds descriptions from Virginia's seventeenth- and eighteenth-century land patent abstracts into usable latitude/longitude coordinates. We digitized 5,471 Virginia patent abstracts (1695–1732) from *Cavaliers and Pioneers* Vol. 3, with a rigorously annotated ground-truth dataset of 45 georeferenced test cases.

We benchmark six OpenAI models spanning three architecture families under two prompting paradigms: (i) one-shot "direct-to-coordinate" and (ii) tool-augmented chain-of-thought that invokes external geocoding APIs. The best purely textual model (OpenAI o3-2025-04-16) achieves a mean great-circle error of 23.4 km (median 14.3 km), a 67% improvement over a professional GIS baseline (71.4 km), while cutting cost and latency by roughly two and three orders of magnitude, respectively.

## Installation

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

## Data

This repository includes:

- **Raw data**: Original abstracts from *Cavaliers and Pioneers* Vol. 3 (1695-1732)
- **Validation sets**: 
  - `validation-dev-A.csv` and `validation-dev-B.csv`: Development sets used for prompt engineering
  - `validation-test.csv`: The test set with 45 ground-truth coordinates

## Usage

### Running Experiments

To run the main experiment with default settings:

```bash
python code/run_experiment.py --evalset data/processed/validation-test.csv
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

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

This work builds upon the meticulous archival research of Nell Marion Nugent, whose *Cavaliers and Pioneers* abstracts have preserved Virginia's colonial land records for generations of scholars. Special thanks to Bimbola Bashorun for providing the professional GIS benchmark, and to the Library of Virginia and Virginia Surveyor's Office for access to their digital archives and land patent collections.
