num1 = float (input("Ingrese numero 1: "))
num2 = float (input("ingrese numero 2: "))

operacion = str(input("ingrese operacion |suma|resta|mult|div|: "))

if operacion == "suma":
    print(f"La suma es: {num1 + num2}")
elif operacion == "resta":
    print(f"La resta es: {num1 - num2}")
elif operacion == "mult":
    print(f"La multiplicación es: {num1 * num2}")
elif operacion == "div":
    print(f"La división es: {num1 / num2}")
else:
    print("Error, no ha ingresado una operación válida")
