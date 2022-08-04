import random
from utilidades import decorar_valor
from ficha_pj import atributos_pj, talentos_pj, definir_atributos,definir_talentos_pj

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

def generar_ficha(clasico_o_moderno_dados,raza_pj,tasha,clase_pj):
    if clasico_o_moderno_dados == "c":
       generador_3d6(raza_pj,tasha)
    else:
       generador_4d6(raza_pj,tasha)
    calcular_habilidad_pj(atributos_pj)
    definir_talentos_pj(raza_pj,talentos_pj)
    for talento in talentos_pj:
        print (talento)
    