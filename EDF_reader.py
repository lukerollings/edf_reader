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
from PIL import Image

os.chdir('C://Users//mbgnwlr2//Documents//PhD_SynchrotronStuff//Winter18_beamtime_data//radio//Al_SiC_1D_0')

images = glob.glob('Al_SiC_1D_0_*.edf')


I = 0

for i in images:
    edf = fabio.open(str(i))
    img = edf.data
    plt.figure(figsize=(8,4))
    plt.imsave('Al_SiC_1D_0_000'+str(I)+'.jpg', img)

    I = I+1