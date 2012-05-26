import os
import sys
import urwid
from argparse import ArgumentParser

def start(args=None):
    usage = "usage: %prog [options] arg"
    parser = ArgumentParser(usage)
    parser.add_argument('-l', '--location', type=str, dest='location', 
        help='The datacenters location.')
    parser.add_argument('-k', '--key_id', type=str, dest='key_id', 
        help='Key id in the form /user_id/keys/key_id.')
    parser.add_argument('-s', '--settings', type=str, dest='settings_module', 
        help='Python module to use for settings.')
    if args != None:
        args = sys.argv
    args = vars(parser.parse_args(args=args))
    location = args.get('location')
    settings_module = args.get('settings_module')
    key_id = args.get('key_id')
    
    if settings_module:
        os.environ['SDCURSES_SETTINGS'] = settings_module

    if key_id:
        os.environ['SDCURSES_KEY_ID'] = key_id

    if location:
        os.environ['SDCURSES_LOCATION'] = location
        
    from . import widgets
    from . import settings
    
    def keystroke(key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()
    view = widgets.BigFrame()
    loop = urwid.MainLoop(view, settings.PALETTE, unhandled_input=keystroke)
    loop.screen.set_terminal_properties(256)
    loop.run()
