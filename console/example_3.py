def get_layer_field_index(lyr, fieldName):
    """
    Returns the index of the field in the layer.
    """
    # Get a reference of all of the fields.
    fields = lyr.fields()
    
    # Find the index of the provided field name.
    return fields.indexFromName(fieldName)
    
# Find the layer to modify.
layer_shp = QgsProject.instance().mapLayersByName('locations shp')[0]

# Begin an editing session on the layer.
layer_shp.startEditing()

# Get the index of the field to change.
index = get_layer_field_index(layer_shp, 'importance')

# Iterate over all of the features within the layer.
for feature in layer_shp.getFeatures():
    if feature['importance'] == 'Loww':
        # Update all importance values of Loww with Low.
        layer_shp.changeAttributeValue(feature.id(), index, 'Low')
        
# Complete the editing session on the layer.
layer_shp.commitChanges()
