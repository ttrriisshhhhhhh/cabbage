import pathlib
import tensorflow as tf
import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
from skimage.filters import sobel
from skimage.color import label2rgb
from scipy import signal
from PIL import Image

#DATADIR = pathlib.Path("cabbage/data/dataset")
#LABELS = ["has", "none"]
#BATCH_SIZE = 32

img = cv2.imread('data/original/has/IMG_3699.jpg')
# img = cv2.imread("C:/Users/ACER/Downloads/sample.jpg")

#image_count = len(list(DATADIR.glob("/.jpg")))

#print(img)

dim = (500, 500)

def noise_red(image_file):
    print("noise")
    #converted = cv2.cvtColor(image_file, cv2.COLOR_GRAY2BGR)

    dst = cv2.fastNlMeansDenoisingColored(image_file, None, 12, 12, 7, 21)

    # plt.subplot(121), plt.imshow(image_file)
    # plt.subplot(122), plt.imshow(dst)
    # plt.show()

    print('noise done')

    return dst

def resizing(image_file):
    resized = cv2.resize(image_file, dim, interpolation=cv2.INTER_AREA)
    #cv2.imshow("Resized image", resized)
    print("Resized Dimensions : ", resized.shape)

    # print(str(resized))
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    print('resize done')

    return resized

# def edge_detect(image_file):
#     print("edge")

#     # print(image_file)

#     edges = cv2.Canny(image_file, 500, 200)

#     plt.subplot(121), plt.imshow(img, cmap="gray")
#     plt.title("Original Image"), plt.xticks([]), plt.yticks([])
#     plt.subplot(122), plt.imshow(edges, cmap="gray")
#     plt.title("Edge Image"), plt.xticks([]), plt.yticks([])

#     plt.show()

#     print('edge done')

#     return edges

def graying(image_file):

    gray = cv2.cvtColor(image_file, cv2.COLOR_BGR2GRAY)

    # cv2.imshow('Original image',image_file)
    cv2.imshow('Gray image', gray)

    print('grayscale done')

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return gray

def cluster(image_file):

    image_file = cv2.imread('data/original/has/IMG_3699.jpg')

    image = cv2.cvtColor(image_file, cv2.COLOR_BGR2RGB)

    # reshape the image to a 2D array of pixels and 3 color values (RGB)
    pixel_values = image.reshape((-1, 3))
    # convert to float
    pixel_values = np.float32(pixel_values)

    print(pixel_values.shape)

    # define stopping criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

    # number of clusters (K)
    k = 4
    _, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # convert back to 8 bit values
    centers = np.uint8(centers)

    # flatten the labels array
    labels = labels.flatten()

    # convert all pixels to the color of the centroids
    segmented_image = centers[labels.flatten()]

    # reshape back to the original image dimension
    segmented_image = segmented_image.reshape(image.shape)
    # show the image
    plt.imshow(segmented_image)
    plt.show()

    # disable only the cluster number 2 (turn the pixel into black)
    masked_image = np.copy(image)
    # convert to the shape of a vector of pixel values
    masked_image = masked_image.reshape((-1, 3))
    # color (i.e cluster) to disable
    cluster = 1
    masked_image[labels == cluster] = [0, 0, 0]
    # convert back to original shape
    masked_image = masked_image.reshape(image.shape)
    # show the image
    plt.imshow(masked_image)
    plt.show()


def threshold(image_file):  

    th = cv2.adaptiveThreshold(image_file, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 199, 5)
    cv2.imshow('original',image_file)
    cv2.imshow('Adaptive threshold',th)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return th

    # img = cv2.imread(image_file,0)
    # ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    # ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    # ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
    # ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
    # ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

    # titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
    # images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

    # plt.imshow()

    # plt.show()

def con_stretch(image_file):
    print('contrast stretching')
    # Read the image
    # print(str(image_file))

    # img1 = cv2.imread(image_file)

    # print(str(img1))
 
    # Create zeros array to store the stretched image
    minmax_img = np.zeros((image_file.shape[0], image_file.shape[1]), dtype = 'uint8')
     
    # Loop over the image and apply Min-Max formulae
    for i in range(image_file.shape[0]):
        for j in range(image_file.shape[1]):
            minmax_img[i,j] = 255*(image_file[i,j]-np.min(image_file))/(np.max(image_file)-np.min(image_file))
 
    # Display the stretched image
    cv2.imshow('Minmax',minmax_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return minmax_img

def back_remove(image_file):

    # image_file = cv2.imread('data/original/has/IMG_3699.jpg')
 
    gray_img = cv2.cvtColor(image_file, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray_img, 127, 255, cv2.ADAPTIVE_THRESH_MEAN_C + cv2.THRESH_BINARY)

    img_contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2]

    img_contours = sorted(img_contours, key=cv2.contourArea)
 
    for i in img_contours:
        if cv2.contourArea(i) > 100:
            break

    mask = np.zeros(image_file.shape[:2], np.uint8)

    cv2.drawContours(mask, [i],-1, 255, -1)

    new_img = cv2.bitwise_and(image_file, image_file, mask=mask)

    cv2.imshow("Original Image", image_file)

    cv2.imshow("Image with background removed", new_img)
 
    cv2.waitKey(0)

    return new_img




    # img = np.asarray(Image.open(image_file))/255.0

    # tmp = np.asarray(img*255.0, dtype=np.uint8)
    # Image.fromarray(tmp).save(path)


    # # estimate 'background' color by a median filter
    # bg = signal.medfilt2d(inp, 11)
    # save('background.png', bg)

    # # compute 'foreground' mask as anything that is significantly darker than
    # # the background
    # mask = inp < bg - 0.1
    # save('foreground_mask.png', mask)

    # # return the input value for all pixels in the mask or pure white otherwise
    # return np.where(mask, inp, 1.0)

    # inp_path = '../input/train/2.png'
    # out_path = 'output.png'

    # inp = load_image(inp_path)
    # out = denoise_image(inp)

    # # save(out_path, out)

    # return out

# reduced = noise_red(img)
# segmented = cluster(reduced)
resized = resizing(img)
# grayed = graying(resized)
# thresh = threshold(grayed)
# stretched = con_stretch(thresh)
# edged = edge_detect(thresh)
# final = back_remove(stretched)

removed = back_remove(resized)