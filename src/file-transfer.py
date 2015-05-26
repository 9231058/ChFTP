# In The Name Of God
# ========================================
# [] File Name : file-transfer.py
#
# [] Creation Date : 26-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'

import threading
import socket
import io
import logging


class FileTransferServer(threading.Thread):
    def __init__(self):
        self.sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sck.bind(("", 21))
        self.sck.listen(5)
        super(FileTransferServer, self).__init__(name="File Transfer Server")

    def run(self):
        # Create logger object
        logger = logging.getLogger("File Transfer Server")

        while True:
            client = self.sck.accept()
            FileTransferHandler(client)


class FileTransferHandler(threading.Thread):
    def __init__(self, sck: socket.socket):
        self.sck = sck
        super(FileTransferHandler, self).__init__(name="File Transfer Handler")

    def run(self):
        # Create logger object
        logger = logging.getLogger("File Transfer Handler")
