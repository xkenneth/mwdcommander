import grok
import pdb

from zope.interface import Interface
from zope.schema import Text, Datetime

class IComment(Interface):
    comment = Text(title=u"Comment:")
    time = Datetime(title=u"Time:")


class Comment(grok.Model):
    grok.implements(IComment)
    def __init__(self,comment,time,id):
        self.id = int(id)
        self.comment = comment
        self.time = time
    

