"""
Models for the xkcd application.

curl http://xkcd.com/info.0.json

{
#    "img": "http://imgs.xkcd.com/comics/formal_logic.png",
#    "title": "Formal Logic",
#    "month": "3",
#    "num": 1033,
#    "link": "",
#    "year": "2012",
    "news": "",
#    "safe_title": "Formal Logic",
    "transcript": "",
#    "alt": "Note that this implies you should NOT honk solely because I stopped for a pedestrian and you're behind me.",
#    "day": "23"
}
"""
from __future__ import print_function, unicode_literals

from datetime import date

from django.core.files.base import ContentFile
from django.db import models
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible

from . import conf

#######################################################################

try:
    # Python 3:
    from urllib.parse import urlparse
    from urllib.request import urlopen
except ImportError:
    # Python 2:
    from urlparse import urlparse
    from urllib2 import urlopen



#######################################################################

IMG_UPLOAD_TO = conf.get('local_img_path')


#######################################################################

class Comic_Manager(models.Manager):

    def from_json(self, jsondata):
        data = {}
        data.update(jsondata)

        d = date(*[int(e) for e in (data["year"], data["month"], data["day"])])
        del data["year"]
        del data["month"]
        del data["day"]
        data["date"] = d

        num = data["num"]
        obj, created = self.get_or_create(num=num, defaults=data)
        if created:
            # try fetching the img [local copy] -- done in model.save
            pass
        else:
            # refresh data:
            do_save = False
            for key in data:
                old_value = getattr(obj, key)
                value = data[key]
                if old_value != value:
                    setattr(obj, key, value)
                    do_save = True
            if do_save:
                obj.save()
        return obj


#######################################################################

@python_2_unicode_compatible
class Comic(models.Model):
    """
    The data model for a comic.
    """
    # core data from xkcd json:
    num = models.PositiveIntegerField(unique=True)
    title = models.CharField(max_length=256)
    safe_title = models.CharField(max_length=256)
    date =  models.DateField()
    img = models.CharField(max_length=256)
    alt = models.TextField(blank=True)
    link = models.CharField(max_length=256, blank=True)
    news = models.TextField(blank=True)
    transcript = models.TextField(blank=True)

    # additional data:
    local_img =  models.ImageField(upload_to=IMG_UPLOAD_TO, max_length=512,
                                   blank=True, null=True,
                                   verbose_name='local comic image')


    objects = Comic_Manager()


    class Meta:
        ordering = ('date', )


    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        self.retrieve_img()
        return super(Comic, self).save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('xkcd-detail', kwargs={'slug': self.num})


    def retrieve_img(self, overwrite=False, timeout=5, save=False):
        """
        Retreive the img file and store it to local_img.

        If overwrite is True, then do this even when there is already
        a local_img.

        Caution: This method hits the public internet.
        It may be slow to run.  Hence the timeout parameter (in seconds)

        If save is True, then the Comic model's save() method is called
        automatically.

        Reference:
            http://garrett.im/django/2011/09/19/saving-django-imagefield.html
            [2012-Jun-28]
        """
        if self.local_img and not overwrite:
            return

        link = urlopen(self.img, timeout=timeout)
        name = urlparse(link.geturl()).path.split('/')[-1]
        self.local_img = name
        self.local_img.save(name, ContentFile(link.read()), save=save)




#######################################################################
