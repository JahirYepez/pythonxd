import matplotlib.image as mpimg
import numpy as np

def leer_imagen(ruta_img):
    img = mpimg.imread(ruta_img).astype(float) #Convierte a flotante

    if img.max() > 1.0: #Busca el pixel con el valor más grande, y los normaliza
        img = img / 255.0

    #Toma
    r = img[:,:,0] 
    g = img[:,:,1]
    b = img[:,:,2]

    return img, r, g, b

def RGB2GRAY(ruta_img):
    img = mpimg.imread(ruta_img).astype(float)

    if img.ndim == 3 and img.shape[-1] == 4:
        img = img[..., :3]
    
    if img.max() < 1.0:
        img = img * 255

    gray_image = (0.299*img[:,:,0]) + (0.587*img[:,:,1]) + (0.114*img[:,:,2])
    return gray_image

def RGB2CMYK(ruta_img):
    img = mpimg.imread(ruta_img).astype(float)

    if img.ndim == 3 and img.shape[-1] == 4:
        img = img[..., :3]

    if img.max() > 1.0: #Busca el pixel con el valor más grande, y los normaliza
        img = img / 255.0

    r = img[:,:,0] 
    g = img[:,:,1]
    b = img[:,:,2]

    k = 1.0 - np.max(img, axis=-1)
    
       # Evitar división por cero
    denom = 1 - k
    denom[denom == 0] = 1e-8

    # Calcular C, M, Y
    C = (1 - r - k) / denom
    M = (1 - g - k) / denom
    Y = (1 - b - k) / denom
    
    return C, M, Y, k

def RGB2HSV(ruta_img):
    img = mpimg.imread(ruta_img).astype(float)

    if img.ndim == 3 and img.shape[-1] == 4:
        img = img[..., :3]

    if img.max() > 1.0: #Busca el pixel con el valor más grande, y los normaliza
        img = img / 255.0

    r = img[:,:,0] 
    g = img[:,:,1]
    b = img[:,:,2]

    Cmax = np.max(img, axis=-1)
    Cmin = np.min(img, axis=-1)
    Delta = Cmax - Cmin

    canal = np.argmax(img, axis=-1)

    