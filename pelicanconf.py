#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Skipper Seabold'
SITENAME = u'jseabold.net'
SITEURL = ''

DEFAULT_DATE_FORMAT = '%b %d, %Y'
TIMEZONE = 'US/Eastern'

DEFAULT_LANG = u'en'

# so as not to break links from old site
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = ARTICLE_URL + '/index.html'

INDEX_URL = 'blog'
INDEX_SAVE_AS = INDEX_URL+'/index.html'

# Feed generation is usually not desired when developing
FEED_URL = SITEURL
FEED_ATOM = 'atom.xml'

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social settings
SOCIAL = (('github', 'https://github.com/jseabold'),
          ('twitter', 'https://twitter.com/jseabold'),
          ('gittip', 'https://gittip.com/jseabold'),)
TWITTER_USERNAME = 'jseabold'
DISQUS_SITENAME = 'jseabold'

DEFAULT_PAGINATION = 10

EXTRA_HEADER = open('_nb_header_mod.html').read().decode('utf-8')

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATH = '/home/skipper/src/pelican-plugins/'
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal']

#Github include settings
GITHUB_USER = 'jseabold'
GITHUB_REPO_COUNT = 3
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

# Sharing
TWITTER_USER = 'jseabold'
FACEBOOK_LIKE = False
TWITTER_TWEET_BUTTON = True
TWITTER_LATEST_TWEETS = True
TWITTER_FOLLOW_BUTTON = True
TWITTER_TWEET_COUNT = 3
TWITTER_SHOW_REPLIES = 'false'
TWITTER_SHOW_FOLLOWER_COUNT = 'true'

# Theme stuff
#THEME = "/home/skipper/src/pelican-themes/pelican-cait"

# for pelican-cait
#USE_CUSTOM_MENU = True
#CUSTOM_MENUITEMS = (('Blog', 'blog'),
#                    ('Projects', 'pages/projects.html'),
#                    ('Courses', 'pages/courses.html'),
#                    ('Talks', 'pages/talks.html'),
#                    )
MENUITEMS = (('Blog', '/blog'),
             ('About', '/pages/about'),
             ('Courses', '/pages/courses'),
             ('Home', '/'),
             ('Projects', '/pages/projects'),
             ('Talks', '/pages/talks'),
             )
DISPLAY_PAGES_ON_MENU = False

# for pelican-fresh
THEME = "themes/pelican-fresh"
HIDE_CATEGORIES_FROM_MENU = True

GOOGLE_ANALYTICS = 'UA-28581141-1'

#TEMPLATE_PAGES = {
#                    'src/' : '',
#                 }

# Full HTML or otherwise generated content
#FILES_TO_COPY = (("content/pages/csc432", "csc432"),
#                )
STATIC_PATHS = ["pages/csc432/",
                "pages/presentations/",
                ]
#
EXTRA_PATH_METADATA = {}


import os
def copy_folder(source, path_dict):
    for r, ds, fs in os.walk(source):
        for f in fs:
            dest = os.path.join(r, f).replace('content/', '')
            path_dict.update({dest : {'path' : dest.replace('pages/', '')}})

copy_folder("content/pages/csc432", EXTRA_PATH_METADATA)
copy_folder("content/pages/presentations", EXTRA_PATH_METADATA)

#EXTRA_PATH_METADATA = {"pages/csc432/*" : {'path' : "csc433/*"},
#                }
