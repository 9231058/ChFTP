# In The Name Of God
# ========================================
# [] File Name : peer.py
#
# [] Creation Date : 25-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'


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
            pass

    instance = None

    def __init__(self):
        if not PeerList.instance:
            PeerList.instance = PeerList.__PeerList()
