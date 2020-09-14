from PIL import Image  # Python Image Library - Image Processing
import os

#change the source folder(where you have images that needs to be converted)
source="C:/Users/STSC/Desktop/images"
for file in os.listdir(source):
     im = Image.open(source+'/'+file)
     rgb_im = im.convert('RGB')
     #change the current and required format of image,here the current format is png changed to jpg
     rgb_im.save(file.replace("png", "jpg"), quality=95)
