import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

ppt = ["piedra", "papel", "tijeras"]
ronda = 0
jugador_gana = 0
maquina_gana = 0

while True:
    jugador = str(input("Ingresa piedra, papel o tijeras o 's' para terminar:   "))

    if jugador.lower() == "s":
        print(" --- >> Termina programa <<< --- ")
        break

    maquina = ppt[random.randint(0, len(ppt) - 1)]

    print("################################################################")
    ronda += 1
    print("Esta es la ronda número: " + str(ronda))
    print("<<<< JUGADOR >>>> ", jugador, " VS ", maquina, "<<<< MAQUINA >>>>")

    # Mostrar imagen del jugador
    if jugador == "piedra":
        img = mpimg.imread("/Users/aki/Desktop/varios_python/piedra.png")
    elif jugador == "papel":
        img = mpimg.imread("/Users/aki/Desktop/varios_python/papel.jpg")
    else:
        img = mpimg.imread("/Users/aki/Desktop/varios_python/tijeras.png")
    
    imgplot = plt.imshow(img)
    plt.axis('off')  # Ocultar ejes
    plt.title("Jugador: " + jugador)
    plt.show()

    # Mostrar imagen de la máquina
    if maquina == "piedra":
        img = mpimg.imread("/Users/aki/Desktop/varios_python/piedra.png")
    elif maquina == "papel":
        img = mpimg.imread("/Users/aki/Desktop/varios_python/papel.jpg")
    else:
        img = mpimg.imread("/Users/aki/Desktop/varios_python/tijeras.png")
    
    imgplot = plt.imshow(img)
    plt.axis('off')  # Ocultar ejes
    plt.title("Máquina: " + maquina)
    plt.show()

    print("################################################################")

    if ((jugador == "piedra" and maquina.lower() == "piedra") or
        (jugador == "papel" and maquina.lower() == "papel") or
        (jugador == "tijeras" and maquina.lower() == "tijeras")):
        print("****   EEEMMPAATTEE!!!  ****")
        
    elif ((jugador == "piedra" and maquina.lower() == "tijeras") or
          (jugador == "papel" and maquina.lower() == "piedra") or
          (jugador == "tijeras" and maquina.lower() == "papel")):
        print("En esta ronda gana jugador")
        jugador_gana += 1

    else:
        print("En esta ronda gana máquina")
        maquina_gana += 1

    if maquina_gana == 2:
        print(">>>  MAQUINA GANADORA!!! <<<< ")
        img = mpimg.imread("/Users/aki/Desktop/varios_python/pc_gana.jpg")
        imgplot = plt.imshow(img)
        plt.axis('off')  # Ocultar ejes
        plt.show()
        break
    elif jugador_gana == 2:
        print("****  JUGADOR GANADOR!!! ****** ")
        img = mpimg.imread("/Users/aki/Desktop/varios_python/user_gana.png")
        imgplot = plt.imshow(img)
        plt.axis('off')  # Ocultar ejes
        plt.show()
        break
    else:
        print("Siguiente ronda")