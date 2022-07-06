import os
import random
os.system("cls")

nombre_pj = input("Por favor, introduce el nombre de tu personaje: ")
atributos_pj = [
    {"atributo":"Fuerza","valor":0,"modificador":0,"habilidades":[
        {"habilidad":"atletismo","competencia":True,"valor":0}
    ]},
    {"atributo":"Destreza","valor":0,"modificador":0,"habilidades":[
         {"habilidad":"Acrobacias","competencia":True,"valor":0},
         {"habilidad":"Juego de Manos","competencia":True,"valor":0},
         {"habilidad":"Sigilo","competencia":True,"valor":0}
    ]},
    {"atributo":"Constitución","valor":0,"modificador":0,"habilidades":[
    ]},
    {"atributo":"Inteligencia","valor":0,"modificador":0,"habilidades":[
        {"habilidad":"Arcano","competencia":True,"valor":0},
        {"habilidad":"Historia","competencia":True,"valor":0},
        {"habilidad":"Investigación","competencia":True,"valor":0}
    ]},
    {"atributo":"Sabiduría","valor":0,"modificador":0,"habilidades":[
        {"habilidad":"Naturaleza","competencia":True,"valor":0},
        {"habilidad":"Religión","competencia":True,"valor":0},
        {"habilidad":"Trato con animales","competencia":True,"valor":0},
        {"habilidad":"Medicina","competencia":True,"valor":0},
        {"habilidad":"Percepción","competencia":True,"valor":0},
        {"habilidad":"Perspicacia","competencia":True,"valor":0},
        {"habilidad":"Supervivencia","competencia":True,"valor":0}
    ]},
    {"atributo":"Carisma","valor":0,"modificador":0,"habilidades":[
        {"habilidad":"Engaño","competencia":True,"valor":0},
        {"habilidad":"Intimidación","competencia":True,"valor":0},
        {"habilidad":"Interpretación","competencia":True,"valor":0},
        {"habilidad":"Persuasión","competencia":True,"valor":0}
    ]}]   

def decorar_valor(valor):
    if valor >= 0:
            valor = f"+{valor}"
    return str(valor)
            
def modificador_pj (valor):
    return (valor-10)//2

def generador_3d6 ():
    for indice in range(len(atributos_pj)):
        atributos_pj[indice]["valor"] = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
        atributos_pj[indice]["modificador"] = modificador_pj(atributos_pj[indice]["valor"])
        atributos_pj[indice]["modificador"] = decorar_valor(atributos_pj[indice]["modificador"])
        print (f"{atributos_pj[indice]['atributo']}: {atributos_pj[indice]['valor']} ({atributos_pj[indice]['modificador']})")
        
def generador_4d6 ():
    for indice in range(len(atributos_pj)):
         cuatrod6 = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
         cuatrod6.remove (min(cuatrod6))
         tresd6 = cuatrod6
         atributos_pj[indice]["valor"]=tresd6[0]+tresd6[1]+tresd6[2]
         atributos_pj[indice]["modificador"] = modificador_pj(atributos_pj[indice]["valor"])
         atributos_pj[indice]["modificador"] = decorar_valor(atributos_pj[indice]["modificador"])
         print (f"{atributos_pj[indice]['atributo']}: {atributos_pj[indice]['valor']} ({atributos_pj[indice]['modificador']})")



clasico_o_moderno_dados = ""
while clasico_o_moderno_dados not in ["C","c","M","m"]:
    clasico_o_moderno_dados = input("Por favor decida si prefiere elegir sus atributos por estilo clásico[C] o moderno[M]: ")
    if clasico_o_moderno_dados == "C" or clasico_o_moderno_dados=="c":
        print(f"Nombre del pj: {nombre_pj}")
        generador_3d6()
    elif clasico_o_moderno_dados == "M" or clasico_o_moderno_dados == "m":
        print(f"Nombre del pj: {nombre_pj}")
        generador_4d6()

def calcular_habilidad_pj (atributos_pj):
    for indice_atributo in range(len(atributos_pj)):
       for indice_habilidad in range(len(atributos_pj[indice_atributo]["habilidades"])):
            atributos_pj[indice_atributo]["habilidades"][indice_habilidad]["valor"] = modificador_pj(atributos_pj[indice_atributo]["valor"])
            if atributos_pj[indice_atributo]["habilidades"][indice_habilidad]["competencia"] == True:
                atributos_pj[indice_atributo]["habilidades"][indice_habilidad]["valor"] += 2
            atributo_habilidad_decorado = decorar_valor(atributos_pj[indice_atributo]["habilidades"][indice_habilidad]["valor"])
            print(f"{atributos_pj[indice_atributo]['habilidades'][indice_habilidad]['habilidad']}: {atributo_habilidad_decorado}")

calcular_habilidad_pj(atributos_pj)