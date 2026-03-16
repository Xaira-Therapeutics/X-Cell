# Dataset: X-Atlas/Pisces

X-Atlas/Pisces is the largest CRISPRi Perturb-seq compendium to date, comprising
**25.6 million perturbed single-cell transcriptomes** across 7 biologically diverse contexts.

## Screens

| Screen | Cell Type | Perturbations | Perturbed Cells | Median KD % |
|--------|-----------|--------------|----------------|-------------|
| HCT116 | Colorectal cancer | 18,924 | 3.4M | 70% |
| HEK293T | Kidney epithelial | 18,312 | 4.5M | 48% |
| HepG2 | Hepatocellular carcinoma | 9,735 | 2.6M | 85% |
| iPSC | Induced pluripotent stem cells | 10,095 | 4.2M | 82% |
| Jurkat Resting | T lymphoblastic leukemia | 10,872 | 2.8M | 79% |
| Jurkat Active | CD3/CD28-stimulated T cells | 10,878 | 2.8M | 71% |
| iPSC Multi-Diff | Multi-lineage differentiation | 12,175 | 5.1M | 96% |

## Data Access

Test perturbation sets (held-out genes from HepG2 and iPSC, plus full Jurkat Resting/Active screens)
are available on HuggingFace:

[:hugging: Xaira-Therapeutics/X-Atlas-Pisces](https://huggingface.co/datasets/Xaira-Therapeutics/X-Atlas-Pisces){ .md-button }

## Format

Data is provided as `.h5ad` files (AnnData format) with:

- `.X` — log-normalized expression (log1p CP10k)
- `.obs["perturbation"]` — gene target of CRISPRi knockdown
- `.obs["is_control"]` — boolean flag for non-targeting controls
- `.var_names` — ENSEMBL gene IDs

## Context-Dependent Biology

A key finding from X-Atlas/Pisces is that perturbation effects are strongly context-dependent.
Hierarchical clustering of perturbation effect profiles (F1 scores from a per-perturbation
binary classifier) reveals three classes:

- **Context-independent**: core essential machinery (e.g., mitochondrial ribosome subunits,
  oxidative phosphorylation) — enriched in shared metabolic functions
- **Context-specific**: lineage-defining regulators — enriched in cell-type-specific pathways
  (e.g., hypoxia response in HepG2, neural crest differentiation in iPSC)
- **Conserved proximal / variable distal**: perturbations where the direct consequence is
  consistent but downstream cascades diverge by context

This context-dependence motivates X-Cell's cross-attention architecture, which conditions
predictions on multi-modal biological priors rather than learning context-invariant representations.
