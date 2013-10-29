from pyy.html import document
from pyy.html.tags import *

class Bradoc(document):
    def __init__(self, title='Brad Janke'):
        super(Bradoc, self).__init__(title=title)

        self.head += meta(name='viewport', content='width=device-width, initial-scale=1.0')
        self.head += link(rel='stylesheet', href=r'//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css')
        self.head += script(src='//ajax.googleapis.com/ajax/libs/jquery/2.0.3/jquery.min.js')
        self.head += script(src='//netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js')

        self.body['style'] = 'padding-top: 15px'