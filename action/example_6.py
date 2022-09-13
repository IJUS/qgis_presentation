from qgis.utils import iface
import processing
lat = [% lat %]
lng = [% lng %]

# Create the parameters for the for the extraction process to get only the selected layer.
extraction_args = {'INPUT': iface.activeLayer(),
                   'EXPRESSION': f"lat = {lat} AND lng = {lng}",
                   'OUTPUT': 'TEMPORARY_OUTPUT'}

temporary_layer = processing.run('qgis:extractbyexpression', extraction_args)['OUTPUT']

buffer_args = {'INPUT': temporary_layer,
        'DISTANCE': 0.001,
        'OUTPUT': 'TEMPORARY_OUTPUT'}

output_layer = processing.run('native:buffer', buffer_args)['OUTPUT']

QgsProject.instance().addMapLayer(output_layer)
output_layer.setOpacity(0.5)
iface.mapCanvas().refresh()
