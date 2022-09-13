from qgis.utils import iface
import processing

# Get the latitude and longitude of the feature the action was run on.
lat = [% lat %]
lng = [% lng %]

# Find the existing Buffered layer.
removable_layer = QgsProject.instance().mapLayersByName('Buffered')[0]

if removable_layer:
    # Remove the existing Buffered layer if it exists.
    QgsProject.instance().removeMapLayer(removable_layer)

# Create the parameters for the for the extraction process to get only the selected layer.
extraction_args = {'INPUT': iface.activeLayer(),
                   # Use the expression syntax to filter down to only the current feature. This is similar in syntax to SQL.
                   'EXPRESSION': f"lat = {lat} AND lng = {lng}",
                   'OUTPUT': 'TEMPORARY_OUTPUT'}

# Create a temporary from the extractbyexpression algorithm.
temporary_layer = processing.run('qgis:extractbyexpression', extraction_args)['OUTPUT']

buffer_args = {'INPUT': temporary_layer,
        'DISTANCE': 0.001,
        'OUTPUT': 'TEMPORARY_OUTPUT'}

output_layer = processing.run('native:buffer', buffer_args)['OUTPUT']

QgsProject.instance().addMapLayer(output_layer)
QgsProject.instance().layerTreeRoot().findLayer(output_layer).setItemVisibilityChecked(True)
output_layer.setOpacity(0.5)
iface.mapCanvas().refresh()
