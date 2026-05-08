temperatura = input("Ingrese temperatura: ")

if temperatura.isdigit():
    temperatura = float(temperatura)
else:
    print("Debe ingresar un numero")
    while True:
            temperatura = input("Ingrese temperatura: ")
            if temperatura.isdigit():
                 temperatura = float (temperatura)





            if eleccion == "c" or eleccion == "C":
                temperaturaCambiada = (temperatura*1.8)+32
                print(f"En farenheit es: {temperaturaCambiada}")

            elif eleccion == "F" or eleccion == "f":
                temperaturaCambiada = (temperatura-32)/1.8
                print(f"En celcius es: {temperaturaCambiada}")
            else:
                 print("Debe ingresar C/F")
            break


eleccion: str = input("la temperatura es celcius o farenheit? c/f")
