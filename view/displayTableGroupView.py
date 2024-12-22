from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class DisplayTableGroupView(QWidget):

    def __init__(self,appController):
        super().__init__()
        label = QLabel("Groupes de table")
        layout = QVBoxLayout()
        layout.addWidget(label)
        tableGroups = appController.getTableGroups()
        for i in range(0,len(tableGroups),1):
            layout.addWidget(QLabel(tableGroups[i].getName()))
        self.setLayout(layout)