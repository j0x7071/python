
from tkinter import Tk, ttk ,StringVar

ventana = Tk()
ventana.config(width=500,height=300)
ventana.title("MemoTest")
#ventana.iconbitmap("icon.ico")
ventana.minsize(height=200,width=300)
  
var_nombre = StringVar()
nom_jugadores = []
entrada = ttk.Entry(ventana, textvariable=var_nombre)
entrada.grid(column=0,row=0)
    
boton_agregar = ttk.Button(ventana,text="Agregar nuevo jugador",command= lambda :agregar(ventana,var_nombre.get(),nom_jugadores,entrada) )
boton_agregar.grid(column=0)
boton_empezar = ttk.Button(ventana,text="Guardar jugadores",command=lambda: guardar_jugadores (ventana))
boton_empezar.grid(column=0)
jugadores_cargados = ttk.Label(ventana,text="Jugadores Ingresados :",justify='left')
jugadores_cargados.grid(column=0,row=3)
