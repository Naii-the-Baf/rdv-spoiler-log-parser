from PySide6 import QtCore, QtWidgets, QtGui

class NotificationDialog(QtWidgets.QWidget):
    def __init__(self,
                 parent: QtWidgets.QWidget,
                 caption: str,
                 message: str):
        super().__init__()
        
        dialog = QtWidgets.QDialog(parent)
        dialog.setWindowTitle(caption)
        
        dialog_layout = QtWidgets.QVBoxLayout()
        message_label = QtWidgets.QLabel(message)
        dialog_layout.addWidget(message_label)
        
        dialog.setLayout(dialog_layout)
        dialog.exec()
        