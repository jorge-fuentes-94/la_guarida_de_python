from utilidades import obtener_datos_seguros,isElfo, isHumano, isEnano, isTeafling, isTasha, isMago, isGuerrero, isPicaro
from razas import talentos_raza
from clases import talentos_clase

atributos_pj = [
    {"atributo":"Fuerza","valor":0,"modificador":0,"habilidades":[
        {"habilidad":"atletismo","competencia":False,"valor":0}
    ]},
    {"atributo":"Destreza","valor":0,"modificador":0,"habilidades":[
         {"habilidad":"Acrobacias","competencia":False,"valor":0},
         {"habilidad":"Juego de Manos","competencia":False,"valor":0},
         {"habilidad":"Sigilo","competencia":False,"valor":0}
    ]},
    {"atributo":"Constitución","valor":0,"modificador":0,"habilidades":[
    ]},
    {"atributo":"Inteligencia","valor":0,"modificador":0,"habilidades":[
        {"habilidad":"Arcano","competencia":False,"valor":0},
        {"habilidad":"Historia","competencia":False,"valor":0},
        {"habilidad":"Investigación","competencia":False,"valor":0}
    ]},
    {"atributo":"Sabiduría","valor":0,"modificador":0,"habilidades":[
        {"habilidad":"Naturaleza","competencia":False,"valor":0},
        {"habilidad":"Religión","competencia":False,"valor":0},
        {"habilidad":"Trato con animales","competencia":False,"valor":0},
        {"habilidad":"Medicina","competencia":False,"valor":0},
        {"habilidad":"Percepción","competencia":False,"valor":0},
        {"habilidad":"Perspicacia","competencia":False,"valor":0},
        {"habilidad":"Supervivencia","competencia":False,"valor":0}
    ]},
    {"atributo":"Carisma","valor":0,"modificador":0,"habilidades":[
        {"habilidad":"Engaño","competencia":False,"valor":0},
        {"habilidad":"Intimidación","competencia":False,"valor":0},
        {"habilidad":"Interpretación","competencia":False,"valor":0},
        {"habilidad":"Persuasión","competencia":False,"valor":0}
    ]}]   

talentos_pj = []  


def definir_atributos(raza_pj,tasha):
    atributo_principal = ""
    atributo_secundario = ""
    if isTasha(tasha) or isHumano(raza_pj):
        while atributo_principal == atributo_secundario:
            atributo_principal = obtener_datos_seguros(["fuerza","destreza","constitución","inteligencia","sabiduría","carisma"],"Por favor, introduce tu atributo principal: ")
            atributo_secundario = obtener_datos_seguros(["fuerza","destreza","constitución","inteligencia","sabiduría","carisma"],"Por favor, introduce tu atributo secundario: ")
            if atributo_principal == atributo_secundario:
                print("El atributo principal y el atributo secundario no puede ser el mismo")         
    elif isEnano(raza_pj):
        atributo_principal = "constitución"
        atributo_secundario = "fuerza"
        
    elif isElfo(raza_pj):
        atributo_principal = "destreza"
        atributo_secundario = "inteligencia"
        
    elif isTeafling(raza_pj):
        atributo_principal = "carisma"
        atributo_secundario = "inteligencia"
    return atributo_principal, atributo_secundario

def definir_competencia_clase(clase_pj,habilidades_competentes_clase):
    for habilidad in habilidades_competentes_clase:
       if isMago(clase_pj):
           if habilidad == 0:
              atributos_pj[3]["habilidades"][0]["competencia"] = True
           if habilidad == 1:
              atributos_pj[3]["habilidades"][1]["competencia"] = True
           if habilidad == 2:
              atributos_pj[3]["habilidades"][2]["competencia"] = True 
           if habilidad == 3:
              atributos_pj[4]["habilidades"][3]["competencia"] = True 
           if habilidad == 4:
              atributos_pj[4]["habilidades"][5]["competencia"] = True 
           if habilidad == 5:
              atributos_pj[4]["habilidades"][1]["competencia"] = True  
       if isGuerrero(clase_pj):
           if habilidad == 0:
              atributos_pj[1]["habilidades"][0]["competencia"] = True
           if habilidad == 1:
              atributos_pj[0]["habilidades"][0]["competencia"] = True
           if habilidad == 2:
              atributos_pj[3]["habilidades"][1]["competencia"] = True 
           if habilidad == 3:
              atributos_pj[5]["habilidades"][1]["competencia"] = True 
           if habilidad == 4:
              atributos_pj[4]["habilidades"][3]["competencia"] = True 
           if habilidad == 5:
              atributos_pj[4]["habilidades"][5]["competencia"] = True    
           if habilidad == 6:
              atributos_pj[4]["habilidades"][6]["competencia"] = True 
           if habilidad == 7:
              atributos_pj[4]["habilidades"][2]["competencia"] = True 
       if isPicaro(clase_pj):
            if habilidad == 0:
              atributos_pj[1]["habilidades"][0]["competencia"] = True
            if habilidad == 1:
              atributos_pj[0]["habilidades"][0]["competencia"] = True
            if habilidad == 2:
              atributos_pj[5]["habilidades"][0]["competencia"] = True 
            if habilidad == 3:
              atributos_pj[5]["habilidades"][2]["competencia"] = True 
            if habilidad == 4:
              atributos_pj[5]["habilidades"][1]["competencia"] = True 
            if habilidad == 5:
              atributos_pj[3]["habilidades"][2]["competencia"] = True  
            if habilidad == 6:
              atributos_pj[1]["habilidades"][1]["competencia"] = True  
            if habilidad == 7:
              atributos_pj[4]["habilidades"][4]["competencia"] = True  
            if habilidad == 8:
              atributos_pj[4]["habilidades"][5]["competencia"] = True  
            if habilidad == 9:
              atributos_pj[5]["habilidades"][3]["competencia"] = True  
            if habilidad == 10:
              atributos_pj[1]["habilidades"][2]["competencia"] = True  
          
def definir_talentos_pj (raza_pj,clase_pj,talentos_pj,estilo_combate,pericias_picaro):
    talentos_pj = talentos_raza(raza_pj,talentos_pj) + talentos_clase(clase_pj,talentos_pj,estilo_combate,pericias_picaro)

        
            
    
def generar_habilidades_competentes(clase_pj):
    lista_habilidades = []
    if isGuerrero(clase_pj):
        lista_habilidades.append("Acrobacias")
        lista_habilidades.append("Atletismo")
        lista_habilidades.append("Historia")
        lista_habilidades.append("Intimidar")
        lista_habilidades.append("Percepción")
        lista_habilidades.append("Perspicacia")
        lista_habilidades.append("Supervivencia")
        lista_habilidades.append("Trato con animales")
    if isMago(clase_pj):
        lista_habilidades.append("Arcano")
        lista_habilidades.append("Historia")
        lista_habilidades.append("Investigación")
        lista_habilidades.append("Medicina")
        lista_habilidades.append("Perspicacia")
        lista_habilidades.append("Religión")
    if isPicaro(clase_pj):
        lista_habilidades.append("Acrobacias")
        lista_habilidades.append("Atletismo")
        lista_habilidades.append("Engañar")
        lista_habilidades.append("Interpretación")
        lista_habilidades.append("Intimidar")
        lista_habilidades.append("Investigación")
        lista_habilidades.append("Juego de manos")
        lista_habilidades.append("Percepción")
        lista_habilidades.append("Perspicacia")
        lista_habilidades.append("Persuasión")
        lista_habilidades.append("Sigilo")
        
    return lista_habilidades
        
    
    
       