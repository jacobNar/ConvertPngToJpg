from PIL import Image 
import os 

files = os.listdir('images/png') # list of files in directory

for file in files:  

    if file.endswith('.png'): # check if file is png

        im = Image.open('images/png/' + file).convert("RGB") # open file as an image object
        filename = 'images/jpg/' + file[:-4]
        im.save(filename + '.jpg', "JPEG" ,quality=95, optimize=True) # save image as jpg with options