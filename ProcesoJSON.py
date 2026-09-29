import json
from pathlib import Path


def cargar_json(ruta_archivo):
    """Carga el contenido de un archivo JSON y lo devuelve como diccionario."""
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def buscar_campo_recursivo(llave_objetivo, estructura):
    """Busca una clave en cualquier nivel del diccionario o lista."""
    if isinstance(estructura, dict):
        if llave_objetivo in estructura:
            return estructura[llave_objetivo]
        for valor in estructura.values():
            resultado = buscar_campo_recursivo(llave_objetivo, valor)
            if resultado is not None:
                return resultado
    elif isinstance(estructura, list):
        for elemento in estructura:
            resultado = buscar_campo_recursivo(llave_objetivo, elemento)
            if resultado is not None:
                return resultado
    return None


def obtener_fallas(data):
    """Recorre la estructura JSON y recoge todas las entradas de fallas_comunes."""
    fallas = []

    if isinstance(data, dict):
        if "fallas_comunes" in data and isinstance(data["fallas_comunes"], list):
            fallas.extend(data["fallas_comunes"])

        for valor in data.values():
            fallas.extend(obtener_fallas(valor))

    elif isinstance(data, list):
        for elemento in data:
            fallas.extend(obtener_fallas(elemento))

    return fallas


def generar_reporte(fallas, archivo_salida):
    """Crea un resumen en Markdown con todas las incidencias detectadas."""
    lineas = []
    lineas.append("# Reporte de mantenimiento eléctrico")
    lineas.append("")
    lineas.append(f"Total de incidencias: {len(fallas)}")
    lineas.append("")

    for falla in fallas:
        lineas.append(f"## {falla.get('id', 'Sin ID')} - {falla.get('componente', 'Sin componente')}")
        lineas.append(f"- Síntoma: {falla.get('sintoma', 'No especificado')}")
        lineas.append(f"- Causa raíz: {falla.get('causa_raiz', 'No especificada')}")
        lineas.append(f"- Gravedad: {falla.get('gravedad', 'No indicada')}")

        soluciones = falla.get("soluciones_anidadas", {})
        lineas.append("- Soluciones:")
        lineas.append(f"  - Inmediata: {soluciones.get('inmediata', 'No especificada')}")
        lineas.append(f"  - Análisis: {soluciones.get('analisis', 'No especificado')}")
        lineas.append(f"  - Definitiva: {soluciones.get('definitiva', 'No especificada')}")
        lineas.append("")

    with open(archivo_salida, "w", encoding="utf-8") as archivo:
        archivo.write("\n".join(lineas))

    return archivo_salida


if __name__ == "__main__":
    carpeta = Path(__file__).resolve().parent
    archivo_json = carpeta / "problemas_ingenieria_electrica.json"
    archivo_reporte = carpeta / "reporte_mantenimiento.md"

    datos = cargar_json(archivo_json)

    print("Tipo del diccionario:", type(datos))
    print("Categoría principal:", datos["ingenieria_electrica"]["sistema_potencia"]["categoria"])
    print("Claves principales:", list(datos["ingenieria_electrica"].keys()))

    fallas = obtener_fallas(datos)
    print(f"Se han encontrado {len(fallas)} incidencias en total.")

    ejemplo = buscar_campo_recursivo("categoria", datos)
    print("Búsqueda recursiva de 'categoria':", ejemplo)

    print(f"Generando reporte en: {generar_reporte(fallas, archivo_reporte)}")
resultado = [
    f for f in fallas
    if f.get("datos_tecnicos", {}).get("temperatura_aceite_c", 0) > 90
]

for f in resultado:
    print(f["id"], f["componente"], f["datos_tecnicos"])
gravedad = input("Introduce la gravedad (Crítica, Alta, Media): ")

resultado = [
    f for f in fallas
    if f.get("gravedad", "").lower() == gravedad.lower()
]

for f in resultado:
    print(f["id"], "-", f["componente"], "-", f["sintoma"])

valor = "PQ-002"
for f in fallas:
    if f.get("id") == valor:
        print(f)

'''Uso de json.dump() (Guardar en un archivo)
Se utiliza junto con la sentencia with open()
 para volcar el contenido directamente en un archivo físico.'''

import json

datos = {"nombre": "Carlos", "edad": 30, "ciudad": "Madrid"}

# Escribe el diccionario directamente en 'datos.json'
with open("datos.json", "w") as archivo:
    json.dump(datos, archivo, indent=4) 


'''Uso de json.dumps() (Convertir a String)
Ideal si necesitas manipular el texto JSON antes de enviarlo, guardarlo o imprimirlo.'''

import json

datos = {"nombre": "Carlos", "edad": 30, "ciudad": "Madrid"}

# Convierte el diccionario en una cadena JSON
cadena_json = json.dumps(datos, indent=4)

print(cadena_json)
print(type(cadena_json))  # Resultado: <class 'str'>

'''JSON codificado estrictamente en UTF-8 (especialmente útil si tus datos contienen acentos,
 eñes o caracteres especiales), debes combinar el parámetro encoding='utf-8' en la función
   open() con el parámetro ensure_ascii=False en json.dump()'''
import json

datos = {
    "usuario": "María José",
    "país": "España",
    "ciudad": "León"
}

# Al abrir el archivo forzamos la codificación UTF-8
with open("datos_utf8.json", "w", encoding="utf-8") as archivo:
    # 'ensure_ascii=False' evita que los acentos se transformen en códigos como \u00f3
    json.dump(datos, archivo, indent=4, ensure_ascii=False)


