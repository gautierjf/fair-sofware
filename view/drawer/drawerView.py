from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtCore import  Qt

from view.drawer.tableView import TableView

class Viewport(QGraphicsView):

    multiplicateur = 40

    def __init__(self,parent=None,appController=None):
        super(Viewport, self).__init__(parent)
        self.appController = appController

        scene = QGraphicsScene(self)

        tables = self.appController.getTables()
        for i in range(0,len(tables),1):
            if tables[i].position == "Vertical" :
                width = tables[i].tableGroup.width*self.multiplicateur
                height = tables[i].tableGroup.length*self.multiplicateur
            else:
                width = tables[i].tableGroup.length*self.multiplicateur 
                height = tables[i].tableGroup.width*self.multiplicateur
            new_x = tables[i].x
            new_y = tables[i].y
            item = TableView(new_x, new_y, width, height,i,self.appController)
            scene.addItem(item)
        rooms = self.appController.getRooms()
        #for i in range(0,len(rooms),1):
        #    scene.addRect(10, 10, rooms[i].width*self.multiplicateur, rooms[i].length*self.multiplicateur)


        # self.setTransformationAnchor(self.ViewportAnchor.AnchorUnderMouse)
        # self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        # self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        # self.setResizeAnchor(self.ViewportAnchor.AnchorUnderMouse)

        width = 2600
        height = 2600
        # if  len(rooms) > 0:
        #   room = rooms[0]
        #   width = room.width*self.multiplicateur
        #   height = room.length*self.multiplicateur

        self.setSceneRect(0, 0, width, height)
        self.setFixedSize( width, height)
        #self.fitInView(scene.itemsBoundingRect(),Qt.AspectRatioMode.KeepAspectRatio)
        self.fitInView(scene.itemsBoundingRect())

        self.setScene(scene)
        self.setRenderHints(
            QPainter.RenderHint.Antialiasing
            | QPainter.RenderHint.SmoothPixmapTransform
        )

    
    # def resizeEvent(self, event):
        # super().resizeEvent(event)

class DrawerView(QWidget):

    def __init__(self,appController):
        super().__init__()
        self.appController = appController
        self.view = Viewport(self,appController)
        gridLayout = QGridLayout()
        gridLayout.addWidget(self.view, 0, 0, 1, 1)
        self.setLayout(gridLayout)

