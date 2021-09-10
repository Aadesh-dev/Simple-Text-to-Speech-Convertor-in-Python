from tkinter import *
import pyttsx3
import PyPDF2
import pytesseract
from gtts import gTTS 
from docx import Document
engine = pyttsx3.init()
engine.setProperty('rate',150)
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import os
import keyboard
import multiprocessing  
root=Tk()
root.title('Text to Speech Convertor')
root.configure(background='light blue')
photo= ImageTk.PhotoImage(Image.open(".\\Elegant_Background-14.jpg")) 
l=Label(root,image=photo)
l.image=photo       
l.pack(fill="both",expand="yes")
lab1=Label(root,text='Text To Speech Convertor',fg='black',bg='light blue',font=('arial 25 bold italic')).place(x=570,y=0)


label =Label(root,text='Enter Text Here',font=('arial 16 bold'),bg='light blue').place(x=310,y=70)

text1=Text(root,height=15,width=100,font=('arial 13'))
text1.place(x=310,y=100)



def setvolume(root):
	sound=V.get()
	if sound==1:
		engine.setProperty('volume',0.1)
		
	if sound==2:
		engine.setProperty('volume',0.2)
		
	if sound==3:
		engine.setProperty('volume',0.3)
		
	if sound==4:
		engine.setProperty('volume',0.4)
		
	if sound==5:
		engine.setProperty('volume',0.5)
		
	if sound==6:
		engine.setProperty('volume',0.6)
		
	if sound==7:
		engine.setProperty('volume',0.7)
		
	if sound==8:
		engine.setProperty('volume',0.8)
		
	if sound==9:
		engine.setProperty('volume',0.9)
		
	if sound==10:
		engine.setProperty('volume',1.0)
def setrate(root):
	speed=R.get()
	if speed==1:
		engine.setProperty('rate',50)
	if speed==2:
		engine.setProperty('rate',100)
	if speed==3:
		engine.setProperty('rate',150)
	if speed==4:
		engine.setProperty('rate',200)
	if speed==5:
		engine.setProperty('rate',250)


def UploadAction():
	root.fileName=filedialog.askopenfilename()
	print(root.fileName)
	A=Button(root,text='Convert',width=20,bg='brown',fg='white',command=select1).place(x=890,y=400)
	A1=Button(root,text='Convert and Save',width=20,bg='brown',fg='white',command=select2).place(x=1080,y=400)
def UploadAction1():
	root.fileName=filedialog.askopenfilename()
	C=Button(root,text='Convert',width=15,bg='brown',fg='white',command=select1).place(x=610,y=600)
	C1=Button(root,text='Convert and Save',width=15,bg='brown',fg='white',command=select2).place(x=800,y=600)	
	
def direct1():
	input=text1.get("1.0",'end-1c')
	mytext=input
	engine.say(mytext)
	engine.runAndWait()
def direct2():
	input=text1.get("1.0",'end-1c')
	mytext=input
	language ='en'
	myobj=gTTS(text=mytext,lang=language,slow=False) 
	myobj.save("welcome1.mp3") 
	os.system("welcome1.mp3")	
def select1():
	global flag
	flag = True
	if ".pdf" in root.fileName:
		#stop=Button(root, text='Stop current playback',width=13,bg='brown',fg='white', command=stopplayback).place(x=720,y=700)
		pdfFileObj = open(root.fileName, 'rb') 
		pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
		num_pages=10
		for i in range(0, num_pages):
			root.update()
			pageObj = pdfReader.getPage(i)
			input1=pageObj.extractText()
			mytext1=input1
			engine.say(mytext1)
			engine.runAndWait()
	if ".txt" in root.fileName:
		f=open(root.fileName)
		input1=f.read()
		mytext1=input1
		engine.say(mytext1)
		engine.runAndWait()
	if ".png" in root.fileName:
		file = Image.open(root.fileName)
		pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
		str = pytesseract.image_to_string(file, lang='eng')
		engine.say(str)
		engine.runAndWait()
	if ".jpg" in root.fileName:
		file = Image.open(root.fileName)
		pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
		str = pytesseract.image_to_string(file, lang='eng')
		engine.say(str)
		engine.runAndWait()
		
		
		
def select2():
	if ".pdf" in root.fileName:
		pdfFileObj = open(root.fileName, 'rb') 
		pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
		mytext1 = "" 
		for pageNum in range(pdfReader.numPages):
			pageObj = pdfReader.getPage(pageNum)
			mytext1+=pageObj.extractText()
		pdfFileObj.close()
		language ='en'
		myobj=gTTS(text=mytext1,lang=language,slow=False) 
		myobj.save("welcome2.mp3") 
		os.system("welcome2.mp3")	
	if ".txt" in root.fileName:
		f=open(root.fileName)
		input1=f.read()
		mytext1=input1
		language ='en'
		myobj=gTTS(text=mytext1,lang=language,slow=False) 
		myobj.save("welcome3.mp3") 
		os.system("welcome3.mp3")
	if ".png" in root.fileName:
		file = Image.open(root.fileName)
		pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
		str = pytesseract.image_to_string(file, lang='eng')
		mytext1=str
		language ='en'
		myobj=gTTS(text=mytext1,lang=language,slow=False) 
		myobj.save("welcome3.mp3") 
		os.system("welcome3.mp3")
	if ".jpg" in root.fileName:
		file = Image.open(root.fileName)
		pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
		str = pytesseract.image_to_string(file, lang='eng')
		mytext1=str
		language ='en'
		myobj=gTTS(text=mytext1,lang=language,slow=False) 
		myobj.save("welcome3.mp3") 
		os.system("welcome3.mp3")
		
		
		
	
	
	
B=Button(root,text ="Submit",width=20,bg='brown',fg='white',command=direct1)
B.place(x=320,y=400)
B1=Button(root,text ="Submit and Save",width=20,bg='brown',fg='white',command=direct2)
B1.place(x=510,y=400)

U=Button(root, text='Select',width=20,bg='brown',fg='white', command=UploadAction).place(x=700,y=400)
lab3=Label(root,text="Select the volume:",font=('arial 16 bold'),fg='black',bg='light blue').place(x=160,y=500)
lab4=Label(root,text="Select the playback speed:",font=('arial 16 bold'),fg='black',bg='light blue').place(x=1160,y=500)
V= Scale(root,from_ = 1,to = 10,fg='white',bg='brown',length=250,orient = HORIZONTAL ,resolution = 1,command=setvolume)
V.place(x=160,y=550)
R=Scale(root,from_ = 1,to = 5,fg='white',bg='brown',length=250,orient = HORIZONTAL ,resolution = 1,command=setrate)
R.place(x=1160,y=550)
lab5=Label(root,text="Select the image to convert:",font=('arial 16 bold'),fg='black',bg='light blue').place(x=630,y=500)
Z=Button(root, text='Select',width=13,bg='brown',fg='white', command=UploadAction1).place(x=720,y=550)



root.geometry("2000x6000")
root.mainloop()