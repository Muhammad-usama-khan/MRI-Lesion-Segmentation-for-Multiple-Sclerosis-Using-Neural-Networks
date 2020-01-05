# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 14:45:14 2019

@author: Usama
"""

import os
import nibabel as nib
import numpy as np
from os import listdir
import matplotlib.pyplot as plt
import scipy.io as sio
from medpy.io import load, save
from os.path import isfile, join
import keras
from keras.preprocessing.image import ImageDataGenerator
#%%
vol_path = 'D:\\Neural_Nets\\Project\\2. Brain_Extracted_Data/'

save_path = 'D:\\Neural_Nets\\Project\\3. Normalised_Data\\FLAIR/'

subfolders = [f.path for f in os.scandir(vol_path) if f.is_dir() ]
save_subfolders = [f.path for f in os.scandir(save_path) if f.is_dir() ]

os.chdir(vol_path) # If this gives error close and restart the program
volumes = [f for f in listdir(vol_path) if isfile(join(vol_path, f))]
#%%
keras.preprocessing.image.ImageDataGenerator(featurewise_center=False, samplewise_center=False, featurewise_std_normalization=False, samplewise_std_normalization=False, zca_whitening=False, zca_epsilon=1e-06, rotation_range=0, width_shift_range=0.0, height_shift_range=0.0, brightness_range=None, shear_range=0.0, zoom_range=0.0, channel_shift_range=0.0, fill_mode='nearest', cval=0.0, horizontal_flip=False, vertical_flip=False, rescale=None, preprocessing_function=None, data_format=None, validation_split=0.0, dtype=None)
#%%
train_datagen = keras.preprocessing.image.ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
#%%
train_generator = train_datagen.flow_from_directory(
        dir,
        target_size=(256, 256),
        batch_size=32,
        class_mode='categorical',
        save_to_dir = 'C:\\Users\\Usama\\OneDrive\\Pictures\\Camera Roll/' )

#%%
train_generator = train_datagen.flow_from_directory(
        dir, 
        target_size=(256, 256),
        color_mode='rgb', 
        classes=None, class_mode='categorical', 
        batch_size=32, 
        shuffle=True, 
        seed=None, 
        save_to_dir=None, 
        save_prefix='', 
        save_format='png', 
        follow_links=False, 
        subset=None, 
        interpolation='nearest',
        )

#%%
validation_generator = test_datagen.flow_from_directory(
        'data/validation',
        target_size=(150, 150),
        batch_size=32,
        class_mode='binary')

model.fit_generator(
        train_generator,
        steps_per_epoch=2000,
        epochs=50,
        validation_data=validation_generator,
        validation_steps=800)
