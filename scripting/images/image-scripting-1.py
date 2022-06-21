import os
import sys 
from PIL import Image

# get arguments
folder = sys.argv[1]
newFolder = sys.argv[2]

# check folder
if not os.path.isdir(newFolder):
    os.mkdir(newFolder)

# open images
allImages = os.listdir(folder)

for image in allImages:
    path = os.path.join(folder, image)
    if os.path.isfile(path):
        img = Image.open(path)
        newPath = os.path.join(newFolder, image)
        newPath = newPath.split('.jpg')[0] + '.png'
        img.save(newPath, 'png')

# for filname in os.listdir(folder):
#     img = Image.open(f'{folder}{filname}')
#     clean_name = os.path.splitext(filname)[0]
#     img.save(f'{newFolder}{clean_name}.png', 'png')

