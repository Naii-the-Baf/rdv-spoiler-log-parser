from PySide6 import QtWidgets


class NotificationDialog:
    def __init__(self):
        pass

    @staticmethod
    def show(caption: str, message: str):
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle(caption)

        dialog_layout = QtWidgets.QVBoxLayout()
        message_label = QtWidgets.QLabel(message)
        dialog_layout.addWidget(message_label)

        button_values = QtWidgets.QDialogButtonBox.StandardButton.Close
        button_box = QtWidgets.QDialogButtonBox(button_values)
        button_box.rejected.connect(dialog.reject)
        dialog_layout.addWidget(button_box)

        dialog.setLayout(dialog_layout)
        dialog.exec()
