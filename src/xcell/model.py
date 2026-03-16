"""X-Cell model: loading and inference."""

from __future__ import annotations

from pathlib import Path

# AnnData is a lightweight dependency; import lazily to keep startup fast
try:
    import anndata as ad
    from anndata import AnnData
except ImportError as e:
    raise ImportError("anndata is required for X-Cell inference. Install with: pip install anndata") from e


PathLike = str | Path
DataInput = AnnData | PathLike | list[PathLike]


class XCell:
    """X-Cell: a diffusion language model for genome-scale perturbation prediction.

    X-Cell predicts the transcriptional response to genetic perturbations from a set
    of control cells. It operates on *sets* of cells (not individual cells) and refines
    predictions iteratively via a masked diffusion process.

    Available variant:

    - ``"mini"``  — 55M parameters, initialized from scGPT, runs on a single GPU.

    Examples
    --------
    Load X-Cell Mini and predict the response to a BRCA1 knockdown:

    >>> import anndata as ad
    >>> from xcell import XCell
    >>> model = XCell.from_pretrained("Xaira-Therapeutics/X-Cell", variant="mini")
    >>> adata = ad.read_h5ad("control_cells.h5ad")
    >>> predictions = model.predict(adata, perturbation="BRCA1")

    Predict from multiple ``.h5ad`` files:

    >>> predictions = model.predict(
    ...     ["screen1.h5ad", "screen2.h5ad"],
    ...     perturbation="BRCA1",
    ... )
    """

    SUPPORTED_VARIANTS = ("mini",)

    def __init__(self) -> None:
        # Internal state populated by from_pretrained
        self._variant: str | None = None
        self._loaded: bool = False

    @classmethod
    def from_pretrained(
        cls,
        model_id: str = "Xaira-Therapeutics/X-Cell",
        variant: str = "mini",
        device: str | None = None,
        cache_dir: PathLike | None = None,
    ) -> XCell:
        """Load a pretrained X-Cell model from HuggingFace Hub.

        Parameters
        ----------
        model_id:
            HuggingFace repository ID. Defaults to ``"Xaira-Therapeutics/X-Cell"``.
        variant:
            Model variant. Currently only ``"mini"`` (55M) is available.
        device:
            PyTorch device string (e.g. ``"cuda"``, ``"cpu"``).
            Defaults to CUDA if available, otherwise CPU.
        cache_dir:
            Local directory for caching downloaded weights.

        Returns
        -------
        XCell
            A loaded model instance ready for inference.

        Raises
        ------
        ValueError
            If ``variant`` is not one of the supported variants.
        """
        if variant not in cls.SUPPORTED_VARIANTS:
            raise ValueError(f"Unknown variant {variant!r}. Choose from: {cls.SUPPORTED_VARIANTS}")

        raise NotImplementedError(
            "Model loading is not yet implemented in this release. "
            "Full inference code is coming soon — watch the repository for updates."
        )

    def predict(
        self,
        data: DataInput,
        perturbation: str,
        n_cells: int = 64,
        n_diffusion_steps: int = 4,
        batch_size: int = 8,
    ) -> AnnData:
        """Predict the transcriptional response to a perturbation.

        Parameters
        ----------
        data:
            Control cell expression. Accepts:

            - an :class:`anndata.AnnData` object,
            - a path (``str`` or :class:`pathlib.Path`) to an ``.h5ad`` file,
            - a list of ``.h5ad`` file paths (cells are pooled across files).

            Expression values should be log-normalized (log1p CP10k). Genes not
            present in the X-Cell vocabulary are zero-imputed.
        perturbation:
            HGNC gene symbol of the CRISPRi knockdown to simulate (e.g. ``"BRCA1"``).
        n_cells:
            Number of control cells to sample per prediction set. Default 64.
        n_diffusion_steps:
            Number of iterative diffusion refinement steps at inference. Default 4.
        batch_size:
            Number of cell sets to process in parallel per forward pass.

        Returns
        -------
        AnnData
            Predicted perturbed expression. Shape matches the input ``data``.

            - ``.X`` — predicted log-normalized expression (log1p CP10k)
            - ``.obs["perturbation"]`` — perturbation name
            - ``.var`` — gene metadata (same as input)

        Raises
        ------
        RuntimeError
            If the model has not been loaded via :meth:`from_pretrained`.
        """
        if not self._loaded:
            raise RuntimeError("Model not loaded. Call XCell.from_pretrained() first.")

        raise NotImplementedError("Inference is not yet implemented in this release.")

    def _load_data(self, data: DataInput) -> AnnData:
        """Normalize ``data`` to a single AnnData, loading from disk if needed."""
        if isinstance(data, AnnData):
            return data
        if isinstance(data, (str, Path)):
            return ad.read_h5ad(data)
        if isinstance(data, list):
            adatas = [ad.read_h5ad(p) for p in data]
            return ad.concat(adatas, merge="same")
        raise TypeError(f"Unsupported data type: {type(data)}")
