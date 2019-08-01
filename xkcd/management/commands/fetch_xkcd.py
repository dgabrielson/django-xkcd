"""
Fetch an xkcd comic data.
"""
#######################
from __future__ import print_function, unicode_literals

import json
from pprint import pprint

from django.core.management.base import BaseCommand, CommandError

#from django.conf import settings
from xkcd.models import Comic

#######################
try:
    # Python 3:
    from urllib.request import urlopen
except ImportError:
    # Python 2:
    from urllib2 import urlopen




class Command(BaseCommand):
    """
    The command.
    """
    help = 'Fetch a specific xkcd comic (default: latest).'

    
    def add_arguments(self, parser):
        parser.add_argument('num', nargs='*', type=int)
        parser.add_argument('--all', action='store_true',
            help='Fetch *all* the comics')
        parser.add_argument('--all-since', type=int,
            help='Fetch all the comics *after and including* the given one')

        parser.add_argument('--verbose', action='store_true',
            help='Report on what is being done')
    
    
    def fetch_comic(self, num=None, save=True, verbose=False):
        """
        If num is None, fetch the current comic.
        """
        if num is None:
            url = 'http://xkcd.com/info.0.json'
        else:
            url = 'http://xkcd.com/%d/info.0.json' % num
        
        if verbose:
            print('Fetching', url, '...', end=' ')
        handle = urlopen(url)
        byte_s = handle.read()
        text = byte_s.decode('utf-8')
        data = json.loads(text)
        if verbose:
            print('got comic %d' % data['num'])
        if save:
            obj = Comic.objects.from_json(data)
            return obj
        else:
            return data
        


    def handle(self, *args, **options):
        """
        Do the command!
        """
        if options['all'] or options['all_since']:
            # fetch the current, get the number, fetch them all:
            data = self.fetch_comic(save=False, verbose=options['verbose'])
            num = data['num']
            if options['all_since']:
                start = int(options['all_since'])
            else:
                start = 1
            for n in range(start, num+1):
                self.fetch_comic(n, verbose=options['verbose'])
        else:
            num_list = options.get('num', None)
            if num_list:
                for arg in num_list:
                    self.fetch_comic(arg, verbose=options['verbose'])
            else:
                self.fetch_comic(verbose=options['verbose'])
