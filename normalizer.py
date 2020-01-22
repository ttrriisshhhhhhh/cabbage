import pathlib
import tensorflow as tf
import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
from skimage.filters import sobel
from skimage.color import label2rgb

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

    print('noise done')

    return dst

def resizing(image_file):
    resized = cv2.resize(image_file, dim, interpolation=cv2.INTER_AREA)
    # cv2.imshow("Resized image", resized)
    print("Resized Dimensions : ", resized.shape)

    # print(str(resized))
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    print('resize done')

    return resized

def edge_detect(image_file):
    print("edge")

    # print(image_file)

    edges = cv2.Canny(image_file, 100, 200)

    # plt.subplot(121), plt.imshow(img, cmap="gray")
    # plt.title("Original Image"), plt.xticks([]), plt.yticks([])
    # plt.subplot(122), plt.imshow(edges, cmap="gray")
    # plt.title("Edge Image"), plt.xticks([]), plt.yticks([])

    # plt.show()

    # print('edge done')

    return edges

def back_remove():
    ### PARAMETERS ###
    BLUR = 21
    CANNY_THRESH_1 = 200
    CANNY_THRESH_2 = 200
    MASK_DILATE_ITER = 10
    MASK_ERODE_ITER = 10
    MASK_COLOR = (0.0,0.0,1.0) # In BGR format

    img = cv2.imread('data/original/has/IMG_3699.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, CANNY_THRESH_1, CANNY_THRESH_2)
    edges = cv2.dilate(edges, None)
    edges = cv2.erode(edges, None)

    contour_info = []
    contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    # Previously, for a previous version of cv2, this line was: 
    #  contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    # Thanks to notes from commenters, I've updated the code but left this note
    for c in contours:
        contour_info.append((
            c,
            cv2.isContourConvex(c),
            cv2.contourArea(c),
        ))
    contour_info = sorted(contour_info, key=lambda c: c[2], reverse=True)
    max_contour = contour_info[0]

    #-- Create empty mask, draw filled polygon on it corresponding to largest contour ----
    # Mask is black, polygon is white
    mask = np.zeros(edges.shape)
    cv2.fillConvexPoly(mask, max_contour[0], (255))

    #-- Smooth mask, then blur it --------------------------------------------------------
    mask = cv2.dilate(mask, None, iterations=MASK_DILATE_ITER)
    mask = cv2.erode(mask, None, iterations=MASK_ERODE_ITER)
    mask = cv2.GaussianBlur(mask, (BLUR, BLUR), 0)
    mask_stack = np.dstack([mask]*3)    # Create 3-channel alpha mask

    #-- Blend masked img into MASK_COLOR background --------------------------------------
    mask_stack  = mask_stack.astype('float32') / 255.0          # Use float matrices, 
    img         = img.astype('float32') / 255.0                 #  for easy blending

    masked = (mask_stack * img) + ((1-mask_stack) * MASK_COLOR) # Blend
    masked = (masked * 255).astype('uint8')                     # Convert back to 8-bit 

    cv2.imshow('img', masked)                                   # Display
    cv2.waitKey()

    #cv2.imwrite('C:/Temp/person-masked.jpg', masked)           # Save

    # split image into channels
    c_red, c_green, c_blue = cv2.split(img)

    # merge with mask got on one of a previous steps
    img_a = cv2.merge((c_red, c_green, c_blue, mask.astype('float32') / 255.0))

    # show on screen (optional in jupiter)
    #matplotlib inline
    plt.imshow(img_a)
    plt.show()

    # save to disk
    #cv2.imwrite('girl_1.png', img_a*255)

    # or the same using plt
    #plt.imsave('girl_2.png', img_a)

#back_remove()

# def remove_back():
#     import numpy as np
#     from scipy import signal
#     from PIL import Image


#     def load_image(path):
#         return np.asarray(Image.open(path))/255.0

#     def save(path, img):
#         tmp = np.asarray(img*255.0, dtype=np.uint8)
#         Image.fromarray(tmp).save(path)

#     def denoise_image(inp):
#         # estimate 'background' color by a median filter
#         bg = signal.medfilt2d(inp, 11)
#         #save('background.png', bg)

#         # compute 'foreground' mask as anything that is significantly darker than
#         # the background
#         mask = inp < bg - 0.1
#         #save('foreground_mask.png', mask)

#         # return the input value for all pixels in the mask or pure white otherwise
#         return np.where(mask, inp, 1.0)


#     inp_path = 'data/original/has/IMG_3699.jpg'
#     out_path = 'output.png'

#     inp = load_image(inp_path)
#     out = denoise_image(inp)

#     imshow(out)

# remove_back()

def segment():

    elevation_map = sobel(coins)

    fig, ax = plt.subplots(figsize=(4, 3))
    ax.imshow(elevation_map, cmap=plt.cm.gray)
    ax.set_title('elevation map')
    ax.axis('off')

    markers = np.zeros_like(coins)
    markers[coins < 30] = 1
    markers[coins > 150] = 2

    fig, ax = plt.subplots(figsize=(4, 3))
    ax.imshow(markers, cmap=plt.cm.nipy_spectral)
    ax.set_title('markers')
    ax.axis('off')

    segmentation = morphology.watershed(elevation_map, markers)

    fig, ax = plt.subplots(figsize=(4, 3))
    ax.imshow(segmentation, cmap=plt.cm.gray)
    ax.set_title('segmentation')
    ax.axis('off')

    

    segmentation = ndi.binary_fill_holes(segmentation - 1)
    labeled_coins, _ = ndi.label(segmentation)
    image_label_overlay = label2rgb(labeled_coins, image=coins)

    fig, axes = plt.subplots(1, 2, figsize=(8, 3), sharey=True)
    axes[0].imshow(coins, cmap=plt.cm.gray)
    axes[0].contour(segmentation, [0.5], linewidths=1.2, colors='y')
    axes[1].imshow(image_label_overlay)

    for a in axes:
        a.axis('off')

    plt.tight_layout()

    plt.show()

segment()