# In The Name Of God
# ========================================
# [] File Name : storage.py
#
# [] Creation Date : 26-05-2015
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
__author__ = 'Parham Alvani'

import os


class FileStorage:
    def __init__(self, folders: list):
        self.folders = folders

    def getFilesPath(self) -> list:
        pass

    def getFilesName(self) -> list:
        retval = []
        for folder in self.folders:
            for file in os.listdir(folder):
                if os.path.isfile(file):
                    retval.append(os.path.basename(file))
        return retval

    def getFile(self, mame: str) -> str:
        pass

# Just for test :-)
if __name__ == '__main__':
    print(FileStorage(["."]).getFilesName())
