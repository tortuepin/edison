# vim:set foldmethod=marker:
import click
import new as newcom
import selecter
import config
import subprocess
import outputter
import os
import json

@click.group()
def cli():
    pass

@cli.command()
@click.option('--title', prompt=True, type=str)
@click.option('--tag', prompt=True, type=str)
@click.option('--genre', prompt=True, type=str)
def new(title='notitle', tag='notag', genre='nogenre'): #{{{
    """Make new edison file"""
    # read config file
    c = config.config()
    
    # split tag by comma
    splitedtag = tag.split(",")

    taglist = list(map(lambda s:s.strip(" "), splitedtag))

    con = {'config':c,\
           'title':title, 'tag':taglist, 'genre':genre}
    newcom.new_command(con)
#}}}

@cli.command()
def edit(): #{{{
    """ select and edit edison note """

    c = config.config()
    # get article list
    se = selecter.selecter()

    # pipe to peco
    data = se.info_to_shaped_str().encode('utf-8')
    po = subprocess.Popen(c.searcher,
                          stdin=subprocess.PIPE,
                          stdout=subprocess.PIPE)
    out, err = po.communicate(data)

    # TODO save modified time

    # get path
    path = out.decode('utf-8').split("\t")[-1].strip("\n")
    if path=="":
        return

    # open with editor
    cmd = [c.editor, c.articlepath + path]
    subprocess.call(cmd)

    print(path)
# }}}

@cli.command()
def ls():
    """ print article list"""
    # get article list
    se = selecter.selecter()
    print(se.info_to_str())
    #print(se.info_to_shaped_str())

@cli.command()
@click.option('--out', '-o',  type=str)
def output(out=""):
    """ output as markdown"""
    c = config.config()
    se = selecter.selecter()
    if out == None:
        print(outputter.write_markdown(se.articleList, c.articlepath))
    else:
        with open(out, "w") as f:
            f.write(outputter.write_markdown(se.articleList, c.articlepath))

@cli.command()
def delete():
    """ delete file"""
    se = selecter.selecter()
    c = config.config()

    # pipe to peco
    data = se.info_to_shaped_str().encode('utf-8')
    po = subprocess.Popen(c.searcher,
                          stdin=subprocess.PIPE,
                          stdout=subprocess.PIPE)
    out, err = po.communicate(data)
    
    path = out.decode('utf-8').split(":")[-1].strip("\n")
    if path=="":
        return

    # delete selected file
    os.remove(c.articlepath+path)
    
    # delete info
    infolist = list()
    for ar in se.articleList:
        if ar['path'] != path:
            infolist.append(ar)
    with open(c.infopath, "w") as f:
        for i in infolist:
            f.write(json.dumps(i))
            f.write("\n")











    
if __name__ == '__main__':
    cli()
