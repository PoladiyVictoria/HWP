'''Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл,
○ флаг каталога,
○ название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя
логирование.'''

import os
import argparse
from collections import namedtuple
import logging

def directory_traversal(dir_path: str):
    '''Функция перебирает всё что есть в заданной директории и логирует всё в файл (.log)'''
    Content_dir = namedtuple("Content_dir",
                             ['file_name', 'extens', 'root_dir'], 
                             defaults=[None, dir, None])
    logging.basicConfig(filename="content_dir.log",
                        encoding="UTF-8",
                        format="{msg}", 
                        style="{",
                        level=logging.INFO,
                        filemode="a")
    logger = logging.getLogger(__name__)
    for root, dirs, files in os.walk(dir_path):
        '''Полный проход по всем папкам в ветке директории'''
        cur_root_dir = root.split("\\")[-1]

        for name_dir in dirs:
            '''Проходимся по всем папкам в текущей директроии и логируем в файл с расширением (.dir)'''
            content_file = Content_dir(name_dir, "dir", cur_root_dir)
            logger.info(f"Имя файла - {content_file[0]}, Расширение - {content_file[1]}, Корневая папка - {content_file[2]}")
        
        for name_file in files:
            '''Проходимся по всем файлам в текущей директроии и логируем в файл с их расширением'''
            cur_file_name = name_file.split(".")[0]
            cur_file_ex = name_file.split(".")[-1]
            content_file = Content_dir(cur_file_name, cur_file_ex, cur_root_dir)
            logger.info(f"Имя файла - {content_file[0]}, Расширение - {content_file[1]}, Корневая папка - {content_file[2]}")




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path_to_dir", type=str, help="Path to you directry")
    args = parser.parse_args()
    directory_traversal(args.path_to_dir)