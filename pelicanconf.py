#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'nikhil'
SITENAME = u'techdroid'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'mytheme'
#THEME = 'dev-random2'
DEFAULT_DATE = 'fs'
JINJA_EXTENSIONS = ['jinja2.ext.loopcontrols']
DIRECT_TEMPLATES = ['blog']
#DIRECT_TEMPLATES = ['index', 'blog']
PAGINATED_DIRECT_TEMPLATES = ['blog']
DEFAULT_PAGINATION = 3
TYPOGRIFY = True
STATIC_PATHS = [
    'images',
    'extras'
    ]
EXTRA_PATH_METADATA = {
    'extras/htaccess': {'path': '.htaccess'},
    }

PLUGIN_PATH = '../pelican-plugins'
PLUGINS = ['multiple_files']
