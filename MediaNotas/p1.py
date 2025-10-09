import csv
import random as rand
import pandas as pd

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


pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
df = pd.read_csv('data.csv') # Read csv as a datafile


non_grade_columns=["ID", "Nombre", "Apellidos"]
grade_columns= [col for col in df.columns if col not in non_grade_columns]

df['Average Score'] = df[grade_columns].mean(axis=1)

sorted_by_average_score = df.sort_values(by=['Average Score'], ascending=False).head(3)
print(sorted_by_average_score)


filtered_students = df[(df[grade_columns] > 60).all(axis=1)]
filtered_students_sorted = filtered_students.sort_values(by=['Average Score'], ascending=False)
#print(filtered_students_sorted)

#df['average_score'] = df[grade_columns].mean(axis=1)

#df_sorted_2 = df.sort_values(by=['average_score'], ascending=False)
#print(df_sorted_2)

#df_sorted = df.sort_values(by=['Mates'], ascending=False) # Sort by Mates grade

# Standard Deviation
# df_sorted['Mates'].std()

