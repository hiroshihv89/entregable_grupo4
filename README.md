# Análisis de Datos y Visualización

Este proyecto realiza un análisis exploratorio de datos, procesamiento y visualización de información proveniente de un archivo CSV con datos de ventas. Se utilizan las librerías **Pandas**, **NumPy** y **Matplotlib** para el procesamiento y generación de gráficos.

## Requisitos
Antes de ejecutar el código, asegúrate de tener instaladas las siguientes dependencias:

```bash
pip install pandas numpy matplotlib
```

## Archivos del Proyecto

### 1. `Carga_ProcDatos.py`
**Descripción:**
- Carga los datos desde un archivo CSV.
- Explora la estructura de los datos.
- Maneja valores nulos y datos faltantes.
- Aplica operaciones matemáticas con NumPy.

**Ejecución:**
```bash
python Carga_ProcDatos.py
```

### 2. `analisis_datos.py`
**Descripción:**
- Convierte la columna de fechas a formato `datetime`.
- Realiza estadísticas descriptivas.
- Calcula la matriz de correlación.
- Identifica patrones de ventas por producto y por mes.
- Filtra ventas superiores a un umbral específico.

**Ejecución:**
```bash
python analisis_datos.py
```

### 3. `graficos_ventas.py`
**Descripción:**
- Genera gráficos de líneas para evolución de ventas mensuales.
- Crea gráficos de barras con los 5 productos más vendidos.
- Muestra la distribución de ventas por producto en un gráfico de torta.
- Construye un histograma de la cantidad de productos vendidos.

**Ejecución:**
```bash
python graficos_ventas.py
```

## Uso del Proyecto
1. Ubica los archivos del proyecto en el mismo directorio que `datos_ventas.csv`.
2. Instala las dependencias necesarias con `pip`.
3. Ejecuta los scripts en el orden recomendado para cargar y analizar los datos antes de visualizar los gráficos.

## Integrantes
**Grupo 4**

Erick Carlos Larrea Carpio

Efren Hiroshi Hernandez Vicente

Franklin Joseph Castro Chocca

Jean Cesar Robles Castro

---
## Instructor

Saúl Sneider Chávez Chico

