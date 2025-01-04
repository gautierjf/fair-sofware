from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from view.tableModel import TableModel
import pandas as pd

class DisplayDoorView(QWidget):

    def __init__(self,appController):
        super().__init__()
        label = QLabel("Portes")
        layout = QVBoxLayout()
        layout.addWidget(label)
        doors = appController.getDoors()

        table = QtWidgets.QTableView()
        rows = []
        datas = []
        for i in range(0,len(doors),1):
            datas.append([doors[i].name,doors[i].room.getName(),doors[i].width,doors[i].position,doors[i].x,doors[i].y])
            rows.append(doors[i].id)

        data = pd.DataFrame(datas, columns = ['Name','Room','Width','Position','X','Y'], index=rows)   
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