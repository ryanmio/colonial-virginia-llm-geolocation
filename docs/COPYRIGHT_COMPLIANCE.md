# Copyright Compliance Implementation

This repository implements copyright protection protocols for the *Cavaliers and Pioneers* Volume 3 dataset.

## Copyright Protocol

Following the social responsibility pillar described in the research paper:

> Although the underlying seventeenth- and eighteenth-century land patent records themselves are public domain, the transcriptions published in the 1979 compilation Cavaliers and Pioneers, Vol. 3 remain under copyright. To balance reproducibility with copyright compliance, I publicly release only limited, non-substitutable excerpts (up to 200 words each) of the 45 abstracts with authoritative ground-truth points. For the full corpus of 5,471 abstracts, I provide only row identifiers, word counts, and SHA-256 hashes of each abstract, allowing researchers to verify their own local copies without exposing protected text.

## Repository Data Organization

### Public Data (Included in Repository)

#### `data/raw/` - Public Copyright-Compliant Data
- **`limited_excerpts_45_abstracts.csv`** (19KB)
  - Up to 200 words each from 45 abstracts with ground-truth coordinates
  - Enables reproducibility while respecting copyright
  - Contains: volume, book, limited_excerpt, word_count, excerpt_word_count, set

- **`metadata_with_hashes.csv`** (446KB) 
  - Row identifiers, word counts, and SHA-256 hashes for all 5,470 abstracts
  - Allows verification of local copies without exposing copyrighted text
  - Contains: row_id, word_count, sha256_hash, volume, book, set

#### `data/processed/` - Research Validation Data
- **`validation.csv`** (36KB)
  - Ground-truth coordinates and metadata for 45 test cases
  - Used for benchmarking and evaluation
  - Contains: latitude/longitude coordinates, accuracy assessments, research annotations

### Private Data (Excluded from Repository)

#### `data/raw/raw_cavaliers_extract.csv` (1.3MB, excluded via .gitignore)
- **Content**: Complete OCR corpus of all 5,470 abstracts from *Cavaliers and Pioneers* Vol. 3
- **Status**: Copyrighted material, excluded from public repository
- **Access**: Available privately under vetted, non-commercial data-use agreement for scholarly research only
- **Verification**: Use SHA-256 hashes in `metadata_with_hashes.csv` to verify integrity

## Data Access for Researchers

### For Reproduction (Public Access)
1. **Ground-truth evaluation**: Use `data/processed/validation.csv` with `data/raw/limited_excerpts_45_abstracts.csv`
2. **Method validation**: Compare your results against the 45 ground-truth points
3. **Hash verification**: Verify any local copies using `data/raw/metadata_with_hashes.csv`

### For Full Corpus Analysis (Private Access)
1. Contact the repository maintainer for data-use agreement
2. Obtain `raw_cavaliers_extract.csv` under vetted, non-commercial terms
3. Place file in `data/raw/` directory (git will ignore it)
4. Verify integrity using SHA-256 hashes in metadata file

## Verification Protocol

Researchers can verify their own copies by comparing SHA-256 hashes:

### Automated Verification (Recommended)

```bash
python3 verify_data_integrity.py
```

This script automatically verifies your local copy of `data/raw/raw_cavaliers_extract.csv` against the public metadata.

### Manual Verification

```python
import pandas as pd
import hashlib

# Load your copy and our metadata
your_data = pd.read_csv('data/raw/raw_cavaliers_extract.csv')
metadata = pd.read_csv('data/raw/metadata_with_hashes.csv')

# Verify hashes match
def compute_sha256(text):
    return hashlib.sha256(str(text).encode('utf-8')).hexdigest()

your_hashes = your_data['raw_entry'].apply(compute_sha256)
verified = (your_hashes == metadata['sha256_hash']).all()
print(f"Data integrity verified: {verified}")
```

## Generated: 2025-05-25 12:34:17
