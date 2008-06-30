import grok

from app import MWDCommander

class AtomPubLayer(grok.IRESTLayer):
    pass

class AtomPubProtocol(grok.RESTProtocol):
   grok.layer(AtomPubLayer)
   grok.name('atompub')

class MyREST(grok.REST):
    grok.context(MWDCommander)
    grok.layer(AtomPubLayer)
    
    def GET(self):
        return "GET request, retrieve container listing"
    
    def POST(self):
        return "POST request, add something to container"
    
    def PUT(self):
        return "PUT request, replace complete contents"
    
    def DELETE(self):
        return "DELETE request, delete this object entirely"
