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

    def __init__ (self):
        footer = urwid.AttrMap(urwid.Text('selected:'), 'head')
        self.view = urwid.Frame(urwid.Text('Waiting on Connection....'), footer=footer)
        self.__super.__init__(self.view)

    def set_sdc(self, location, key_id, allow_agent=None):
        if allow_agent == None:
            allow_agent = True
        self.sdc = DataCenter(location=location, key_id=key_id, allow_agent=allow_agent, config=DEBUG_CONFIG)
        vms = self.sdc.machines()
        items = []
        for (i, vm) in enumerate(vms):
            items.append(SMWidget(i, '%s - %s' % (vm.name, vm.public_ips[0])))
        self.listbox = urwid.ListBox(urwid.SimpleListWalker(items))
        self.view.set_body(self.listbox)
        
    def keypress(self, size, key):
        if key is 'enter':
            focus = self.listbox.get_focus()[0].content
            self.view.set_footer(urwid.AttrWrap(urwid.Text(
                'selected: %s' % str(focus)), 'head'))
        else:
            return self.listbox.keypress(size, key)
