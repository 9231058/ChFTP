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
from gi.repository import GObject
import getpass
import logging

from presence import PresenceService
from peer import PeerList
from storage import FileStorage
from file_transfer import FileTransferServer
from file_transfer import recv_file


class ChFTP(Gtk.Window):
    def __init__(self):
        super(ChFTP, self).__init__(title="ChFTP")
        self.set_border_width(10)

        self.presenceService = None
        self.fileTransferServer = None

        self.peer_model = Gtk.ListStore(str, str, str)

        self.connect("delete-event", self.on_quit)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        self.peer_view = Gtk.TreeView(self.peer_model)
        for column_index, column_title in enumerate(["Peer Username", "Peer IP Address", "Local Folder Name"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=column_index)
            self.peer_view.append_column(column)
        hbox.pack_start(self.peer_view, True, True, 0)

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
        self.username_entry.set_sensitive(False)
        self.peer_view.get_column(2).set_title("Remote File Name")
        self.run_button.set_sensitive(False)
        self.add_button.set_sensitive(False)
        self.get_button.set_sensitive(True)

        folders = []
        for row in self.peer_model:
            folders.append(row[2])

        self.presenceService = PresenceService(FileStorage(folders).get_files_name(), username)
        self.presenceService.start()
        self.fileTransferServer = FileTransferServer()
        self.fileTransferServer.start()

        GObject.timeout_add(1000, self.peer_list_update)

    def on_get_clicked(self, button):
        model, it = self.peer_view.get_selection().get_selected()
        if it:
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK,
                                       "%s Received" % model[it][2])
            recv_file(model[it][1], model[it][2], "_" + model[it][2])
            dialog.run()
            dialog.destroy()

    def on_add_clicked(self, button):
        dialog = Gtk.FileChooserDialog("Please choose a folder", self, Gtk.FileChooserAction.SELECT_FOLDER,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Add Folder", Gtk.ResponseType.OK))
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.peer_model.append(["You", "localhost", dialog.get_filename()])

        dialog.destroy()

    def on_quit(self, *args):
        if self.presenceService:
            self.presenceService.shutdown()
        Gtk.main_quit(args)

    def peer_list_update(self):
        self.peer_model.clear()
        for peer in PeerList():
            for file in peer.files:
                self.peer_model.append([peer.username, peer.ip, file])
        return True


logging.basicConfig(filename="ChFTP.log", level=logging.INFO)
win = ChFTP()
win.show_all()
Gtk.main()
