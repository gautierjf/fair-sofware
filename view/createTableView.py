from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class CreateTableView(QWidget):

    def __init__(self,appController):
        self.appController = appController
        super().__init__()
        label = QLabel("Créer table")   
        layout = QFormLayout()
        layout.addWidget(label)

        self.name = QLineEdit()
        layout.addRow("Nom:", self.name)

        comboboxRooms = []
        self.rooms = self.appController.getRooms()
        for i in range(0,len(self.rooms),1):
            comboboxRooms.append(self.rooms[i].getName())
        self.room = QComboBox()
        self.room.addItems(comboboxRooms)
        self.room.activated.connect(self.check_index_table_room)
        layout.addRow("Salle:", self.room )

        comboboxTableGroups = []
        self.tableGroups = self.appController.getTableGroups()
        for i in range(0,len(self.tableGroups),1):
            comboboxTableGroups.append(self.tableGroups[i].getName())
        self.tableGroup = QComboBox()
        self.tableGroup.addItems(comboboxTableGroups)
        self.tableGroup.activated.connect(self.check_index_table_group)
        layout.addRow("Groupe de table:", self.tableGroup )

        bouton = QPushButton("Valider")
        bouton.clicked.connect(self.validTable)
        layout.addWidget(bouton)
        self.setLayout(layout)

    def check_index_table_room(self, index):
        self.selectedRoom = self.rooms[index]

    def check_index_table_group(self, index):
        self.selectedTableGroup= self.tableGroups[index]

    def validTable(self):
        self.appController.addTable(self.name.text(),self.selectedRoom,self.selectedTableGroup) 