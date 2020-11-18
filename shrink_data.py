import os
from shutil import copy2

path_from_jpg = r'D:\disk_e\Wh u gonna do\Egitim\Bilgem\Drone-vs-Bird\obj_clean_all\train_jpg'
path_from_txt = r'D:\disk_e\Wh u gonna do\Egitim\Bilgem\Drone-vs-Bird\obj_clean_all\train_txt'


path_to = r'D:\disk_e\Wh u gonna do\Egitim\Bilgem\Drone-vs-Bird\obj\train'

old_jpg_list = []
os.chdir(path_from_jpg)
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        old_jpg_list.append(path_from_jpg + "\\" + filename)
        
old_txt_list = []
os.chdir(path_from_txt)
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".txt"):
        old_txt_list.append(path_from_txt + "\\" + filename)

        
for file in old_jpg_list[::3]:
    copy2(file, path_to)    # target filename is /dst/dir/file.ext
    
for file in old_txt_list[::3]:
    copy2(file, path_to)