# ==============================================================================
# Entrega 3: 🐍 Modelo de Regresión Lineal Múltiple para Predecir Importe de Venta
# ==============================================================================

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- FUNCIÓN CLAVE: CALCULAR ERROR PORCENTUAL (MAPE) ---
def mean_absolute_percentage_error(y_true, y_pred):
    """Calcula el Error Absoluto Porcentual Medio (MAPE)."""
    # Se añade una pequeña constante (np.finfo(float).eps) para evitar división por cero
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

# --- CONFIGURACIÓN DE ARCHIVOS ---
RUTA_DATASET = "consolidado.csv" # Usando el archivo limpio de la Entrega 2

print("--- EJECUCIÓN: MODELO DE REGRESIÓN INDIVIDUAL ---")
print("-" * 50)

# 1. CARGA Y PREPROCESAMIENTO
try:
    df = pd.read_csv(RUTA_DATASET)
except FileNotFoundError:
    print(f"ERROR: No se encontró el archivo de datos limpio en la ruta: {RUTA_DATASET}")
    exit()

# Definición de variables predictoras (X) y objetivo (y)
X = df[['precio_unitario', 'cantidad', 'categoria_corregida', 'ciudad', 'medio_pago']]
y = df['importe'] 

# Codificación de variables categóricas (One-Hot Encoding)
X = pd.get_dummies(X, drop_first=True)

# 2. DIVISIÓN TRAIN/TEST
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. ENTRENAMIENTO DEL MODELO
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# 4. PREDICCIONES Y EVALUACIÓN
y_pred = modelo.predict(X_test)

# Cálculo de Métricas
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)
mape = mean_absolute_percentage_error(y_test, y_pred)

print("--- MÉTRICAS DE RENDIMIENTO (TEST SET) ---")
print(f"R² (Varianza Explicada): {r2:.4f}")
print(f"RMSE (Error en unidades): {rmse:.2f}")
print(f"MAE (Error Absoluto Medio): {mae:.2f}")
print(f"MAPE (Error Porcentual Medio): {mape:.2f}%")
print("-" * 50)

# 5. INTERPRETACIÓN DE COEFICIENTES
coeficientes = pd.DataFrame(modelo.coef_, X_train.columns, columns=['Impacto en Importe'])

print("\n--- COEFICIENTES DEL MODELO (TOP 5 IMPULSORES) ---")
# Mostrar los 5 coeficientes más influyentes
top_coeficientes = coeficientes.reindex(
    coeficientes['Impacto en Importe'].abs().sort_values(ascending=False).index
).head(5)
print(top_coeficientes)

# 6. VISUALIZACIONES GENERADAS

# Gráfico 1: Predicción vs. Valores Reales
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred, alpha=0.7, color='teal')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2, label="Predicción Perfecta")
plt.title('Modelo de Regresión Múltiple: Predicción vs. Valores Reales')
plt.xlabel('Importe Real')
plt.ylabel('Importe Predicho')
plt.legend()
plt.grid(True)
plt.show()

# Gráfico 2: Importancia de las Variables (Coeficientes)
plt.figure(figsize=(10, 6))
sns.barplot(x='Impacto en Importe', y=top_coeficientes.index, data=top_coeficientes, palette='viridis')
plt.title('Importancia de Variables (Coeficientes Top 5)')
plt.show()