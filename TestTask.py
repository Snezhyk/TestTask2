# Импорт библиотек
import os
import hashlib
from sys import argv


# Принимаем два параметра. summ - файл хэш-сумм. catalog - директория с проверяемыми файлами.
script, summ, catalog = argv


# Функция для вычисления md5 hash
def hof_md5(x):
    with open(x, "rb") as f:
        md5 = hashlib.md5(f.read()).hexdigest()
    return md5


# Функция для вычисления sha1 hash
def hof_sha1(x):
    with open(x, "rb") as f:
        sha1 = hashlib.sha1(f.read()).hexdigest()
    return sha1


# Функция для вычисления sha256 hash
def hof_sha256(x):
    with open(x, "rb") as f:
        sha256 = hashlib.sha256(f.read()).hexdigest()
    return sha256


# Чтение файла сумм построчно и вычисление колличества файлов.
# Проверка на присутствие файла в каталоге, затем идет вычисление хэша и ссравнение с хэшем из файла.
with open(summ, "r") as f:
    text = f.readlines()
    quantity = len(text) # Колличество файлов.
    os.chdir(catalog)
    cat_files = os.listdir()
    for i in range(quantity):
        string = text[i]
        name, alg, check_hash = string.split()
        path = catalog + name # Путь до проверяемого файла.
        check_hash_lower = check_hash.lower()
        if name in cat_files: # Проверка на присутствие и выбор алгоритма.
            if alg == 'md5':
                hof = hof_md5(path)
            elif alg == 'sha1':
                hof = hof_sha1(path)
            elif alg == 'sha256':
                hof = hof_sha256(path)
            else:
                hof = 0
            if check_hash_lower == hof:
                print(name, ' OK')
            else:
                print(name, ' FAIL')
        else:
            print(name, ' NOT FOUND')