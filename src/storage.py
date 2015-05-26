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
    class __FileStorage:
        def __init__(self, folders: list):
            self.folders = folders

    instance = None

    def __init__(self, folders: list=None):
        if not FileStorage.instance:
            FileStorage.instance = FileStorage.__FileStorage(folders)

    @staticmethod
    def get_files_name() -> list:
        retval = []
        for folder in FileStorage.instance.folders:
            for file in os.listdir(folder):
                if os.path.isfile(file):
                    retval.append(os.path.basename(file))
        return retval

    @staticmethod
    def get_file(name: str) -> list:
        for folder in FileStorage.instance.folders:
            for file in os.listdir(folder):
                if os.path.isfile(file) and os.path.basename(file) == name:
                    return open(file, "r").readlines()

# Just for test :-)
if __name__ == '__main__':
    print(FileStorage(["."]).get_files_name())
