import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

ppt=["piedra","papel","tijeras"]
ronda = 0
jugador_gana=0
maquina_gana=0

while True:
   

    jugador = str(input("ingresa piedra, papel o tijeras o s para terminar:   "))
    
    
       #print("esto indica el jugador: " + str(jugador))

    if jugador.lower() == "s":
       print(" --- >> Termina programa <<< --- ")
       break

    maquina=ppt[random.randint(0,len(ppt)-1)]
    #print("maquina dice: " +  str(maquina))

    print("################################################################")
    ronda = ronda + 1
    print("Esta es la ronda número: " + str(ronda))

    print( "<<<< JUGADOR >>>> ", jugador , " VS "  , maquina, "<<<< MAQUINA >>>>" )
    if jugador == "piedra": 
      img = mpimg.imread("/Users/aki/Desktop/varios_python/piedra.png")
      imgplot = plt.imshow(img)
      plt.show()
    elif jugador == "papel":
      img = mpimg.imread("/Users/aki/Desktop/varios_python/papel.jpg")
      imgplot = plt.imshow(img)
      plt.show()
    else:
      img = mpimg.imread("/Users/aki/Desktop/varios_python/tijeras.png")
      imgplot = plt.imshow(img)
      plt.show()
    print("################################################################")

    if ((jugador == "piedra" and maquina.lower() == "piedra" ) or (jugador == "papel" and maquina.lower() == "papel" ) or (jugador == "tijeras" and maquina.lower() == "tijeras")):
          print("****   EEEMMPAATTEE!!!  ****" )
          
    elif (jugador == "piedra" and maquina.lower() == "tijeras") or (jugador == "papel" and maquina.lower() == "piedra") or (jugador == "tijeras" and maquina.lower() == "papel"):
          print("En esta ronda gana jugador" )
          jugador_gana=jugador_gana + 1

    else: #(maquina == "piedra" and jugador == "tijeras") or (maquina == "papel" and jugador == "piedra") or (maquina == "tijeras" and jugador== "papel"):
     print("En esta ronda gana máquina" )
     maquina_gana=maquina_gana + 1
    
   
    if (maquina_gana == 2):
     print(">>>  MAQUINA GANADORA!!! <<<< " )
     img = mpimg.imread("/Users/aki/Desktop/varios_python/pc_gana.jpg")
     imgplot = plt.imshow(img)
     plt.show()
     break
    else: 
       if (jugador_gana == 2):
        print("****  JUGADOR GANADOR!!! ****** ")
        img = mpimg.imread("/Users/aki/Desktop/varios_python/user_gana.png")
        imgplot = plt.imshow(img)
        plt.show()
        break
       else: 
          print("siguiente ronda")
