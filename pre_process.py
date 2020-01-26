import cv2
import numpy as np
from matplotlib import pyplot as plt

def resize_img(image_file):
	print('resizing')

	dim = (600, 600)

	resized = cv2.resize(image_file, dim)
	 
	# cv2.imshow('Resized Image', resized)
	 
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	print('resize done')

	return resized

def bgr(image_file):
	gray_img = cv2.cvtColor(image_file, cv2.COLOR_BGR2GRAY)
	retval, thresh = cv2.threshold(gray_img, 127, 255, 0)
	img_contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	cv2.drawContours(image_file, img_contours, -1, (0, 255, 0))
	cv2.imshow('Image Contours', image_file)
 
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	return image_file

def remove_bg(image_file):
	gray_img = cv2.cvtColor(image_file, cv2.COLOR_BGR2GRAY)
	retval, thresh = cv2.threshold(gray_img, 127, 255, 0)
	img_contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	mask = np.zeros(image_file.shape[:2], np.uint8)
	cv2.drawContours(mask, img_contours,-1, 255, -1)
	new_img = cv2.bitwise_and(image_file, image_file, mask=mask)
	cv2.imshow("Original Image", image_file)
	cv2.imshow("Image with background removed", new_img)

	cv2.waitKey(0)
	cv2.destroyAllWindows()

	return new_img

def bgr2(image_file):
	# image = cv2.imread("data/original/has/IMG_3699.jpg")
	original = image_file.copy()
	hsv = cv2.cvtColor(image_file, cv2.COLOR_BGR2HSV)

	hsv_lower = np.array([41,57,78])
	hsv_upper = np.array([145,255,255])
	mask = cv2.inRange(hsv, hsv_lower, hsv_upper)
	result = cv2.bitwise_and(original, original, mask=mask)

	cv2.imshow('mask', mask)
	cv2.imshow('result', result)

	cv2.waitKey()
	cv2.destroyAllWindows()

	return result


# def remove_bg(image_file):
# 	print('bgr')
# 	#== Parameters =======================================================================
# 	BLUR = 21
# 	CANNY_THRESH_1 = 10
# 	CANNY_THRESH_2 = 200
# 	MASK_DILATE_ITER = 10
# 	MASK_ERODE_ITER = 10
# 	MASK_COLOR = (0.0,0.0,1.0) # In BGR format
# 	#== Processing =======================================================================

# 	#-- Read image -----------------------------------------------------------------------
# 	gray = cv2.cvtColor(image_file,cv2.COLOR_BGR2GRAY)

# 	#-- Edge detection -------------------------------------------------------------------
# 	edges = cv2.Canny(gray, CANNY_THRESH_1, CANNY_THRESH_2)
# 	edges = cv2.dilate(edges, None)
# 	edges = cv2.erode(edges, None)

# 	#-- Find contours in edges, sort by area ---------------------------------------------
# 	contour_info = []
# 	# _, contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# 	# Previously, for a previous version of cv2, this line was: 
# 	contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# 	# Thanks to notes from commenters, I've updated the code but left this note
# 	for c in contours:
# 	    contour_info.append((
# 	        c,
# 	        cv2.isContourConvex(c),
# 	        cv2.contourArea(c),
# 	    ))
# 	contour_info = sorted(contour_info, key=lambda c: c[2], reverse=True)
# 	max_contour = contour_info[0]

# 	#-- Create empty mask, draw filled polygon on it corresponding to largest contour ----
# 	# Mask is black, polygon is white
# 	mask = np.zeros(edges.shape)
# 	cv2.fillConvexPoly(mask, max_contour[0], (255))

# 	#-- Smooth mask, then blur it --------------------------------------------------------
# 	mask = cv2.dilate(mask, None, iterations=MASK_DILATE_ITER)
# 	mask = cv2.erode(mask, None, iterations=MASK_ERODE_ITER)
# 	mask = cv2.GaussianBlur(mask, (BLUR, BLUR), 0)
# 	mask_stack = np.dstack([mask]*3)    # Create 3-channel alpha mask

# 	#-- Blend masked image_file into MASK_COLOR background --------------------------------------
# 	mask_stack  = mask_stack.astype('float32') / 255.0          # Use float matrices, 
# 	image_file         = image_file.astype('float32') / 255.0                 #  for easy blending

# 	masked = (mask_stack * image_file) + ((1-mask_stack) * MASK_COLOR) # Blend
# 	masked = (masked * 255).astype('uint8')                     # Convert back to 8-bit 

# 	cv2.imshow('image_file', masked)                                   # Display
	
# 	cv2.waitKey(0)
# 	cv2.destroyAllWindows()

# 	print('bgr done')

# 	return masked


img = cv2.imread('data/original/has/IMG_3699.jpg')

resized_img = resize_img(img)
#contrasted_img = contrast_img(resized_img)
# segmented_img = segment_img(resized_img)
# bg_removed = remove_bg(resized_img)
# brem = bgr(resized_img)
bgr2r = bgr2(resized_img)