from PIL import Image
import os

#------------ unnormalized label text files --------------------------
label_files = []
images = []
path = r'D:\disk_e\Wh u gonna do\Egitim\Bilgem\Drone-vs-Bird\Unnormalized\fnc100818-104318_two_parrot_disco_1'
os.chdir(path)

for filename in os.listdir(os.getcwd()):
    if filename.endswith(".txt"):
        label_files.append(path + "\\" + filename)
        
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        images.append(path + "\\" + filename)
        

#------------ normalized label text files --------------------------
new_label_files = []
path_new = r'D:\disk_e\Wh u gonna do\Egitim\Bilgem\Drone-vs-Bird\fnc100818-104318_two_parrot_disco_1'
os.chdir(path_new)

for filename in os.listdir(os.getcwd()):
    if filename.endswith(".txt"):
        new_label_files.append(path_new + "\\" + filename)

#------------ convert test annotations ---------------------------

i = 0
for img in images:
    im = Image.open(img)
    width, height = im.size
    with open(label_files[i], "r") as txtFile:
        with open(new_label_files[i], "w") as outFile:
            for line in txtFile:
                line = line.strip("\n")
                words = line.split()
                class_num, x_old, y_old, width_old, height_old = words[0], words[1], words[2], words[3], words[4]
                outFile.write(class_num + " " + str((float(x_old)+(float(width_old)/2))/width) + " " + str((float(y_old)+(float(height_old)/2))/height) + " " + str(float(width_old)/width) + " " + str(float(height_old)/height) + "\n")                
    i+=1    
    