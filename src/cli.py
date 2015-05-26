# In The Name Of God
# ========================================
# [] File Name : main.py
#
# [] Creation Date : 26-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'

import cmd
import sys
import logging

from presence import PresenceService
from peer import PeerList
from storage import FileStorage
from file_transfer import FileTransferServer
from file_transfer import recv_file


class ChFTP(cmd.Cmd):
    def __init__(self):
        super(ChFTP, self).__init__()
        self.folders = []
        self.username = ""
        self.presenceService = None
        self.fileTransferServer = None

    def do_login(self, args: str):
        self.username = args
        print("Welcome %s" % self.username)

    def help_login(self):
        print("login username")
        print("save your username in application")

    def do_add(self, args: str):
        self.folders += args.split(" ")

    def do_run(self, args: str):
        self.presenceService = PresenceService(FileStorage(self.folders).get_files_name(), self.username)
        self.presenceService.start()
        print("Presence service started....")
        self.fileTransferServer = FileTransferServer()
        self.fileTransferServer.start()
        print("File transfer server started....")

    def help_run(self):
        print("run")
        print("run presence and file transfer services")
        print("please note that after this you cannot change your username or add new folders")

    def do_list(self, args: str):
        for peer in PeerList():
            print(peer)

    def do_get(self, args: str):
        args = args.split(" ")
        if len(args) != 3:
            print("*** invalid number of arguments")
            return
        username = args[0]
        rfile = args[1]
        lfile = args[2]
        for peer in PeerList():
            if peer.username == username and peer.files.count(rfile) > 0:
                ip = peer.ip
                break
        else:
            print("*** invalid username, file pair")
            return
        recv_file(ip, rfile, lfile)

    def do_quit(self, args: str):
        if self.presenceService:
            self.presenceService.shutdown()
        sys.exit(0)


logging.basicConfig(filename='ChFTP.log', level=logging.INFO)
cli = ChFTP()
cli.prompt = "ChFTP> "
cli.intro = "Welcome to ChFTP shell from chapna company.\n"
try:
    cli.cmdloop()
except KeyboardInterrupt:
    cli.do_quit("")
