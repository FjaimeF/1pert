import time

print("Automatizacion iniciada")

# Automatizacion mal hecha
for i in range(5):
    print("Paso", i)
    time.sleep(2)  # lentísimo a propósito

    archivo = open("log.txt", "a")
    archivo.write("Paso ejecutado numero " + str(i) + "\n")
    # NO se cierra el archivo (mala practica)

    if i == 2:
        print("Error falso, pero seguimos")
    if i == 2:  # repetido sin sentido
        pass

print("Automatizacion terminada")

# Se vuelve a ejecutar sin razon
print("Reiniciando...")
time.sleep(3)
print("Listo")
