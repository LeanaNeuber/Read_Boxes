# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 16:15:43 2020
@author: Xiang Guo
"""

import numpy as np
import os
import cv2
import re
from matplotlib import pyplot as plt
import pandas as pd
from tqdm import tqdm
os.chdir('/Users/leas/Desktop/Read_Boxes/Data/')


frame_dir = 'movie_2022-07-03'
framelist = os.listdir(os.path.join('vid_frames',frame_dir))

frame_out_dir = os.path.join('video_frames_out_LR',frame_dir)
try: 
    os.mkdir(frame_out_dir)
except:
    pass

#number of frame images
framelen=len(framelist)

# read the raw data
csv_dir = '/Users/leas/Desktop/Read_Boxes/Data/'
csv_file = 'vr_data_20220703T162408.csv'
df = pd.read_csv(csv_dir + csv_file)

df_valid = df[df['CombinedGazeRayWorldValid'] == True]
#length of raw data
dflen = len(df)



img_path = os.getcwd() + '/vid_frames/'  + frame_dir + '/' + framelist[0]
img =cv2.imread(img_path)
dimensions = img.shape
 # height, width, number of channels in image
height = img.shape[0]
width = img.shape[1]


def closest(lst, K):       
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))] 



time_series = df['AdjustedTime']
valid_time_series = df_valid['AdjustedTime']

# Given the gaze vector, return the x/y position for the gaze point in open-cv video
def return_x_y(gaze):
    pattern = "[" + '(' + ')' + "]"
    new_gaze_string = re.sub(pattern, "", gaze)    
    xyz = new_gaze_string.split(',')
    x= width/2*float(xyz[0])
    y = height/2*float(xyz[1])        
    cv_x = round(width/2 + x)
    cv_y = round(height/2 - y)        
    return cv_x,cv_y






for j in tqdm(framelist):
    i = int(re.findall("\d+",j)[0])
    img_path = os.getcwd() + '/vid_frames/'  + frame_dir + '/' + j
    # time from the video
    t = i/30
    # time in raw data
    t1 = closest(list(time_series), t)    
    t_index = list(time_series).index(t1)
    
    
    if df['CombinedGazeRayWorldValid'][t_index] == True:
        #gaze_dir = df['CombinedGazeRayWorldDirection'][t_index]
        gaze_l = df['LeftGazeDirection'][t_index]
        gaze_r = df['RightGazeDirection'][t_index]
        
        gaze_origin_l = df['LeftGazeOrigin'][t_index]
        gaze_origin_r = df['RightGazeOrigin'][t_index]
        
 
        #cv_x,cv_y = return_x_y(gaze_dir)
        cv_x_l,cv_y_l = return_x_y(gaze_l)
        cv_x_r,cv_y_r = return_x_y(gaze_r)
        

        
        img =cv2.imread(img_path)
        #cv2.circle(img,(cv_x, cv_y), 20, (0,0,255),-1)
        cv2.circle(img,(cv_x_l, cv_y_l), 20, (0,255,0),-1)
        cv2.circle(img,(cv_x_r,cv_y_r), 20, (255,0,0),-1)
        #plt.imshow(img)
        cv2.imwrite(frame_out_dir + '/' + re.findall("\d+",j)[0] +'.jpg',img)        
    
    else:
        # Find the closest time in valid raw data
        t_2 = closest(list(valid_time_series), t) 
        
        if abs(t_2 - t) <= 0.1:
            t2_index = valid_time_series[valid_time_series == t_2].index[0]
            #gaze_dir = df['CombinedGazeRayWorldDirection'][t2_index]
            gaze_l = df['LeftGazeDirection'][t2_index]
            gaze_r = df['RightGazeDirection'][t2_index]
            
            #cv_x,cv_y = return_x_y(gaze_dir)
            cv_x_l,cv_y_l = return_x_y(gaze_l)
            cv_x_r,cv_y_r = return_x_y(gaze_r)
            
    
            
            img =cv2.imread(img_path)
            #cv2.circle(img,(cv_x, cv_y), 20, (0,0,255),-1)
            cv2.circle(img,(cv_x_l, cv_y_l), 20, (0,255,0),-1)
            cv2.circle(img,(cv_x_r,cv_y_r), 20, (255,0,0),-1)
            #plt.imshow(img)
            cv2.imwrite(frame_out_dir + '/' + re.findall("\d+",j)[0] +'.jpg',img)                  
            
        else:
            img =cv2.imread(img_path)
            cv2.imwrite(frame_out_dir + '/' + re.findall("\d+",j)[0] +'.jpg',img)
            


