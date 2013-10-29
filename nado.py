from pyy.web.tornado_simple_server import *
from bradoc import Bradoc
from pyy.html.tags import *

from views.index import Views

def testing():
    div('here goes nothing')

@get('^/$')
@Bradoc(title='Brad Janke')
def index(request):
    v = Views()
    v.getView()

server.add_static_route(r'/static/(.*)', 'static')
server.run(static_path='static')