# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 15:23:24 2018

@author: mbgnwlr2
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import fabio
import glob
from skimage import exposure

os.chdir('C://Users//mbgnwlr2//Documents//PhD_SynchrotronStuff//Winter18_beamtime_data//radio//Al_SiC_1D_0')

images = glob.glob('Al_SiC_1D_0_*[0-4].edf')

light = fabio.open('Al_SiC_1D_0_0005.edf')
background = light.data
dark = fabio.open('Al_SiC_1D_0_0006.edf')
darkfield = dark.data
full = np.full_like(background, np.amax(background))

I = 0

for i in images:
    edf = fabio.open(str(i))
    img = edf.data
    new = np.divide(img, background, dtype = np.float32)
    final = exposure.rescale_intensity(new, (0.0510, 1.7))
    plt.figure(figsize=(8,4))
    plt.imshow(new)
#    plt.imsave('Al_SiC_1D_0_000'+str(I)+'.jpg', new)

    I = I+1
    
#images = glob.glob('Al_SiC_1D_0_*.jpg')