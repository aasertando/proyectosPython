#95> honores
#50-95 aprobado 
#<50 erprobó

puntaje: int = int(input("Ingrese su puntaje: "))

if puntaje >= 95:
    print("Honores")
elif puntaje >= 50 and puntaje < 95:
    print("aprobó")
elif puntaje <50:
    print("reprobó")
else:
    print("error")