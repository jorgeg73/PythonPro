des = True
opcion = 1

print "Operaciones basicas"
print ("Selecciona\n \
       1. Suma\n \
       2. Resta\n \
       3. Multiplicacion\n \
       4. Division\n")
opcion = input()

while opcion <= 4 and des == True:

    num1 = int(input("primer numero? "))
    num2 = int(input("Segundo Numero?  "))

    if opcion == 1:
        yx = [num1, num2]
        r = sum(yx)
        print num1, "+", num2, "=", r
        des = input("Quieres otra operacion si/no? ")
                #if des == "si":
                 #   des = True

    elif opcion == 2:
            r = num1 - num2
            print num1, "-", num2, "=", r
            opcion = 0

    elif opcion == 3:
            r = num1 * num2
            print num1, "*", num2, "=", r
            opcion = 0

    elif opcion == 4:
            r = num1 / num2
            print num1, "/", num2, "=", r
            opcion = 0

else:
    print "Gracias"

