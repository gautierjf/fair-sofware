from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from view.tableModel import TableModel
import pandas as pd

class DisplayTableView(QWidget):

    def __init__(self,appController):
        super().__init__()
        label = QLabel("Tables")
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.appController = appController
        tables = appController.getTables()

        table = QtWidgets.QTableView()
        
        rows = []
        datas = []
        for i in range(0,len(tables),1):
            datas.append([tables[i].name,tables[i].room.getName(),tables[i].tableGroup.getName(),tables[i].x,tables[i].y,tables[i].position])
            rows.append(tables[i].id)
         
        data = pd.DataFrame(datas, columns = ['Name','Room','Table Group','X','Y','Position'], index=rows)   
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