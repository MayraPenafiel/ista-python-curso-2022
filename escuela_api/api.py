from flask import Flask, request
import csv
import json

app = Flask(__name__)

@app.route('/obtener_estudiantes')
def obtener_estudiantes():
    with open('datos\estudiante.csv') as files:
        estudiante = csv.reader(files)
        next(estudiante)
        estudiante_lista = []
        for fila in estudiante:
            estudiante_lista.append({'cedula': fila[0],'primer_apellido': fila[1],'segundo_apellido': fila[2],'primer_nombre': fila[3],'segundo_nombre': fila[4] })
    return json.dumps(sorted(estudiante_lista, key=lambda x: x['primer_nombre'] + x['primer_apellido']))

@app.route('/registrar_asistencia', methods=['POST'])
def registrar_asistencia():
    with open('datos\datos_asistencia.csv', 'a' , newline='') as files:
        escritor_csv = csv.writer(files,delimiter=',')
        escritor_csv.writerow([
            request.json['cedula'],request.json['materia'],request.json['fecha_anio'],request.json['fecha_mes'],request.json['fecha_dia']])
    return 'registro exitoso'

@app.route('/obtener_un_estudiantes/<cedula>')
def obtener_un_estudiantes(cedula):
    with open('datos\estudiante.csv') as files:
        estudiante = csv.reader(files)
        next(estudiante)
        estudiante_lista = []
        for fila in estudiante:
            if fila[0] == cedula:
                estudiante_lista.append({'cedula': fila[0],'primer_apellido': fila[1],'segundo_apellido': fila[2],'primer_nombre': fila[3],'segundo_nombre': fila[4] })
    return json.dumps(estudiante_lista)

if __name__ == '__main__':
    app.run(debug=True)