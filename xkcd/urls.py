"""
Url patterns for the xkcd application.
"""
#######################
from __future__ import print_function, unicode_literals

from django.conf.urls import url

from .feeds import ComicFeed
from .views import *

#######################





urlpatterns = [
    url(r'^$',
        comic_latest,
        name='xkcd-latest',
        ),
    url(r'^(?P<slug>\d+)/$',
        comic_detail,
        name='xkcd-detail',
        ),
    url(r'^archive/$', 
        comic_archive_index,
        name='xkcd-archive-index',
        ),
    url(r'^archive/(?P<year>\d{4})/$',
        comic_year_archive,
        name='xkcd-year-archive',
        ),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d{1,2})/$',
        comic_month_archive,
        name='xkcd-month-archive',
        ),
    url(r'^feed/$',
        ComicFeed(),
        name='xkcd-feed',
        ),
    ]
