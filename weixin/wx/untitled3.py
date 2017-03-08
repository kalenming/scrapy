# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 16:50:30 2017

@author: Administrator
"""

from PIL import Image
import glob, os
import numpy as np



mw = 120 # 图片大小+图片间隔
ms = 18

msize = mw * ms


toImage = Image.new('RGBA', (msize, msize))

for y in range(1, 19):  ## 先试一下 拼一个5*5 的图片
    for x in range(1,19):

        # 之前保存的图片是顺序命名的，x_1.jpg, x_2.jpg ...
        fname = "%s.jpg" % (ms*(y-1)+x)

        fromImage = Image.open(fname)
        #fromImage =fromImage.resize((mw, mw), Image.ANTIALIAS)   # 先拼的图片不多，不用缩小

        toImage.paste(fromImage, ((x-1) * mw, (y-1) * mw))

toImage.save('./all.jpg')