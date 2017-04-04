import sys
import os
import json
import config
import utils
import operator


class selecter():
    """ selecting article """

    def __init__(self, infopath=""):
        if infopath == "":
            c = config.config()
            self.infopath = c.infopath
        else:
            self.infopath = infopath
         
        self.articleList = self.read_info()

    def read_info(self):
        """ return articles as dictionaries list """
        with open(self.infopath, "r") as f:
            lines = f.readlines()
        return  [a for a in map(json.loads, lines) if self.filterfunc(a)]

    def info_to_shaped_str(self):
        # TODO make this be able to select format
        s = ""
        for dic in self.articleList:
            l = [utils.ljust(dic['title'], 10), utils.ljust(dic['genre'], 10), 
                 utils.ljust(', '.join(dic['tag'])[0:10], 10), dic['createDate'][0:10].ljust(12),
                 dic['modifiedDate'][0:10].ljust(12), dic['path']]
            s = s + "\n" + ":".join(l)
        return s.strip()
        
    def filterfunc(self, arg):
        """ This is used in read_info and filter articles read from info."""
        # TODO filter by tag or title or ...
        return True

        

        

if __name__ == '__main__':
    se = selecter()
    ope = operator.attrgetter('tag')
    print(se.articleList[0])
    print(type(se.articleList[0]))
    print(se.articleList[0].keys())
    print(se.articleList[0]['tag'])
    ss = sorted(se.articleList, key=lambda a:a['title'])
    for k in ss:
        print(k)


