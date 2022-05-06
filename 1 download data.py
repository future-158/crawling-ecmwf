from pathlib import Path
from time import sleep
from typing import *
from omegaconf import OmegaConf
import cdsapi
import pandas as pd

def download_month(year: int, month: int, out_dir: Union[str, Path]):
    yyyy = str(year)
    mm = str(month).zfill(2)

    if not isinstance(out_dir, Path): out_dir = Path(out_dir)
    dest = out_dir  /  f"{yyyy}_{mm}.nc"

    if dest.exists():
        return 0

    c.retrieve(
        'reanalysis-era5-single-levels',
        {
            'product_type': 'reanalysis',
            # 'format': 'grib',
            'format': 'netcdf',
            'variable': [
            # '10m_u_component_of_wind',
            # '10m_v_component_of_wind',
            # '2m_dewpoint_temperature',
            # '2m_temperature',
            # 'mean_sea_level_pressure',
            'sea_surface_temperature',
            # 'surface_pressure',
            ],
            'year': yyyy,
            'month': mm,
            'day': [
                '01', '02', '03',
                '04', '05', '06',
                '07', '08', '09',
                '10', '11', '12',
                '13', '14', '15',
                '16', '17', '18',
                '19', '20', '21',
                '22', '23', '24',
                '25', '26', '27',
                '28', '29', '30',
                '31',
            ],
            'time': [
                '00:00', '01:00', '02:00',
                '03:00', '04:00', '05:00',
                '06:00', '07:00', '08:00',
                '09:00', '10:00', '11:00',
                '12:00', '13:00', '14:00',
                '15:00', '16:00', '17:00',
                '18:00', '19:00', '20:00',
                '21:00', '22:00', '23:00',
            ],
            'area': [
                50, 110, 20,
                140,
            ],
        }, dest
        )



if __name__ =='__main__':
    cfg = OmegaConf.load('config.yml')
    c = cdsapi.Client()
    start_date = cfg.start_date
    end_date = cfg.end_date
    out_dir = cfg.path.raw
    
    dts = pd.date_range(start_date, end_date, freq='MS')
    out_dir = Path(out_dir)
    for dt in dts:
        download_month(dt.year, dt.month, out_dir)
        

