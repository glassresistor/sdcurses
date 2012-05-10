import urwid
from smartdc import DataCenter, DEBUG_CONFIG

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


class SDCWidget(urwid.WidgetWrap):

    def __init__ (self, location=None, key_id=None):
        sdc = DataCenter(key_id=key_id, allow_agent=True, config=DEBUG_CONFIG)
        vms = sdc.machines()
        self.items = []
        for (i, vm) in enumerate(vms):
            self.items.append(SMWidget(i, '%s - %s' % (vm.name, vm.public_ips[0])))
        footer = urwid.AttrMap(urwid.Text('selected:'), 'head')
        self.listbox = urwid.ListBox(urwid.SimpleListWalker(self.items))
        self.view = urwid.Frame(urwid.AttrWrap(self.listbox, 'body'), footer=footer)
        self.__super.__init__(self.view)

    def keypress(self, size, key):
        if key is 'enter':
            focus = self.listbox.get_focus()[0].content
            self.view.set_footer(urwid.AttrWrap(urwid.Text(
                'selected: %s' % str(focus)), 'head'))
        else:
            return self.listbox.keypress(size, key)
