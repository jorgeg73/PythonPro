import random

#numeros al azar
print "Numeros al Azar"
print random.random()
print "Da el rango:\n"

enum= input ("Primer rango\n")
enum1 = input ("Segundo Rango\n")

print random.randint(enum,enum1)