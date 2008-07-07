import grok
import pdb
import datetime

from zope.interface import Interface
from zope.schema import TextLine, Datetime, Float

class IDepth(Interface):
    depth = Float(title=u"Depth:")
    time = Datetime(title=u"Time:")
    

class Depth(grok.Model):
    grok.implements(IDepth)
    def __init__(self,depth,time,id):
        t = datetime.timedelta(hours=2)
        self.id = int(id)
        self.depth = int(depth)
        self.time = time + t
