import pathlib
import tensorflow as tf
import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

DATADIR = pathlib.Path("cabbage/data/dataset")
LABELS = ["has", "none"]
IMG_SIZE = 500
BATCH_SIZE = 32

img = cv2.imread('cabbage/data/dataset/has/IMG_3690.jpg', cv2.IMREAD_UNCHANGED)

#image_count = len(list(DATADIR.glob('*/*.jpg')))

dim = (IMG_SIZE, IMG_SIZE)

def resizing():
	resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	cv2.imshow("Resized image", resized)
	print('Resized Dimensions : ',resized.shape)

	#print(str(resized))
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	return resized

def noise_red():
	print('noise')
	img = resizing()

	dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

	plt.subplot(121),plt.imshow(img)
	plt.subplot(122),plt.imshow(dst)
	plt.show()

	return dst

def edge_detect():
	print('edge')
	img = noise_red()
	
	edges = cv2.Canny(img,100,200)

	plt.subplot(121),plt.imshow(img, cmap = 'gray')
	plt.title('Original Image'), plt.xticks([]), plt.yticks([])
	plt.subplot(122),plt.imshow(edges,cmap = 'gray')
	plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

	plt.show()

edge_detect()

# source_dir = pathlib.Path('cabbage/data/original')
# files = list(source_dir.glob('*/*.jpg'))
# print(len(files))
# print(os.getcwd())
# for file in files:
# 	print(file)