import napari

viewer = napari.Viewer()


viewer.open('input.rrr')

viewer.active_layer.save('output.rrr')

