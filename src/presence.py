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


class PresenceService(threading.Thread):
    def __init__(self, files: list):
        self.sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
        self.sck.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.sck.bind(('', 8182))
        self.files = files
        super(PresenceService, self).__init__(name="PresenceService")

    def run(self):
        hello_message = "hi" + '\\' + "username" + '\\' + socket.gethostname() + '\\' + str(self.files)
        self.sck.sendto(bytes(hello_message, "ascii"), ("255.255.255.255", 8182))
        while (True):
            data, address = self.sck.recvfrom(1024)
            message = data.decode("ascii")
            print(message)
            print(address)


if __name__ == '__main__':
    PresenceService(["a.txt"]).start()
