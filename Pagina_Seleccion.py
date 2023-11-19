# -*- coding: utf-8 -*-
"""
Pagina Selección Proyecto 2

Encargada: Daniela Arias

          
Contenido:  
    
"""
#IMPORTS
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import ttk
from Pagina_Probabilidad import CrearVentProb

#ESTILO
color1="black"
color2="blue"
fuente=("Helvetica",10)

#GLOBALES
colores=["Rojo","Amarillo","Verde","Azul","Negro","Blanco","Naranja","Morado","Café","Rosado"]
coloresEnUso=[0,0,0,0,0,0,0,0,0,0]
lugaresX=[50,50,50,50,50,400,400,400,400,400]
lugaresY=[100,150,200,250,300,100,150,200,250,300]
cant=2


def CrearVentSelec(ventP,num):
    global cant
    cant=num
    
    #FUNCIONES
    def ActListaCol(event,combo,numCombo):
        global coloresEnUso, colores
        
        colorSelec=combo.get()
        if coloresEnUso[numCombo]!=0:
             
            colores.append(coloresEnUso[numCombo])
            coloresEnUso[numCombo]=colorSelec
            colores.remove(colorSelec)
            
        else:
            coloresEnUso[numCombo]=colorSelec
            colores.remove(colorSelec)
            
        for i in listaC:
            if i!=combo:
                i["values"]=sorted(colores)   
                
    def botoncini():
        
        v=0
        for i in listaC:
            if i.index("end") == 0:
                #print("ta vacio")
                break
            else: 
                v+=1
                
        for i in listaS:
            if i.index("end")==0:
                #print("ta vacio un num")
                break
            else:
                v+=1
        print(v)
        if v==cant*2:
            #print("cambie de ventana")
            datos=[]
            for i in range(cant):
                
                datos.append([listaC[i].get(),int(listaS[i].get())])
            
            print(datos)
            CrearVentProb(datos,ventanaS)
            #ventanaS.btnCont.config(state="disabled")
        
       
    
        
        
    #ventanaS = tk.Tk()
    ventanaS=tk.Toplevel(ventP)
    
    ventanaS.geometry("770x400")
    ventanaS.title("Selección color y cantidad")
    ventanaS.config(bg="#F4EAE6")
    
    ventanaS.inst=tk.Message(ventanaS,bg="#F4EAE6",text="Seleccione el color de cada pelota y su cantidad correspondiente. Cuando haya completado todas las selecciones de click en el botón Continuar",font=fuente,width=690,fg=color1)
    ventanaS.inst.place(x=50,y=30)
    
    ventanaS.l0=tk.Label(ventanaS,bg="#F4EAE6",text="Pelota 1:",fg=color1,font=fuente)
    ventanaS.l1=tk.Label(ventanaS,bg="#F4EAE6",text="Pelota 2:",fg=color1,font=fuente)
    ventanaS.l2=tk.Label(ventanaS,bg="#F4EAE6",text="Pelota 3:",fg=color1,font=fuente)
    ventanaS.l3=tk.Label(ventanaS,bg="#F4EAE6",text="Pelota 4:",fg=color1,font=fuente)
    ventanaS.l4=tk.Label(ventanaS,bg="#F4EAE6",text="Pelota 5:",fg=color1,font=fuente)
    ventanaS.l5=tk.Label(ventanaS,bg="#F4EAE6",text="Pelota 6:",fg=color1,font=fuente)
    ventanaS.l6=tk.Label(ventanaS,bg="#F4EAE6",text="Pelota 7:",fg=color1,font=fuente)
    ventanaS.l7=tk.Label(ventanaS,bg="#F4EAE6",text="Pelota 8:",fg=color1,font=fuente)
    ventanaS.l8=tk.Label(ventanaS,bg="#F4EAE6",text="Pelota 9:",fg=color1,font=fuente)
    ventanaS.l9=tk.Label(ventanaS,bg="#F4EAE6",text="Pelota 10:",fg=color1,font=fuente)
    
    
    ventanaS.c0=Combobox(ventanaS,values=sorted(colores),width=20,font=fuente,state="readonly")
    ventanaS.c1=Combobox(ventanaS,values=sorted(colores),width=20,font=fuente,state="readonly")
    ventanaS.c2=Combobox(ventanaS,values=sorted(colores),width=20,font=fuente,state="readonly")
    ventanaS.c3=Combobox(ventanaS,values=sorted(colores),width=20,font=fuente,state="readonly")
    ventanaS.c4=Combobox(ventanaS,values=sorted(colores),width=20,font=fuente,state="readonly")
    ventanaS.c5=Combobox(ventanaS,values=sorted(colores),width=20,font=fuente,state="readonly")
    ventanaS.c6=Combobox(ventanaS,values=sorted(colores),width=20,font=fuente,state="readonly")
    ventanaS.c7=Combobox(ventanaS,values=sorted(colores),width=20,font=fuente,state="readonly")
    ventanaS.c8=Combobox(ventanaS,values=sorted(colores),width=20,font=fuente,state="readonly")
    ventanaS.c9=Combobox(ventanaS,values=sorted(colores),width=20,font=fuente,state="readonly")
    
    
    
    ventanaS.s1 = ttk.Spinbox(ventanaS,from_=1, to=9999, state="readonly",font=fuente)
    ventanaS.s2 = ttk.Spinbox(ventanaS,from_=1, to=9999, state="readonly",font=fuente)
    ventanaS.s3 = ttk.Spinbox(ventanaS,from_=1, to=9999, state="readonly",font=fuente)
    ventanaS.s4 = ttk.Spinbox(ventanaS,from_=1, to=9999, state="readonly",font=fuente)
    ventanaS.s5 = ttk.Spinbox(ventanaS,from_=1, to=9999, state="readonly",font=fuente)
    ventanaS.s6 = ttk.Spinbox(ventanaS,from_=1, to=9999, state="readonly",font=fuente)
    ventanaS.s7 = ttk.Spinbox(ventanaS,from_=1, to=9999, state="readonly",font=fuente)
    ventanaS.s8 = ttk.Spinbox(ventanaS,from_=1, to=9999, state="readonly",font=fuente)
    ventanaS.s9 = ttk.Spinbox(ventanaS,from_=1, to=9999, state="readonly",font=fuente)
    ventanaS.s0 = ttk.Spinbox(ventanaS,from_=1, to=9999, state="readonly",font=fuente)
    
    
    
    
    
    listaL=[ventanaS.l0,ventanaS.l1,ventanaS.l2,ventanaS.l3,ventanaS.l4,ventanaS.l5,ventanaS.l6,ventanaS.l7,ventanaS.l8,ventanaS.l9]
    listaC=[ventanaS.c0,ventanaS.c1,ventanaS.c2,ventanaS.c3,ventanaS.c4,ventanaS.c5,ventanaS.c6,ventanaS.c7,ventanaS.c8,ventanaS.c9]
    listaS=[ventanaS.s0,ventanaS.s1,ventanaS.s2,ventanaS.s3,ventanaS.s4,ventanaS.s5,ventanaS.s6,ventanaS.s7,ventanaS.s8,ventanaS.s9]
    
    for i in range(cant):
        listaL[i].place(x=lugaresX[i],y=lugaresY[i])
        listaC[i].place(x=lugaresX[i]+70,y=lugaresY[i])
        listaS[i].place(x=lugaresX[i]+250, y=lugaresY[i], width=70)
        
        
        listaC[i].bind("<<ComboboxSelected>>",lambda event,combo=listaC[i], x=i:  ActListaCol(event,combo,x))
        
    ventanaS.btnCont=tk.Button(ventanaS,bg="#E57F84",font=fuente,command=botoncini,width=30,text="Continuar")
    ventanaS.btnCont.place(x=260,y=350)
    
    
    #ventanaS.mainloop()

    
    ventanaS.protocol("WM_DELETE_WINDOW",lambda: volverVentP(ventanaS, ventP))
    #root.mainloop()
    
    def volverVentP(ventanaActual,ventanaDestino): 
        ventanaActual.withdraw()
        ventanaDestino.deiconify()

