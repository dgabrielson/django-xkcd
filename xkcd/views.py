"""
Views for the xkcd application.
"""
#######################
from __future__ import print_function, unicode_literals

from django.views.generic.dates import (ArchiveIndexView, MonthArchiveView,
                                        YearArchiveView)
from django.views.generic.detail import DetailView

from .models import Comic

#######################




class Comic_Mixin(object):
    
    model = Comic
    date_field = 'date'
    month_format = '%m'
    
    

class Comic_ArchiveIndexView(Comic_Mixin, ArchiveIndexView):
    paginate_by = 6
comic_archive_index = Comic_ArchiveIndexView.as_view()



class Comic_YearArchiveView(Comic_Mixin, YearArchiveView):
    pass
comic_year_archive = Comic_YearArchiveView.as_view()



class Comic_MonthArchiveView(Comic_Mixin, MonthArchiveView):
   make_object_list = True
comic_month_archive = Comic_MonthArchiveView.as_view()



class Comic_DetailView(Comic_Mixin, DetailView):
    slug_field = 'num'
    
    def get_context_data(self, **kwargs):
        """
        Call the base implementation first to get a context
        """
        context = super(Comic_DetailView, self).get_context_data(**kwargs)
        # Add in local context
        if self.object.local_img:
            width = self.object.local_img.width
            context['image_offset'] = -width/2
        return context

comic_detail = Comic_DetailView.as_view()



class LatestComic_DetailView(Comic_DetailView):
    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
            
        return queryset.order_by('-date')[0]
comic_latest = LatestComic_DetailView.as_view()
