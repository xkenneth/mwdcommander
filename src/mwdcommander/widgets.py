import grok
import pdb

from viewletmanagers import Widget
from zope.interface import Interface

### APP ###
from app import MWDCommander

class Clock(grok.Viewlet):
    grok.context(MWDCommander)
    grok.viewletmanager(Widget)
