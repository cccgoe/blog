# -*- coding: utf-8 -*-
import os

PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'blog-src/'))

AUTHOR = u'Marcel Hellkamp'
SITENAME = u"cccgoe/blog"
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


# Copy everything from the source directory to the ourpur directory
STATIC_PATHS = []

for path, dirs, files in os.walk(PATH):
  for fname in files:
    STATIC_PATHS.append(os.path.relpath(os.path.join(path, fname), PATH))

DELETE_OUTPUT_DIRECTORY = True

if 'PREVIEW' in os.environ:
  RELATIVE_URLS=True
