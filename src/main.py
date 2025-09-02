import matplotlib.pyplot as plt
import espaciosColor as ec

ruta = 'data/omero.jpg'

img, r, g, b = ec.leer_imagen(ruta)

print("Tamaño de la imagen:", img.shape)

plt.imshow(img)
plt.show()

gray_image = ec.RGB2GRAY(ruta)
C, M, Y, K = ec.RGB2CMYK(ruta)

plt.imshow(gray_image, cmap="gray", vmin=0, vmax=1)
plt.axis("off")
plt.show()