import pyy.html
from pyy.html.document import *
from pyy.html.tags import *
import resume as resumeview

class Views(object):
    def getView(self):
        with div(a(name='top'), cls='container'):
            self.navigation()
            self.header()
            self.about()
            self.resume()
            #self.contact()
            self.footer()

    def topButton(self):
        return a('top', cls='btn btn-primary btn-xs pull-right', href='#top')

    def navigation(self):
        with div(cls='navbar navbar-inverse', role='navigation'):
            with div(cls='navbar-header'):
                with button(type='button', cls='navbar-toggle', data_toggle='collapse', data_target='.navbar-ex1-collapse'):
                    span('Toggle navigation', cls='sr-only')
                    span(cls='icon-bar')
                    span(cls='icon-bar')
                    span(cls='icon-bar')
                span('Brad Janke', cls='navbar-brand')
            with div(cls='collapse navbar-collapse navbar-ex1-collapse'):
                with ul(cls='nav navbar-nav'):
                    li(a('About', href='#about'))
                    li(a('Resume', href='#resume'))
                    #li(a('Contact', href='#contact'))

    def header(self):
        header = div(cls='page-header')
        with header:
            with h1('Welcome to my site.'):
                small('I program and design things.')

    def about(self):
        about = div(a(name='about'), cls='panel panel-default')
        with about:
            with div('About', cls='panel-heading'):
                self.topButton()
            with div(cls='panel-body'):
                p('My name is Brad and I like building things. This site is about the applications I can build.')
                with div(cls='btn-group-horizontal btn-group-lg'):
                    with a(cls='btn btn-primary', href='http://github.com/bradj', target='_new'):
                        i(cls='fa fa-github')
                    with a(cls='btn btn-primary', href='http://bitbucket.org/bradj', target='_new'):
                        i(cls='fa fa-bitbucket')

    def resume(self):
        resume = div(a(name='resume'), cls='panel panel-default')
        with resume:
            with div('Resume', cls='panel-heading'):
                self.topButton()
            resumeview.view()

    def contact(self):
        contact = div(a(name='contact'), cls='panel panel-default')
        with contact:
            with div('Contact', cls='panel-heading'):
                self.topButton()
            with div(cls='panel-body'):
                span('Coming soon.')

    def footer(self):
        footer = div()
        with footer:
            small('Ubuntu')
            small(cls='glyphicon glyphicon-chevron-right')
            small('nginx')
            small(cls='glyphicon glyphicon-chevron-right')
            small('tornado')