# -*- coding: utf-8 -*-
import os

AUTHOR = u'Marcel Hellkamp'
SITENAME = u"cccgoe.de"
SITESUBTITLE = u"Chaos Computer Club Göttingen"
SITEURL = 'https://cccgoe.de/blog'
TIMEZONE = "Europe/Berlin"
FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

GITHUB_URL = 'https://github.com/cccgoe/blog'
MENUITEMS = (('Wiki','/wiki'),)

LINKS = (
  ('cccgoe.de','http://cccgoe.de/'),
)
      
#SOCIAL = (('twitter', 'http://twitter.com/bottlepy'),
#          ('github', 'http://github.com/defnull'),)

# global metadata to all the contents
#DEFAULT_METADATA = (('yeah', 'it is'),)

# static paths will be copied under the same name
STATIC_PATHS = ["static"]

DELETE_OUTPUT_DIRECTORY = True

if 'PREVIEW' in os.environ:
  RELATIVE_URLS=True
