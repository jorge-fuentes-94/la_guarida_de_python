import json
import os

def persistir(nombre_pj,atributos_pj,talentos_pj,nombre_archivo):
    nombre_archivo_ruta = os.path.join (os.getcwd(),"fichas",nombre_archivo)
    print (nombre_archivo_ruta)
    with open (nombre_archivo_ruta,"w",encoding="utf-8") as archivo:
        informacion_pj = {"nombre":nombre_pj,"atributos":atributos_pj,"talentos":talentos_pj}
        json.dump(informacion_pj,archivo,ensure_ascii=False)
        
def obtener_supervivencia(nombre_archivo):
    with open (nombre_archivo,"r") as archivo:
        datos_pj = json.load (archivo)
        return datos_pj ["atributos"][4]["habilidades"][6]["valor"]

def comprobar_existencia_archivo(nombre_archivo):
    directorio_archivos = os.listdir()
    return nombre_archivo in directorio_archivos
