import sys
import urwid
from .widgets import SDCWidget, QuestionWidget
from . import DEFAULT_PALETTE

def start(args=sys.argv[1:]):
    location = args.pop(0)
    key_id = args.pop(0)
    palette = DEFAULT_PALETTE
    
    def keystroke (key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()
    view = SDCWidget(*args)
    
    def next_question(location):
        question = QuestionWidget('Whats your key_id?', view.set_sdc, location)
        view.view.set_footer(question)
    
    question = QuestionWidget('Whats datacenter do you want to look at?', next_question)
    
    view.view.set_footer(question)
    loop = urwid.MainLoop(view, palette, unhandled_input=keystroke)
    loop.screen.set_terminal_properties(256)
    loop.run()
