#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 15:36:59 2019

@author: tonyciccarone
"""

import os, sys
from PIL import Image

for infile in os.listdir(r"./FOLDER"):
    print("file : " + infile)
    if infile[-3:] == "tif" or infile[-3:] == "bmp" :
       script_dir = os.path.dirname(os.path.abspath(__file__))
       outfile = infile[:-3] + "jpeg"
       im = Image.open(os.path.join(script_dir, 'FOLDER/' + infile))
       out = im.convert("RGB")
       out.save(outfile, "JPEG", quality=90)
