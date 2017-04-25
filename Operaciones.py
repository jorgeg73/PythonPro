def suma ():
    (x + y)

def resta ():
    (x - y)

print "Programa para multiplicar, Suma, Resta, Division"

print ("Selecciona un numero\n 1. Suma\n 2. Resta\n 3. Multiplicacion\n 4. Division\n")

opcion=0

while (opcion != 5):
    opcion = input()

    if opcion == 1:
        print "Suma"
        x = input("Primer numero: ")
        y = input("Segundo numero: ")
        suma = int(x + y)
        print x, "+", y, "=", suma
        continuar = str(input("Quieres otra operacion si/no: "))
        print continuar

        if continuar == 'si':
            print ("Selecciona un numero\n 1. Suma\n 2. Resta\n 3. Multiplicacion\n 4. Division\n")
            opcion = 0
            continuar = 0
        else:
            opcion = 5

    elif opcion == 2:
        print "Resta"
        x = input("Primer numero: ")
        y = input("Segundo numero: ")
        res = int(x - y)
        print x, "-", y, "=", res

    elif opcion == 3:
        print "Multiplicacion"
        x = input("Primer numero: ")
        y = input("Segundo numero: ")
        mul = int(x * y)
        print x, "*", y, "=", mul

    elif opcion == 4:
        print "Division"
        x = input("Primer numero: ")
        y = input("Segundo numero: ")
        div = int(x / y)
        print x, "/", y, "=", div

    else:
        print "Quieres otra operacion: "
else:
    print "No es opcion valida"