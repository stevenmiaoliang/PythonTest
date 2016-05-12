import numpy as np
from PIL import Image
from matplotlib.pyplot import *
from scipy.ndimage import filters
from imtool import imtool as it
import cv2

pil_im = Image.open("lena.bmp")
figure(),gray(),imshow(pil_im)
im2,hist = it.histeq(np.array(pil_im));
figure(),gray(),imshow(im2)
imlist = ["lena.bmp","lena.bmp","lena.bmp"]
imAve = it.compute_average(imlist)
figure(),gray(),imshow(imAve)
show()

im = np.array( Image.open("lena.bmp"))
m,n = im.shape[0:2]
immaxtrix = np.array(im,'f')



