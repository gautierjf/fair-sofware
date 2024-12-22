from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class CreateRoomView(QWidget):

    def __init__(self,appController):
        self.appController = appController
        super().__init__()
        label = QLabel("Créer salle")   
        layout = QFormLayout()
        layout.addWidget(label)
        self.name = QLineEdit()
        layout.addRow("Nom:", self.name)
        self.width = QLineEdit()
        self.width.setValidator(QIntValidator(1, 999, self))
        layout.addRow("Largeur:", self.width)
        self.height = QLineEdit()
        self.height.setValidator(QIntValidator(1, 999, self))
        layout.addRow("Longueur:", self.height)
        bouton = QPushButton("Valider")
        bouton.clicked.connect(self.validRoom)
        layout.addWidget(bouton)
        self.setLayout(layout)
    
    def validRoom(self):
        self.appController.addRoom(self.name.text(),self.width.text(),self.height.text())