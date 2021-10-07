"""
This module is an example of a barebones numpy reader plugin for napari.

It implements the ``napari_get_reader`` hook specification, (to create
a reader plugin) but your plugin may choose to implement any of the hook
specifications offered by napari.
see: https://napari.org/docs/dev/plugins/hook_specifications.html

Replace code below accordingly.  For complete documentation see:
https://napari.org/docs/dev/plugins/for_plugin_developers.html
"""
import numpy as np
from napari_plugin_engine import napari_hook_implementation
import pandas as pd

@napari_hook_implementation
def napari_get_reader(path):
    if isinstance(path, str) and path.endswith(".rrr"):
        return reader_function

    return None


def reader_function(path):

    df = pd.read_csv(path)

    df.columns = df.columns.str.lower()

    if not ('x' in df.columns and 'y' in df.columns) :
        print('no point columns found!')
        return None

    data = df[['x','y']].to_numpy()

    kwargs = dict(size=5,
                  face_color=[0,0,0,0],
                  edge_color=[1.,.5,.2], edge_width=4)

    return [(data, kwargs, 'points')]
