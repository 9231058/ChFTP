# In The Name Of God
# ========================================
# [] File Name : file-transfer.py
#
# [] Creation Date : 26-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================

import logging
import socket
import threading

from .storage import FileStorage


class FileTransferServer(threading.Thread):
    def __init__(self):
        self.sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sck.bind(("", 21))
        self.sck.listen(5)
        super(FileTransferServer, self).__init__(name="File Transfer Server")
        self.setDaemon(True)

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
        self.setDaemon(True)

    def run(self):
        # Create logger object
        logger = logging.getLogger("File Transfer Handler")

        sck_file = self.sck.makefile(mode="wr", encoding="ascii", newline='\n')
        verb, option = sck_file.readline().split(" ")
        option = option.strip()
        logger.info(" Request from %s: " % str(self.sck.getpeername()))
        logger.info(" -> verb: %s" % verb)
        logger.info(" -> option: %s" % option)
        if verb == 'RETR':
            sck_file.write("150 File status okay; about to open data connection.\n")
            sck_file.flush()
            tsck = socket.socket()
            try:
                tsck.connect((self.sck.getpeername()[0], 20))
            except ConnectionError:
                sck_file.write("425 Can't open data connection.\n")
                sck_file.flush()
                self.sck.close()
                return
            tsck.makefile(mode="wr", encoding="ascii", newline='\n').writelines(FileStorage().get_file(option))
            sck_file.write("226 Closing data connection. Requested file action successful.\n")
            sck_file.flush()
            tsck.close()
            self.sck.close()
        else:
            sck_file.write("202 Command not implemented, superfluous at this site.\n")
            sck_file.flush()
            self.sck.close()


def recv_file(ip: str, remote_name: str, local_name: str):
    file = open(local_name, "w")

    sck = socket.socket()

    tsck = socket.socket()
    tsck.bind(("", 20))
    tsck.listen(5)

    sck.connect((ip, 21))
    sck_file = sck.makefile(mode="wr", encoding="ascii", newline='\n')
    sck_file.write("RETR %s\n" % remote_name)
    sck_file.flush()

    fsck, address = tsck.accept()
    while True:
        data = fsck.recv(1024)
        if not data:
            break
        file.write(data.decode('ascii'))
        file.flush()


# Just for test :-)
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    print(FileStorage(["."]).get_files_name())
    FileTransferServer().start()
    recv_file("127.0.0.1", ".gitignore", "sample.txt")
