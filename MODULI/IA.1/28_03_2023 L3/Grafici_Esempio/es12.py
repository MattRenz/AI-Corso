"""
Curva ROC: Una curva caratteristica operativa del ricevitore (ROC) è un grafico che mostra il 
compromesso tra il tasso di veri positivi (TPR) e il tasso di falsi positivi (FPR) per diversi 
valori di soglia di un classificatore binario. Le curve ROC possono essere utilizzate per 
valutare le prestazioni di un classificatore, confrontare le prestazioni di diversi modelli e 
determinare il valore di soglia ottimale per un determinato compito. Ad esempio, il codice 
seguente traccia la curva ROC per un modello di regressione logistica su un compito di 
classificazione binaria:
"""


import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, roc_auc_score

X, y = make_classification(n_samples=1000, n_features=10, n_classes=2)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)

y_prob = model.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
auc = roc_auc_score(y_test, y_prob)

plt.plot(fpr, tpr, label=f"AUC={auc:.2f}")
plt.plot([0, 1], [0, 1], linestyle="--", color="gray")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()
