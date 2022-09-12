import processing

# Create the arguments needed for the buffer. At minimum, INPUT and OUTPUT are required.
args = {'INPUT': QgsProject.instance().mapLayersByName('locations shp'),
        'DISTANCE': 0.0005,
        'OUTPUT': 'TEMPORARY_OUTPUT'}

# Create the buffer using the processing API and get its output from the returned dictionary.
output = processing.run('native:buffer', args)['OUTPUT']

# Add the new buffer layer to the project.
QgsProject.instance().addMapLayer(output)
