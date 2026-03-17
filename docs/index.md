---
hide:
  - navigation
  - toc
---

# X-Cell

**A diffusion language model for genome-scale perturbation prediction across diverse cellular contexts.**

<p align="center">
  <img src="figs/x-cell-overview.png" alt="X-Cell Architecture" width="100%">
</p>

X-Cell predicts genome-scale transcriptional responses to genetic perturbations across diverse cellular contexts. Trained on **X-Atlas/Pisces** — 25.6 million perturbed single cells across 7 CRISPRi Perturb-seq screens — X-Cell integrates multi-modal biological priors through cross-attention and generalizes zero-shot to unseen cell types and perturbations.

[:fontawesome-solid-file-pdf: Preprint](#){ .md-button .md-button--primary }
[:hugging: Model Weights](https://huggingface.co/Xaira-Therapeutics/X-Cell){ .md-button }
[:hugging: Dataset](https://huggingface.co/datasets/Xaira-Therapeutics/X-Atlas-Pisces){ .md-button }

!!! note "Availability"
    Model weights and inference code are coming soon. The API examples below reflect the planned interface.
    Watch the [GitHub repository](https://github.com/Xaira-Therapeutics/X-Cell) for release updates.

---

## Key Results

<div class="grid cards" markdown>

-   :material-dna: **State-of-the-art fold-change prediction**

    ---

    X-Cell achieves Pearson &Delta; of 0.51 on held-out iPSC perturbations — over **5&times;** higher than the next-best method.

-   :material-graph: **Zero-shot T-cell inactivation**

    ---

    Predicts CD3 complex inactivators and novel regulators (LRBA, APPL2) confirmed by an independent primary T-cell screen.

-   :material-chart-line: **LLM-class scaling laws**

    ---

    Train loss scales as a power law (&alpha; = 0.32) matching large language models, across 83M to 4.9B parameters.

-   :material-test-tube: **Zero-shot cell type generalization**

    ---

    Generalizes to melanocyte progenitors and primary human CD4+ T cells using test-time adaptation on unlabeled controls.

</div>

---

## Installation

```bash
pip install xcell
```

## Quick Start

```python
import anndata as ad
from xcell import XCell

# Load pretrained X-Cell Mini
model = XCell.from_pretrained("Xaira-Therapeutics/X-Cell", variant="mini")

# Predict from an AnnData object
adata = ad.read_h5ad("your_control_cells.h5ad")
predictions = model.predict(adata, perturbation="BRCA1")

# Or predict from one or more .h5ad file paths directly
predictions = model.predict(
    ["screen1.h5ad", "screen2.h5ad"],
    perturbation="BRCA1",
)
```

See [Quick Start](quickstart.md) for full examples including batch prediction and output interpretation.

---

## Model

| Model | Parameters | Description | Weights |
|-------|-----------|-------------|---------|
| **X-Cell Mini** | 55M | Fast inference; initialized from scGPT | [:hugging: Xaira-Therapeutics/X-Cell](https://huggingface.co/Xaira-Therapeutics/X-Cell) |

---

## Dataset: X-Atlas/Pisces

The largest CRISPRi Perturb-seq compendium to date, comprising **25.6 million perturbed single cells** across 7 diverse biological contexts.

| Screen | Context | Perturbations |
|--------|---------|--------------|
| HCT116 | Colorectal cancer | 18,924 |
| HEK293T | Kidney epithelial | 18,312 |
| HepG2 | Hepatocellular carcinoma | 9,735 |
| iPSC | Induced pluripotent stem cells | 10,095 |
| Jurkat Resting | T lymphoblastic leukemia | 10,872 |
| Jurkat Active | CD3/CD28-stimulated T cells | 10,878 |
| iPSC Multi-Diff | Multi-lineage differentiation | 12,175 |

Test perturbation sets available at [:hugging: Xaira-Therapeutics/X-Atlas-Pisces](https://huggingface.co/datasets/Xaira-Therapeutics/X-Atlas-Pisces).

---

## Citation

If you use X-Cell or X-Atlas/Pisces in your research, please cite:

```bibtex
@article{xcell2026,
  title   = {X-Cell: Scaling Causal Perturbation Prediction Across Diverse
             Cellular Contexts via Diffusion Language Models},
  author  = {Xaira Therapeutics},
  year    = {2026},
}
```

---

## License

This project is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).
