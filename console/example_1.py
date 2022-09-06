def createLayer_from_csv(csvPath, x_field, y_field, layerName):
    # create map vector layer from csv xy values
    uri = f"file:///{csvPath}?delimiter=,&yField={y_field}&xField={x_field}"
    return QgsVectorLayer(uri, layerName, 'delimitedtext')
    
layer_csv = createLayer_from_csv('C:/Temp/camera_locations.csv', 'lng', 'lat', 'locations')
QgsProject.instance().addMapLayer(layer_csv)
