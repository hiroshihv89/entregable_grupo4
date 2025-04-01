
import pandas as pd 

# Cargar los datos desde un archivo CSV
df = pd.read_csv('datos_ventas.csv')

# Convertir la columna de fecha a formato datetime
df['Fecha'] = pd.to_datetime(df['Fecha'])

# Análisis descriptivo
descriptive_stats = df.describe()
print("Estadísticas descriptivas:")
print(descriptive_stats)

# Matriz de correlación
correlation_matrix = df[['Cantidad', 'Total_Venta']].corr()
print("\nMatriz de correlación:")
print(correlation_matrix)

# Identificación de patrones: ventas por producto
ventas_por_producto = df.groupby('Producto').agg({'Cantidad': 'sum', 'Total_Venta': 'sum'}).reset_index()
print("\nVentas por producto:")
print(ventas_por_producto)

# Segmentación por mes especificos
df['Mes'] = df['Fecha'].dt.month
ventas_por_mes = df.groupby('Mes').agg({'Cantidad': 'sum', 'Total_Venta': 'sum'}).reset_index()
print("\nVentas por mes:")
print(ventas_por_mes)

# Filtrar ventas mayores a un umbral especifico
umbral = 1000
ventas_altas = df[df['Total_Venta'] > umbral]
print("\nVentas mayores a $1000:")
print(ventas_altas)

