import time
import sys

print("Automatizacion iniciada")

# Variables globales innecesarias
contador = "0"   # debería ser int

for i in range(5):
    print("Paso", i)
    time.sleep(1)

    # Error lógico y de tipo
    contador = contador + i   # ❌ string + int

    # Escritura de archivo sin control
    f = open("log.txt", "a")
    f.write("Paso " + str(i) + "\n")
    # ❌ no se cierra el archivo

    # Error intencional en medio
    if i == 2:
        print("Algo salio mal pero seguimos...")

print("Resultado final:", contador)

print("Automatizacion terminada")
