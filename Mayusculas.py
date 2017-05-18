#import ascii_uppercase
import string

mayusculas = string.ascii_uppercase + "Ñ"
frase =input("Ingrese la frase: ")

mayus = 0

for i in frase:

    if i in mayusculas:
        mayus = mayus + 1

print ('EL número de mayúsculas en la frase es de: {}'.format(mayus))