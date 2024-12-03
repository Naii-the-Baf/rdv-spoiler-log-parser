from PySide6 import QtCore, QtWidgets, QtGui

class Prime2(QtWidgets.QWidget):
    def __init__(self, item_locations):
        super().__init__()

        self.layout = QtWidgets.QVBoxLayout(self)
        
        for item_category in item_locations:
            
            for item, locations in item_category.items():
                text = QtWidgets.QLabel(item)
                self.layout.addWidget(text,
                                      alignment=QtCore.Qt.AlignCenter)
                for location in locations:
                    text = QtWidgets.QLabel(" ".join(location))
                    self.layout.addWidget(text,
                                          alignment=QtCore.Qt.AlignCenter)
                    
            


