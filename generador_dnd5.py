# Persistencia ahora mismo no termina de funcionar, no guarda las fichas de manera correcta.
import os
# from persistencia import persistir,obtener_supervivencia,comprobar_existencia_archivo
from generador_ficha import atributos_pj, generar_ficha
from utilidades import obtener_datos_seguros,obtener_razas_seguras
os.system("cls")
      
  
nombre_pj = input("Por favor, introduce el nombre de tu personaje: ")
#nombre_archivo = f"Ficha de personaje - {nombre_pj}.json"
#archivo_ya_existe = comprobar_existencia_archivo(nombre_archivo)
#if not archivo_ya_existe: 
clasico_o_moderno_dados = obtener_datos_seguros(["c","m"],"Por favor decida si prefiere elegir sus atributos por estilo clásico[C] o moderno[M]: ")
raza_pj = obtener_razas_seguras("Por favor, elige tu raza: Humano [h], Elfo [e], Enano [d] o Tiefling [t]: ")
clase_pj = obtener_datos_seguros(["g","p","m"],"Por favor, elige la clase: Guerrero [g], Pícaro [p] o Mago [m]: ")
tasha = obtener_datos_seguros (["sí","no","si","s","n"],"Por favor, decide si quieres crear tu personaje usando la variante del manual de Tasha [s/n]: ")    

generar_ficha (clasico_o_moderno_dados,raza_pj,tasha,clase_pj)

     
#    persistir(nombre_pj,atributos_pj,talentos_pj,nombre_archivo)

#supervivencia = obtener_supervivencia(nombre_archivo)
#print(f"La supervivencia del personaje es {decorar_valor(supervivencia)}")




    

    
