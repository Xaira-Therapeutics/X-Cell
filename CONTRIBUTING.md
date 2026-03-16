# Contributing to X-Cell

Thank you for your interest in contributing to X-Cell.

## Development Setup

```bash
git clone https://github.com/Xaira-Therapeutics/X-Cell.git
cd x-cell
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pre-commit install
```

## Workflow

1. Create a feature branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes and ensure tests pass:
   ```bash
   ruff check .
   ruff format --check .
   pytest
   ```
3. Commit with a clear message and open a pull request against `main`.
4. All PRs require at least one approving review before merge.

## Code Style

- We use [Ruff](https://docs.astral.sh/ruff/) for linting and formatting (line length: 120).
- Type hints are encouraged.
- Write tests for new functionality.

## Reporting Issues

Open an issue on GitHub with a clear description and minimal reproduction steps.
