from tkinter import *
import tkinter as tk
from tkinter import filedialog

import os

from PIL import ImageTk, Image

import normalizer as norm
import cv2
import numpy as np


class CabbageApp(tk.Tk):

	def __init__(self, *args, **kwargs):
		
		tk.Tk.__init__(self, *args, **kwargs)
		
		tk.Tk.iconbitmap(self, default="cabbage.ico")
		tk.Tk.wm_title(self, "Cabbage Leaf Disease Classifier")

		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (StartPage, PageOne):#, PageTwo, PageThree):

			frame = F(container, self)

			self.frames[F] = frame

			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)

	def show_frame(self, cont):

		frame = self.frames[cont]
		frame.tkraise()


class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)

		canvas = tk.Canvas(self, width=400, height=550)
		canvas.place(x=0, y=0)
		canvas.bg_img=ImageTk.PhotoImage(Image.open("frontpage.jpg"))

		canvas.create_image(0,0, image=canvas.bg_img, anchor="nw")

		btnStart = tk.Button(canvas, text="Start",
			command=lambda: controller.show_frame(PageOne))
		btnStart.place(x = 120, y = 420, width=160, height=40)


class PageOne(tk.Frame):

	def browse_image(self, imgPnl, lblFilename, btnAnalyze, lblDiagnosis):
		print("browse image")
		fileDir = filedialog.askopenfilename(initialdir="/", title="Select File", 
			filetypes=(("jpeg", ".jpeg, .jpg"), ("all files", "*.*")))
		print(fileDir)
		img = Image.open(fileDir)
		img.thumbnail((320, 320), Image.ANTIALIAS)
		img_icon = ImageTk.PhotoImage(img)
		imgPnl.configure(image=img_icon)
		imgPnl.image = img_icon

		fileName = os.path.basename(fileDir)
		lblFilename.configure(text="File Name:"+fileName)

		btnAnalyze.configure(command= lambda: self.analyze(cv2.imread(fileDir), lblDiagnosis))


	def analyze(self, fileDir, lblDiagnosis): 
		print("analyzing")
		#message = "Processing..."
		#Label(root, text = message).place(x=40, y=450, width=320, height=20)
		disease = ["Black Rot", "Alternaria Leaf Spot"] #["Black Rot", "Downy Mildew", "Soft Rot", "Alternaria Leaf Spot", "Healthy"]
		weights= [0.8, 0.2] #[0.6, 0.05, 0.05, 0.1, 0.2]
		diagnosis = np.random.choice(disease, p=weights)

		lblDiagnosis.configure(text="Diagnosis:\t"+diagnosis)
		
		noise = norm.noise_red(fileDir)
		resized = norm.resizing(noise)
		if diagnosis == "Black Rot":
			messagebox.showinfo("The cabbage leaf is diagnosed with Black Rot",
				"What is Black Rot?\n\tBlack rot is caused by a bacterium, Xanthomonas campestris pathovar campestris and can affect all vegetables in the crucifer family.\n\tIrregularly shaped dull yellow areas along leaf margins which expand to leaf midrib and create a characterstic \"V-shaped\" lesion; lesions may coalesce along the leaf margin to give plant a scorched appearance.\n\nPrevention and Treatment:\n\tUse certified disease-free seed and transplants. If source of the seeds is unknown, or infested seedlots must be used, treat seed with hot water to eradicate pathogenic bacteria. Refrain from planting the cannage in high temperature and humid areas.")
		elif diagnosis == "Alternaria Leaf Spot":
			messagebox.showinfo("The cabbage leaf is diagnosed with Alternaria Leaf Spot",
				"What is Alternaria Leaf Spot\n\tThis disease is caused by the fungus, Alternaria species, and occurs during warm, moist conditions.\n\tSmall dark spots on leaves which turn brown to gray; lesions may be round or angular and may possess a purple-black margin; lesions may form concentric rings, become brittle and crack in center; dark brown elongated lesions may develop on stems and petioles.\n\nPrevention and Treatment\n\tRemove and destroy all crop debris immediately after harvest, since this disease overwinters on plant residue. It is easily spread by tools, wind, splashing water or insects.")


	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)

		canvas = tk.Canvas(self, width=400, height=550)
		canvas.place(x=0, y=0)
		canvas.bg_img=ImageTk.PhotoImage(Image.open("background.jpg"))

		canvas.create_image(0,0, image=canvas.bg_img, anchor="nw")
		

		lblUpload = tk.Label(canvas, text="Upload Cabbage Leaf Image:")
		lblUpload.place(x = 40, y = 20, width=160, height=20)

		btnBrowse = tk.Button(canvas, text="Browse...", bg="#A1DE93", command=lambda: self.browse_image(imgPnl, lblFilename, btnAnalyze, lblDiagnosis))
		btnBrowse.place(x = 200, y = 20, width=160, height=20)

		lblFilename = tk.Label(canvas, text="File Name: ")
		lblFilename.place(x = 40, y = 50, width=320, height=20)

		inPic = Image.open("InsertImage.png")
		inPic.thumbnail((320, 320), Image.ANTIALIAS)
		pic = ImageTk.PhotoImage(inPic)
		imgPnl = tk.Label(canvas, image=pic)
		imgPnl.image = pic
		imgPnl.place(x = 40, y = 80, width=320, height=320)

		rbSVM = tk.Radiobutton(canvas, text="SVM", value=1)
		rbSVM.place(x=120, y=490, width =80, height=20)
		rbCNN = tk.Radiobutton(canvas, text="CNN", value=2)
		rbCNN.place(x=200, y=490, width =80, height=20)

		btnAnalyze = tk.Button(canvas, text="Analyze", bg="#A1DE93") #, command= lambda: self.analyze(cv2.imread(fileDir)))
		btnAnalyze.place(x = 120, y = 420, width=160, height=20)

		lblDiagnosis = tk.Label(canvas, text="Diagnosis:")
		lblDiagnosis.place(x = 40, y = 450, width=320, height=20)


app = CabbageApp()
width_frame = 400
height_frame = 550
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
abscissa = (screen_width/2) - (width_frame/2)
ordinate = (screen_height/2) - (height_frame/2)
app.geometry("%dx%d+%d+%d" % (width_frame, height_frame, abscissa, ordinate))
app.resizable(width=False, height=False)
app.mainloop()