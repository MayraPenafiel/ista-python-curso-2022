import pandas as pd
import matplotlib.pyplot as plt
import csv

estudiate = pd.read_csv('datos\estudiante.csv')
print('lsitado de estudiantes:')

print(estudiate)

asistencia = pd.read_csv('datos\datos_asistencia.csv')

print('listado de asistencia:')

print(asistencia)

informacion_del_estudiante = pd.merge(estudiate,asistencia, how='right')

print(informacion_del_estudiante)

print('CEDULA = 1123459039')

print(informacion_del_estudiante[informacion_del_estudiante.cedula == 1123459039])

informacion_del_estudiante[informacion_del_estudiante.cedula == 1123459039].to_csv('datos\datos_reporte_1123459039.csv', index=True)

informacion_del_estudiante[informacion_del_estudiante.cedula == 1123459039]['materia'].value_counts().plot(kind='bar')

plt.show()

