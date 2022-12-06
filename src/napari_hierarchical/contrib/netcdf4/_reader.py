import os
from typing import Union

from napari_hierarchical.model import Group

PathLike = Union[str, os.PathLike]


def read_netcdf4(path: PathLike) -> Group:
    # TODO netCDF4 reader
    raise NotImplementedError()
