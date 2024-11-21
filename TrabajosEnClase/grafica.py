from tkinter import *

def interfaz () :
    contador=0
    raiz = Tk()
    #print(type(raiz))
    #raiz.title("Login grupo Aprobado")
    #label = Label(text="¡Hola Mundo!")
    #label.pack()
    
    #raiz.resizable(False,False)
    raiz.geometry("300x200")
    #raiz.iconbitmap("icono.ico")
    raiz.config(bg="#fff",relief="sunken")
   
    perrito=Frame()
    miFrame=Frame()
    
    print(type(Frame()))
    
    #perrito.pack()
    miFrame.pack()
    
#    perrito.config(bg="red",widht="200", height="150",relief="sunken" , bd="4")
    miFrame.config(bg="blue", width="300", height="130", relief="sunken" , bd="5")
    
    #Label(perrito, text='Me gusta cagarrrrrrrr').grid(row=0,column=2,padx=10,pady=10)
    Label(miFrame , text="Usuario Alumno:").grid(row=0,column=0 ,padx=10,pady=10)

    Label(miFrame , text="Contraseña:").grid(row=1,column=0 ,padx=10,pady=10)

    cuadro_alumno = Entry(miFrame)
    cuadro_alumno.grid(row=0,column=1, sticky="e" ,padx=10,pady=10)
    cuadro_pass = Entry(miFrame)
    cuadro_pass.config(show="*")
    cuadro_pass.grid(row=1,column=1, sticky="e" ,padx=10,pady=10)
    
    raiz.mainloop()
        

interfaz()
