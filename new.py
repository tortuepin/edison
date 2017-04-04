# vim:set foldmethod=marker:
import sys
import os
import datetime
import info

def new_command(context):
    """
    args:
        context : dictionary including 'title', 'tag', 'genre' and 'config'
    """
    dt = datetime.datetime.today()

    # make directory and filepath
    filepath = create_filepath(context['config'].articlepath, dt)
    # make relative file path
    rpath = filepath[len(context['config'].articlepath):]
    print("made" + filepath)
    
    # make info data
    file_info =\
    info.info(title=context['title'], tag=context['tag'],\
              genre=context['genre'], path=rpath, createDate=dt)
    print(file_info.dump_json())

    # save info data
    file_info.save_info(context['config'].infopath)

    # write header
    write_header(file_info, context['config'].articlepath)

    # open file by editor
    os.system(context['config'].editor + " " + filepath)





def create_filepath(homepath, dt): 
    """ return newfile's filepath """
    dir_path = prepare_directory(dt, homepath)
    return generate_filepath(dt, dir_path)

def prepare_directory(datetime, homepath): # {{{
    dir_path = homepath + "/" + datetime.strftime('%y%m%d') + "/"
    if not(os.path.exists(dir_path)):
        os.makedirs(dir_path)
    return dir_path
# }}}
def generate_filepath(datetime, dir_path): # {{{
    if not(os.path.exists(dir_path)):
        return "exec"
    files = os.listdir(dir_path)
    count = 1
    fname = datetime.strftime('%H%M')
    for f in files:
        if f.startswith(fname):
            count = int(f.split(".")[1]) + 1
    fname = fname + "." + str(count)
    filepath = dir_path + fname + ".md"
    return filepath
# }}}
def write_header(info, articlepath):
    """ write header data to file """
    str = "# " + info.title
    filepath = articlepath + info.path
    with open(filepath, 'w') as f:
        f.write(str)




if __name__ == '__main__':
    os.system("vim")
    print("hoge")
