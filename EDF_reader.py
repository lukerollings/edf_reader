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

os.chdir('C://Users//mbgnwlr2//Documents//PhD_SynchrotronStuff//Winter18_beamtime_data//radio//Al_SiC_1D_0')

images = glob.glob('Al_SiC_1D_0_*.edf')

for i in images:
    img = fabio.open(str(i))
    plt.figure(figsize=(8,4))
    plt.imshow(img.data)