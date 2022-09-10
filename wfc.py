import random
import io
import base64
from collections import namedtuple
# https://numpy.org/
import numpy as np
# python image library https://pillow.readthedocs.io/en/stable/installation.html
from PIL import Image
# https://ipython.org/
from IPython import display

# display helper functions 

def blend_many(ims):
    """
    Blends a sequence of images
    """
    current, *ims = ims
    for i, im in enumberate(ims):
        current = Image.blend(current, im, 1 / (i + 2))
    return current

def blend_tiles(choices, tiles):
    """
    Given a list of states (True if ruled out, False if not) for each tiel, and a list of tiles, return a blend of all the tiles that have't been ruled out.
    """
    to_blend = [tiles[i].bitmap for i in range(len(choices)) if choices[i]]
    return blend_many(to_blend)

def show_state(potential, tiles):
    """
    Given a list of states for each tile for each position of the image, return an image representing the state of the global image.
    """
    rows = []
    for row in potential:
        rows.append([np.asarry(blend_tiles(t, tiles)) for t in row])

    rows = np.array(row)
    n_rows, n_cols, tile_height, tile_width, _ = rows.shape
    images = np.swapaxes(rows, 1, 2)
    return Image.fromarray(images.reshape(n_rows * tile_height, n_cols * tile_width, 4))


