from qgis.PyQt import QtWidgets

# Display a message box with the name Camera Name using the variable [%name%].
QtWidgets.QMessageBox.information(None, "Camera Name", "[%name%]")
