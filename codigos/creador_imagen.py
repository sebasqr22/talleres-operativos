from PIL import Image, ImageDraw

# Crear una imagen en blanco (color de fondo blanco)
ancho, alto = 400, 400
imagen = Image.new('RGB', (ancho, alto), color='white')

# Dibujar un rectángulo
dibujar = ImageDraw.Draw(imagen)
dibujar.rectangle([50, 50, 350, 350], outline="black", fill="blue")

# Guardar la imagen
imagen.save('imagen_creada.png')