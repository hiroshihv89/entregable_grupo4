import pandas as pd
import numpy as np
#=====================================
#Carga y Procesamiento de Datos
#=====================================

#Cargamos el archivo CSV de datos_ventas.csv en un DF de pandas

print ('Cargamos el archivo CSV de datos_ventas.csv en un DF de pandas')

df = pd.read_csv('datos_ventas.csv')
print(df)

print('=========================')

# Explorar la estructura de los datos (número de filas, columnas, tipos de datos).

print("Número de filas y columnas:", df.shape)

#Tipos de datos de cada columna

print("\nTipos de datos de cada columna:")
print(df.dtypes)

print('=========================')

#Manejo de valores nulos y datos faltantes.

print('Valores nulos por columna')

df = pd.read_csv('datos_ventas.csv')
print(df.isnull().sum())


print('=========================')

#Aplicar operaciones con NumPy para transformar o calcular métricas sobre los datos.


total_venta = df['Total_Venta'].values

print("Suma total de ventas:", np.sum(total_venta))

print("Valor mínimo:", np.min(total_venta))

print("Valor máximo:", np.max(total_venta))

print("Media de ventas:", np.mean(total_venta))

print("Mediana de ventas:", np.median(total_venta))

