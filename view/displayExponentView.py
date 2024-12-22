from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class DisplayExponentView(QWidget):

    def __init__(self,appController):
        super().__init__()
        label = QLabel("Exposants")
        layout = QVBoxLayout()
        layout.addWidget(label)
        exponents = appController.getExponents()
        for i in range(0,len(exponents),1):
            layout.addWidget(QLabel(exponents[i].getName()))
        self.setLayout(layout)