# -*- coding: utf-8 -*-
import json
import os

def procesar_incidencias(archivo_json, severidad_filtro=None, archivo_reporte="reporte_mantenimiento.md"):
    """
    Lee un archivo JSON con problemas de ingeniería eléctrica, filtra las incidencias
    por su nivel de severidad e imprime y guarda un reporte técnico estructurado.
    """
    if not os.path.exists(archivo_json):
        print(f"Error: El archivo '{archivo_json}' no existe en la ruta actual.")
        return

    try:
        with open(archivo_json, 'r', encoding='utf-8') as f:
            data = json.load(f) #Accede y crea un diccionario del fichero
    except json.JSONDecodeError:
        print(f"Error: El archivo '{archivo_json}' no tiene un formato JSON válido.")
        return
    except Exception as e:
        print(f"Ocurrió un error inesperado al leer el archivo: {e}")
        return

    sistema = data.get("sistema_electrico", {})
    nombre_red = sistema.get("nombre_red", "Red Eléctrica")
    fecha = sistema.get("fecha_actualizacion", "N/D")
    
    lineas_reporte = []
    lineas_reporte.append(f"# REPORTE TÉCNICO DE INCIDENCIAS ELÉCTRICAS")
    lineas_reporte.append(f"**Sistema:** {nombre_red}")
    lineas_reporte.append(f"**Fecha de Análisis:** {fecha}")
    if severidad_filtro:
        lineas_reporte.append(f"**Filtro Aplicado:** Severidad = '{severidad_filtro}'")
    lineas_reporte.append("-" * 60 + "\n")
    
    total_leidas = 0
    total_mostradas = 0
    
    for subestacion in sistema.get("subestaciones", []):
        sub_info = f"=== SUBESTACIÓN: {subestacion.get('nombre')} ({subestacion.get('nivel_tension')}) ==="
        sub_agregada = False
        
        for falla in subestacion.get("fallas_registradas", []):
            total_leidas += 1
            sev_falla = falla.get("severidad", "")
            
            # Aplicar filtro de severidad (Ignora mayúsculas/minúsculas)
            if severidad_filtro and sev_falla.lower() != severidad_filtro.lower():
                continue
                
            if not sub_agregada:
                lineas_reporte.append(sub_info)
                lineas_reporte.append(f"ID: {subestacion.get('id')} | Aislamiento: {subestacion.get('tipo_aislamiento')}\n")
                sub_agregada = True
            
            total_mostradas += 1
            lineas_reporte.append(f"  [+] Incidencia: {falla.get('codigo_incidencia')} | Severidad: **{sev_falla}**")
            lineas_reporte.append(f"      Componente: {falla.get('componente_afectado')}")
            lineas_reporte.append(f"      Categoría Causa: {falla.get('analisis_causa_raiz', {}).get('categoria')}")
            lineas_reporte.append(f"      Descripción: {falla.get('analisis_causa_raiz', {}).get('descripcion')}")
            
            lineas_reporte.append("      Síntomas Detectados:")
            for sintoma in falla.get("sintomas", []):
                lineas_reporte.append(f"        - {sintoma}")
                
            plan = falla.get("plan_accion", {})
            lineas_reporte.append("      Plan de Acción Correctivo:")
            lineas_reporte.append(f"        * Inmediato: {plan.get('inmediato')}")
            lineas_reporte.append(f"        * Técnico:   {plan.get('tecnico')}")
            lineas_reporte.append(f"        * Definitivo:{plan.get('definitivo')}")
            lineas_reporte.append("") # Línea en blanco entre fallas

    resumen = f"Resumen: Se encontraron {total_mostradas} incidencias de severidad '{severidad_filtro if severidad_filtro else 'Cualquiera'}' (de un total de {total_leidas} registradas)."
    lineas_reporte.append("-" * 60)
    lineas_reporte.append(resumen)

    # Mostrar en consola
    texto_final = "\n".join(lineas_reporte)
    print(texto_final)
    
    # Guardar en archivo de texto Markdown
    try:
        with open(archivo_reporte, 'w', encoding='utf-8') as rf:
            rf.write(texto_final)
        print(f"\n[Éxito] El reporte filtrado se ha guardado correctamente en: '{archivo_reporte}'")
    except Exception as e:
        print(f"Error al escribir el archivo de reporte: {e}")

if __name__ == "__main__":
    # CONFIGURACIÓN DEL PROCESAMIENTO
    archivo_origen = "problemas_ingenieria_electrica.json"
    archivo_destino = "reporte_mantenimiento.md"
    
    # Cambia este valor a "Critica", "Alta", "Media" o None (para ver todas)
    filtro_severidad = "Critica" 
    
    print(f"Iniciando procesamiento de '{archivo_origen}'...\n")
    procesar_incidencias(archivo_origen, severidad_filtro=filtro_severidad, archivo_reporte=archivo_destino)

#Acceder a un campo del diccionario obtenido a partir del JSON

def buscar_campo_cualquiera(llave_objetivo, estructura):
    """Busca de forma recursiva una llave en cualquier nivel del JSON."""
    # Si es un diccionario, buscamos en sus llaves y valores
    if isinstance(estructura, dict):
        if llave_objetivo in estructura:
            return estructura[llave_objetivo]
        for valor in estructura.values():
            resultado = buscar_campo_cualquiera(llave_objetivo, valor)
            if resultado is not None:
                return resultado
                
    # Si es una lista, buscamos dentro de cada elemento
    elif isinstance(estructura, list):
        for elemento in estructura:
            resultado = buscar_campo_cualquiera(llave_objetivo, elemento)
            if resultado is not None:
                return resultado
                
    return None

# --- Uso del código ---
with open("problemas_ingenieria_electrica.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

# Puedes escribir CUALQUIER campo que sepas que existe en el JSON
#campo_a_buscar = input("Dato: ")
campo_a_buscar = datos.get(input("Dato: "))
valor_encontrado = buscar_campo_cualquiera(campo_a_buscar, datos)

print(f"El valor del campo '{campo_a_buscar}' es: {valor_encontrado}")


#funcion: dumps  pasa un campo de un diccionario a un JSON