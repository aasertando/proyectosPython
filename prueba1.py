num1 = input("Num1: ")
num2 = input("Num2: ")

if num1.isdigit() and num2.isdigit():
    num1 = int (num1)
    num2 = int (num2)

    print(f"La suma es: {num1+num2}")

else:
    if not num1.isdigit() or not num2.isdigit():
        print("no es un numero")
        while True:
            print("ingrese nuevamente")
            num1 = input("Num1: ")
            num2 = input("Num2: ")
            if num1.isdigit() and num2.isdigit():

                num1 = int (num1)
                num2 = int (num2)

                print(f"La suma es: {num1+num2}")
                break