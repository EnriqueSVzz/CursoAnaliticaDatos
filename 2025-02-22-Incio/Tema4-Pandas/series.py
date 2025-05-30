import pandas as pd
import numpy as np 

# Crear una Serie de pandas
datos = [1, 3, 5, np.nan, 6, 8]
serie = pd.Series(datos, name="Ejemplo")

# Mostrar la Serie
print(serie)