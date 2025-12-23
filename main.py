import os
import shutil
path = "A"
files = os.listdir(path)

for file in files:
    if file.endswith(".txt"):
        os.makedirs(path+"/text",exist_ok=True)
        shutil.move(path+"/"+file,path+"/text/"+file) 

    elif file.endswith(".jpg"):
        os.makedirs(path+"/images",exist_ok=True)
        shutil.move(path+"/"+file,path+"/images/"+file)