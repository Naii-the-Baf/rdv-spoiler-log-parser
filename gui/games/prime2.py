from PySide6 import QtCore, QtWidgets, QtGui

class Prime2(QtWidgets.QWidget):
    def __init__(self, item_locations):
        super().__init__()

        self.layout : QtWidgets.QGridLayout = QtWidgets.QGridLayout(self)
        self.layout.setColumnStretch(0, 20)
        self.layout.setColumnStretch(1, 30)
        self.layout.setColumnStretch(2, 50)
        row_pos = 0
        
        for item_category in item_locations:
            for item, locations in item_category.items():
                if len(locations) == 0:
                    continue
                text = QtWidgets.QLabel(item)
                text.setStyleSheet("border:1px solid black;")
                text.setAlignment(QtCore.Qt.AlignCenter)
                self.layout.addWidget(text, row_pos, 0, len(locations), 1)
                for location in locations:
                    text = QtWidgets.QLabel(location[0])
                    self.layout.addWidget(text, row_pos, 1, 1, 1)
                    text = QtWidgets.QLabel(" ".join([location[1], location[2]]))
                    self.layout.addWidget(text, row_pos, 2, 1, 1)
                    row_pos += 1


