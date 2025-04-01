import pandas as pd
import matplotlib.pyplot as plt

# Carga el archivo csv
df = pd.read_csv("datos_ventas.csv")

# Convertir la columna Fecha a formato datetime
df["Fecha"] = pd.to_datetime(df["Fecha"])

# ------------------ GRÁFICO DE LÍNEAS ------------------
# Agrupa las ventas por mes
df["Mes"] = df["Fecha"].dt.to_period("M")
ventas_mensuales = df.groupby("Mes")["Total_Venta"].sum()

plt.figure(figsize=(10, 5))
plt.plot(ventas_mensuales.index.astype(str), ventas_mensuales, marker='o', linestyle='-')
plt.xlabel("Mes")
plt.ylabel("Total Venta")
plt.title("Evolución de Ventas Mensuales")
plt.xticks(rotation=45)
plt.grid()
plt.show()

# ------------------ GRÁFICO DE BARRAS ------------------
# Muestra los 5 productos más vendidos
top_productos = df.groupby("Producto")["Total_Venta"].sum().nlargest(5)

plt.figure(figsize=(8, 5))
plt.bar(top_productos.index, top_productos.values)
plt.xlabel("Producto")
plt.ylabel("Total Venta")
plt.title("Top 5 Productos más Vendidos")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# ------------------ GRÁFICO DE TORTA ------------------
# Agrupa productos pequeños en "Otros"
ventas_por_producto = df.groupby("Producto")["Total_Venta"].sum()
top_productos = ventas_por_producto.nlargest(5)  # Top 5
otros = ventas_por_producto[~ventas_por_producto.index.isin(top_productos.index)].sum()  # Resto

# Crear un nuevo DataFrame con "Otros"
ventas_final = pd.concat([top_productos, pd.Series(otros, index=["Otros"])])

plt.figure(figsize=(8, 8))
plt.pie(ventas_final, labels=ventas_final.index, autopct="%1.1f%%", startangle=90)
plt.title("Distribución de Ventas por Producto (Top 5 + Otros)")
plt.show()

# ------------------ HISTOGRAMA ------------------
plt.figure(figsize=(8, 5))
plt.hist(df["Cantidad"], bins=10, edgecolor='black')
plt.xlabel("Cantidad Vendida")
plt.ylabel("Frecuencia")
plt.title("Distribución de Cantidad Vendida")
plt.grid()
plt.show()
