# -*- coding: utf-8 -*-
AUTHOR = u'Marcel Hellkamp'
SITENAME = u"cccgoe.de"
SITESUBTITLE = u"Chaos Computer Club Göttingen"
SITEURL = 'https://cccgoe.de/blog'
TIMEZONE = "Europe/Berlin"
FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

GITHUB_URL = 'http://github.com/cccgoe/cccgoe-blog'
MENUITEMS = (('Wiki','/wiki'),)

LINKS = (
  ('python.org','http://python.org/'),
  ('Deutsches Python Forum','http://python-forum.de/'),
  ('Python Wiki','http://wiki.python.de'),
  ('Python Stammtisch Hannover','http://www.python-hannover.de'),
)
      

#SOCIAL = (('twitter', 'http://twitter.com/bottlepy'),
#          ('github', 'http://github.com/defnull'),)

# global metadata to all the contents
#DEFAULT_METADATA = (('yeah', 'it is'),)

# static paths will be copied under the same name
STATIC_PATHS = ["static"]

DELETE_OUTPUT_DIRECTORY = True
