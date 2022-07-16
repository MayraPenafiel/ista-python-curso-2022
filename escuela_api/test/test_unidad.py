from asyncio.windows_events import NULL
from escuela_api import api

def test_lista_estudiante():
    assert api.obtener_un_estudiantes('1123459039') == '[{"cedula": "1123459039", "primer_apellido": "Penafiel", "segundo_apellido": "Torres", "primer_nombre": "Mayra", "segundo_nombre": "Alejandra"}]'