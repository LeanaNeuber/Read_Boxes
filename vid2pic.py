# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 10:15:56 2018
@author: Xiang Guo
"""

## To read the videos and write frame images.
import numpy as np
import cv2
import os
import glob
os.chdir('/Users/leas/Desktop/Read_Boxes/Data/raw_vids/')

videolist = glob.glob('*.mp4')
output_path = '/Users/leas/Desktop/Read_Boxes/Data/vid_frames/'

for vid in videolist:
    path = output_path + vid.split('.')[0]  
    print(path)
    try:
        os.mkdir(path)
    except:
        pass
    vidcap = cv2.VideoCapture(vid)
    

    
    success,image = vidcap.read()
    print(success)
    count = 0
    success = True
    while success:
        success,image = vidcap.read()
        filename = str("/%d.jpg" % (count+1))
        filepath = path + filename
        print(count)
        cv2.imwrite(filepath, image)     # save frame as JPEG file
        count += 1
    os.remove(filepath)
