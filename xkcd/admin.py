#######################
from __future__ import print_function, unicode_literals

from django.contrib import admin

from .models import Comic

#######################





class Comic_Admin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display = ['num', 'title', 'img', 'date', ]
    list_display_links = ['title', ]
    list_filter = ['date', ]
    search_fields = ['title',  ]
    ordering = ['-num', ]
    readonly_fields = ['num', 'title', 'safe_title', 'date', 'img', 'alt', 
                       'link', 'news', 'transcript', ]

admin.site.register(Comic, Comic_Admin)
