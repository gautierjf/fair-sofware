from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from view.tableModel import TableModel
import pandas as pd


class DisplayExponentView(QWidget):

    def __init__(self,appController):
        super().__init__()
        label = QLabel("Exposants")
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.appController = appController
        exponents = appController.getExponents()

        table = QtWidgets.QTableView()
        rows = []
        datas = []
        for i in range(0,len(exponents),1):
            datas.append([exponents[i].firstname,exponents[i].lastname])
            rows.append(exponents[i].id)
         
        data = pd.DataFrame(datas, columns = ['Firstname', 'Lastname'], index=rows)   
        self.model = TableModel(data)
        table.setModel(self.model)

        layout.addWidget(table)
        table.resizeRowsToContents()

        bouton = QPushButton("Fermer")
        bouton.clicked.connect(self.close)
        layout.addWidget(bouton)

        self.setLayout(layout)
        
    def close(self):
        self.appController.goBack()