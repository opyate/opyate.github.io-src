#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Juan Uys'
SITENAME = "Juan Uys' personal website"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#PLUGIN_PATHS = ['/Users/juanuys/Documents/pelican-static-website-generator/pelican-plugins']
#PLUGINS = []

FILENAME_METADATA = '(?P<slug>.*)'
PATH_METADATA = '(?P<category>[a-zA-Z]+)/(?P<date>\d{4}/\d{2}/\d{2})'
USE_FOLDER_AS_CATEGORY = False

THEME = './grid-theme'
