def leerMatriz(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    entorno = []
    for line in lines:
        row = [int(char) for char in line.strip()]
        entorno.append(row)
    return entorno

# Leer la matriz del archivo
entorno = leerMatriz("agenteReflejoSimple/entorno.txt")

acciones = {
    'irArriba': (-1, 0),
    'irAbajo': (1, 0),
    'irIzquierda': (0, -1),
    'irDerecha': (0, 1),
    'tomarQueso': (0, 0)
}

posicionInicial_raton = (1,0)  

def obtenerSensores(entorno, posicionInicial_raton):
    x, y = posicionInicial_raton
    sensorIzquierdo = 1 if (y > 0 and entorno[x][y - 1] == 0) else 0
    sensorArriba = 1 if (x > 0 and entorno[x - 1][y] == 0) else 0
    sensorDerecho = 1 if (y < len(entorno[0]) - 1 and entorno[x][y + 1] == 0) else 0
    sensorAbajo = 1 if (x < len(entorno) - 1 and entorno[x + 1][y] == 0) else 0
    hueleQueso = 1 if entorno[x][y] == 3 else 0
    return sensorIzquierdo, sensorArriba, sensorDerecho, sensorAbajo, hueleQueso

def tomarDecision(lecturasSensores):
    sensorIzquierdo, sensorArriba, sensorDerecho, sensorAbajo, hueleQueso = lecturasSensores

    if hueleQueso:
        return 'tomarQueso'
    
    if (
        sensorArriba == 0 and
        sensorAbajo == 0 and
        sensorDerecho == 0 and
        sensorIzquierdo == 0 and 
        hueleQueso == 0 
    ):
        return 'irArriba'
    
    if (
        sensorArriba == 0 and
        sensorAbajo == 1 and
        sensorDerecho == 0 and 
        sensorIzquierdo == 0 and 
        hueleQueso == 0 
    ):
        return 'irArriba'
    
    if (
        sensorArriba == 0 and
        sensorAbajo == 0 and
        sensorIzquierdo == 0 and 
        sensorDerecho == 1 and
        hueleQueso == 0 
    ):
        return 'irArriba'
    
    if (
        sensorIzquierdo == 0 and 
        sensorArriba == 0 and
        sensorDerecho == 1 and
        sensorAbajo == 1 and
        hueleQueso == 0 
    ):
        return 'irArriba'
    
    if (
        sensorIzquierdo == 0 and 
        sensorArriba == 1 and
        sensorDerecho == 0 and
        sensorAbajo == 0 and
        hueleQueso == 0 
    ):
        return 'irIzquierda'
    
    if (
        sensorIzquierdo == 0 and 
        sensorArriba == 1 and
        sensorDerecho == 0 and
        sensorAbajo == 1 and
        hueleQueso == 0 
    ):
        return 'irDerecha'
    
    if (
        sensorIzquierdo == 0 and 
        sensorArriba == 1 and
        sensorDerecho == 1 and
        sensorAbajo == 0 and
        hueleQueso == 0 
    ):
        return 'irIzquierda'
    
    if (
        sensorIzquierdo == 0 and 
        sensorArriba == 1 and
        sensorDerecho == 1 and
        sensorAbajo == 1 and
        hueleQueso == 0 
    ):
        return 'irIzquierda'
    
    if (
        sensorIzquierdo == 1 and 
        sensorArriba == 0 and
        sensorDerecho == 0 and
        sensorAbajo == 0 and
        hueleQueso == 0 
    ):
        return 'irArriba'
    
    if (
        sensorIzquierdo == 1 and 
        sensorArriba == 0 and
        sensorDerecho == 0 and
        sensorAbajo == 1 and
        hueleQueso == 0 
    ):
        return 'irDerecha'
    if (
        sensorIzquierdo == 1 and 
        sensorArriba == 0 and
        sensorDerecho == 1 and
        sensorAbajo == 0 and
        hueleQueso == 0 
    ):
        return 'irAbajo'
    if (
        sensorIzquierdo == 1 and 
        sensorArriba == 0 and
        sensorDerecho == 1 and
        sensorAbajo == 1 and
        hueleQueso == 0 
    ):
        return 'irArriba'
    if (
        sensorIzquierdo == 1 and 
        sensorArriba == 1 and
        sensorDerecho == 0 and
        sensorAbajo == 0 and
        hueleQueso == 0 
    ):
        return 'irDerecha'
    if (
        sensorIzquierdo == 1 and 
        sensorArriba == 1 and
        sensorDerecho == 0 and
        sensorAbajo == 1 and
        hueleQueso == 0 
    ):
        return 'irDerecha'
    if (
        sensorIzquierdo == 1 and 
        sensorArriba == 1 and
        sensorDerecho == 1 and
        sensorAbajo == 0 and
        hueleQueso == 0 
    ):
        return 'irAbajo'
        
    return 'tomarQueso'
    
def moverRaton(entorno, posicionInicial_raton):
   
    while True:
        lecturasSensores = obtenerSensores(entorno, posicionInicial_raton)
        decision = tomarDecision(lecturasSensores)
        
        print(f"ratón decide: {decision}")  # Imprimir la decisión actual
        
        # Verificar si el ratón ha encontrado el queso
        if decision == "tomarQueso":
            print("El ratón ha encontrado el queso!!!")
            break
        
        # Resto del código para mover el ratón
        dx, dy = acciones[decision]
        x, y = posicionInicial_raton
        nueva_x, nueva_y = x + dx, y + dy
        
        if (
            0 <= nueva_x < len(entorno) and 0 <= nueva_y < len(entorno[0]) and entorno[nueva_x][nueva_y] != 1
        ):
            posicionInicial_raton = (nueva_x, nueva_y)
# Iniciar la simulación
moverRaton(entorno, posicionInicial_raton)