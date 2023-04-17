from collections.abc import Iterator, Mapping
from matplotlib import cbook, colors, scale
from matplotlib.colorbar import Colorbar
from matplotlib._cm import datad

import numpy as np
from numpy.typing import ArrayLike

class ColormapRegistry(Mapping[str, colors.Colormap]):
    def __init__(self, cmaps: Mapping[str, colors.Colormap]) -> None: ...
    def __getitem__(self, item: str) -> colors.Colormap: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
    def __call__(self) -> list[str]: ...
    def register(
        self, cmap: colors.Colormap, *, name: str | None = ..., force: bool = ...
    ) -> None: ...
    def unregister(self, name: str) -> None: ...
    def get_cmap(self, cmap: str | colors.Colormap): ...

_colormaps: ColormapRegistry = ...
def get_cmap(name: str | colors.Colormap | None =..., lut: int | None =...): ...

class ScalarMappable:
    cmap: colors.Colormap | None
    colorbar: Colorbar | None
    callbacks: cbook.CallbackRegistry
    def __init__(
        self,
        norm: colors.Normalize | None = ...,
        cmap: str | colors.Colormap | None = ...,
    ) -> None: ...
    def to_rgba(
        self,
        x: np.ndarray,
        alpha: float | ArrayLike | None = ...,
        bytes: bool = ...,
        norm: bool = ...,
    ) -> np.ndarray: ...
    def set_array(self, A: ArrayLike | None) -> None: ...
    def get_array(self) -> np.ndarray | None: ...
    def get_cmap(self) -> colors.Colormap: ...
    def get_clim(self) -> tuple[float, float]: ...
    def set_clim(self, vmin: float | tuple[float, float] | None = ..., vmax: float | None = ...) -> None: ...
    def get_alpha(self) -> float | None: ...
    def set_cmap(self, cmap: str | colors.Colormap) -> None: ...
    @property
    def norm(self) -> colors.Normalize: ...
    @norm.setter
    def norm(self, norm: colors.Normalize | str | None) -> None: ...
    def set_norm(self, norm: colors.Normalize | str | None) -> None: ...
    def autoscale(self) -> None: ...
    def autoscale_None(self) -> None: ...
    def changed(self) -> None: ...
