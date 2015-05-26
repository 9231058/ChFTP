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


class ChFTP(cmd.Cmd):
    username = ""
    files = []

    def do_login(self, args: str):
        ChFTP.username = args
        print("Welcome %s" % ChFTP.username)

    def do_add(self, args: str):
        ChFTP.files.append(args.split(' '))

    def do_run(self, args: str):
        PresenceService(ChFTP.files, ChFTP.username).start()
        print("Presence service started....")

    def do_list(self, args: str):
        for peer in PeerList():
            print(peer)

    def do_quit(self, args: str):
        sys.exit(0)


logging.basicConfig(filename='ChFTP.log', level=logging.INFO)
cli = ChFTP()
cli.prompt = "ChFTP> "
cli.cmdloop()
