# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 12:38:26 2019

@author: Usama
"""
#%%
import os
import nibabel as nib
import numpy as np
from os import listdir
import matplotlib.pyplot as plt
import scipy.io as sio
from medpy.io import load, save
from os.path import isfile, join

#%%
vol_path = 'D:\\Neural_Nets\\Project\\1.Raw_Data/'

save_path = 'D:\\Neural_Nets\\Project\\2. Brain_Extracted_Data'

os.chdir(vol_path) # If this gives error close and restart the program

subfolders = [f.path for f in os.scandir(vol_path) if f.is_dir() ]
save_subfolders = [f.path for f in os.scandir(save_path) if f.is_dir() ]

#%%
x=1
y=0
num_folders = len(subfolders)

for i in range(num_folders):

    
    print(i)
    
    #go into patients and get all teh volumes
    os.chdir (subfolders[i]) 
    volumes = [f for f in listdir(subfolders[i]) if isfile(join(subfolders[i], f))]
    
    #get Mask
    mask_name = volumes[0]
    mask = nib.load(mask_name)
    mask=mask.get_data()
    
    #get Flair
    flair_name = volumes[2]
    flair = nib.load(flair_name)
    flair=flair.get_data()
    
     #get GT
    gt_name = volumes[1]
    gt = nib.load(gt_name)
    gt=gt.get_data()
    
    extracted_brain = flair*mask
    
    patient = 'patient_'
    extractbrain='_extracted_brain.nii.gz'
    gt_gt='_gt.nii.gz'

    if x < 10:
        extracted_brain_name = patient + str(y) + str(x) + extractbrain
        gt_name_new = patient+ str(y) + str(x) + gt_gt
    else:
        x=0
        y=y+1
        extracted_brain_name = patient + str(y) + str(x) + extractbrain
        gt_name_new = patient+ str(y) + str(x) + gt_gt
    

    os.chdir(save_subfolders[0])
    save(extracted_brain, extracted_brain_name)
    os.chdir(save_subfolders[1])
    save(gt, gt_name_new)    
    
    del gt
    del extracted_brain
    del flair
    del mask
    
    x=x+1
#%%
x=1
y=0
z=1
for i in range(num_folders):
    
    if x < 10:
        print(y,x)
        x=x+1
    else:
        x=1
        y=y+1
        
    print(z)
    z=z+1








