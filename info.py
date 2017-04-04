import sys
import datetime
import json

class info():
    """ 
    class about file info 

    args:
        title
        tag
        genre
        path
        createDate
        modifiedDate
    """
    def __init__(self, title="", tag=list(), genre="", path="", 
                modifiedDate=None, createDate=None):
        self.title = title
        self.tag = tag
        self.genre = genre
        self.path = path
        self.modifiedDate = modifiedDate
        self.createDate = createDate


    def dump_json(self):
        dic = {'title':self.title, 'tag':self.tag, 'genre':self.genre, 
               'path':self.path, 'modifiedDate':str(self.modifiedDate),
               'createDate':str(self.createDate)}
        return json.dumps(dic)

    def save_info(self, filepath):
        with open(filepath, 'a') as f:
            f.write(self.dump_json())
            f.write("\n")


if __name__ == '__main__':
    i = info()
    print(i.dump_json())
