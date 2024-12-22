from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class DisplayTableView(QWidget):

    def __init__(self,appController):
        super().__init__()
        label = QLabel("Tables")
        layout = QVBoxLayout()
        layout.addWidget(label)
        tables = appController.getTables()
        for i in range(0,len(tables),1):
            layout.addWidget(QLabel(tables[i].getName()))
        self.setLayout(layout)