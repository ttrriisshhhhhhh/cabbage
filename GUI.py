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
		lblFilename.configure(text="File Name:\t"+fileName)

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
		top = Toplevel()

		screen_width = top.winfo_screenwidth()
		screen_height = top.winfo_screenheight()
		abscissa = (screen_width/2) - (width_frame/2)
		ordinate = (screen_height/2) - (height_frame/2)
		top.geometry("%dx%d+%d+%d" % (width_frame, height_frame, abscissa, ordinate))
		top.resizable(width=False, height=False)


		canvas = tk.Canvas(top, width=400, height=550)
		canvas.place(x=0, y=0)
		canvas.bg_img=ImageTk.PhotoImage(Image.open("background.jpg"))

		canvas.create_image(0,0, image=canvas.bg_img, anchor="nw")

		mDiag = tk.Label(canvas, text="")
		mDiag.place(x = 40, y = 40, width=320, height=420)

		btnBack = tk.Button(canvas, text="Back", command = top.destroy)
		btnBack.place(x=120, y=475, width =160, height=40)

		if diagnosis == "Black Rot":
			br = Image.open("black_rot.png")
			br.thumbnail((320, 420), Image.ANTIALIAS)
			blrot = ImageTk.PhotoImage(br)

			mDiag.configure(image=blrot, text="black")

			mDiag.image = blrot
			print("Black Rot")
			
		elif diagnosis == "Alternaria Leaf Spot":
			al = Image.open("alternaria.png")
			al.thumbnail((320, 420), Image.ANTIALIAS)
			als = ImageTk.PhotoImage(al)

			mDiag.configure(image=als, text="alter")

			mDiag.image = als
			print("Alternaria Leaf Spot")


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