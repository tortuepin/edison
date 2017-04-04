import sys
import os
import toml

class config():
    """ handring config file """

    def __init__(self, configpath=os.path.expanduser('~')+"/edison/config.toml"):
        self.configpath = configpath
        self.__homepath = ""
        self.__editor = "vim"
        self.__infopath = ""
        self.__articlepath = ""
        self.register()


    def register(self):
        if len(self.configpath) == 0:
            home = os.path.expanduser('~')
            if not(home+"/edison"):
                os.makedirs(home)
        conf = {}
        if os.path.exists(self.configpath):
            with open(self.configpath, "r") as f:
                data = f.read()
                conf = toml.loads(data)
        else:
            f = open(self.configpath, "w")
            f.close()

        self.homepath = conf['homepath'] if 'homepath' in conf else os.path.expanduser('~')+"/edison"
        self.editor = conf['editor'] if 'editor' in conf else "vim"
        self.infopath = conf['infopath'] if 'infopath' in conf\
                                         else self.homepath + "/" + "info"
        self.articlepath = conf['articlepath'] if 'articlepath' in conf\
                                         else self.homepath + "/" + "article"
        if not (os.path.exists(self.infopath)):
            f = open(self.infopath, 'w')
            f.close()
        if not (os.path.exists(self.articlepath)):
            os.makedirs(self.articlepath)




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
    @property
    def articlepath(self):
        return self.__articlepath
    @articlepath.setter
    def articlepath(self, articlepath):
        self.__articlepath = articlepath
        
if __name__ == '__main__':
    c = config()
    c.register()
