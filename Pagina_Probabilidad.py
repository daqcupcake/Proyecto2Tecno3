# -*- coding: utf-8 -*-
"""
Pagina Probabilidad Proyecto 2

Encargada: Daniela Arias

          
Contenido:  
    
"""
#IMPORTS
import tkinter as tk

#ESTILO
color1="black"
color2="blue"
fuente=("Helvetica",10)

#GLOBALES
bolitas=[]
lugaresX=[70,70,70,70,70,320,320,320,320,320]
lugaresY=[100,150,200,250,300,100,150,200,250,300]
checks=[0,0,0,0,0,0,0,0,0,0]
totalbolitas=0

def CrearVentProb(datosSelec,ventana):
    
    ventana.withdraw()
    global bolitas, totalbolitas
    bolitas=datosSelec
    

    #FUNCIONES
    def CalcProb():
        global bolitas,checks,totalbolitas
        cantcolores=len(bolitas)
        
        #print(totalbolitas)
        cantcoloresSelec=0
        for i in range(cantcolores):
            if checks[i].get()==1:
                cantcoloresSelec+=1
        
        texto="La probabilidad de sacar una bolita de color "
        probabilidad=0
        
        if cantcoloresSelec!=1:
            while cantcoloresSelec>0:
                
                i=0
                if cantcoloresSelec > 1:
                    for j in range(len(bolitas)):
                        
                        if checks[j].get()==1:
                            i+=1
                        
                        if i==cantcoloresSelec:
                            texto=texto+bolitas[j][0]
                            probabilidad+=bolitas[j][1]
                            break
                    
                    
                    
                    if cantcoloresSelec > 2:
                        texto=texto+","
                
                    texto=texto+" "
                    
                else:
                    for j in range(len(bolitas)):
                        if checks[j].get()==1:
                            i+=1
                        
                        if i==cantcoloresSelec:
                            texto=texto+"o "+bolitas[j][0]
                            probabilidad+=bolitas[j][1]
                            break
                cantcoloresSelec=cantcoloresSelec-1
                
        else:
            for j in range(len(bolitas)):
                if checks[j].get()==1:
                    i+=1
                
                if i==cantcoloresSelec:
                    texto=texto+bolitas[j][0]
                    probabilidad+=bolitas[j][1]
                    break
            
        probabilidad=probabilidad/totalbolitas
        texto+= f" es de: {probabilidad:.2f}"
        lblProb.config(text=texto)
            
    def nosequehaceaun():
        
        return(0)
    
    #ventanaP = tk.Tk()
    ventanaP=tk.Toplevel()
    
    ventanaP.geometry("600x450")
    ventanaP.title("Cálculo de Probabilidades")
    ventanaP.config(bg="#F4EAE6")
    
    ventanaP.inst=tk.Message(ventanaP,bg="#F4EAE6",text="Seleccione el color y cantidad de cada tipo de pelota, luego presione el botón continuar",font=fuente,width=700,fg=color1)
    ventanaP.inst.place(x=50,y=30)
    
    
    checks[0]=tk.IntVar()
    checks[1]=tk.IntVar()
    checks[2]=tk.IntVar()
    checks[3]=tk.IntVar()
    checks[4]=tk.IntVar()
    checks[5]=tk.IntVar()
    checks[6]=tk.IntVar()
    checks[7]=tk.IntVar()
    checks[8]=tk.IntVar()
    checks[9]=tk.IntVar()
    
    cb0= tk.Checkbutton(ventanaP,bg="#F4EAE6",text="CB0",variable=checks[0],onvalue=1, offvalue=0,command=nosequehaceaun(),font=fuente)
    cb1= tk.Checkbutton(ventanaP,bg="#F4EAE6",text="CB1",variable=checks[1],onvalue=1, offvalue=0,command=nosequehaceaun(),font=fuente)
    cb2= tk.Checkbutton(ventanaP,bg="#F4EAE6",text="CB2",variable=checks[2],onvalue=1, offvalue=0,command=nosequehaceaun(),font=fuente)
    cb3= tk.Checkbutton(ventanaP,bg="#F4EAE6",text="CB3",variable=checks[3],onvalue=1, offvalue=0,command=nosequehaceaun(),font=fuente)
    cb4= tk.Checkbutton(ventanaP,bg="#F4EAE6",text="CB4",variable=checks[4],onvalue=1, offvalue=0,command=nosequehaceaun(),font=fuente)
    cb5= tk.Checkbutton(ventanaP,bg="#F4EAE6",text="CB5",variable=checks[5],onvalue=1, offvalue=0,command=nosequehaceaun(),font=fuente)
    cb6= tk.Checkbutton(ventanaP,bg="#F4EAE6",text="CB6",variable=checks[6],onvalue=1, offvalue=0,command=nosequehaceaun(),font=fuente)
    cb7= tk.Checkbutton(ventanaP,bg="#F4EAE6",text="CB7",variable=checks[7],onvalue=1, offvalue=0,command=nosequehaceaun(),font=fuente)
    cb8= tk.Checkbutton(ventanaP,bg="#F4EAE6",text="CB8",variable=checks[8],onvalue=1, offvalue=0,command=nosequehaceaun(),font=fuente)
    cb9= tk.Checkbutton(ventanaP,bg="#F4EAE6",text="CB9",variable=checks[9],onvalue=1, offvalue=0,command=nosequehaceaun(),font=fuente)
    
    checkButtons=[cb0,cb1,cb2,cb3,cb4,cb5,cb6,cb7,cb8,cb9]
    
    for i in range(len(bolitas)):
        
        if bolitas[i][1]==1:
            checkButtons[i].config(text=f"Bolita Color {bolitas[i][0]} ({bolitas[i][1]})")
        else:
            checkButtons[i].config(text=f"Bolitas Color {bolitas[i][0]} ({bolitas[i][1]})")
            
        checkButtons[i].place(x=lugaresX[i], y=lugaresY[i])
        totalbolitas+=bolitas[i][1]
    
    
    btnCalc=tk.Button(ventanaP,text="Calcular Probabilidad",command=CalcProb,font=fuente,bg="#E57F84")
    btnCalc.place(x=220,y=350)
    
    lblProb=tk.Label(ventanaP,bg="#F4EAE6",text="",font=fuente)
    lblProb.place(x=50,y=400)
    
    
    ventanaP.protocol("WM_DELETE_WINDOW",lambda: volverVentP(ventanaP, ventana))
    
    def volverVentP(ventanaActual,ventanaDestino): 
        ventanaActual.withdraw()
        ventanaDestino.deiconify()
    #ventanaP.mainloop()