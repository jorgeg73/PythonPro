def num1():
    num12 = int(input("primer numero? "))
def num2():
    num22 = int(input("Segundo numero? "))

print "Operaciones con funciones"
print ("Selecciona\n \
       1. Suma\n \
       2. Resta\n \
       3. Multiplicacion\n \
       4. Division\n")

opcion = input()

while opcion >= 1 and opcion <= 4:
    num1 = int(input("primer numero? "))
    num2 = int(input("Segundo Numero?  "))

    if opcion == 1:
       # num1()
       # num2()
        yx = [num1, num2]
        r = sum(yx)
        print num1, "+", num2, "=", r
        opcion = 0

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

    elif opcion == 0:
        continuar = input("Quieres otra operacion si/no? ")
        # print (input())
        #    if continuar == "si":
        #opcion = 0
else:
    print "Adios"