print "Calculo de perimetro y  area de un circulo"
print "Presiona 1 para Perimetro"
print "Presiona 2 para Area"

deci = int(input())

if deci == 1 or 2:

    print "El radio del circulo: "
    radi = int(input())

elif deci == 1:
    resP = (2 * 3.14) * radi
    print (resP)
    print

elif deci == 2:
    resA = 3.14 * (radi * radi)
    print (resA)
    print
else:
    print "Seleccion no valida"
