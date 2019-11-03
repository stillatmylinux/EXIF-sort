import  PIL as pillow
from PIL import Image
import time
from shutil import move
import os

def sort(sourceFolder, destFolder): 

    tree = os.walk(sourceFolder) #create generator

    files = [] # all files from source folder to list
    for i in tree:
        files.append(i)

    for file in files[0][2]:

        if not (file.rsplit('.',1)[1].upper() == "JPG" or file.rsplit('.',1)[1].upper() == "JPEG"):
            continue

        path = files[0][0]+file
        img = Image.open(path)
        exifData = img._getexif()
        img.close()
        strImageDate = exifData[306]
        imageDate = time.strptime(strImageDate,"%Y:%m:%d %H:%M:%S")
        #create folder with name = date of jpeg(EXIF)
        destSubFolder = destFolder + str(imageDate[0]) + "-" + str('%02d' % imageDate[1]) + "-" + str('%02d' % imageDate[2]) + "/"

        try:
            os.mkdir(destSubFolder)
        except:
            print(destSubFolder, "already exist")

        #name of jpg = time of shot
        newPath = destSubFolder + str(imageDate[3]) + "-" + str('%02d' % imageDate[4]) + "-" + str('%02d' % imageDate[5]) + ".jpg"
        move(path, newPath)


# sort(sourceFolder, destFolder)



