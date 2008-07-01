import grok

from app import MWD,MWDCommander, Pulses, Chirps, ToolStatus, GammaRay, Inclination, Azimuth, GX, GY, GZ, HX, HY, HZ, PulseCount, BigNumbers

from viewletmanagers import MainContent, SideContent

from zope.interface import Interface

class Nav(grok.Viewlet):
    grok.context(Interface)
    grok.viewletmanager(SideContent)
    grok.order(1)

class BigNumbersViewlet(grok.Viewlet):
    grok.context(MWDCommander)
    grok.viewletmanager(MainContent)
    grok.view(BigNumbers)
    grok.order(1)
    
class PulsesViewlet(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.context(MWDCommander)
    grok.view(Pulses)
    grok.order(1)

class ChirpsViewlet(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.context(MWDCommander)
    grok.view(Chirps)
    grok.order(1)

class ToolStatusViewlet(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.context(MWDCommander)
    grok.view(ToolStatus)
    grok.order(1)

class AzimuthViewlet(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.context(MWDCommander)
    grok.view(Azimuth)
    grok.order(1)

class InclinationViewlet(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.context(MWDCommander)
    grok.view(Inclination)
    grok.order(1)

class GammaRayViewlet(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.context(MWDCommander)
    grok.view(GammaRay)
    grok.order(1)

class GXViewlet(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.context(MWDCommander)
    grok.view(GX)
    grok.order(1)

class GYViewlet(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.context(MWDCommander)
    grok.view(GY)
    grok.order(1)

class GZViewlet(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.context(MWDCommander)
    grok.view(GZ)
    grok.order(1)

class HXViewlet(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.context(MWDCommander)
    grok.view(HX)
    grok.order(1)

class HYViewlet(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.context(MWDCommander)
    grok.view(HY)
    grok.order(1)

class HZViewlet(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.context(MWDCommander)
    grok.view(HZ)
    grok.order(1)

class PulseCountViewlet(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.context(MWDCommander)
    grok.view(PulseCount)
    grok.order(1)


