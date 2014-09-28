#!coding: utf-8
import os

#создает папки в текущей директории
for i in xrange(50):
    os.mkdir(str(i))


# переименовывает
for f in os.listdir("."):
    if not f.endswith(".py"):
        os.rename(f,"My " + f)

#join на путях
os.mkdir("ainur")
p = os.path.abspath("ainur") # возвращает полный путь к папке или файлу

# создает папку внутри папки р
new_folder_path = os.path.join(p,"mozg")
os.mkdir(new_folder_path)
