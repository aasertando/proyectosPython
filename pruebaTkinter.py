import tkinter as tk

#INICIAR VENTANA
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("500x400")

#INICIO FUNCIONES
def sumar():

    num1 = input1.get()
    num2 = input2.get()

    num1 = int (num1)
    num2 = int (num2)

    resultado = num1 + num2
    print(resultado)

    txt2 = tk.Label(ventana, text = str (resultado))
    txt2.pack()

    return resultado

#FIN FUNCIONES

#INICIO
etiqueta = tk.Label(ventana, text = "Ingrese 2 numeros a sumar")
etiqueta.pack()

input1 = tk.Entry(ventana, width=7)
input1.pack()

txt1 = tk.Label(ventana, text = "+")
txt1.pack()

input2 = tk.Entry(ventana, width=7)
input2.pack()

btn1 = tk.Button(ventana, text = "Click para sumar", padx=10, pady=10, command = sumar,)
btn1.pack()


#lambda:




ventana.mainloop()