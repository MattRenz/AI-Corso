"""
Grafico a linee: Un grafico a linee è un modo per visualizzare l'andamento o il modello dei 
dati nel tempo o tra diverse variabili. I grafici a linee possono essere utilizzati per 
identificare le tendenze, confrontare le prestazioni di diversi modelli e analizzare l'impatto 
di diverse variabili sul risultato. Ad esempio, il codice seguente traccia un grafico a linee 
dell'accuratezza di un modello per epoche
"""

import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = make_classification(n_samples=1000, n_clusters_per_class=4, n_redundant=3, n_features=20, n_informative=10, n_classes=10)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LogisticRegression()
epochs = 200
train_acc = []
test_acc = []
for epoch in range(epochs):
    model.fit(X_train, y_train)
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)
    train_acc.append(accuracy_score(y_train, y_pred_train))
    test_acc.append(accuracy_score(y_test, y_pred_test))

plt.plot(range(1, epochs+1), train_acc, label="Train")
plt.plot(range(1, epochs+1), test_acc, label="Test")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.title("Accuracy over Epochs")
plt.legend()
plt.show()
