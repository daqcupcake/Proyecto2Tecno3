# -*- coding: utf-8 -*-
"""
Pagina Principal Proyecto 2

Encargada: Daniela Arias

          
Contenido:  El programa contiene la pantalla principal donde se le indica al usuario el proposito
            e instrucciones de la aplicación. 
"""

#IMPORTS
import tkinter as tk
from tkinter.ttk import Combobox
from Pagina_Seleccion import CrearVentSelec



#ESTILO
color1="black"
color2="#4297A0"
fuente=("Helvetica",10)




class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()  #define que esta es la ventana principal
        
        self.geometry("600x400")
        self.title("Probabilidad")
        self.config(bg="#F4EAE6")
        
        
        self.titulo=tk.Label(self,text="Simulador de Suma de probabilidades",bg="#F4EAE6",font=("Helvica",15),fg="#4297A0")
        self.titulo.place(x=140,y=30)
        self.inst=tk.Message(self,text="Bienvenidos al simulador de suma de eventos probabilisticos. \n\nLa aplicación tiene como propósito ayudar a calcular la probabilidad eventos con múltiples combinaciones. En este caso, simularemos un experimento donde se tienen pelotas de varios colores en una canasta y se desea calcular la probabilidad de sacar una pelota de un color o varios colores específicos.",font=fuente,width=510,bg="#F4EAE6",fg=color1)
        self.inst.place(x=50,y=80)
        self.inst2=tk.Label(self,bg="#F4EAE6",text="Para empezar introduzca el número de colores de pelotas con el que desea trabajar",font=fuente,fg=color1)
        self.inst2.place(x=55,y=200)
        
        self.labelCantidad=tk.Label(self,bg="#F4EAE6",text="Cantidad de colores: ",font=fuente,fg=color1)
        self.labelCantidad.place(x=50,y=250)
        self.cantidad=Combobox(self,values=[2,3,4,5,6,7,8,9,10],width=5,font=fuente)
        self.cantidad.current(0)        #Default value es 2
        self.cantidad.place(x=190,y=250)
        self.cantidad.bind("<<ComboboxSelected>>",self.CambiaBoton)
        
        self.empezar=tk.Button(self,bg="#E57F84",text="De click aquí para asignar las cantidad de pelotas de cada color (2 colores)",command=self.mostrarVentanaS,fg=color1)
        self.empezar.place(x=100,y=300)
        
        
        
    def CambiaBoton(self,event):
        selec=self.cantidad.get()
        self.empezar.config(text=f"De click aquí para asignar las cantidad de pelotas de cada color ({selec} colores)")
        
    def mostrarVentanaS(self):
        self.withdraw()
        CrearVentSelec(self,int(self.cantidad.get()))
        
        
if __name__=="__main__":
    app=VentanaPrincipal()
    app.mainloop()