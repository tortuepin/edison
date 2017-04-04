import sys
import os
import toml

class config():
    """ handring config file """

    def __init__(self, configpath="./temp/config"):
        self.configpath = configpath
        self.__homepath = ""
        self.__editor = "vim"
        self.__infopath = ""
        self.register()


    def register(self):
        conf = {}
        with open(self.configpath, "r") as f:
            data = f.read()
            conf = toml.loads(data)

        self.homepath = conf['homepath'] if 'homepath' in conf else "./temp"
        self.editor = conf['editor'] if 'editor' in conf else "vim"
        self.infopath = conf['infopath'] if 'infopath' in conf\
                                         else self.homepath + "/" + "info"
        if not (os.path.exists(self.infopath)):
            f = open(self.infopath, 'w')
            f.close()

                




    @property
    def homepath(self):
        return self.__homepath
    @homepath.setter
    def homepath(self, path):
        self.__homepath = path
    @property
    def editor(self):
        return self.__editor
    @editor.setter
    def editor(self, editor):
        self.__editor = editor
    @property
    def infopath(self):
        return self.__infopath
    @infopath.setter
    def infopath(self, infopath):
        self.__infopath = infopath
        
if __name__ == '__main__':
    c = config()
    c.register()
