print "Operaciones con funciones"
print ("Selecciona\n \
       1. Suma\n \
       2. Resta\n \
       3. Multiplicacion\n \
       4. Division\n")
valopc = 0
opcion = input()

while opcion != 5:
    num1 = int(input("primer numero? "))
    num2 = int(input("Segundo Numero?  "))

    if opcion == 1:
        yx = [num1, num2]
        r = sum(yx)
        print num1, "+", num2, "=", r
        opcion = 0

    elif opcion == 2:
        r = num1 - num2
        print num1, "-", num2, "=", r

    elif opcion == 3:
        r = num1 * num2
        print num1, "*", num2, "=", r

    elif opcion == 4:
        r = num1 / num2
        print num1, "/", num2, "=", r

    else:
        opcion = 0
        continuar = input("Quieres otra operacion? ")
        # print (input())
        #    if continuar == "si":
        #opcion = 0
    #else:
print "Adios"