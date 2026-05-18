import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# 1. Criação de um Dataset Simulado (1000 transações)
np.random.seed(42)
n_samples = 1000

# Características: Valor da transação, Hora (0-23h), Distância da residência (km)
valor = np.random.exponential(scale=50, size=n_samples)
hora = np.random.randint(0, 24, size=n_samples)
distancia = np.random.exponential(scale=10, size=n_samples)

# Regra simulada para gerar fraudes
fraude = np.where((valor > 150) & (hora < 5) & (distancia > 30), 1, 0)
ruido = np.random.choice([0, 1], size=n_samples, p=[0.98, 0.02])
fraude = np.clip(fraude + ruido, 0, 1)

df = pd.DataFrame({
    'valor_transacao': valor,
    'hora_dia': hora,
    'distancia_km': distancia,
    'fraude': fraude
})

# 2. Divisão dos Dados (Treino e Teste)
X = df[['valor_transacao', 'hora_dia', 'distancia_km']]
y = df['fraude']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Treino do Modelo de Classificação
modelo = RandomForestClassifier(random_state=42)
modelo.fit(X_train, y_train)

# 4. Avaliação do Modelo
y_pred = modelo.predict(X_test)
print("=== Matriz de Confusão ===")
print(confusion_matrix(y_test, y_pred))
print("\n=== Relatório de Classificação ===")
print(classification_report(y_test, y_pred))
