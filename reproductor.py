import os
from tkinter import *
def reproducir():
    os.system(txt.get())
#var="C:\\Users\\chumo\\Music\\eter.mp3"
#reproducir(var)
var=StringVar
vtn=Tk()
vtn.title("Reproductor de musica")
vtn.iconbitmap("logo.ico")
vtn.geometry("350x400")
lbl=Label(vtn,text="Ingresa la direccion del audio")
lbl.grid(row=0,column=0,sticky="e",padx=10,pady=10)
txt=Entry(vtn,textvariable=var)
txt.grid(row=0,column=1,sticky="e",padx=10,pady=10)
btn=Button(vtn,text="Reproducir",command=reproducir)
btn.grid(row=1,column=0,sticky="e",padx=10,pady=10)
vtn.mainloop()
