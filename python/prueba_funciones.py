
from  tkinter import *
import tkinter
import serial

	
def MostrarCapacitancias():
	
	global valorcapacitanciaP
	global valorcapacitanciaN
	global valorcapacitanciaM
	global boton1
	global boton2
	global boton3
	
	arduino= serial.Serial("COM3",9600)
	capacitancia=arduino.readline()
	capacitancia1= float(capacitancia)
	Nanofaradios= (capacitancia1*1000)
	Microfaradios=(Nanofaradios*1000)
	valorcapacitanciaP.set(capacitancia1)
	boton1.config(textvariable=valorcapacitanciaP,bg="LightCyan2")
	valorcapacitanciaN.set(Nanofaradios)
	boton2.config(textvariable=valorcapacitanciaN,bg="LightCyan2")
	valorcapacitanciaM.set(Microfaradios)
	boton3.config(textvariable=valorcapacitanciaM,bg="LightCyan2")
	
	
def NuevaVentana():
	global valorcapacitanciaP
	global valorcapacitanciaN
	global valorcapacitanciaM
	global boton1
	global boton2
	global boton3

	ventana2=Toplevel()
	ventana2.geometry("800x600")
	ventana2.title("capacimetro")  
	ventana2.config(bg="gray25")
	ventana2.iconbitmap("capacitor.ico")
	ventana2.resizable(0,0) 
	label4=Label(ventana2,text="valores en unidades de: ",font=("Daily Challenge DEMO",30),bg="gray86")
	label4.pack(pady=20)
	label1=Label(ventana2,text="Picofaradios: ",font=("Daily Challenge DEMO",40),bg="gray86")
	label1.pack()
	boton1=Button(ventana2, text="",font=("212 Orion Sans",20))
	boton1.pack()
	label2=Label(ventana2,text="Nanofaradios: ",font=("Daily Challenge DEMO",40),bg="gray87")
	label2.pack()
	boton2=Button(ventana2, text="",font=("212 Orion Sans",20))
	boton2.pack()
	label3=Label(ventana2,text="Microfaradios: ",font=("Daily Challenge DEMO",40),bg="gray88")
	label3.pack()
	boton3=Button(ventana2, text="",font=("212 Orion Sans",20))
	boton3.pack()
	boton=Button(ventana2, text="Salir", font=("212 Orion Sans",25),bg="indian red",command=ventana2.destroy)
	boton.place(x=490, y=480)
	boton=Button(ventana2, text="Mostrar valores ", font=("Daily Challenge DEMO",25),bg="indian red",command=MostrarCapacitancias)
	boton.place(x=140, y=480)


ventana=Tk()
ventana.geometry("800x600")
ventana.title("capacimetro")  
ventana.resizable(0,0) 
ventana.config(bg="gray25")
ventana.iconbitmap("capacitor.ico")
img=tkinter.PhotoImage(file="logo.png")
valorcapacitanciaP= DoubleVar()
valorcapacitanciaN= DoubleVar()
valorcapacitanciaM= DoubleVar()
label=Label(ventana, text="CAPACÍMETRO",font=("Daily Challenge DEMO",40)).place(x=300, y=20)
boton=Button(ventana, text="Calcular capacitancias",font=("212 Orion Sans",25),bg="pale turquoise",command=NuevaVentana)
boton.place(x=310,y=300)
label_img=Label(ventana, image=img)
label_img.place(x=10,y=5)
ventana.mainloop()




