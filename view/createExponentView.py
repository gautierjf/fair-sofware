from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class CreateExponentView(QWidget):

    def __init__(self,appController):
        self.appController = appController
        super().__init__()
        label = QLabel("Créer exposant")   
        layout = QFormLayout()
        layout.addWidget(label)
        self.firstName = QLineEdit()
        layout.addRow("Prénom:", self.firstName )
        self.lastName = QLineEdit()
        layout.addRow("Nom:", self.lastName )

        cancelButton = QPushButton("Annuler")
        cancelButton.clicked.connect(self.close)
        validButton = QPushButton("Valider")
        validButton.clicked.connect(self.validExponent)
        layout.addRow(cancelButton, validButton)


        self.setLayout(layout)
    
    def validExponent(self):
        self.appController.addExponent(self.firstName.text(),self.lastName.text())

    def close(self):
        self.appController.goBack()