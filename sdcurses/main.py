import sys
import urwid
from .widgets import SDCWidget
from .defaults import PALETTE

def start(args=sys.argv[1:]):
    location = args.pop(0)
    key_id = args.pop(0)
    palette = PALETTE
    
    def keystroke (key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()
    view = SDCWidget(*args)
    
    view.set_sdc(location, key_id)
    loop = urwid.MainLoop(view, palette, unhandled_input=keystroke)
    loop.screen.set_terminal_properties(256)
    loop.run()
