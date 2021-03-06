import os
import sys

settings_module = os.environ.get('SDCURSES_SETTINGS')

if settings_module:
    import importlib
    settings = importlib.import_module(settings_module)
else:
    from . import defaults as settings

this_module = sys.modules[__name__]
for (key, value) in settings.__dict__.iteritems():
    setattr(this_module, key, value)
del this_module
    
if os.environ.get('SDCURSES_KEY_ID'):
   KEY_ID  = os.environ['SDCURSES_KEY_ID']

if os.environ.get('SDCURSES_LOCATION'):
   LOCATIONS = [os.environ['SDCURSES_LOCATION']]
