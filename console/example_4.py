import processing

# Create the arguments needed for the buffer. At minimum, INPUT and OUTPUT are required.
args = {'INPUT': QgsProject.instance().mapLayersByName('locations shp')[0],
        'DISTANCE': 0.001,
        'OUTPUT': 'TEMPORARY_OUTPUT'}

# Create the buffer using the processing API and get its output from the returned dictionary.
output_layer = processing.run('native:buffer', args)['OUTPUT']

QgsProject.instance().addMapLayer(output_layer)
output_layer.setOpacity(0.5)
iface.mapCanvas().refresh()
