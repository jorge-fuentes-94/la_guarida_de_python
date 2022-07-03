import os
import random
os.system("cls")

nombre_pj = input("Por favor, introduce el nombre de tu personaje: ")
atributos_pj = [0,0,0,0,0,0]
nombre_atributos_pj = ["Fuerza","Destreza","Constitución","Inteligencia","Sabiduría","Carisma"]

def modificador_pj (valor):
    return (valor-10)//2

def generador_3d6 ():
    for indice in range(6):
        atributos_pj[indice] = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
        modificador_attr=modificador_pj(atributos_pj[indice])
        if modificador_attr >= 0:
            modificador_attr = f"+{modificador_attr}"
        print (f"{nombre_atributos_pj[indice]}: {atributos_pj[indice]} ({modificador_attr})")
        
def generador_4d6 ():
    for indice in range(6):
         cuatrod6 = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
         cuatrod6.remove (min(cuatrod6))
         tresd6 = cuatrod6
         atributos_pj[indice]=tresd6[0]+tresd6[1]+tresd6[2]
         modificador_attr=modificador_pj(atributos_pj[indice])
         if modificador_attr >= 0:
            modificador_attr = f"+{modificador_attr}"
         print (f"{nombre_atributos_pj[indice]}: {atributos_pj[indice]} ({modificador_attr})")



clasico_o_moderno_dados = ""
while clasico_o_moderno_dados not in ["C","c","M","m"]:
    clasico_o_moderno_dados = input("Por favor decida si prefiere elegir sus atributos por estilo clásico[C] o moderno[M]: ")
    if clasico_o_moderno_dados == "C" or clasico_o_moderno_dados=="c":
        print(f"Nombre del pj: {nombre_pj}")
        generador_3d6()
    elif clasico_o_moderno_dados == "M" or clasico_o_moderno_dados == "m":
        print(f"Nombre del pj: {nombre_pj}")
        generador_4d6()
        