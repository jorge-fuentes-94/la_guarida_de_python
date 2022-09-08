from raza import Humano,Elfo,Enano,Tiefling

class Clase():
    def __init__(self, personaje_con_raza):
        self._personaje = personaje_con_raza
        self._raza = personaje_con_raza.getRaza()
        self._talentos_pj = personaje_con_raza.getTalentos()
    def __str__(self):
           return self.get_ficha_de_personaje()
    def get_ficha_de_personaje(self):
           decoración = "----------------------\n"
           ficha =  f"Mi nombre es {self._personaje.getNombre()}.\n"
           ficha += f"Mi raza es {self._raza}.\n"
           ficha += f"Mi clase es {self._clase}.\n"
           ficha += decoración
           for atributo in self._personaje.getAtributos().values():
                   ficha += f"- {atributo}"
           ficha += decoración
           for habilidad in self._personaje.getHabilidades().values():
                   ficha += f"- {habilidad}"
           ficha += decoración
           for talento in self._talentos_pj:
                   ficha += f"{talento}\n"
           ficha += decoración
           return ficha 
    @classmethod
    def getHabilidadesCompetentes(self):
        return self._lista_habilidades_competentes
    
    

class Guerrero(Clase):
        _lista_habilidades_competentes = ["Acrobacias","Atletismo","Historia","Intimidar","Percepción","Perspicacia","Supervivencia","Trato con animales"]
        _lista_estilo_combate = ["[Combate con armas grandes]:Cuando saques 1 o 2 en un dado de daño de un ataque que realices con un arma cuerpo a cuerpo que empuñes con las dos manos, puedes volver a tirarlo, pero debes usar el nuevo resultado, incluso si es 1 o 2. El arma debe tener la propiedad «dos manos» o «versátil» para que puedas obtener este beneficio.","[Combate con dos armas]:Cuando luchas con dos armas, puedes añadir tu modificador por característica al daño del segundo ataque.","[Defensa]:Mientras llevas armaduras, recibes un bonificador de +1 a tu CA.","[Duelo]:Cuando solo empuñas un arma cuerpo a cuerpo en una mano, ganas un bonificador de +2 a las tiradas de daño que hagas con ella.","[Protección]:Cuando una criatura que puedas ver ataque a un objetivo que no eres tú y que se encuentre a 5 pies de ti, puedes usar tu reacción para imponerle desventaja en la tirada de ataque. Debes llevar un escudo.","[Tiro al blanco]:Consigues un bonificador de +2 a las tiradas de ataque que hagas con armas a distancia."]
        _clase = "Guerrero"
        def __init__(self, personaje_con_raza, competencia1, competencia2,estilo_de_combate):
               super().__init__(personaje_con_raza)
               self._personaje.set_competencia(competencia1,2)
               self._personaje.set_competencia(competencia2,2)
               self._estilo_de_combate = estilo_de_combate
               self._talentos_pj.append("[Tomar aliento]: Dispones de una fuente ilimitada de vitalidad a la que puedes recurrir para protegerte del daño. Durante tu turno, puedes usar una acción adicional para recuperar un número de puntos de golpe igual a 1d10 + tu nivel de guerrero. Una vez usas este rasgo, debes terminar un descanso corto o largo antes de poder usarlo otra vez.")
               self._talentos_pj.append(f"{self.get_lista_estilo_combate(estilo_de_combate)}")
               
        def get_lista_estilo_combate(self,estilo_de_combate):
                   return self._lista_estilo_combate[estilo_de_combate] 
        def getClase(self):
            return self._clase 
             
