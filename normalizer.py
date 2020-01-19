import pathlib
import tensorflow as tf
import cv2

DATADIR = pathlib.Path("cabbage/data/dataset")
LABELS = ["has", "none"]
IMG_SIZE = 500
BATCH_SIZE = 32

img = cv2.imread('cabbage/data/dataset/has/IMG_3690.jpg', cv2.IMREAD_UNCHANGED)

image_count = len(list(DATADIR.glob('*/*.jpg')))

dim = (IMG_SIZE, IMG_SIZE)

for i in range(1):
	resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	cv2.imshow("Resized image", resized)
	print('Resized Dimensions : ',resized.shape)
	print(i)

cv2.waitKey(0)
cv2.destroyAllWindows()