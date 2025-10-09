import csv
import random as rand
import pandas as pd

from MediaNotas.Alumno import Alumno

nombres = ["Ana", "Bea", "Carlos", "David", "Euge", "Federico", "Gema", "Hugo", "Ignacio", "Julia",
           "Kiko", "Lucia", "Maria", "Nuria", "Oscar", "Paula", "Q", "Raquel", "Susana", "Tiana",
           "Úrsula", "Víctor"]

apellidos = ["Alvarez", "B", "C", "D", "E", "F", "G", "H", "I", "J",
             "K", "L", "M", "N", "O", "P", "Q", "Rodriguez", "S", "T",
             "U", "V"]


data = []
for i in range(100):
    data.append(Alumno(rand.choice(nombres), rand.choice(apellidos),
                       rand.randint(0, 100),rand.randint(0, 100),rand.randint(0, 100),rand.randint(0, 100)).to_dict())



with open('data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Nombre', 'Apellidos', 'Mates', 'Biología', 'Inglés', 'Lengua']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()  # Write the header row
    writer.writerows(data)  # Write all rows


df = pd.read_csv('data.csv') # Read csv as a datafile

non_grade_columns=["Nombre" , "Apellidos"]
grade_columns= [col for col in df.columns if col not in non_grade_columns]

#filtered_students = df[(df[grade_columns] > 40).all(axis=1)]
#filtered_students_sorted = filtered_students.sort_values(by=['Mates'], ascending=False)

df['average_score'] = df[grade_columns].mean(axis=1)

df_sorted_2 = df.sort_values(by=['average_score'], ascending=False)
print(df_sorted_2)

#df_sorted = df.sort_values(by=['Mates'], ascending=False) # Sort by Mates grade

# Standard Deviation
# df_sorted['Mates'].std()

