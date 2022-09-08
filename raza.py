from personaje import Personaje

class Humano(Personaje):
    def __init__(self,nombre, clasico_o_moderno):
        super().__init__(nombre,clasico_o_moderno)
        self._raza = "Humano"
        self._talentos_pj.append("[Humano (Variante)]: Elige una dote extra al crear el personaje.")
    
    def getRaza(self):
        return self._raza
        
class Enano(Personaje):
    def __init__(self,nombre, clasico_o_moderno):
        super().__init__(nombre,clasico_o_moderno)
        self._raza = "Enano"
        self._talentos_pj.append("[Visión en la oscuridad]: Estás acostumbrado a la luz crepuscular de los bosques y al cielo nocturno. Puedes ver en la penumbra a una distancia de 60 pies como si fuera luz brillante y, en la oscuridad como si fuera penumbra. En la oscuridad no puedes distinguir colores, solo tonos de gris.")
        self._talentos_pj.append("[Fortaleza enana]: Tienes ventaja en las tiradas de salvación contra venenos y eres resistente al daño por veneno.")
        self._talentos_pj.append("[Afinidad con la piedra]: uando realices una prueba de Inteligencia (Historia) relacionada con el origen de una obra de mampostería, se considera que tienes competencia con la habilidad de Historia y añades a la prueba tu bonificador por competencia multiplicado por 2 en lugar del bonificador habitual.x")
    
    def getRaza(self):
        return self._raza

class Elfo(Personaje):
    def __init__(self,nombre, clasico_o_moderno):
        super().__init__(nombre,clasico_o_moderno)
        self._raza = "Elfo"
        self._talentos_pj.append("[Visión en la oscuridad]: Estás acostumbrado a la luz crepuscular de los bosques y al cielo nocturno. Puedes ver en la penumbra a una distancia de 60 pies como si fuera luz brillante y, en la oscuridad como si fuera penumbra. En la oscuridad no puedes distinguir colores, solo tonos de gris.")
        self._talentos_pj.append("[Linaje feérico]: Tienes ventaja en las tiradas de salvación para no quedar hechizado y no puedes quedarte dormido por ningún efecto mágico.")
        self._talentos_pj.append("[Trance]: Los elfos no necesitan dormir, en lugar de ello meditan profundamente y permanecen semiinconscientes durante cuatro horas al día (conocido como «trance»). Descansar de este modo te otorga los mismos beneficios que dormir ocho horas a un humano.")
        self._talentos_pj.append("[Truco]: Conoces un truco de tu elección de la lista de conjuros de mago. La característica que usas para lanzarlo es Inteligencia.")
    
    def getRaza(self):
        return self._raza
        
class Tiefling(Personaje):
    def __init__(self,nombre, clasico_o_moderno):
        super().__init__(nombre,clasico_o_moderno)
        self._raza = "Tiefling"
        self._talentos_pj.append("[Visión en la oscuridad]: Estás acostumbrado a la luz crepuscular de los bosques y al cielo nocturno. Puedes ver en la penumbra a una distancia de 60 pies como si fuera luz brillante y, en la oscuridad como si fuera penumbra. En la oscuridad no puedes distinguir colores, solo tonos de gris.")
        self._talentos_pj.append("[Resistencia infernal]: Tienes resistencia al daño por fuego.")
        self._talentos_pj.append("[Legado infernal]: Conoces el truco Taumaturgia. Cuando alcanzas el nivel 3, puedes lanzar el conjuro Represión infernal como un conjuro de nivel 2 una vez con este rasgo y volver a utilizarlo cuando completes un descanso prolongado. Cuando alcanzas el nivel 5, puedes lanzar el conjuro Oscuridad una vez con este rasgo y volver a utilizarlo cuando completes un descanso prolongado. La característica con la que lanzas estos conjuros es Carisma.")
    
    def getRaza(self):
        return self._raza    
        