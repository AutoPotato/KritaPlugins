from krita import *
from .csp_icons_for_krita import *

Scripter.addExtension(CSPiconsForKritaExtension(krita.Krita.instance()))

# Information
__version__ = ' qt=5 krita=5.3.5 (Steam) date=2026_11_25 '
__license__ = ' GPLv3+ '
__author__ = ' AutoPotato '
__email__ = ' andrew.t.visual@gmail.com '
__url__ = ' https://github.com/AutoPotato '
