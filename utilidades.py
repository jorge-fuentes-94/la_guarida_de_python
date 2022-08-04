def decorar_valor(valor):
    if valor >= 0:
            valor = f"+{valor}"
    return str(valor)

def obtener_datos_seguros (valores_posibles,mensaje_entrada):
    entrada_recibida = input(mensaje_entrada)
    while entrada_recibida.lower() not in valores_posibles:
        entrada_recibida = input(mensaje_entrada)
    return entrada_recibida.lower()

def isEnano(variable):
    return variable.lower() in ["enano","d"]
def isHumano(variable):
    return variable.lower() in ["humano","h"]
def isElfo(variable):
    return variable.lower() in ["elfo","e"]
def isTeafling(variable):
    return variable.lower() in ["tiefling","t"]
def isMago(variable):
    return variable.lower() in ["mago","m"]
def isGuerrero(variable):
    return variable.lower() in ["guerrero","g"]
def isPicaro(variable):
    return variable.lower() in ["picaro","p"]

def obtener_razas_seguras (mensaje_entrada):
    entrada_recibida = input(mensaje_entrada)
    while not isEnano(entrada_recibida) and not isHumano(entrada_recibida) and not isElfo(entrada_recibida) and not isTeafling(entrada_recibida):
        entrada_recibida = input(mensaje_entrada)
    return entrada_recibida

def isTasha (variable):
    if variable in ["sí","s","si"]:
       return True
    else:
        return False