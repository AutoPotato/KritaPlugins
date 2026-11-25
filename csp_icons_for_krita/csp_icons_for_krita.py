from krita import *
from PyQt5 import *
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
        # Krita.instance().icon("KisToolSelectOutline"button)
        # Krita.instance().icon("tool_outline_selection")
        cspIconPath = os.path.join(os.path.dirname(__file__), "tool_outline_selection.svg")
        iconReplace = QIcon(cspIconPath)
        Krita.instance().action("KisToolSelectOutline").setIcon(iconReplace)
