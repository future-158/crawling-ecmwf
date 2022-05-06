import xarray as xr 
import matplotlib.pyplot as plt
import imageio
from PIL import Image
import numpy as np
from pathlib import Path


# define some constants.
CALV  = 273.15

# define few functions
def visualize_file():
    pass


source_dir = Path('./data')
files = list(source_dir.glob('*.grib'))

for file in files:
    ds = xr.open_dataset(file, engine='cfgrib')
    ds
    raise

    sst_calv = ds.sst.values
    sst = sst_calv - CALV
    # Get the color map by name:
    cm = plt.get_cmap('Reds')
    # Apply the colormap like a function to any array:
    # colored_image = cm(sst)
    imgs = []
    for i in range(sst.shape[0]):
        out_dir = Path('./gif') / file.stem
        out_dir.mkdir(parents=True, exist_ok=True)
        day = i // 24 
        hour = day % 24
        dest = out_dir / f"{file.stem}_{day:02d}_{hour:02d}.png"

        plt.figure(figsize=(9,9))
        plt.imshow(sst[i])
        plt.colorbar()
        plt.savefig(dest, dpi=200)

    # for n in np.arange(colored_image.shape[0]):
    #     img = Image.fromarray((colored_image[n,..., :3] * 255).astype(np.uint8))
    #     img = img.resize((1280,420))
    #     imgs.append(img)

    # img, imgs = imgs[0], imgs[1:]
    # with open('sst.gif', 'wb') as fp_out:
    #     img.save(fp=fp_out, format='GIF', append_images=imgs,
    #             save_all=True, duration=200, loop=0)