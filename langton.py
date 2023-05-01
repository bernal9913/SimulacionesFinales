import turtle

def langton():
    # iniciar la ventana
    window = turtle.Screen()
    window.bgcolor('white')
    window.screensize(1000,1000)

    # contiene las coordenadas y el color
    maps = {}

    # iniciar al mochomo
    ant = turtle.Turtle()

    # forma de la hormiga
    ant.shape('square')
    # tamaño de la hormiga
    ant.shapesize(0.5)
    # velocidad de la hormiga
    ant.speed(0)

    #obtiene las coordenadas de la hormiga
    pos = coordinate(ant)

    # Inicializa el contador de pasos
    steps = 0
    while True:
        # distancia que se moverla la hormiga
        step = 10

        if pos not in maps or maps[pos] == "white":
            # invierte el color
            ant.fillcolor("black")
            # dibujar hormiga
            ant.stamp()
            invert(maps, ant, "black")
            ant.right(90)
            # mueve la hormiga hacia delante
            ant.forward(step)
            pos = coordinate(ant)

        elif maps[pos] == "black":
            ant.fillcolor("white")
            invert(maps,ant,"white")
            ant.stamp()
            ant.left(90)
            ant.forward(step)
            pos = coordinate(ant)

        # Incrementa el contador de pasos
        steps += 1

        # Imprime el número de pasos cada 1000 iteraciones
        if steps % 1000 == 0:
            print(f"Steps: {steps}")

def invert(graph, ant, color):
    graph[coordinate(ant)] = color
def coordinate(ant):
    return (round(ant.xcor()), round(ant.ycor()))

langton()
'''
simplicidad, caos y orden emergente 
pasos <100 = patrones sencillos y simetricos
pasos > 100 = patron grande e irregular
paso > 10,000 = el camino raro de 104 pasos indefinido
'''