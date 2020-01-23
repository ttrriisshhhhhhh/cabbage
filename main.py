import pathlib
import tensorflow as tf
import cv2
import glob
import os
import numpy as np
from matplotlib import pyplot as plt
import shutil
import normalizer

DATADIR = pathlib.Path("cabbage/data")
# files = DATADIR.glob("/.jpg")

def preprocess():
	print('start')

	normalizer.edge_detect()

	datasource_dir = pathlib.Path("cabbage/data/original")
	dataset_dir = pathlib.Path("cabbage/data/resized")
	
	# empty dataset dir
	print('empty')
	if dataset_dir.exists():
	    shutil.rmtree(dataset_dir)
	os.mkdir(dataset_dir)

	# create labels folder
	print('labels')
	for label in list(datasource_dir.glob("*")):
	    os.mkdir(dataset_dir/label.name)

	for file in list(datasource_dir.glob("*/*.jpg")):
	    img = cv.imread(str(file))
	    #img = cv.resize(img, (500, 500), interpolation = cv.INTER_AREA)
	    
	    label = file.parts[-2]
	    name = file.name
	    dest = dataset_dir/label/name
	    cv.imwrite(str(dest), img)

	    print('done')

	cabbage_img = list(DATADIR.glob("original/*.jpg"))
	print("pre")
	for image_path in cabbage_img[:3]:
		print("GUMANA")
		display.display(Image.open(str(image_path)))

preprocess()

# IMG_SIZE = 500
# BATCH_SIZE = 32

# img = cv2.imread('cabbage/data/dataset/has/IMG_3690.jpg', cv2.IMREAD_UNCHANGED)

# image_count = len(list(DATADIR.glob('*/*.jpg')))

# def preprocess():
# 	print('pre')
# 	path = glob.glob("cabbage/data/*.jpg")
# 	cv2_img = []
# 	for i in path[:3]:
# 		print(i)
# 		n = cv2.imread(i)
# 		cv2_img.append(n)

# preprocess()
