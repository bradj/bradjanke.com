import pyy.html
from pyy.html.document import *
from pyy.html.tags import *
import resume as resumeview

def topButton():
    return a('top', cls='btn btn-primary btn-xs pull-right', href='#top')

def view():
    d = document()

    d.title = 'Brad Janke'
    d.head += meta(name='viewport', content='width=device-width, initial-scale=1.0')
    d.head += link(rel='stylesheet', href=r'//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css')

    container = div(a(name='top'), cls='container')
    nav = div(cls='navbar navbar-inverse', role='navigation')

    # navigation
    with nav:
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
                li(a('Contact', href='#contact'))

    # header
    header = div(cls='page-header')
    with header:
        with h1('Welcome to my site.'):
            small('I program and design things.')

    # about
    about = div(a(name='about'), cls='panel panel-default')
    with about:
        with div('About', cls='panel-heading'):
            topButton()
        with div(cls='panel-body'):
            p('My name is Brad and I like building things. This site is about the applications I can build.')
            with div(cls='btn-group-vertical btn-group-md'):
                button('github', cls='btn btn-primary', href='http://github.com/bradj')
                button('bitbucket', cls='btn btn-primary', href='http://bitbucket.com/bradj')

    # resume
    resume = div(a(name='resume'), cls='panel panel-default')
    with resume:
        with div('Resume', cls='panel-heading'):
            topButton()
        resumeview.view()

    # contact
    contact = div(a(name='contact'), cls='panel panel-default')
    with contact:
        with div('Contact', cls='panel-heading'):
            topButton()
        with div(cls='panel-body'):
            span('Coming soon.')

    # footer
    footer = div()
    with footer:
        small('Ubuntu')
        small(cls='glyphicon glyphicon-chevron-right')
        small('nginx')
        small(cls='glyphicon glyphicon-chevron-right')
        small('tornado')

    container += nav
    container += header
    container += about
    container += resume
    container += contact
    container += footer
    d.body += container
    d.body['style'] = 'padding-top: 15px'

    return d.render()