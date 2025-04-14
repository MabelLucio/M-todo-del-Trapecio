### Alexa Mabel Lucio Mendoza

# Importar librerías
from numpy import zeros
import matplotlib.pyplot as plt
import pandas as pd 
import tkinter as tk

## Función que comprueba si se ingresa un valor no válido 
def comprobarres():
    try:
        funcion = funcioni.get()
        a = float(lima.get())
        b = float(limb.get())
        n  = int(inn.get())
    except:
        tk.messagebox.showerror(message="Ingresaste un valor no válido. Intenta de nuevo.", title="Error")        
    if n <= 0:
        tk.messagebox.showwarning(message="Ingresaste un numero de divisiones no válido. Intenta de nuevo.", title="Error")
    # Método del trapecio
    dx = (b-a)/n
    tabla = zeros(shape=(n+1,2))
    suma = 0
    for i in range(n+1):
        x = a + i*(dx)
        tabla[i][0] = x        
        try:
            fv = eval(funcion) 
        except:
            tk.messagebox.showerror(message="La función no está definida en ese intervalo. Intenta con otros limites.", title="Error")        
        fs = fv        
        tabla[i][1] = fs
        if i == 0 or i == n:
            fv = fv
        else:
            fv = 2*fv                          
        fs = 0
        suma = fv+suma
    ddx = dx/2
    integra = ddx*(suma)        
    nombres = ["x_i", "f(x)"]
    df = pd.DataFrame(tabla, columns=nombres)    
    
    # Diseño de la gráfica
    plt.fill_between(df["x_i"], 0, df["f(x)"], color = "gold", label = "área del trapecio") 
    plt.plot(df["x_i"], df["f(x)"], marker="o", color="r", label = "función aproximada")   
    plt.title(funcion)     
    plt.plot(df["x_i"], df["f(x)"],color="r")       
    plt.grid()
    plt.show
    print(f"\n Tabla:\n{df}")
    print(f"\nEl resultado de la integracion es : {integra}")
    

# Interfaz
ventana = tk.Tk()
ventana.geometry("370x280")
ventana.title("Metodo del trapecio")
mensaje = tk.Label(ventana, text = "Ingresa la función:",)
mensaje.pack()
funcioni =  tk.Entry(ventana, font = "arial 10")
funcioni.pack()
mensajea = tk.Label(ventana, text = "Ingresa el limite izquierdo:").place(x=20, y=50)
lima =  tk.Entry(ventana, font = "arial 10")
lima.place(x=170, y=50, width=40)
mensajeb = tk.Label(ventana, text = "Ingresa el limite derecho:").place(x=20, y=80)
limb =  tk.Entry(ventana, font = "arial 10")
limb.place(x=170, y=80, width=40)
mensajen = tk.Label(ventana, text = "Ingresa el numero de divisiones:").place(x=20, y=110)
inn =  tk.Entry(ventana, font = "arial 10")
inn.place(x=200, y=110, width=40)
boton = tk.Button(ventana, text="Aceptar", command = comprobarres).place(x=150,y=150)
ventana.mainloop()



