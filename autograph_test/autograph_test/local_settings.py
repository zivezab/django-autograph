import os
import sys

from settings import MIDDLEWARE_CLASSES, INSTALLED_APPS

DEBUG_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../DEBUG').replace('\\','/')
if os.path.exists(DEBUG_DIR): 
    sys.path.append(DEBUG_DIR)
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', 'snippetscream.ProfileMiddleware',)
    INSTALLED_APPS += ('debug_toolbar', 'django_extensions',)
    INTERNAL_IPS = ('127.0.0.1',)
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }