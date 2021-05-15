import os
from PIL import Image
import shutil
from tqdm import tqdm

curdir = (os.path.abspath(__file__))
songdir = os.path.dirname(os.path.dirname(curdir)) + "\Songs"
os.chdir(os.path.dirname(curdir))

jpg = ['.jpg', '.JPG']
jpeg = ['.jpeg', '.JPEG']
png = ['.png', '.PNG']
file_list = []
ext_list1 = jpg + jpeg + png
ext_list2 = ['.mp4','.mkv','.webm','.avi','.MP4','.MKV','.WEBM','.AVI']

BGdir = os.path.join(os.path.dirname(curdir),'bg.png')
myBG = Image.open(BGdir)
if myBG.mode != 'RGB':
    myBG = myBG.convert('RGB')
myBG.save("bg.jpg")
myBG.save("bg.jpeg")

for (path, dir, files) in tqdm(os.walk(songdir)):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        file_path = os.path.join(path, filename)
        if ext in ext_list1: file_list.append(file_path)
        if ext in ext_list2: os.remove(file_path)
            
for name in tqdm(file_list):
    os.remove(name)
    if os.path.splitext(name)[-1] in jpg: shutil.copy("bg.jpg",name)
    elif os.path.splitext(name)[-1] in jpeg: shutil.copy("bg.jpeg",name)
    elif os.path.splitext(name)[-1] in png: shutil.copy("bg.png",name)
        
