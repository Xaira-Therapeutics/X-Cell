---
license: cc-by-nc-sa-4.0
language:
  - en
thumbnail: x-cell-overview.png
tags:
  - biology
  - single-cell
  - perturbation-prediction
  - diffusion-model
  - genomics
  - CRISPRi
datasets:
  - Xaira-Therapeutics/X-Atlas-Pisces
pipeline_tag: other
---

# X-Cell

**A diffusion language model for genome-scale perturbation prediction across diverse cellular contexts.**

> **Status: Model weights and inference code coming soon.**
> The Python API, model weights, and tutorials are under active development.
> Watch the [GitHub repository](https://github.com/Xaira-Therapeutics/X-Cell) for release updates.

<p align="center">
  <img src="x-cell-overview.png" alt="X-Cell Architecture" width="100%">
</p>

## Model Description

X-Cell predicts genome-scale transcriptional responses to genetic perturbations across diverse cellular contexts. Trained on **X-Atlas/Pisces** (25.6M perturbed single cells, 7 CRISPRi Perturb-seq screens), X-Cell integrates multi-modal biological priors through cross-attention and generalizes zero-shot to unseen cell types and perturbations.

### Key Results

- **5x higher Pearson delta** than the next-best method on held-out iPSC perturbations
- **Zero-shot T-cell inactivation** — predicts CD3 complex inactivators and novel regulators (LRBA, APPL2)
- **LLM-class scaling laws** — train loss scales as L(N) ~ N^-0.32 (R^2 = 0.96)
- **Zero-shot cell type generalization** to melanocyte progenitors and primary human CD4+ T cells

## Model

| Model | Parameters | Description |
|-------|-----------|-------------|
| **X-Cell Mini** | 55M | Fast inference; initialized from scGPT |

## Architecture

X-Cell is a **set-level diffusion transformer** that operates on sets of cells (not individual cells) and refines predictions iteratively via a masked diffusion process. Key components:

- **Diffusion-based training** with 4-step coarse-to-fine refinement at inference
- **Multi-modal biological priors** via Flamingo-style cross-attention (ESM-2, STRING, GenePT, DepMap, JUMP-Cell Painting, scGPT)
- **Tied output embeddings** with PaLM-style 1/sqrt(d) scaling

## Intended Use

X-Cell is designed for predicting transcriptional responses to CRISPRi gene knockdowns. It is intended for research use in computational biology and genomics.

## Training Data

Trained on X-Atlas/Pisces — the largest CRISPRi Perturb-seq compendium to date:

| Screen | Context | Perturbations | Cells |
|--------|---------|--------------|-------|
| HCT116 | Colorectal cancer | 18,924 | 3.4M |
| HEK293T | Kidney epithelial | 18,312 | 4.5M |
| HepG2 | Hepatocellular carcinoma | 9,735 | 2.6M |
| iPSC | Induced pluripotent stem cells | 10,095 | 4.2M |
| Jurkat Resting | T lymphoblastic leukemia | 10,872 | 2.8M |
| Jurkat Active | CD3/CD28-stimulated T cells | 10,878 | 2.8M |
| iPSC Multi-Diff | Multi-lineage differentiation | 12,175 | 5.1M |

Dataset: [Xaira-Therapeutics/X-Atlas-Pisces](https://huggingface.co/datasets/Xaira-Therapeutics/X-Atlas-Pisces)

## Usage (Coming Soon)

```python
from xcell import XCell

model = XCell.from_pretrained("Xaira-Therapeutics/X-Cell", variant="mini")
predictions = model.predict("control_cells.h5ad", perturbation="BRCA1")
```

Full documentation: [xaira-therapeutics.github.io/X-Cell](https://xaira-therapeutics.github.io/X-Cell)

## Citation

```bibtex
@article{xcell2026,
  title   = {X-Cell: Scaling Causal Perturbation Prediction Across Diverse
             Cellular Contexts via Diffusion Language Models},
  author  = {Xaira Therapeutics},
  year    = {2026},
}
```

## License

This model is released under the [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) license.
