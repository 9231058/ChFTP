# In The Name Of God
# ========================================
# [] File Name : peer.py
#
# [] Creation Date : 25-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'

import threading


class Peer:
    def __init__(self, username: str, ip: str, files: list):
        self.username = username
        self.ip = ip
        self.files = files

    def __str__(self):
        return self.username + '\\' + self.ip + '\\' + str(self.files)


class PeerList:
    class __PeerList:
        def __init__(self):
            self.peers = []

    instance = None
    lock = threading.Semaphore()

    def __init__(self):
        if not PeerList.instance:
            PeerList.instance = PeerList.__PeerList()
            self.index = 0
        else:
            self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        PeerList.lock.acquire()
        if self.index < len(PeerList.instance.peers):
            peer = PeerList.instance.peers[self.index]
            self.index += 1
            PeerList.lock.release()
            return peer
        else:
            PeerList.lock.release()
            raise StopIteration

    @staticmethod
    def add(peer):
        if not isinstance(peer, Peer):
            raise TypeError()
        PeerList.lock.acquire()
        PeerList.instance.peers.append(peer)
        PeerList.lock.release()
