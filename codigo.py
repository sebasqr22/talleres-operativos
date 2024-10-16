import threading
from PIL import Image, ImageFilter

contador = 0

# Definir la clase Imagen
class Imagen:
    def __init__(self, nombre):
        self.nombre = nombre
        self.imagen = Image.open(nombre)

    def aplicar_filtro(self, filtro):
        if filtro == "BLUR":
            return self.imagen.filter(ImageFilter.BLUR)
        elif filtro == "CONTOUR":
            return self.imagen.filter(ImageFilter.CONTOUR)
        else:
            raise ValueError("Filtro no soportado")
        
def imprimirContador():
    global contador
    if contador % 1000 == 0:
        print(contador)

# Función para aplicar el filtro en cada hilo
def aplicar_filtro_en_hilo(objeto):
    try:
        imagen_filtrada = objeto.aplicar_filtro("BLUR")
        global contador
        contador += 1
        imprimirContador()
        # Puedes guardar la imagen si quieres
        # imagen_filtrada.save(f"filtrada_{objeto.nombre}")
    except Exception as e:
        print(f"Error procesando {objeto.nombre}: {e}")

# Crear más de 10000 objetos de la clase Imagen
imagenes = [Imagen(f"foto.png") for i in range(10001)]

# Crear una lista para manejar hilos
hilos = []
for img in imagenes:
    hilo = threading.Thread(target=aplicar_filtro_en_hilo, args=(img,))
    hilos.append(hilo)
    if len(hilos) >= 10:  # Limitar a 10 hilos simultáneamente
        for hilo in hilos:
            hilo.start()   # Iniciar los hilos
        for hilo in hilos:
            hilo.join()    # Esperar a que los hilos terminen
        hilos.clear()       # Limpiar la lista de hilos una vez que han terminado

# Asegurarse de que el último grupo de hilos también se ejecute
for hilo in hilos:
    hilo.start()
for hilo in hilos:
    hilo.join()

# Print cuando todos los hilos hayan terminado
print("Todos los hilos han terminado de procesar las imágenes.")
