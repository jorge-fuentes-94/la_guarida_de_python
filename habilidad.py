class Habilidad:
    _nombre = ""
    
    def __init__(self,nombre,atributo, competencia):
        self._nombre = nombre
        self._atributo = atributo
        self._competencia = competencia
    
    def __str__(self):
        valor_habilidad = self._atributo.obtener_mod() + self._competencia
        simbolo_competencia = "○"
        if self._competencia > 0:
            simbolo_competencia = "●"
        return f"{simbolo_competencia} {self._nombre} ({self._atributo.obtener_siglas()}): {valor_habilidad}\n"
        
    def chequear(self):
        return self._atributo.chequear() + self._competencia
    
    def set_competencia(self,competencia):
        self._competencia = competencia
        
    def getNombre(self):
        return self._nombre
    