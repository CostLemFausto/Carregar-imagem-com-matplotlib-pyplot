import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("/endereço/da/imagem/imagem.extensao")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()