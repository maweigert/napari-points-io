"""
This module is an example of a barebones writer plugin for napari

It implements the ``napari_get_writer`` and ``napari_write_image`` hook specifications.
see: https://napari.org/docs/dev/plugins/hook_specifications.html

Replace code below according to your needs
"""

from napari_plugin_engine import napari_hook_implementation


@napari_hook_implementation
def napari_get_writer(path, layer_types):
    if isinstance(path, str) and path.endswith('.rrr'):
        return napari_write_points
    

@napari_hook_implementation
def napari_write_points(path, data, meta):
    with open(path,'w') as f:
        f.write('bazingassss!')
    
