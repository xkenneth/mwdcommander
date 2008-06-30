import grok

from app import MWD,MWDCommander, Pulses, Chirps, ToolStatus, GammaRay, Inclination, Azimuth, GX, GY, GZ, HX, HY, HZ, PulseCount, BigNumbers

from viewletmanagers import MainContent, SideContent

class Nav(grok.Viewlet):
    grok.context(MWDCommander)
    grok.viewletmanager(SideContent)
    grok.order(0)

class BigNumbersViewlet(grok.Viewlet):
    grok.context(MWDCommander)
    grok.viewletmanager(MainContent)
    grok.view(BigNumbers)
    
class PulsesViewlet(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.context(MWDCommander)
    grok.view(Pulses)

class ChirpsViewlet(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.context(MWDCommander)
    grok.view(Chirps)

class ToolStatusViewlet(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.context(MWDCommander)
    grok.view(ToolStatus)

class AzimuthViewlet(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.context(MWDCommander)
    grok.view(Azimuth)

class InclinationViewlet(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.context(MWDCommander)
    grok.view(Inclination)

class GammaRayViewlet(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.context(MWDCommander)
    grok.view(GammaRay)

class GXViewlet(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.context(MWDCommander)
    grok.view(GX)

class GYViewlet(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.context(MWDCommander)
    grok.view(GY)

class GZViewlet(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.context(MWDCommander)
    grok.view(GZ)

class HXViewlet(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.context(MWDCommander)
    grok.view(HX)

class HYViewlet(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.context(MWDCommander)
    grok.view(HY)

class HZViewlet(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.context(MWDCommander)
    grok.view(HZ)

class PulseCountViewlet(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.context(MWDCommander)
    grok.view(PulseCount)


