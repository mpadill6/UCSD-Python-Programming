# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 13:58:06 2020

@author: mpadilla
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy.io import wavfile 

#Show Original Image

class MMedia_Processing:
     def __init__ (self,filename_image,filename_audio):
        self.filename_image=filename_image #File Name for Image
        self.filename_audio=filename_audio #Filename audio
        
     def ImgProc(self):
        self.img=mpimg.imread(self.filename_image) #Read Desired Image
        plt.figure()
        plt.title('Original Image')
        plt.imshow(self.img) #Show Normal Image
        
        self.red=self.img[:,:,0]
        self.green=self.img[:,:,1]
        self.blue=self.img[:,:,2]
       
        #Plot Red Component
        plt.figure()
        plt.title('Red Channel')
        plt.imshow(self.red)
   
        #Plot Green Channel
        plt.figure()
        plt.title('Green Channel')
        plt.imshow(self.green)
        
        
        #Plot Blue Channel
        plt.figure()
        plt.title('Blue Channel')
        plt.imshow(self.blue)        
        
        #Plot Histogram of original picture
        plt.figure(figsize=(10,20))
        
        plt.subplot(311)
        plt.hist(self.red.ravel(),bins=256,range=(0,255),fc='k',ec='k')
        plt.xlabel("Pixel Intensity")
        plt.ylabel("Count")
        plt.grid()
        plt.title("Red Channel Histogram")
        plt.subplot(312)
        plt.hist(self.green.ravel(),bins=256,range=(0,255),fc='k',ec='k')
        plt.xlabel("Pixel Intensity")
        plt.ylabel("Count")
        plt.grid()
        plt.title("Green Channel Histogram")
        plt.subplot(313)
        plt.hist(self.blue.ravel(),bins=256,range=(0,255),fc='k',ec='k')
        plt.xlabel("Pixel Intensity")
        plt.ylabel("Count")
        plt.grid()
        plt.title("Blue Channel Histogram")
     
     def AudProc(self):
        plt.figure(figsize=(10,20))
        self.Fs, self.data=wavfile.read(self.filename_audio)
        self.length=self.data.shape[0]/self.Fs #Duration of Audio in Seconds
        self.time=np.linspace(0.,self.length,self.data.shape[0]) #Create linspace for time in intervals of each sample point
        self.index=np.arange(0,self.data.shape[0]) #Create array with size of sample index for each sample point
        plt.subplot(211)
        plt.plot(self.index,self.data[:,0]) #Choose Time or Index. Plot is the same either way
        plt.title("Alone-Sistar.wav")
        plt.xlabel("Sample Index")
        plt.grid()
        #plt.xlabel("Seconds")
        plt.ylabel("Amplitude")
        self.reverse=np.zeros((self.data.shape[0],self.data.shape[1]))
        for a in range(0,2):
            self.neg_index=-1
            for i in range(0, self.data.shape[0]):
                self.reverse[i][a]=int(self.data[self.neg_index][a])
                self.neg_index-=1
        self.reverseint=self.reverse.astype('int16')
        wavfile.write("Reverse Alone-Sistar.wav", self.Fs,self.reverseint)
        plt.subplot(212)
        plt.plot(self.index,self.reverseint[:,0]) #Choose Time or Index. Plot is the same either way
        plt.title("Reverse Alone-Sistar.wav")
        plt.xlabel("Sample Index")
        plt.grid()
        #plt.xlabel("Seconds")
        plt.ylabel("Amplitude")
        
        
Media=MMedia_Processing('BigDataImage-1.jpg','Alone-Sistar.wav')
Media.ImgProc()
Media.AudProc()