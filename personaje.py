from atributo import Atributo
from habilidad import Habilidad

class Personaje:
    _nombre = ""
    _atributos = {}
    _habilidades = {}

    def __init__(self,nombre,clasico_o_moderno):
        self._nombre = nombre
        self._atributos ["Fuerza"] = Atributo("Fuerza",clasico_o_moderno)
        self._atributos ["Destreza"] = Atributo("Destreza",clasico_o_moderno)
        self._atributos ["Constitución"] = Atributo("Constitución",clasico_o_moderno)
        self._atributos ["Inteligencia"] = Atributo("Inteligencia",clasico_o_moderno)
        self._atributos ["Sabiduría"] = Atributo("Sabiduría",clasico_o_moderno)
        self._atributos ["Carisma"] = Atributo("Carisma",clasico_o_moderno)
        lista_fuerza = ["Atletismo"]
        for habilidad in lista_fuerza:
            self._habilidades[habilidad] = Habilidad(habilidad,self._atributos["Fuerza"],0)
        lista_destreza = ["Acrobacias","Juego_de_manos", "Sigilo"]
        for habilidad in lista_destreza:
            self._habilidades[habilidad] = Habilidad(habilidad,self._atributos["Destreza"],0)
        lista_inteligencia = ["Arcano","Historia","Investigación"]
        for habilidad in lista_inteligencia:
            self._habilidades[habilidad] = Habilidad(habilidad,self._atributos["Inteligencia"],0)
        lista_sabiduria = ["Naturaleza","Religión","Trato_con_animales","Medicina","Percepción","Perspicacia","Supervivencia"]
        for habilidad in lista_sabiduria:
            self._habilidades[habilidad] = Habilidad(habilidad,self._atributos["Sabiduría"],0)
        lista_carisma = ["Engaño","Intimidación","Interpretación","Persuasión"]
        for habilidad in lista_carisma:
            self._habilidades[habilidad] = Habilidad(habilidad,self._atributos["Carisma"],0)
        self._talentos_pj = []
    
    def Obtener_CA (self):
        pass
        
    def Chequear_habilidad (self,habilidad):
        return self._habilidades[habilidad].chequear()
    
    
    def Chequear_Atributo (self,atributo):
        return self._atributos[atributo].chequear()
    
    def set_competencia(self,habilidad,competencia):
        self._habilidades[habilidad].set_competencia(competencia)
        
    def getNombre(self):
        return self._nombre
    
    def getAtributos(self):
        return self._atributos
    
    def getAtributo(self,atributo):
        return self._atributos[atributo]
    
    def getHabilidades(self):
        habilidades_ordenadas = sorted(self._habilidades)
        diccionario_ordenado = {}
        for habilidad in habilidades_ordenadas:
            diccionario_ordenado[habilidad] = self.getHabilidad(habilidad)
        return diccionario_ordenado
    
    def getTalentos(self):
        return self._talentos_pj
        
    
    def getHabilidad(self,habilidad):
        return self._habilidades[habilidad]
        
    
