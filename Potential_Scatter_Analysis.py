
# coding: utf-8

# ## Working Space
# Directory: Insert the directory with images under quotations

# In[1]:


dirname='/Users/mbeck/Desktop/filename'


# ## Import

# In[ ]:


import os 
from PIL import Image
import numpy as np

dirname = 'tiff_folder_path'#Insert folder file path
final = []
for fname in os.listdir(dirname):
    im = Image.open(os.path.join(dirname, fname))
    imarray = np.array(im)
    final.append(imarray)

final = np.asarray(final) #creates a numpy array for each image in the folder
length=len(final) #determines length of numpy array


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#function converts images to grayscale
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

gray = rgb2gray(final)    
plt.imshow(gray, cmap = plt.get_cmap('gray'))
plt.show()


# ## Getting Data From Coordinates
# Coordinates
