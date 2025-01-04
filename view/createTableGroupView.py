from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class CreateTableGroupView(QWidget):

    def __init__(self,appController):
        self.appController = appController
        super().__init__()
        label = QLabel("Créer groupe de table") 
        layout = QFormLayout()
        self.tableWidth = QLineEdit()
        layout.addWidget(label)
        layout.addRow("Largeur:", self.tableWidth )
        self.tableWidth.setValidator(QIntValidator(1, 999, self))
        self.tableLength = QLineEdit()
        layout.addRow("Longueur:", self.tableLength )
        self.tableLength.setValidator(QIntValidator(1, 999, self))
        self.color = QLineEdit()
        layout.addRow("Couleur:", self.color )

        cancelButton = QPushButton("Annuler")
        cancelButton.clicked.connect(self.close)
        validButton = QPushButton("Valider")
        validButton.clicked.connect(self.validGroupTable)
        layout.addRow(cancelButton, validButton)
        self.setLayout(layout)
    
    def validGroupTable(self):
        self.appController.addTableGroup(self.tableWidth.text(),self.tableLength.text() ,self.color.text())

    def close(self):
        self.appController.goBack()