class Picaro(Clase):
        _lista_habilidades_competentes = ["Acrobacias","Atletismo","Engañar","Interpretación","Intimidar","Investigación","Juego de manos","Percepción","Perspicacia","Persuasión","Sigilo"]
        _clase = "Pícaro"
        def __init__(self, personaje_con_raza, competencia1, competencia2,competencia3,competencia4,pericia1,pericia2):
               super().__init__(personaje_con_raza)
               self._personaje.set_competencia(competencia1,2)
               self._personaje.set_competencia(competencia2,2)
               self._personaje.set_competencia(competencia3,2)
               self._personaje.set_competencia(competencia4,2)
               self._talentos_pj.append("[Ataque furtivo]: Sabes aprovechar la distracción de un enemigo para atacarlo por la espalda. Una vez por turno, puedes infligir daño adicional a una criatura a la que impactes con un ataque si tienes ventaja en la tirada de ataque. El ataque debe usar un arma sutil o a distancia. Este rasgo funciona aunque no tengas ventaja en la tirada de ataque si otro enemigo del objetivo no incapacitado está a menos de 5 pies de él y si tú no tienes desventaja en la tirada de ataque. La cantidad de daño adicional aumenta conforme subes de nivel en esta clase.")
               self._talentos_pj.append("[Jerga de ladrones]: Durante tu entrenamiento como pícaro, aprendes la jerga de ladrones, una mezcla de dialecto, argot y código secretos que te permite enviar mensajes en una conversación aparentemente normal. Solo otra criatura que conozca la germanía puede entender tales mensajes. Transmitir un mensaje de este tipo cuesta cuatro veces más que decir la misma idea directamente. Además, entiendes una serie de signos y símbolos que se usan para esconder mensajes cortos y sencillos, como si un área es peligrosa o es territorio de un gremio de ladrones, si hay un botín cerca o si las gentes que viven en la zona son presas fáciles u ofrecerán cobijo a un ladrón a la fuga.")
               self._talentos_pj.append(f"[Pericia]: Tus dos siguientes competencias duplican el bono de competencia al usarse: {pericia1} y {pericia2}.")
               
        def getClase(self):
            return self._clase      
               
class Mago(Clase):
        _lista_habilidades_competentes = ["Arcano","Historia","Investigación","Medicina","Perspicacia","Religión"]
        _clase = "Mago"
        def __init__(self, personaje_con_raza, competencia1, competencia2):
               super().__init__(personaje_con_raza)
               self._personaje.set_competencia(competencia1,2)
               self._personaje.set_competencia(competencia2,2)
               self._talentos_pj.append("[Libro de conjuros]: Como estudiante de magia arcana, tienes un libro de conjuros que contiene conjuros que muestran los primeros destellos del verdadero poder.")
               self._talentos_pj.append("[Lanzamiento ritual]: Puedes lanzar cualquier conjuro de mago como si fuera un ritual si tiene la etiqueta «ritual» y si lo tienes en tu libro de conjuros. No necesitas tener el conjuro preparado.")
               self._talentos_pj.append("[Recuperación arcana]: Has aprendido a recuperar parte de tu energía arcana estudiando tu libro de conjuros. Una vez por día, cuando hagas un descanso breve, puedes recuperar espacios de conjuro. Los espacios de conjuro pueden tener un nivel combinado igual o menor que la mitad de tu nivel de mago (redondeando hacia arriba) y, como máximo, nivel 5. Por ejemplo, si eres un mago de nivel 4, puedes recuperar hasta un valor de dos niveles de espacios de conjuro. Puedes recuperar un espacio de conjuro de nivel 2 o dos espacios de conjuro de nivel 1.")
        def getClase(self):
            return self._clase 
    
eduardo = Guerrero(Humano("Eduardo",True),"Acrobacias","Atletismo",1)
Manuela = Mago(Enano("Manuela",False),"Arcano","Historia")
Iñigo = Picaro(Tiefling("Iñigo",True),"Acrobacias","Sigilo","Perspicacia", "Percepción","Herramientas de Ladrón","Sigilo")
print (eduardo.get_ficha_de_personaje())
print(Manuela.get_ficha_de_personaje())
print(Iñigo.get_ficha_de_personaje())

