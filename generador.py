import os
import random
os.system("cls")

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

def decorar_valor(valor):
    if valor >= 0:
            valor = f"+{valor}"
    return str(valor)
            
def modificador_pj (valor):
    return (valor-10)//2

def generador_3d6 (atributo_principal,atributo_secundario):
    for indice in range(len(atributos_pj)):
        atributos_pj[indice]["valor"] = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
        if atributos_pj[indice]["atributo"] == atributo_principal:
            atributos_pj[indice]["valor"] +=2
        if atributos_pj[indice]["atributo"] == atributo_secundario:
            atributos_pj[indice]["valor"] +=1
        atributos_pj[indice]["modificador"] = modificador_pj(atributos_pj[indice]["valor"])
        atributos_pj[indice]["modificador"] = decorar_valor(atributos_pj[indice]["modificador"])
        print (f"{atributos_pj[indice]['atributo']}: {atributos_pj[indice]['valor']} ({atributos_pj[indice]['modificador']})")
        
def generador_4d6 (atributo_principal,atributo_secundario):
    for indice in range(len(atributos_pj)):
         cuatrod6 = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
         cuatrod6.remove (min(cuatrod6))
         tresd6 = cuatrod6
         atributos_pj[indice]["valor"]=tresd6[0]+tresd6[1]+tresd6[2]
         if atributos_pj[indice]["atributo"] == atributo_principal:
            atributos_pj[indice]["valor"] +=2
         if atributos_pj[indice]["atributo"] == atributo_secundario:
            atributos_pj[indice]["valor"] +=1
         atributos_pj[indice]["modificador"] = modificador_pj(atributos_pj[indice]["valor"])
         atributos_pj[indice]["modificador"] = decorar_valor(atributos_pj[indice]["modificador"])
         print (f"{atributos_pj[indice]['atributo']}: {atributos_pj[indice]['valor']} ({atributos_pj[indice]['modificador']})")


def obtener_datos_seguros (valores_posibles,mensaje_entrada):
    entrada_recibida = input(mensaje_entrada)
    while entrada_recibida.lower() not in valores_posibles:
        entrada_recibida = input(mensaje_entrada)
    return entrada_recibida.lower()

def obtener_razas_seguras (mensaje_entrada):
    entrada_recibida = input(mensaje_entrada)
    while not isEnano(entrada_recibida) and not isHumano(entrada_recibida) and not isElfo(entrada_recibida) and not isTeafling(entrada_recibida):
        entrada_recibida = input(mensaje_entrada)
    return entrada_recibida

def calcular_habilidad_pj (atributos_pj):
    for indice_atributo in range(len(atributos_pj)):
       for indice_habilidad in range(len(atributos_pj[indice_atributo]["habilidades"])):
            atributos_pj[indice_atributo]["habilidades"][indice_habilidad]["valor"] = modificador_pj(atributos_pj[indice_atributo]["valor"])
            if atributos_pj[indice_atributo]["habilidades"][indice_habilidad]["competencia"] == True:
                atributos_pj[indice_atributo]["habilidades"][indice_habilidad]["valor"] += 2
            atributo_habilidad_decorado = decorar_valor(atributos_pj[indice_atributo]["habilidades"][indice_habilidad]["valor"])
            print(f"{atributos_pj[indice_atributo]['habilidades'][indice_habilidad]['habilidad']}: {atributo_habilidad_decorado}")

def isTasha (variable):
    if variable in ["sí","s","si"]:
       return True
    else:
        return False

def isEnano(variable):
    return variable.lower() in ["enano","d"]
def isHumano(variable):
    return variable.lower() in ["humano","h"]
def isElfo(variable):
    return variable.lower() in ["elfo","e"]
def isTeafling(variable):
    return variable.lower() in ["tiefling","t"]

def definir_atributos(raza_pj):
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

def talentos_raza (raza_pj,talentos_pj):
    if isHumano(raza_pj):
        talentos_pj.append("[Humano (Variante)]: Elige una dote extra al crear el personaje.")
    if isElfo(raza_pj):
        talentos_pj.append("[Visión en la oscuridad]: Estás acostumbrado a la luz crepuscular de los bosques y al cielo nocturno. Puedes ver en la penumbra a una distancia de 60 pies como si fuera luz brillante y, en la oscuridad como si fuera penumbra. En la oscuridad no puedes distinguir colores, solo tonos de gris.")
        talentos_pj.append("[Linaje feérico]: Tienes ventaja en las tiradas de salvación para no quedar hechizado y no puedes quedarte dormido por ningún efecto mágico.")
        talentos_pj.append("[Trance]: Los elfos no necesitan dormir, en lugar de ello meditan profundamente y permanecen semiinconscientes durante cuatro horas al día (conocido como «trance»). Descansar de este modo te otorga los mismos beneficios que dormir ocho horas a un humano.")
    if isEnano(raza_pj):
        talentos_pj.append("[Enanismo puro]: Elige una dote extra al crear el personaje.")
    if isTeafling(raza_pj):
        talentos_pj.append("Me puedo transformar en vaca según las normas: Elige una dote extra al crear el personaje.")
    return talentos_pj
    
talentos_pj = []    
nombre_pj = input("Por favor, introduce el nombre de tu personaje: ")        
clasico_o_moderno_dados = obtener_datos_seguros(["c","m"],"Por favor decida si prefiere elegir sus atributos por estilo clásico[C] o moderno[M]: ")
raza_pj = obtener_razas_seguras("Por favor, elige tu raza: Humano [h], Elfo [e], Enano [d] o Tiefling [t]: ")
clase_pj = obtener_datos_seguros(["g","p","m"],"Por favor, elige la clase: Guerrero [g], Pícaro [p] o Mago [m]: ")
tasha = obtener_datos_seguros (["sí","no","si","s","n"],"Por favor, decide si quieres crear tu personaje usando la variante del manual de Tasha [s/n]: ")    
print(f"Nombre del pj: {nombre_pj}")

atributo_principal, atributo_secundario = definir_atributos(raza_pj)

if clasico_o_moderno_dados == "c":
    generador_3d6(atributo_principal,atributo_secundario)
else:
    generador_4d6(atributo_principal,atributo_secundario)
    
calcular_habilidad_pj(atributos_pj)
talentos_pj = talentos_raza(raza_pj,talentos_pj)
for talento in talentos_pj:
    print(talento)