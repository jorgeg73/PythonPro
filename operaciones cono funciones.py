#import math

print "Operaciones con funciones"
print ("Selecciona\n \
       1. Suma\n \
       2. Resta\n \
       3. Multiplicacion\n \
       4. Division\n")

opcion = input()
num1 = int(input("primer numero? "))
num2 = int(input("Segundo Numero?  "))

if opcion == 1:
    yx = [num1, num2]
    r = sum(yx)
    print num1, "+", num2, "=", r

if opcion == 2:
    r = num1 - num2
    print num1, "-", num2, "=", r

if opcion == 3:
    r = num1 * num2
    print num1, "*", num2, "=", r

if opcion == 4:
    r = num1 / num2
    print num1, "/", num2, "=", r

else:
    print "Adios"
