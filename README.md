# Regresión Logística — Exploración Computacional

Trabajo del curso Machine Learning (Universidad El Bosque,
Programa de  Estadística, Semestre 2026-2).

## Integrantes

- Mariana Lizarazo

## Objetivo

Estudiar computacionalmente propiedades del modelo de regresión logística mediante
experimentos reproducibles: superficie del riesgo, comparación entre datos separables
y no separables, recuperación de parámetros, interpretación de los coeficientes, y
estabilidad numérica de la verosimilitud. Todo el trabajo está implementado únicamente
con numpy, scipy y matplotlib.

## Estructura del repositorio

- `README.md`
- `requirements.txt`
- `.gitignore`
- `src/`
  - `__init__.py`
  - `modelo.py` — sigmoide, p_theta y riesgo empírico
  - `optimizacion.py` — ajuste de theta con scipy.optimize.minimize
  - `simulacion.py` — generación de datos
- `notebooks/`
  - `experimentos.ipynb` — desarrollo de los 5 ejercicios del taller
- `resultados/`
  - figuras generadas por el notebook (.png)

Las funciones reutilizables están en `src/`. El cuaderno `experimentos.ipynb`
únicamente las importa y las usa para resolver cada ejercicio; no las redefine.

## Instalación

Clonar el repositorio y, desde la carpeta del proyecto, instalar las dependencias:pip install -r requirements.txt

## Ejecución

Abrir el cuaderno con Jupyter:jupyter notebook notebooks/experimentos.ipynb


y ejecutar todas las celdas en orden (Run All), desde un kernel reiniciado. Las
figuras se generan automáticamente y se guardan en `resultados/`.