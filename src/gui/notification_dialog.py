from PySide6 import QtCore, QtWidgets, QtGui

class NotificationDialog():
    def __init__(self):
        pass
    
    @staticmethod
    def show(parent: QtWidgets.QWidget,
             caption: str,
             message: str):
        dialog = QtWidgets.QDialog(parent)
        dialog.setWindowTitle(caption)
        
        dialog_layout = QtWidgets.QVBoxLayout()
        message_label = QtWidgets.QLabel(message)
        dialog_layout.addWidget(message_label)
        
        button_values = QtWidgets.QDialogButtonBox.Close
        button_box = QtWidgets.QDialogButtonBox(button_values)
        button_box.rejected.connect(dialog.reject)
        dialog_layout.addWidget(button_box)
        
        dialog.setLayout(dialog_layout)
        dialog.exec()
        