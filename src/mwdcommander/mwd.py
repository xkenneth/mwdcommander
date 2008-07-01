import grok

from app import MWD,MWDCommander, Pulses, Chirps, ToolStatus, GammaRay, Inclination, Azimuth, GX, GY, GZ, HX, HY, HZ, PulseCount, BigNumbers

from viewletmanagers import MainContent, SideContent

from zope.interface import Interface

class Nav(grok.Viewlet):
    grok.context(MWDCommander)
    grok.view(MWD)
    grok.viewletmanager(SideContent)
    grok.order(1)

class BigNumbersViewlet(grok.Viewlet):
    grok.context(MWDCommander)
    grok.viewletmanager(MainContent)
    grok.view(BigNumbers)
    grok.order(1)

class MWDViewlet(grok.Viewlet):
    grok.context(MWDCommander)
    grok.viewletmanager(MainContent)
    grok.view(MWD)
    grok.order(1)
    
