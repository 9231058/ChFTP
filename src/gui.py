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
import getpass


class ChFTP(Gtk.Window):
    def __init__(self):
        super(ChFTP, self).__init__(title="ChFTP")
        self.set_border_width(10)

        self.peer_model = Gtk.ListStore(str, str, str)
        self.peer_view = Gtk.TreeView(self.peer_model)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        self.add_button = Gtk.Button(label="Add")
        self.add_button.connect('clicked', self.on_add_clicked)
        hbox.pack_start(self.add_button, True, True, 0)

        self.run_button = Gtk.Button(label="Run")
        self.run_button.connect('clicked', self.on_run_clicked)
        hbox.pack_start(self.run_button, True, True, 0)

        self.get_button = Gtk.Button(label="Get", sensitive=False)
        self.get_button.connect('clicked', self.on_get_clicked)
        hbox.pack_start(self.get_button, True, True, 0)

        self.username_entry = Gtk.Entry()
        self.username_entry.set_text(getpass.getuser())
        hbox.pack_start(self.username_entry, True, True, 0)

    def on_run_clicked(self, button):
        username = self.username_entry.get_text()
        print(username)
        self.run_button.set_sensitive(False)
        self.add_button.set_sensitive(False)
        self.get_button.set_sensitive(True)

    def on_get_clicked(self, button):
        pass

    def on_add_clicked(self, button):
        dialog = Gtk.FileChooserDialog("Please choose a folder", self, Gtk.FileChooserAction.SELECT_FOLDER,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Add Folder", Gtk.ResponseType.OK))
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Folder selected: " + dialog.get_filename())

        dialog.destroy()


win = ChFTP()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
