# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 22:08:33 2018
@author: Xiang Guo
"""

import glob

import os
#os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/local/Caskroom/miniforge/base/envs/vr/lib/python3.8/site-packages/ffmpeg"
import moviepy.editor as mpy
import re
from tqdm import tqdm


os.chdir('/Users/leas/Desktop/Read_Boxes/Data/video_frames_out_LR/')
out_dir = '/Users/leas/Desktop/Read_Boxes/Data/gaze_vids_out/'

fps = 30

for sub_dir in tqdm(os.listdir()):
    print(sub_dir)
    folder = '/Users/leas/Desktop/Read_Boxes/Data/video_frames_out_LR/' + sub_dir
    print(folder)
    os.chdir(folder)
    file_list = glob.glob('*.jpg') # Get all the pngs in the current directory
    #file_list = glob.glob(folder + '/*.jpg') # Get all the pngs in the current directory
    

    lsorted = sorted(file_list,key=lambda x: int(os.path.splitext(x)[0]))
    
    #ordered_file_list =sorted(file_list, key=lambda x: (int(re.sub('/D','',x)),x))
    
    clip = mpy.ImageSequenceClip(lsorted, fps=fps)
    #clip = mpy.ImageSequenceClip(file_list, fps=fps)
    
    clip.write_videofile(out_dir + sub_dir + ".mp4")
