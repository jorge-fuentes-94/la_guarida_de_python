class Vehiculo:
    _numero_de_ruedas = 4
    _arrancado = False
    _velocidad = 0
    _velocidad_máxima = 120
    _direccion = "delante"
    _color = ""
    def __init__ (self,color):
        self._color = color
    def arrancar (self):
        print("¡Burrumm Burummm!")
        self._arrancado = True
    def check_arrancado(self):
        if not self._arrancado:
            raise Exception("Tienes que arrancar el vehículo.") 
    def isArrancado (self):
        return self._arrancado
    def acelerar(self,velocidad):
        self.check_arrancado()
        self._velocidad += velocidad
        if self._velocidad >= self._velocidad_máxima:
            self._velocidad = self._velocidad_máxima
    def frenar(self,velocidad):
        self._velocidad -= velocidad
        if self._velocidad <= 0:
            self._velocidad = 0
    def getVelocidad (self):
        return self._velocidad
    def getColor(self):
        return self._color

class Coche(Vehiculo):
    def tirar_de_freno_de_mano(self):
        self._velocidad = 0
    def marcha_atras(self):
        if self._velocidad != 0:
            raise Exception("El vehículo tiene que estar parado para poner la marcha atrás.")
        else:
            self._direccion = "atrás"
            
class Moto(Vehiculo):
    _numero_de_ruedas = 2
    _velocidad_máxima = 90
    def hincar_rodilla(self):
        self.check_arrancado()
        print("Cuidado muchacho, que te vas a hacer daño.")
        
hyundai = Coche ("rojo")
hyundai.arrancar() #Esto es el equivalente a arrancar (hyundai)   
print(hyundai.isArrancado())
print(hyundai.getColor())
print(hyundai._velocidad_máxima)

seat_ibiza = Coche("azul")
triumph = Moto("azul")
triumph.arrancar()
triumph.hincar_rodilla()


