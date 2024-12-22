from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class DisplayDoorView(QWidget):

    def __init__(self,appController):
        super().__init__()
        label = QLabel("Portes")
        layout = QVBoxLayout()
        layout.addWidget(label)
        doors = appController.getDoors()
        for i in range(0,len(doors),1):
            layout.addWidget(QLabel(doors[i].getName()))
        self.setLayout(layout)