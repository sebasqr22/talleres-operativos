import matplotlib.pyplot as plt

def leer(ruta):
    with open(ruta, 'r') as file:  # 'r' indica que se abre en modo lectura
        contenido = file.read()
        contenido = contenido.split("\n")
        return contenido

def procesar(data):
    swappiness = []
    tiempos = []

    for i in data:
        contenido = i.split(" ")
        swappiness.append(int(contenido[0]))

        min = float(contenido[1].split("m")[0]) * 60
        seg = float(contenido[1].split("m")[1].replace("s", ""))
        print(f"seg: {seg}")
        tiempos.append(min + seg)
    
    return swappiness, tiempos

def graficar(ruta):
    data = leer(ruta)
    swappiness, tiempos = procesar(data)

    plt.plot(swappiness, tiempos)
    plt.xlabel("Swappiness")
    plt.ylabel("Tiempo (s)")
    plt.title("Swappiness vs Tiempo en Segundos")
    plt.grid(True)
    plt.show()

graficar('./p1.txt')
graficar('./p2.txt')