# -*- coding: utf-8 -*-
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

# 1. Criando dados sintéticos (Duração, Volume de Dados)
# Imagine que ataques duram pouco tempo mas transmitem muitos dados
X = np.array([
    [1, 20], [1.5, 25], [2, 18], [5, 100], [6, 110],  # Normais
    [0.1, 500], [0.2, 600], [0.1, 450], [0.3, 700]    # Ataques (Ex: DoS)
])

# Labels: 0 para Normal, 1 para Ataque
y = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1])

# 2. Dividindo entre treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Inicializando o modelo k-NN (k=3)
# O algoritmo olha para os 3 vizinhos mais próximos para decidir a classe
knn = KNeighborsClassifier(n_neighbors=3)

# 4. Treinando o modelo
knn.fit(X_train, y_train)

# 5. Prevendo um novo acesso suspeito
# (Duração curtíssima de 0.15s e 550MB de dados)
novo_acesso = np.array([[0.15, 550]])
predicao = knn.predict(novo_acesso)

print(f"Resultado da análise: {'ATAQUE DETECTADO!' if predicao[0] == 1 else 'Acesso Normal'}")

# 6. Avaliação do Desempenho
y_pred = knn.predict(X_test)
print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred))

