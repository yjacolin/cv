#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Yves Jacolin'
SITENAME = u'CV de Yves Jacolin'
SITEURL = 'http://localhost:8000/'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('OSGeo-fr', 'http://osgeo.asso.fr/'),
#         ('GeoRezo', 'http://georezo.org/'))

# Social widget
SOCIAL = (('github', 'http://github.com/yjacolin'),
          ('twitter', 'http://twitter.com/yjacolin'),
          ('linkedin', 'http://fr.linkedin.com/in/yjacolin'),
          ('talentio', ''))

TWITTER_USERNAME = 'yjacolin'
DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

## Templates settings

#THEME = 'pelican-blueidea'
THEME = 'themes/Flex'
#THEME = 'crowsfoot'
#THEME = 'html5-dopetrope'

# Template pelican-blueidea
PAGES_SORT_ATTRIBUTE = 'sortorder'
ARTICLES_SORT_ATTRIBUTE = 'sortorder'

# Template Flex
MAIN_MENU = True
ROBOTS = 'index, follow'
SITELOGO = ''
SITESUBTITLE = 'Yves Jacolin'
SITEDESCRIPTION = 'Curriculum de Yves Jacolin'
OG_LOCALE = 'fr'
