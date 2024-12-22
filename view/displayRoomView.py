from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class DisplayRoomView(QWidget):

    def __init__(self,appController):
        super().__init__()
        label = QLabel("Salles")
        layout = QVBoxLayout()
        layout.addWidget(label)
        rooms = appController.getRooms()
        for i in range(0,len(rooms),1):
            layout.addWidget(QLabel(rooms[i].getName()))
        self.setLayout(layout)
        