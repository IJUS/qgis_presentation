def createLayer_from_csv(csvPath, x_field, y_field, layer_name):
    """
    Create a vector layer from the given CSV file, x field, y field, and layer name.
    """
    uri = f"file:///{csvPath}?delimiter=,&yField={y_field}&xField={x_field}"
    return QgsVectorLayer(uri, layer_name, 'delimitedtext')
    
layer_csv = createLayer_from_csv('C:/Temp/camera_locations.csv', 'lng', 'lat', 'locations')
QgsProject.instance().addMapLayer(layer_csv)
