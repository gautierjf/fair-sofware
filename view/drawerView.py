from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtCore import  Qt


class Viewport(QGraphicsView):

    multiplicateur = 40

    def __init__(self,parent=None,appController=None):
        super(Viewport, self).__init__(parent)
        self.appController = appController
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

    def paintEvent(self, event):
        super(Viewport, self).paintEvent(event)
        qp = QPainter()
        qp.begin(self.viewport())
        rooms = self.appController.getRooms()
        for i in range(0,len(rooms),1):
            square = QRect(10, 10, rooms[i].width*self.multiplicateur, rooms[i].length*self.multiplicateur)
            qp.drawRect(square)
        tables = self.appController.getTables()
        for i in range(0,len(tables),1):
            square = QRect(10, 10, tables[i].tableGroup.width*self.multiplicateur, tables[i].tableGroup.length*self.multiplicateur)
            brush = QBrush()
            brush.setColor(QColor('black'))
            brush.setStyle(Qt.BrushStyle.SolidPattern)
            qp.fillRect(square,brush)
            qp.drawRect(square)
        qp.end()

class DrawerView(QWidget):

    def __init__(self,appController):
        super().__init__()
        self.appController = appController
        self.view = Viewport(self,appController)
        gridLayout = QGridLayout()
        gridLayout.addWidget(self.view, 0, 0, 1, 1)
        self.setLayout(gridLayout)

