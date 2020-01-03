import os
import shutil
import datetime


def create_file(name, text=None):
    with open(name, 'w', encoding='utf -8') as f:
        f.write(text)  # только один аргумент для записи в файл


def create_folder():
    try:
        os.mkdir('folder_4')  #
    except FileExistsError as a:
        print(a)


def filter_folders(only_folders=False):  # когда нужно прояснить муки выбора,
    # отфильтровать результат (возможна тернальная ситуация)
    result = os.listdir()  # а это список папок и файлов
    if only_folders:  # когда only_folders True!!! по папкам
        result = [f for f in result if os.path.isdir(f)]
    return result


def delete_fol_files(name):
    if os.path.isfile(name):
        os.remove(name)
    else:
        try:
            os.rmdir(name)
        except FileNotFoundError as s:
            print(s)


def copy_file_fol(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)  # копирование папок copytree
        except FileExistsError as a:
            print(a)
    else:
        shutil.copyfile(name, new_name)  # копирование файлов copyfile


def save_info(message):
    current_time = datetime.datetime.now()
    res = f'---> {current_time} --->{message}'
    with open('log.txt', 'a', encoding='utf -8') as f:
        f.write(res+'\n')

if __name__ == '__main__':
    create_file('texx.txt', 'Some text')
    create_folder()
    print(filter_folders())
    delete_fol_files('texx3.txt')

    copy_file_fol('folder_4', 'f_5')

    copy_file_fol('texx.txt', 'texx2.txt')
    save_info('qwe')
