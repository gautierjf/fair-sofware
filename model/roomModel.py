
from PyQt6.QtCore import QAbstractListModel,Qt

class RoomModel(QAbstractListModel):
    def __init__(self, rooms, parent=None):
        super().__init__(parent)
        self.rooms = rooms

    def data(self, index, role):
        if role == Qt.DisplayRole:
            room = self.rooms[index.row()]
            return room

    def rowCount(self, index):
        return len(self.rooms)