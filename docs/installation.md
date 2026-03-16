# Installation

## Requirements

- Python &ge; 3.10
- PyTorch &ge; 2.1

A CUDA-capable GPU is recommended for inference but not required for X-Cell Mini.

## Install from PyPI

```bash
pip install xcell
```

## Install from Source

```bash
git clone https://github.com/Xaira-Therapeutics/X-Cell.git
cd x-cell
pip install -e .
```

For development (linting, tests, type checking):

```bash
pip install -e ".[dev]"
```

## GPU Setup

X-Cell Mini runs comfortably on a single GPU with &ge;8 GB VRAM. To verify PyTorch sees your GPU:

```python
import torch
print(torch.cuda.is_available())   # True if GPU is available
print(torch.cuda.get_device_name()) # e.g. 'NVIDIA A100'
```

## Verify Installation

```python
import xcell
print(xcell.__version__)
```
