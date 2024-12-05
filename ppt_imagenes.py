import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Opciones del juego
options = ["piedra", "papel", "tijeras"]

# Función para jugar
def play(user_choice):
    computer_choice = random.choice(options)
    user_label.config(image=images[user_choice])
    computer_label.config(image=images[computer_choice])
    
    if user_choice == computer_choice:
        result = "¡Es un empate!"
    elif (user_choice == "piedra" and computer_choice == "tijeras") or \
         (user_choice == "papel" and computer_choice == "piedra") or \
         (user_choice == "tijeras" and computer_choice == "papel"):
        result = "¡Ganaste!"
    else:
        result = "¡Perdiste!"
    
    messagebox.showinfo("Resultado", result)

# Crear la ventana principal
root = tk.Tk()
root.title("Piedra, Papel o Tijeras")

# Cargar imágenes
images = {
    "piedra": ImageTk.PhotoImage(Image.open("/Users/aki/Desktop/varios_python/piedra.png")),
    "papel": ImageTk.PhotoImage(Image.open("/Users/aki/Desktop/varios_python/papel.jpg")),
    "tijeras": ImageTk.PhotoImage(Image.open("/Users/aki/Desktop/varios_python/tijeras.png")),
}

# Crear botones
button_frame = tk.Frame(root)
button_frame.pack()

piedra_button = tk.Button(button_frame, text="Piedra", command=lambda: play("piedra"))
piedra_button.pack(side=tk.LEFT)

papel_button = tk.Button(button_frame, text="Papel", command=lambda: play("papel"))
papel_button.pack(side=tk.LEFT)

tijeras_button = tk.Button(button_frame, text="Tijeras", command=lambda: play("tijeras"))
tijeras_button.pack(side=tk.LEFT)

# Crear etiquetas para mostrar las imágenes
user_label = tk.Label(root)
user_label.pack(side=tk.LEFT)

computer_label = tk.Label(root)
computer_label.pack(side=tk.RIGHT)

# Iniciar el bucle principal
root.mainloop()