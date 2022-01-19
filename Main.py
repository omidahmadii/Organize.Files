import os
import shutil


def organize_files_by_name():
    cwd = os.getcwd()
    try:
        for item in os.listdir(cwd):
            if item == os.path.basename(__file__):
                continue
            path = cwd + "\\" + item
            path_split_by_dot = cwd + "\\" + item.split('.')[0]
            path_split_by_dash = cwd + "\\" + item.split('.')[0].split('-')[0]
            if os.path.isfile(path):
                if not item.__contains__('-'):
                    isExist = os.path.exists(path_split_by_dot)
                    if not isExist:
                        os.mkdir(path_split_by_dot)
                    shutil.move(path, path_split_by_dot)

                else:
                    isExist = os.path.exists(path_split_by_dash)
                    if not isExist:
                        pass
                        os.mkdir(path_split_by_dash)
                    shutil.move(path, path_split_by_dash)

    except:
        print(" An error has been occurred")


organize_files_by_name()