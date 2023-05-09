import matplotlib.pyplot as plt

"""
Scrivere un programma Python che legga un file di testo chiamato 
"es02temperatures.txt" contenente le letture della temperatura in gradi
 Celsius e Fahrenheit su righe separate (ad esempio "23.5\n74.3\n").
 Il programma deve convertire le temperature Celsius in Fahrenheit, 
 creare un elenco di tuple contenenti le temperature Celsius e Fahrenheit e 
 creare un grafico a linee dei dati utilizzando matplotlib.
"""

# file = "C:\\Users\\Matteo\\OneDrive\\Desktop\\Data Scientist\\IA\\IA\\27_03_2023 L2\\es02temperatures.csv"
file = input("Path file: ")


with open(file, 'r') as file:
    lines = file.readlines()


celsius_temperatures = [float(line.strip()) for line in lines]
fahrenheit_temperatures = [(celsius * 9/5) + 32 for celsius in celsius_temperatures]
data = list(zip(celsius_temperatures, fahrenheit_temperatures))

plt.plot(data)
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Temperature Readings')
plt.legend(['Celsius', 'Fahrenheit'])
plt.show()

"""
I dati
23.5
24.0
24.5
25.0
25.5
"""