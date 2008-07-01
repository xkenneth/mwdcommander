### GROK ###
import grok

### GENERIC ###
import os
import pdb
import mx.DateTime

### PYDRILL ###
from PyDrill import DataBase

### KSS ###
#from megrok.kss import KSSActions

### ZOPE ###
from zope.component import getMultiAdapter
from zope.interface import Interface

### ZODB ###
from persistent.list import PersistentList

### APP ###
from viewletmanagers import Navigation, MainContent, Head
from boilerplate import GenericContainer, get_application
from pipetallylog import PipeTallyLog, IPipeTallyLog
from comment import Comment, IComment
from depth import Depth, IDepth


### KSS ###
# class AppKSS(KSSActions):

#     def welcome(self):
#         core = self.getCommandSet('core')
#         core.replaceHTML('#click-me', '<p>ME GROK KISSED !</p>')
    
#     def delete_pipe_tally_log(self,logid=None):
#         #pdb.set_trace()
#         core = self.getCommandSet('core')
#         core.replaceHTML('#'+str(logid), '<span/>')
#         self.context['pipetallies'].item_order.pop(self.context['pipetallies'].item_order.index(int(logid[1:])))
        
### MWD ###
class MWDCommander(grok.Application, grok.Container):
    td_db = DataBase.Layer("localhost",8050)
    def time(self):
        return mx.DateTime.now()

### VIEWS ###
class Index(grok.View):
    grok.context(MWDCommander)
    def update(self):
        #pdb.set_trace()
        pass
    
class BigNumbers(grok.View):
    grok.context(MWDCommander)
    grok.template('index')
    refresh=True

class MWD(grok.View):
    grok.context(MWDCommander)
    grok.template('index')

    def update(self):
        pass

class System(grok.View):
    grok.context(MWDCommander)
    grok.template('index')

class Pulses(grok.View):
    grok.context(MWDCommander)
    grok.template('index')
    refresh = True

class Chirps(grok.View):
    grok.context(MWDCommander)
    grok.template('index')
    refresh = True

class Frames(grok.View):
    grok.context(MWDCommander)
    grok.template('index')
    refresh = True

class ToolStatus(grok.View):
    grok.context(MWDCommander)
    grok.template('index')
    refresh = True

class GammaRay(grok.View):
    grok.context(MWDCommander)
    grok.template('index')
    refresh = True

class Azimuth(grok.View):
    grok.context(MWDCommander)
    grok.template('index')
    refresh = True

class Inclination(grok.View):
    grok.context(MWDCommander)
    grok.template('index')
    refresh = True

class GX(grok.View):
    grok.context(MWDCommander)
    grok.template('index')
    refresh = True

class GY(grok.View):
    grok.context(MWDCommander)
    grok.template('index')
    refresh = True

class GZ(grok.View):
    grok.context(MWDCommander)
    grok.template('index')
    refresh = True

class HX(grok.View):
    grok.context(MWDCommander)
    grok.template('index')
    refresh = True

class HY(grok.View):
    grok.context(MWDCommander)
    grok.template('index')
    refresh = True

class HZ(grok.View):
    grok.context(MWDCommander)
    grok.template('index')
    refresh = True

class PulseCount(grok.View):
    grok.context(MWDCommander)
    grok.template('index')
    refresh = True

class PipeTally(grok.View):
    grok.template('index')

    def update(self):
        try:
            self.context['pipetallies']
        except:
            self.context['pipetallies'] = GenericContainer('Pipe Tally Container',0)

class Comments(grok.View):
    grok.template('index')
    def update(self):
        try:
            self.context['commentslist']
        except KeyError:
            self.context['commentslist'] = GenericContainer('Comments Container',0)

class DepthLog(grok.View):
    grok.template('index')
    def update(self):
        try:
            self.context['depthlist']
        except KeyError:
            self.context['depthlist'] = GenericContainer('Depth Container',0)

### VIEWLETS ###

class AppCSS(grok.Viewlet):
    grok.viewletmanager(Head)
    grok.context(Interface)

class Welcome(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.view(Index)
    grok.order(2)
    

class ConnectionStatus(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.view(System)
    grok.order(1)

class PipeTallyLogList(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.view(PipeTally)
    grok.order(2)

### Pipe Tally Log Management ###
class AddPipeTallyLog(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.order(1)
    grok.view(PipeTally)
    
    def update(self):
        self.form = getMultiAdapter((self.context,self.request), name=u'addpipetallylogform')
        self.form.update_form()
        
    def render(self):
        return self.form.render()

class AddPipeTallyLogForm(grok.AddForm):
    grok.context(MWDCommander)
    form_fields = grok.AutoFields(PipeTallyLog)
    template = grok.PageTemplate(filename=os.path.join('app_templates','edit_form.pt'))
    
    @grok.action('Add Pipe Tally Log')
    def add(self, **data):
        #see if the container exists
        
        
        data['id'] = unicode(self.context['pipetallies'].item_count)

        obj = PipeTallyLog(**data)
            
        #add the tally log
        self.context['pipetallies'].add_item(obj)

        app = get_application(self.context)
        self.redirect(self.url(app,'pipetally'))


### Comments Management ###
class ViewComments(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.order(2)
    grok.view(Comments)
    
    def update(self):
        #pdb.set_trace()
        pass

class ViewDepth(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.order(2)
    grok.view(DepthLog)
    
    def update(self):
        pass
    

class AddComment(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.order(1)
    grok.view(Comments)
    
    def update(self):
        self.form = getMultiAdapter((self.context, self.request), name=u'addcommentform')
        self.form.update_form()

    def render(self):
        return self.form.render()

class AddDepth(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.order(1)
    grok.view(DepthLog)
     
    def update(self):
        self.form = getMultiAdapter((self.context, self.request), name=u'adddepthform')
        self.form.update_form()

    def render(self):
        return self.form.render()

class AddCommentForm(grok.AddForm):
    grok.context(MWDCommander)
    form_fields = grok.AutoFields(Comment)
    template = grok.PageTemplate(filename=os.path.join('app_templates','edit_form.pt'))

    @grok.action('Add Comment')
    def add(self, **data):
        data['id'] = unicode(self.context['commentslist'].item_count)
        
        obj = Comment(**data)
        
        self.context['commentslist'].add_item(obj)

        app = get_application(self.context)
        self.redirect(self.url(app,'comments'))

class AddDepthForm(grok.AddForm):
    grok.context(MWDCommander)
    form_fields = grok.AutoFields(Depth)
    template = grok.PageTemplate(filename=os.path.join('app_templates','edit_form.pt'))

    @grok.action('Add Depth')
    def add(self, **data):
        data['id'] = unicode(self.context['depthlist'].item_count)
        
        obj = Depth(**data)
        
        self.context['depthlist'].add_item(obj)

        app = get_application(self.context)
        self.redirect(self.url(app,'depthlog'))

### XML-RPC ###

class MWDCommanderXMLRPC(grok.XMLRPC):
    def latestROP(self):
        try:
            start = self.context['pipetallies'].max().max().start
            save = self.context['pipetallies'].max().max().end
            end = self.context['pipetallies'].max().max().end
        except IndexError:
            return None

        if start is None or end is None:
            return None

        start = mx.DateTime.DateTimeFrom(str(start))
        end = mx.DateTime.DateTimeFrom(str(end))

        delta = end - start

        delta = float(delta)/60.0
        
        data = [delta,save]

        return data

    def latestDepth(self):
        try:
            depth = self.context['depthlist'].max()
        except IndexError:
            return None
        
        return [depth.depth, depth.time]
