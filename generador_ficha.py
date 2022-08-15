import random
from utilidades import decorar_valor,isPicaro,isGuerrero,isMago
from ficha_pj import atributos_pj, talentos_pj, definir_atributos,definir_talentos_pj,generar_habilidades_competentes, definir_competencia_clase

def modificador_pj (valor):
    return (valor-10)//2

def generador_3d6 (raza_pj,tasha):
    atributo_principal,atributo_secundario = definir_atributos(raza_pj,tasha)
    for indice in range(len(atributos_pj)):
        atributos_pj[indice]["valor"] = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
        if atributos_pj[indice]["atributo"] == atributo_principal:
            atributos_pj[indice]["valor"] +=2
        if atributos_pj[indice]["atributo"] == atributo_secundario:
            atributos_pj[indice]["valor"] +=1
        atributos_pj[indice]["modificador"] = modificador_pj(atributos_pj[indice]["valor"])
        atributos_pj[indice]["modificador"] = decorar_valor(atributos_pj[indice]["modificador"])
        print (f"{atributos_pj[indice]['atributo']}: {atributos_pj[indice]['valor']} ({atributos_pj[indice]['modificador']})")
        
def generador_4d6 (raza_pj,tasha):
    atributo_principal,atributo_secundario = definir_atributos(raza_pj,tasha)
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
         
def calcular_habilidad_pj (atributos_pj):
    for indice_atributo in range(len(atributos_pj)):
       for indice_habilidad in range(len(atributos_pj[indice_atributo]["habilidades"])):
            atributos_pj[indice_atributo]["habilidades"][indice_habilidad]["valor"] = modificador_pj(atributos_pj[indice_atributo]["valor"])
            if atributos_pj[indice_atributo]["habilidades"][indice_habilidad]["competencia"] == True:
                atributos_pj[indice_atributo]["habilidades"][indice_habilidad]["valor"] += 2
            atributo_habilidad_decorado = decorar_valor(atributos_pj[indice_atributo]["habilidades"][indice_habilidad]["valor"])
            print(f"{atributos_pj[indice_atributo]['habilidades'][indice_habilidad]['habilidad']}: {atributo_habilidad_decorado}")

def generar_ficha(clasico_o_moderno_dados,raza_pj,tasha,clase_pj,habilidades_competentes_clase,estilo_combate,pericias_picaro):
    if clasico_o_moderno_dados == "c":
       generador_3d6(raza_pj,tasha)
    else:
       generador_4d6(raza_pj,tasha)
    calcular_habilidad_pj(atributos_pj)
    definir_competencia_clase(clase_pj,habilidades_competentes_clase)
    definir_talentos_pj(raza_pj,clase_pj,talentos_pj,estilo_combate,pericias_picaro)
    for talento in talentos_pj:
        print (talento)
    
def obtener_competencias_y_especiales (clase_pj):
    lista_habilidades = generar_habilidades_competentes(clase_pj)
    lista_pericias_picaro = ["Acrobacias", "Atletismo", "Engañar", "Interpretación", "Intimidar", "Investigación", "Juego de manos", "Percepción", "Perspicacia", "Persuasión", "Sigilo","competencia con herramientas de ladrón"]
    competencias_seleccionadas = []
    competencias_elegidas = 1
    numero_competencias = 2
    estilo_combate = 0
    pericia_picaro = []
    if isPicaro(clase_pj):
        numero_competencias = 4
    while competencias_elegidas <= numero_competencias:
        for habilidad in lista_habilidades:
            print(f"[{lista_habilidades.index(habilidad)}]{habilidad}")
        competencias_input = input("\nDe esta lista de habilidades tienes que elegir {numero_competencias}. No puedes repetir la habilidad. Escribe el número correspondiente: ")
        competencias_seleccionadas.append(competencias_input)
        lista_habilidades[int(competencias_input)] = ""
        competencias_elegidas += 1
    if isGuerrero(clase_pj):
        estilo_combate = int(input("Al ser guerrero debes elegir un estilo de combate de entre los siguientes.\n[1] Combate con armas grandes\n[2] Combate con dos armas\n[3] Defensa\n[4] Duelo\n[5] Protección\n[6] Tiro al blanco\nEscribe el número del estilo que eliges: "))
    elif isPicaro(clase_pj):
       while len(pericia_picaro) < 2:
             for pericia in lista_pericias_picaro:
                 print(f"[{lista_pericias_picaro.index(pericia)}]{pericia}")
             pericia_picaro_input = int(input("Al ser pícaro, dos de tus competencias (o tu competencia con herramientas de ladrón) serán pericias, es decir, duplicarán su competencia. Elige escribiendo un número cada vez y no lo repitas: "))
             pericia_picaro.append(pericia_picaro_input)
             lista_pericias_picaro[pericia_picaro_input] = ""
    return competencias_seleccionadas,estilo_combate,pericia_picaro
        
    
        