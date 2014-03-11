import pyy.html
from pyy.html.document import *
from pyy.html.tags import *

def view():
    parent = div(cls='container')
    with parent:

        with div(cls='col-md-8'):
            h2('Titan Cloud')
            h4('Senior Software Engineer')
            p('Brentwood, TN')

            with ul(cls='list-group'):
                li('Created JavaScript library that focuses on making regularly used patterns easy to implement as well as taking steps back from being too jQuery reliant.  The goal was to decrease development time.', cls="list-group-item")
                li('Wrote test suites in Selenium using both the IDE and WebDriver API and created a test environment with Selenium nodes.  The tests were deployed to Selenium nodes and run periodically across multiple browsers.', cls="list-group-item")
                li('Aided in creating a scheduling service that is used as application wide cron management. This is a multi threaded service which uses thread pooling to manage concurrent tasks. A usage example is scheduling a report to run at set increments.', cls="list-group-item")
                li('UI/UX revamp of the entire application. This required creating project plans, client interaction, storyboarding, and requirements gathering while on a 2 week deliverable schedule.', cls="list-group-item")
                li('Created a prototype of the next TitanCloud on AWS using MVC 4, WebAPI, Razor, and Bootstrap.', cls="list-group-item")
                li('Aided in moving Titan\'s platform to AWS.', cls="list-group-item")
                li('Moved Titan from svn to git.', cls="list-group-item")

        with div(cls='col-md-8'):
            h2('GISbiz')
            h4('Software Engineer')
            p('Nashville, TN')

            with ul(cls='list-group'):
                li('Designed and Developed a Javascript mapping application for Cook County, IL using ESRI Javascript 3.1 API on top of ArcGIS Server 9.3.', cls='list-group-item')
                li('Created 4 Flex mapping applications using ESRI Flex API\'s 1.3 - 3.0. All of these applications relied heavily on ArcGIS Server 9.3 - 10.1.', cls='list-group-item')
                li('Developed a data aggregator for GIS data coming from public agencies. The aggregator routinely updates its cache and serves it through WCF services as JSON. A uniform data object was created in order to have the smallest client footprint possible.', cls='list-group-item')
                li('Built a Google Maps application to collect and display the aggregated data. The UI was created using Jquery Mobile with an embedded Google map.', cls='list-group-item')
                li('Created custom Flex UI controls using Actionscript drawing and shading abilities. This drastically reduced load time by creating the design at runtime rather than downloading potentially hundreds of images.', cls='list-group-item')
                li('Created an ArcMap addin application and EditorExtension addin. The editor extension captures feature insert and update events in order to accurately populate attribute data.', cls='list-group-item')
                li('Initiated development of custom JavaScript API for mobile, desktop, and tablet based applications. The API is geared toward GIS based applications.', cls='list-group-item')
                li('Developed backup procedures for all Linux servers. The backups were sent to in house drives as well as Amazon S3. They were written in Bash and Python.', cls='list-group-item')
                li('Developed and coordinated development of TDOT SEMS components in ASP.NET MVC 2.', cls='list-group-item')
                li('Generated NHibernate mappings, domain classes, controllers, views, view models, routing entries and BluePrint CSS user interface.', cls='list-group-item')
                li('Created custom theme for Dojo that was incorporated into the ESRI Javascript 3.0 application.', cls='list-group-item')

        with div(cls='col-md-8'):
            h2('Plant CML')
            h4('Software Engineer')
            p('Franklin, TN')

            with ul(cls='list-group'):
                li('Designed and created a SMS client in C# that can be installed on multiple systems and allow each system to simultaneously send millions of SMS messages to a collection of gateways.', cls='list-group-item')
                li('Created a Flex mapping application that was used for emergency notifications in large metropolitan areas or universities. The application allowed the user to select the areas which would be notified.', cls='list-group-item')

    return parent