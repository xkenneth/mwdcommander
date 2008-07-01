import grok

from viewletmanagers import Navigation, Widget, SideContent, MainContent, Pre, Post
from zope.interface import Interface

class NavigationTop(grok.Viewlet):
    grok.context(Interface)
    grok.viewletmanager(Navigation)
    grok.order(0)
    
    def render(self):
        return """
<b class="b1n"></b>
<b class="b2n"></b>
<b class="b3n"></b>
<b class="b4n"></b>
<div class="contentn">
<div id="nav">
"""

class NavigationBottom(grok.Viewlet):
    grok.context(Interface)
    grok.viewletmanager(Navigation)
    grok.order(3)

    def render(self):
        return """
 </div></div>
<b class="b4n"></b>
<b class="b3n"></b>
<b class="b2n"></b>
<b class="b1n"></b>
"""

class WidgetTop(grok.Viewlet):
    grok.context(Interface)
    grok.viewletmanager(Widget)
    grok.order(0)
    
    def render(self):
        return """
<b class="b1w"></b>
<b class="b2w"></b>
<b class="b3w"></b>
<b class="b4w"></b>
<div class="contentw">
<div id="widget">
"""

class WidgetBottom(grok.Viewlet):
    grok.context(Interface)
    grok.viewletmanager(Widget)
    grok.order(3)

    def render(self):
        return """
 </div></div>
<b class="b4w"></b>
<b class="b3w"></b>
<b class="b2w"></b>
<b class="b1w"></b>
"""


### SideContent ###
class SideContentTop(grok.Viewlet):
    grok.context(Interface)
    grok.viewletmanager(SideContent)
    grok.order(0)
    
    def render(self):
        return """
<b class="b1s"></b>
<b class="b2s"></b>
<b class="b3s"></b>
<b class="b4s"></b>
<div class="contents">
<div id="side">
"""

class SideContentBottom(grok.Viewlet):
    grok.context(Interface)
    grok.viewletmanager(SideContent)
    grok.order(3)

    def render(self):
        return """
 </div></div>
<b class="b4s"></b>
<b class="b3s"></b>
<b class="b2s"></b>
<b class="b1s"></b>
"""

### MainContent ###
class MainContentTop(grok.Viewlet):
    grok.context(Interface)
    grok.viewletmanager(MainContent)
    grok.order(0)
    
    def render(self):
        return """
<b class="b1m"></b>
<b class="b2m"></b>
<b class="b3m"></b>
<b class="b4m"></b>
<div class="contentm">
<div id="main">
"""

class MainContentBottom(grok.Viewlet):
    grok.context(Interface)
    grok.viewletmanager(MainContent)
    grok.order(3)

    def render(self):
        return """
 </div></div>
<b class="b4m"></b>
<b class="b3m"></b>
<b class="b2m"></b>
<b class="b1m"></b>
"""

### Pre Post ###
class PreTop(grok.Viewlet):
    grok.context(Interface)
    grok.viewletmanager(Pre)
    grok.order(0)
    
    def render(self):
        return """
<b class="b1p"></b>
<b class="b2p"></b>
<b class="b3p"></b>
<b class="b4p"></b>
<div class="contentp">
<div id="outer">
"""

class PostBottom(grok.Viewlet):
    grok.context(Interface)
    grok.viewletmanager(Post)
    grok.order(3)

    def render(self):
        return """
 </div></div>
<b class="b4p"></b>
<b class="b3p"></b>
<b class="b2p"></b>
<b class="b1p"></b>
"""


