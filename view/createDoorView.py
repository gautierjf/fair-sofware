from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class CreateDoorView(QWidget):

    def __init__(self,appController):
        self.appController = appController
        super().__init__()
        label = QLabel("Créer porte")   
        layout = QFormLayout()
        self.name = QLineEdit()

        layout.addWidget(label)
        layout.addRow("Nom:", self.name)

        comboboxRooms = []
        self.rooms = self.appController.getRooms()
        for i in range(0,len(self.rooms),1):
            comboboxRooms.append(self.rooms[i].getName())
        self.room = QComboBox()
        self.room.addItems(comboboxRooms)
        self.room.activated.connect(self.check_index_door)
        layout.addRow("Salle:", self.room )


        cancelButton = QPushButton("Annuler")
        cancelButton.clicked.connect(self.close)
        validButton = QPushButton("Valider")
        validButton.clicked.connect(self.validDoor)
        layout.addRow(cancelButton, validButton)

        self.setLayout(layout)
    

    def check_index_door(self, index):
        self.selectedRoom = self.rooms[index]

    def validDoor(self):
        self.appController.addDoor(self.name.text(),self.selectedRoom)

    def close(self):
        self.appController.goBack()