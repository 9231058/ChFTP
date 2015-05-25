# In The Name Of God
# ========================================
# [] File Name : presence.py
#
# [] Creation Date : 25-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'

import threading
import socket
import logging
import time

from peer import Peer
from peer import PeerList


class PresenceService(threading.Thread):
    def __init__(self, files: list, username: str):
        self.sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
        self.sck.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.sck.bind(('', 8182))
        self.files = files
        self.username = username
        super(PresenceService, self).__init__(name="PresenceService")

    def run(self):
        # Create logger object
        logger = logging.getLogger("PresenceService")

        # Broadcasting hi message
        hi_message = "hi" + '\\' + self.username + '\\' + str(self.files)
        self.sck.sendto(bytes(hi_message, "ascii"), ("255.255.255.255", 8182))

        # Handle ingoing presence messages
        while (True):
            data, address = self.sck.recvfrom(1024)
            message = data.decode("ascii")
            verb, username, foreign_files = message.split('\\')
            foreign_files = eval(foreign_files)

            logger.info(" Message from %s:%d:" % (address[0], address[1]))
            logger.info(" -> verb: %s" % verb)
            logger.info(" -> username: %s" % username)
            logger.info(" -> files: %s" % str(foreign_files))

            if verb == 'hi':
                # hi messages handling
                peer = Peer(username, address[0], foreign_files)
                PeerList().add(peer)
                if username != self.username:
                    hiback_message = "hiback" + '\\' + self.username + '\\' + str(self.files)
                    self.sck.sendto(bytes(hiback_message, "ascii"), address)
            if verb == 'hiback':
                # hi back messages handling
                peer = Peer(username, address[0], foreign_files)
                PeerList().add(peer)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    PresenceService(["a.txt"], "1995parham").start()
    time.sleep(1)
    for peer in PeerList():
        print(peer)
