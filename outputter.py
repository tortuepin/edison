# vim:set foldmethod=marker:
import os
import sys
import datetime as dt


def write_markdown(sorted_articles, articlepath):
    """ write html file """
    tmp = ""

    dtime_a = dt.datetime(dt.MINYEAR, 1, 1)
    for article in sorted_articles:
        dtime = dt.datetime.strptime(article['createDate'], "%Y-%m-%d %H:%M:%S.%f")
        if dtime_a.date() != dtime.date():
            # TODO write cover
            cover = "<dev class=\"cover\">" + str(dtime.date()) + "</dev>\n\n"
            tmp += cover
            dtime_a = dtime

        # write article content
        with open(articlepath + article['path'], 'r') as k:
            s = k.read()
            tmp += (s + "\n\n")

    return tmp











if __name__ == '__main__':
    import selecter
    se = selecter.selecter()
    print(write_markdown(se.articleList, "./out"))


