#######################
from __future__ import print_function, unicode_literals

#######################
from django.contrib.syndication.views import Feed

from .models import Comic


class ComicFeed(Feed):
    title = "xkcd Comics"
    link = "/xkcd/"
    description = "Local xkcd feed"
    #title_template = 'xkcd/feed/title.html'
    description_template = 'xkcd/feed/description.html'

    def items(self):
        return Comic.objects.order_by('-date')[:12]
        
    def item_title(self, item):
        return item.title
