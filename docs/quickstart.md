# Quick Start

!!! note "Availability"
    Model weights and inference code are coming soon. The examples below reflect the planned API interface.

## Load a Pretrained Model

```python
from xcell import XCell

model = XCell.from_pretrained("Xaira-Therapeutics/X-Cell", variant="mini")
```

`variant="mini"` loads X-Cell Mini (55M parameters).

---

## Predict from an AnnData Object

```python
import anndata as ad
from xcell import XCell

model = XCell.from_pretrained("Xaira-Therapeutics/X-Cell", variant="mini")

# Load your control cells
adata = ad.read_h5ad("control_cells.h5ad")

# Predict transcriptional response to a single-gene CRISPRi knockdown
predictions = model.predict(adata, perturbation="BRCA1")

# predictions is an AnnData with predicted perturbed expression in .X
print(predictions)
```

!!! note "Input expectations"
    `adata` should contain log-normalized (log1p CP10k) expression values.
    X-Cell covers all ~19,000 protein-coding genes; genes not in the vocabulary are zero-imputed.

---

## Predict from `.h5ad` File Paths

```python
# Single file path
predictions = model.predict("control_cells.h5ad", perturbation="BRCA1")

# Multiple files — cells are pooled across datasets
predictions = model.predict(
    ["screen1.h5ad", "screen2.h5ad"],
    perturbation="BRCA1",
)
```

---

## Batch Predict Across Perturbations

```python
import pandas as pd

perturbations = ["BRCA1", "TP53", "MYC", "EGFR"]

results = {}
for pert in perturbations:
    results[pert] = model.predict(adata, perturbation=pert)

# Concatenate into a single AnnData
import anndata as ad
all_predictions = ad.concat(results, label="perturbation")
```

---

## Interpreting Outputs

The returned `AnnData` contains:

| Field | Description |
|-------|-------------|
| `.X` | Predicted perturbed expression (log1p CP10k, same shape as input) |
| `.obs["perturbation"]` | Perturbation name |
| `.var` | Gene metadata (same as input `adata.var`) |

To compute predicted fold-change relative to control:

```python
import numpy as np

# Pseudobulk fold-change
ctrl_mean = adata.X.mean(axis=0)
pred_mean = predictions.X.mean(axis=0)
fold_change = pred_mean - ctrl_mean  # in log space, this is log fold-change

# Top differentially expressed genes
top_genes = np.argsort(np.abs(fold_change))[::-1][:20]
print(adata.var_names[top_genes])
```
