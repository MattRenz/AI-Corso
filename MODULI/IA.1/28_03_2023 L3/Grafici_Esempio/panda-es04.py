"""
Dataset di cifre: Per caricare il dataset cifre da sklearn.datasets e convertirlo in un 
dataframe pandas, si può usare la funzione load_digits() e creare un dataframe dagli array 
data e target
"""

from sklearn.datasets import load_digits
import pandas as pd

# Load the digits dataset
digits = load_digits()

# Create dataframe
df = pd.DataFrame(digits.data, columns=[f'pixel_{i}' for i in range(digits.data.shape[1])])
df['target'] = digits.target

print(df.head())