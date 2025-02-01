#Inicialización del archivo
#Nuevas líneas en el archivo
#Modificación en la rama andres-branch

import pandas as pd
import numpy as np

#Generar numeros aleatorios
mu = 1
sigma = 0.002
n=50
vals = np.random.normal(loc=mu, scale=sigma, size=n)
print(vals)
