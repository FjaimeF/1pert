import time
import sys

print("Automatizacion iniciada")


contador = "0"   

for i in range(5):
    print("Paso", i)
    time.sleep(1)

    
    contador = contador + i   

    
    f = open("log.txt", "a")
    f.write("Paso " + str(i) + "\n")
    

    
    if i == 2:
        print("Algo salio mal pero seguimos...")

print("Resultado final:", contador)

print("Automatizacion terminada")
