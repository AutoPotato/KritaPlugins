from krita import *
from PyQt5 import *
from .Tool_List import newIconName
import os

class CSPiconsForKritaExtension(Extension):
    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction("csp_icons_for_krita", "CSP Icons", "tools/scripts")
        action.triggered.connect(self.CSPiconReplace)

    def CSPiconReplace(self):
        for id, image in newIconName.items():
            newIconPath = os.path.join(os.path.dirname(__file__), "Selected_Icons", image)
            iconReplacement = QIcon(newIconPath)
            Krita.instance().action(id).setIcon(iconReplacement)
