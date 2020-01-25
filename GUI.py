from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import normalizer
from importlib import reload
import cv2

# Browse Image Button
def browse_image(imgPnl):
	print(5)
	fileDir = filedialog.askopenfilename(initialdir="/", title="Select File", 
		filetypes=(("jpeg", ".jpeg, .jpg"), ("all files", "*.*")))
	print(fileDir)
	img = Image.open(fileDir)
	img.thumbnail((320, 320), Image.ANTIALIAS)
	img_icon = ImageTk.PhotoImage(img)
	imgPnl.configure(image=img_icon)
	imgPnl.image = img_icon

	fileName = os.path.basename(fileDir)
	Label(root, text="File Name: "+fileName).place(x = 40, y = 50, width=320, height=20)
	Button(root, text="Analyze", bg="#A1DE93", command=lambda: analyze(cv2.imread(fileDir))
	).place(x = 120, y = 420, width=160, height=20)
	print(4)
	Radiobutton(root, text="SVM", value=1).place(x=120, y=490, width =80, height=20)
	Radiobutton(root, text="CNN", value=2).place(x=200, y=490, width =80, height=20)

# Analyze Button
def analyze(fileDir): 
	print(6)
	message = "Processing..."
	Label(root, text = message).place(x=40, y=450, width=320, height=20)
	reload(normalizer.edge_detect(normalizer.resizing(normalizer.noise_red(fileDir))))

# Frame
root = Tk()

Label(root, text="Upload Cabbage Leaf Image:").place(x = 40, y = 20, width=160, height=20)
print(1)
Button(root, text="Browse...", bg="#A1DE93", command=lambda: browse_image(imgPnl)
	).place(x = 200, y = 20, width=160, height=20)
print(2)
inPic = Image.open("InsertImage.png")
inPic.thumbnail((320, 320), Image.ANTIALIAS)
pic = ImageTk.PhotoImage(inPic)
imgPnl = Label(root, image=pic)
imgPnl.image = pic
imgPnl.place(x = 40, y = 80, width=320, height=320)
print(3)


# Setting the frame center
width_frame = 400
height_frame = 550
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
abscissa = (screen_width/2) - (width_frame/2)
ordinate = (screen_height/2) - (height_frame/2)
root.geometry("%dx%d+%d+%d" % (width_frame, height_frame, abscissa, ordinate))

root.resizable(width=False, height=False)
root.title("Cabbage Leaf Disease Identifier")
root.mainloop()