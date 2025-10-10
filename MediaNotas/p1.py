import csv
import random as rand
import pandas as pd
import numpy as np

from MediaNotas.Alumno import Alumno

nombres = ["Ana", "Bea", "Carlos", "David", "Euge", "Federico", "Gema", "Hugo", "Ignacio", "Julia",
           "Kiko", "Lucia", "Maria", "Nuria", "Oscar", "Paula", "Raquel", "Susana", "Tiana",
           "Úrsula", "Víctor"]

apellidos = ["Alvarez", "Blanco", "Castillo", "Díaz", "Estévez", "Fernandez", "García", "Hernández", "Ibáñez", "Jiménez",
            "López", "Martinez", "Navarro", "Ortega", "Pérez", "Quintero", "Rodriguez", "Sánchez", "Torres",
             "Úbeda", "Vargas"]



#nombre, apellidos, py, dm, ds, calc, oop, java, cplus, db, webdev, ai)
def escribirCSV():
    data = []
    for i in range(1000000):
        data.append(Alumno(rand.choice(nombres), rand.choice(apellidos),
                           rand.randint(0, 100),rand.randint(0, 100), rand.randint(0, 100),
                           rand.randint(0, 100),rand.randint(0, 100),rand.randint(0, 100),
                           rand.randint(0, 100),rand.randint(0, 100),rand.randint(0, 100),
                           rand.randint(0, 100)).to_dict())
    with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['ID', 'Nombre', 'Apellidos', 'Python', 'Discrete Mathematics', 'Data Structures', 'Calculus',
                      'Object-Oriented Programming', 'Java', 'C++', 'Databases', 'Web Development', 'AI']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

#escribirCSV()

#modificar los valores de muestra
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('data.csv') # Read csv as a DataFile

#df.head() # muestra los 5 primeros
#df.head(10) # muestra los 10 primeros
#df.tail() # muestra los 5 ultimos

#df.info() # Data types and memory usage
#df.describe() # Muestra aun mas informacion
#df.shape # Muestra el numero de filas y el numero de columnas
#df.columns # Muestra el nombre de las columnas
#df.index # Muestra el index (donde empieza, donde acaba y cada cuentos "pasos" cuenta)

df["Nombre"] # Muestra la columna que se especifique como serie,
df[["Apellidos"]] # Muestra la columna que se especifique como dataframe

df.iloc[0] # muestra la primera fila (indice 0)
df.iloc[0:6] # muestra del indice 0 al indice 6 (del 1 al 7)

df.loc[1] #muestra el indice que se especifica

df[df['C++'] > 90].head(10) # mostrar los 10 primeros que tengan mas de 90 puntos en C++
df[df["Java"] < 10].sort_values(by=['Java'], ascending=False).tail(10) # Mostrar los 10 ultimos que tengan menos de 10 puntos en java ordenados por los puntos que han sacado en java

df.query("Java >= 95 and Python >= 95 and `C++`>= 95") # Muestra aquellos que tengan 95 o mas en Java, Python y C++

columnas_no_media = ["ID", "Nombre", "Apellidos"]
columnas_media = [col for col in df.columns if col not in columnas_no_media]

#df['Average'] # agregar columna
#df['Average'] = df[columnas_media].mean(axis=1) # axis = 1 indica la fila, axis = 0 indica la columna

#df.mean()        # Mean of each column
#df.sum()         # Sum of each column
#df.min()         # Minimum value
#df.max()         # Maximum value
#df.std()         # Standard deviation
#df.count()       # Count non-NA values