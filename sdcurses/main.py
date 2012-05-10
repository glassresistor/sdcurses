import sys
import urwid
from .widgets import SDCWidget
from . import DEFAULT_PALETTE

def start(args=sys.argv[1:]):
    palette = DEFAULT_PALETTE
    
    def keystroke (key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()
    view = SDCWidget(*args)
    loop = urwid.MainLoop(view, palette, unhandled_input=keystroke)
    loop.screen.set_terminal_properties(256)
    loop.run()
