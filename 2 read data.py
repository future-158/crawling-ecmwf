# import imageio
from pathlib import Path
from this import d
import pandas as pd

import dask.array
import matplotlib.pyplot as plt
import numpy as np
import tqdm
import xarray as xr
from omegaconf import OmegaConf
from PIL import Image
from xarray.core import variable

CALV  = 273.15


cfg = OmegaConf.load('config.yml')
files = list(Path(cfg.catalogue.raw).glob('*.nc'))

for file in tqdm.tqdm(files):
    ds = xr.open_dataset(file, 
    # engine='cfgrib'
    )
    raise
    
    if not Path(cfg.catalogue.concat).exists():
        ds.sst.to_dataset().to_zarr(
            cfg.catalogue.concat
        )
    else:
        ds.sst.to_dataset().to_zarr(
            cfg.catalogue.concat,
            append_dim="time"
        )

full_time = pd.date_range('2020-01-01', '2022-01-01', freq='1H')
list(ds.variables)

# ds = xr.Dataset(
#     data_vars=dict(
#         sst=(["time", "latitude", "longitude"]),
#     ),
#     coords=dict(
#         time=full_time,
#         latitude=ds.latitude.data,
#         longitude=ds.longitude.data,
#     )
# )

ds_template.to_zarr(tempdir, compute=False)
and then use the region argument to write, i.e. something like
for j in range(ntimesteps):
    dd.to_zarr(tempdir, region={'time': slice(j, j+1)}


ds.set_index(time=xr.DataArray(full_time))
type(ds.time)
ds.reindex({"time": full_time}, method="bfill")

ds.drop('time').

ds



for file in tqdm.tqdm(files):
    ds = (
        xr.open_dataset(file)
        .sst
        .to_dataset()
        )

    

    ds.time

    ds.time.to_pandas()
    
    dummies = dask.array.zeros(30, chunks=10)
    ds = xr.Dataset({"foo": ("x", dummies)})
    path = "path/to/directory.zarr"
    ds.to_zarr(path, compute=False)
    ds = xr.Dataset({"foo": ("x", np.arange(30))})
    ds.isel(x=slice(0, 10)).to_zarr(path, region={"x": slice(0, 10)})
    ds.isel(x=slice(10, 20)).to_zarr(path, region={"x": slice(10, 20)})
    ds.isel(x=slice(20, 30)).to_zarr(path, region={"x": slice(20, 30)})
    