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

        # Handle ingoing FTP messages
        while True:
            client, address = self.sck.accept()
            logger.info(" New connection accepted from %s:%d" % (address[0], address[1]))
            FileTransferHandler(client).start()


class FileTransferHandler(threading.Thread):
    def __init__(self, sck: socket.socket):
        self.sck = sck
        super(FileTransferHandler, self).__init__(name="File Transfer Handler")

    def run(self):
        # Create logger object
        logger = logging.getLogger("File Transfer Handler")

        sck_file = self.sck.makefile(mode="wr", encoding="ascii", newline='\n')
        verb, option = sck_file.readline().split(" ")
        logger.info(" Request from %s: " % str(self.sck.getpeername()))
        logger.info(" -> verb: %s" % verb)
        logger.info(" -> option: %s" % option)

# Just for test :-)
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    FileTransferServer().start()
