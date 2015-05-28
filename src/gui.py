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

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        run_button = Gtk.Button(label="Run")
        hbox.add(run_button)

        get_button = Gtk.Button(label="Get", sensitive=0)
        hbox.add(get_button)


win = ChFTP()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
