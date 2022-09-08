import random

class Atributo:
    _nombre = ""
    _valor = 0
    
    def __init__(self,nombre,clasico_o_moderno):
        self._nombre = nombre
        if clasico_o_moderno == True:
           self._valor = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
        else:
            cuatrod6 = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
            cuatrod6.remove (min(cuatrod6))
            self._valor = cuatrod6[0] + cuatrod6[1] + cuatrod6[2]
    
    def __str__(self):
        modificador = ""
        if self.obtener_mod() >= 0:
            modificador = "+"
        return f"{self._nombre}: {self._valor} ({modificador}{self.obtener_mod()})\n"
    
    def chequear(self):
        return self._tirada_d20() + self._obtener_mod(self)
    
    def _tirada_d20(self):
        return random.randint(1,20)
    
    def obtener_mod (self):
        return (self._valor -10)//2
    
    def obtener_siglas(self):
        siglas = self._nombre[0:3] 
        return siglas.upper()