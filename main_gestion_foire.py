import sys

from model.room import Room
from model.door import Door
from model.roomModel import RoomModel
from model.exponent import Exponent
from model.table import Table
from model.tableGroup import TableGroup

from view.createRoomView import CreateRoomView
from view.displayRoomView import DisplayRoomView

from view.createDoorView import CreateDoorView
from view.displayDoorView import DisplayDoorView

from view.displayTableGroupView import DisplayTableGroupView
from view.createTableGroupView import CreateTableGroupView

from view.displayTableView import DisplayTableView
from view.createTableView import CreateTableView

from view.displayExponentView import DisplayExponentView
from view.createExponentView import CreateExponentView

from view.drawerView import DrawerView

from controller.appController import AppController

import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *



class MainWindow(QMainWindow, ):

    appController = AppController()
    doors = []
    exponents = []
    selectedExponent : Exponent
    tableGroups = []
    selectedTableGroup : TableGroup
    tables = []
    selectedTable : Table
    rooms = []
    selectedRoom : Room

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestion foire")
        
        button_action = QAction(QIcon("bug.png"), "&Créer salle", self)
        button_action.triggered.connect(self.displayCreateRoom)

        button_action2 = QAction(QIcon("bug.png"), "&Salles", self)
        button_action2.triggered.connect(self.displayRooms)

        button_action5 = QAction(QIcon("bug.png"), "voir salles", self)
        button_action5.triggered.connect(self.displayDrawer)

        button_action3= QAction(QIcon("bug.png"), "&Créer porte", self)
        button_action3.triggered.connect(self.displayCreateDoor)

        button_action4= QAction(QIcon("bug.png"), "&Portes", self)
        button_action4.triggered.connect(self.displayDoors)


        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()

        room_menu = menu.addMenu("&Salles")
        room_menu.addAction(button_action)
        room_menu.addAction(button_action2)
        room_menu.addAction(button_action5)
        room_menu.addSeparator()
        room_menu.addAction(button_action3)
        room_menu.addAction(button_action4)

        button_action = QAction(QIcon("bug.png"), "&Créer groupe de tables", self)
        button_action.setStatusTip("")
        button_action.triggered.connect(self.displayCreateTableGroup)

        button_action2 = QAction(QIcon("bug.png"), "&Groupes de tables", self)
        button_action2.setStatusTip("")
        button_action2.triggered.connect(self.displayTableGroups)

        button_action3= QAction(QIcon("bug.png"), "&Créer table", self)
        button_action3.setStatusTip("")
        button_action3.triggered.connect(self.displayCreateTable)

        button_action4= QAction(QIcon("bug.png"), "&Tables", self)
        button_action4.setStatusTip("")
        button_action4.triggered.connect(self.displayTables)

        table_menu = menu.addMenu("&Tables")
        table_menu.addAction(button_action)
        table_menu.addAction(button_action2)
        table_menu.addSeparator()
        table_menu.addAction(button_action3)
        table_menu.addAction(button_action4)

        button_action = QAction(QIcon("bug.png"), "&Créer exposant", self)
        button_action.setStatusTip("")
        button_action.triggered.connect(self.displayCreateExponent)

        button_action2 = QAction(QIcon("bug.png"), "&Exposants", self)
        button_action2.setStatusTip("")
        button_action2.triggered.connect(self.displayExponents)

        button_action3= QAction(QIcon("bug.png"), "&Importer exposant", self)
        button_action3.setStatusTip("")
        button_action3.triggered.connect(self.displayImportExponents)

        button_action4= QAction(QIcon("bug.png"), "&Exporter exposant", self)
        button_action4.setStatusTip("")
        button_action4.triggered.connect(self.displayExportExponents)
        
        exponent_menu = menu.addMenu("&Exposants")
        exponent_menu.addAction(button_action)
        exponent_menu.addAction(button_action2)
        exponent_menu.addSeparator()
        exponent_menu.addAction(button_action3)
        exponent_menu.addAction(button_action4)

        button_action = QAction(QIcon("bug.png"), "&Contenu", self)
        button_action.setStatusTip("")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)

        button_action2 = QAction(QIcon("bug.png"), "&A propos", self)
        button_action2.setStatusTip("")
        button_action2.triggered.connect(self.displayAbout)
        button_action2.setCheckable(True)

        help_menu = menu.addMenu("&Aide")
        help_menu.addAction(button_action)
        help_menu.addAction(button_action2)

    def onMyToolBarButtonClick(self, s):
        print("click", s)
 
    def displayCreateRoom(self, s):  
        widget = CreateRoomView(self.appController)
        self.setCentralWidget(widget)

    def displayDrawer(self, s):  
        widget = DrawerView(self.appController)
        self.setCentralWidget(widget)

    def displayRooms(self, s):
        widget = DisplayRoomView(self.appController)
        self.setCentralWidget(widget)

    def displayCreateDoor(self, s):
        widget = CreateDoorView(self.appController)
        self.setCentralWidget(widget)

    def displayDoors(self, s):
        widget = DisplayDoorView(self.appController)
        self.setCentralWidget(widget)

    def displayCreateTableGroup(self, s):
        widget = CreateTableGroupView(self.appController)
        self.setCentralWidget(widget)
  
    def displayTableGroups(self, s):
        widget = DisplayTableGroupView(self.appController)
        self.setCentralWidget(widget)
  
    def displayCreateTable(self, s):
        widget = CreateTableView(self.appController)
        self.setCentralWidget(widget)

    def displayTables(self, s):
        widget = DisplayTableView(self.appController)
        self.setCentralWidget(widget)

    def displayExponents(self, s):
        widget = DisplayExponentView(self.appController)
        self.setCentralWidget(widget)           

    def displayCreateExponent(self, s):
        widget = CreateExponentView(self.appController)
        self.setCentralWidget(widget)

    def displayImportExponents(self, s):
        label = QLabel("Import exponents")
        self.setCentralWidget(label)       

    def displayExportExponents(self, s):
        label = QLabel("Export exponents")
        self.setCentralWidget(label)     

    def displayAbout(self, s):
        label = QLabel("About")
        self.setCentralWidget(label)     

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
