import grok
from megrok.kss import KSSActions

from viewletmanagers import Navigation, MainContent

class AppKSS(KSSActions):

    def welcome(self):
        core = self.getCommandSet('core')
        core.replaceHTML('#click-me', '<p>ME GROK KISSED !</p>')

class MWDCommander(grok.Application, grok.Container):
    pass

class Index(grok.View):
    pass # see app_templates/index.pt

class Welcome(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.view(Index)
