def suma():
    num1 = int(input("primer numero? "))
    num2 = int(input("Segundo Numero?  "))
    r = sum(yx)
    print num1, "+", num2, "=", r

def Resta():
    num1 = int(input("primer numero? "))
    num2 = int(input("Segundo Numero?  "))
    r = num1 - num2
    print num1, "-", num2, "=", r

def multiplicacion():
    num1 = int(input("primer numero? "))
    num2 = int(input("Segundo Numero?  "))
    r = num1 * num2
    print num1, "*", num2, "=", r

def Division():
    num1 = int(input("primer numero? "))
    num2 = int(input("Segundo Numero?  "))
    r = num1 / num2
    print num1, "/", num2, "=", r

x = 0
go = "si"

print "Operaciones basicas"

menu = [suma, Resta, multiplicacion, Division]

while x < len(menu):
    print menu[x].__name__, ", presiona ", "[" + str(x) + "]"
    x += 1

while go != "n":
    c = input("Selecciona opcion: ")
    menu[c]()
    num1 = 0
    num2 = 0
    go = raw_input("Otra Operacion? [si/n]: ")