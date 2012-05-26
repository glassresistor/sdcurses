import urwid
from smartdc import DataCenter, DEBUG_CONFIG
from . import settings

class SMWidget(urwid.WidgetWrap):

    def __init__ (self, id, description):
        self.id = id
        self.content = 'item %s: %s...' % (str(id), description[:25])
        self.item = [
            ('fixed', 15, urwid.Padding(urwid.AttrWrap(
                urwid.Text('item %s' % str(id)), 'body', 'focus'), left=2)),
            urwid.AttrWrap(urwid.Text('%s' % description), 'body', 'focus'),
        ]
        w = urwid.Columns(self.item)
        self.__super.__init__(w)

    def selectable (self):
        return True

    def keypress(self, size, key):
        return key


class SDCWidget(urwid.ListBox):
    def __init__(self, location):
        self.sdc = DataCenter(location=location, key_id=settings.KEY_ID, 
            allow_agent=settings.ALLOW_AGENT)
        vms = self.sdc.machines()
        items = []
        for (i, vm) in enumerate(vms):
            items.append(SMWidget(i, '%s - %s' % (vm.name, vm.public_ips[0])))
        super(SDCWidget, self).__init__(urwid.SimpleListWalker(items))
            
    
class BigFrame(urwid.Frame):
    def __init__(self):
        for location in settings.LOCATIONS:
            sdc = SDCWidget(location)
        super(BigFrame, self).__init__(sdc,
            footer=urwid.AttrWrap(urwid.Text(''), 'head'))
