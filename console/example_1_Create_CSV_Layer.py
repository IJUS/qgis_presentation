def create_layer_from_csv(csvPath, x_field, y_field, layer_name):
    """
    Create a vector layer from the given CSV file, x field, y field, and layer name.
    """
    # Create the formatted URI for the CSV file.
    uri = f"file:///{csvPath}?delimiter=,&yField={y_field}&xField={x_field}"
    
    # Return a new reference to the CSV file as a vector layer.
    return QgsVectorLayer(uri, layer_name, 'delimitedtext')

# Use the create_layer_from_csv function to get a reference to the CSV layer.
layer_csv = create_layer_from_csv('C:/Temp/camera_locations.csv', 'lng', 'lat', 'locations')

# Add the CSV layer to the project.
QgsProject.instance().addMapLayer(layer_csv)
