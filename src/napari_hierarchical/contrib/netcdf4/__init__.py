import os
from pathlib import Path
from typing import Optional, Union

from pluggy import HookimplMarker

from napari_hierarchical.hookspecs import GroupReaderFunction, GroupWriterFunction
from napari_hierarchical.model import Group

from ._reader import read_netcdf4
from ._writer import write_netcdf4

PathLike = Union[str, os.PathLike]

available = False  # TODO netCDF4 reader/writer
hookimpl = HookimplMarker("napari-hierarchical")


@hookimpl
def napari_hierarchical_get_group_reader(
    path: PathLike,
) -> Optional[GroupReaderFunction]:
    if available and Path(path).suffix.lower() == ".nc":
        return read_netcdf4
    return None


@hookimpl
def napari_hierarchical_get_group_writer(
    path: PathLike, group: Group
) -> Optional[GroupWriterFunction]:
    if available and Path(path).suffix.lower() == ".nc":
        return write_netcdf4
    return None


__all__ = [
    "available",
    "read_netcdf4",
    "write_netcdf4",
    "napari_hierarchical_get_group_reader",
    "napari_hierarchical_get_group_writer",
]
