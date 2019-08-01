"""
The DEFAULT configuration is loaded when the named _CONFIG dictionary
is not present in your settings.
"""
#######################
from __future__ import print_function, unicode_literals

from django.conf import settings

#######################

CONFIG_NAME = 'XKCD_CONFIG'    # must be uppercase!



DEFAULT = {

    'local_img_path': 'xkcd/img/%Y/%m/%d',
    
}


#########################################################################




def get(setting):
    """
    get(setting) -> value

    setting should be a string representing the application settings to
    retrieve.
    """
    assert setting in DEFAULT, 'the setting %r has no default value' % setting
    app_settings = getattr(settings, CONFIG_NAME, DEFAULT)
    return app_settings.get(setting, DEFAULT[setting])


def get_all():
    """
    Return all current settings as a dictionary.
    """
    app_settings = getattr(settings, CONFIG_NAME, DEFAULT)
    return dict([(setting, app_settings.get(setting, DEFAULT[setting])) \
                 for setting in DEFAULT])

#########################################################################
