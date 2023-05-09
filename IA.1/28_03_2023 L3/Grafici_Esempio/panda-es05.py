"""
Come caricare vari formati di dati in python
"""
import pandas as pd

# CSV
df = pd.read_csv('data.csv')

# Excel
df = pd.read_excel('data.xlsx')

# JSON
df = pd.read_json('data.json')

# Normale file di testo
with open('data.txt', 'r') as f:
    data = f.read()


#Database sqlite3
import sqlite3

# Connect to the SQL database
conn = sqlite3.connect('database.db')

# Load data from an SQL database
df = pd.read_sql('SELECT * FROM table', conn)
