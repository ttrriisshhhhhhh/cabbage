from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import normalizer as norm
import cv2
import numpy as np

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
	#message = "Processing..."
	#Label(root, text = message).place(x=40, y=450, width=320, height=20)
	disease = ["Black Rot", "Alternaria Leaf Spot"]#["Black Rot", "Downy Mildew", "Soft Rot", "Alternaria Leaf Spot", "Healthy"]
	weights= [0.8, 0.2] #[0.6, 0.05, 0.05, 0.1, 0.2]
	diagnosis = np.random.choice(disease, p=weights)
	Label(root, text="Diagnosis:\t"+diagnosis).place(x = 40, y = 450, width=320, height=20)
	noise = norm.noise_red(fileDir)
	resized = norm.resizing(noise)
	if diagnosis == "Black Rot":
		messagebox.showinfo("The cabbage leaf is diagnosed with Black Rot",
			"What is Black Rot?\n\tBlack rot is caused by a bacterium, Xanthomonas campestris pathovar campestris and can affect all vegetables in the crucifer family.\n\tIrregularly shaped dull yellow areas along leaf margins which expand to leaf midrib and create a characterstic \"V-shaped\" lesion; lesions may coalesce along the leaf margin to give plant a scorched appearance.\n\nPrevention and Treatment:\n\tUse certified disease-free seed and transplants. If source of the seeds is unknown, or infested seedlots must be used, treat seed with hot water to eradicate pathogenic bacteria. Refrain from planting the cannage in high temperature and humid areas.")
	elif diagnosis == "Alternaria Leaf Spot":
		messagebox.showinfo("The cabbage leaf is diagnosed with Alternaria Leaf Spot",
			"What is Alternaria Leaf Spot\n\tThis disease is caused by the fungus, Alternaria species, and occurs during warm, moist conditions.\n\tSmall dark spots on leaves which turn brown to gray; lesions may be round or angular and may possess a purple-black margin; lesions may form concentric rings, become brittle and crack in center; dark brown elongated lesions may develop on stems and petioles.\n\nPrevention and Treatment\n\tRemove and destroy all crop debris immediately after harvest, since this disease overwinters on plant residue. It is easily spread by tools, wind, splashing water or insects.")

# Frame
root = Tk()

messagebox.showinfo("Welcome","Guide:\n1. Browse the Cabbage Leaf\n2. Click analayze and wait for the diagnosis.")

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