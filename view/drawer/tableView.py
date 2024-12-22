
from PyQt6.QtWidgets import (
    QGraphicsItem,QGraphicsRectItem
)
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtCore import  Qt


class TableView(QGraphicsRectItem):
    
    multiplicateur = 40


    def __init__(self, x,y,w,h,index,appController):
        super().__init__(x,y,w,h)
        self.appController = appController
        self.index = index
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        pen = QPen()
        pen.setWidth(1)
        pen.setColor(QColor('red'))
        
        brush = QBrush()
        brush.setColor(QColor('red'))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        self.setPen(pen)
        self.setBrush(brush)


    def mouseReleaseEvent(self, event):
        new_position = self.scenePos()
        self.appController.updatePositionTable(self.index,new_position.x(),new_position.y())
        super().mouseReleaseEvent(event)
