import json as j
import xml.etree.cElementTree as e
import os
import cv2
import numpy as np
dest='C:/Users/STSC/Desktop/labels'
images='C:/Users/STSC/Desktop/Medical mask/Medical Mask/images'
#path='C:/Users/STSC/Desktop/Medical mask/Medical Mask/annotations'
path='C:/Users/STSC/Downloads/Medical+mask/Medical mask/Medical Mask/anoCopy'
for file in os.listdir(path):

    with open(path+'/'+file) as json_format_file:
        d = j.load(json_format_file)
        imgno=file.strip('.json')
        #print(imgno)

        im = cv2.imread(images+'/'+imgno)
        height, width, channels = im.shape



        r = e.Element("annotation")

        e.SubElement(r,"folder").text = path

        e.SubElement(r,"filename").text = file

        e.SubElement(r,"path").text = path

        source = e.SubElement(r,"source")
        e.SubElement(source,"database").text = "Unknown"
        size = e.SubElement(r,"size")
        e.SubElement(size,"width").text = str(height)
        e.SubElement(size,"height").text = str(width)
        e.SubElement(size,"depth").text = str(channels)

        e.SubElement(r,"segmented").text = "0"



#object = e.SubElement(r,"objects")

        for z in d["Annotations"]:
            object = e.SubElement(r,"object")
            e.SubElement(object,"name").text = z["classname"]
            e.SubElement(object,"pose").text = "Unspecified"
            e.SubElement(object,"truncated").text = "0"
            e.SubElement(object,"difficult").text = "0"
            bndbox = e.SubElement(object,"bndbox")
            e.SubElement(bndbox,"xmin").text = str(z["BoundingBox"][0])
            e.SubElement(bndbox,"xmax").text = str(z["BoundingBox"][1])
            e.SubElement(bndbox,"ymin").text = str(z["BoundingBox"][2])
            e.SubElement(bndbox,"ymax").text = str(z["BoundingBox"][3])

        a = e.ElementTree(r)

        a.write(dest+'/'+file+".xml")
        json_format_file.close()
