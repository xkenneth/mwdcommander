### GROK ###
import grok

### GENERIC ###
import os
import pdb

### KSS ###
#from megrok.kss import KSSActions

### ZOPE ###
from zope.component import getMultiAdapter
from zope.interface import Interface

### ZODB ###
from persistent.list import PersistentList

### APP ###
from viewletmanagers import Navigation, MainContent
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
    pass

### VIEWS ###

class Index(grok.View):
    grok.context(MWDCommander)
    pass # see app_templates/index.pt

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
class Welcome(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.view(Index)

class PipeTallyLogList(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.view(PipeTally)
    grok.order(1)

### Pipe Tally Log Management ###
class AddPipeTallyLog(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.order(0)
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
    grok.order(1)
    grok.view(Comments)
    
    def update(self):
        #pdb.set_trace()
        pass

class ViewDepth(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.order(1)
    grok.view(DepthLog)
    
    def update(self):
        pass
    

class AddComment(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.order(0)
    grok.view(Comments)
    
    def update(self):
        self.form = getMultiAdapter((self.context, self.request), name=u'addcommentform')
        self.form.update_form()

    def render(self):
        return self.form.render()

class AddDepth(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.order(0)
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
    def hello(self):
        return 'Hello world!'

        

        
            
        



        
