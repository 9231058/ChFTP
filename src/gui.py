# In The Name Of God
# ========================================
# [] File Name : gui.py
#
# [] Creation Date : 28-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'

from gi.repository import Gtk


class ChFTP(Gtk.Window):
    def __init__(self):
        super(ChFTP, self).__init__(title="ChFTP")
        self.set_border_width(10)

        self.peer_model = Gtk.ListStore(str, str, str)
        self.peer_view = Gtk.TreeView(self.peer_model)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        self.run_button = Gtk.Button(label="Run")
        self.run_button.connect('clicked', self.on_run_clicked)
        hbox.add(self.run_button)
        hbox.pack_start(self.run_button, True, True, 0)

        self.get_button = Gtk.Button(label="Get", sensitive=0)
        hbox.add(self.get_button)
        hbox.pack_start(self.get_button, True, True, 0)

        self.username_entry = Gtk.Entry()
        self.username_entry.set_text("Username")
        hbox.pack_start(self.username_entry, True, True, 0)

    def on_run_clicked(self, button):
        pass


win = ChFTP()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
