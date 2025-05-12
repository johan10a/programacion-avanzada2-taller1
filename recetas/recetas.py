# R1: pedir el número de porciones
def pedir_datos():
    return -1
  

# R2: calcular la cantidad de los ingredientes
def calcular_ingredientes(porciones):
    if porciones <= 0 or porciones % 4 != 0:
        return (0.0, 0.0, 0.0, 0.0)

    unidades = porciones // 4
    harina = 225.0 * unidades
    huevos = 1.0 * unidades
    azucar = 100.0 * unidades
    mantequilla = 200.0 * unidades

    return (harina, huevos, azucar, mantequilla)

# R3: mostrar los ingredientes necesarios
def mostrar_resultados (porciones, ingredientes):
    print("ok")

