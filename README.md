# Proyecto de Ciencia de Datos: Análisis de Datos Sintéticos de Pacientes COVID-19

Este proyecto analiza datos sintéticos de pacientes de dos hospitales con el objetivo de predecir el impacto del COVID-19 utilizando técnicas de minería de datos.

## Estructura del Proyecto

1. **`0_uploading_supabase.py`**  
   - Subida inicial de los archivos a Supabase para su almacenamiento y acceso.

2. **`1_initial_inspection.ipynb`**  
   - Exploración inicial de los datos (`hospital1.xlsx`, `hospital2.xlsx`).
   - Verificación de la integridad, detección de valores nulos y anomalías.

3. **`2_preprocessing_data1.ipynb`** y **`2_preprocessing_data2.ipynb`**  
   - Limpieza de datos para cada hospital:
     - Tratamiento de IDs.
     - Manejo de incoherencias.
     - Manejo de valores faltantes.
     - Transformación de datos categóricos y numéricos.
     - Columnas redundantes.
   - Generación de los archivos preprocesados (`hospital1_preprocessed.csv`, `hospital2_preprocessed.csv`).

4. **`3_joining.ipynb`**  
   - Integración de los datos de ambos hospitales en un único dataset combinado (`X.csv` y `y.csv`).
   - Creación de las etiquetas para el análisis predictivo.

5. **`4_models.ipynb`**  
   - Aplicación de algoritmos de aprendizaje automático:
     - Entrenamiento y validación de modelos.
     - Evaluación de métricas para optimizar los KPIs definidos.

---

Para más información, consulta los notebooks y el código proporcionado.
