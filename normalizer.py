import pathlib
import tensorflow as tf
import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

#DATADIR = pathlib.Path("cabbage/data/dataset")
#LABELS = ["has", "none"]
#BATCH_SIZE = 32

#img = cv2.imread("data/original/has/IMG_3690.jpg")

#image_count = len(list(DATADIR.glob("/.jpg")))

#print(img)

dim = (500, 500)

def noise_red(image_file):
    print("noise")
    #converted = cv2.cvtColor(image_file, cv2.COLOR_GRAY2BGR)

    dst = cv2.fastNlMeansDenoisingColored(image_file, None, 10, 10, 7, 21)

    # plt.subplot(121), plt.imshow(img)
    # plt.subplot(122), plt.imshow(dst)
    # plt.show()

    return dst

def resizing(image_file):
    resized = cv2.resize(image_file, dim, interpolation=cv2.INTER_AREA)
    # cv2.imshow("Resized image", resized)
    print("Resized Dimensions : ", resized.shape)

    # print(str(resized))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return resized

def edge_detect(image_file):
    print("edge")

    edges = cv2.Canny(img, 200, 500)

    # plt.subplot(121), plt.imshow(img, cmap="gray")
    # plt.title("Original Image"), plt.xticks([]), plt.yticks([])
    # plt.subplot(122), plt.imshow(edges, cmap="gray")
    # plt.title("Edge Image"), plt.xticks([]), plt.yticks([])

    # plt.show()