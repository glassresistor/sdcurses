import sys
import urwid
from .widgets import SDCWidget
from .defaults import PALETTE
from argparse import ArgumentParser

def start(args=None):
    usage = "usage: %prog [options] arg"
    parser = ArgumentParser(usage)
    parser.add_argument('-l', '--location', type=str, dest='location', 
        help='The datacenters location.')
    parser.add_argument('-k', '--key_id', type=str, dest='key_id', 
        help='Key id in the form /user_id/keys/key_id.')
    if args != None:
        args = sys.argv
    args = vars(parser.parse_args(args=args))
    location = args.pop('location')
    key_id = args.pop('key_id')
    palette = PALETTE
    
    def keystroke (key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()
    
    view = SDCWidget()
    
    view.set_sdc(location, key_id)
    loop = urwid.MainLoop(view, palette, unhandled_input=keystroke)
    loop.screen.set_terminal_properties(256)
    loop.run()
