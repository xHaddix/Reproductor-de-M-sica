import tkinter as tk
from tkinter import Listbox
import pygame
from backend import MusicPlayer  # Importa la clase MusicPlayer
from PIL import Image, ImageTk

# Inicializar pygame mixer (esto también se puede hacer en el __init__ de la clase MusicPlayer)
pygame.mixer.init()

# Crear la ventana principal
root = tk.Tk()
root.title("Reproductor de Música")
root.config(bg="#030506")

# Etiqueta para mostrar la canción actual
music_label = tk.Label(root, text="Sin reproducción", anchor='center', background="#030506", foreground="#fff")
music_label.grid(row=2, column= 1, columnspan=4)

listbox = Listbox(root, height=30, width=30, background="#030506", highlightbackground="#030506", relief='flat', foreground="#fff")
listbox.grid(row=1, column=0, rowspan=3)

# Crear una instancia de la clase MusicPlayer y pasar la etiqueta como argumento
player = MusicPlayer(music_label, listbox)


# Cargar la imagen usando PIL
image = Image.open(r"C:\Proyecto\Reproductor-de-M-sica\app-web\Python-Code\Images\rigby.jpg")
# Redimensionar la imagen
nuevo_tamano = (300, 300)  # Ancho x Alto en píxeles
image = image.resize(nuevo_tamano, Image.LANCZOS)
photo = ImageTk.PhotoImage(image)
#Imagen de reproduccion
imagen_reproduccion = tk.Label(root, image=photo, highlightbackground="#030506", relief='flat')
imagen_reproduccion.image = photo  # Esto es necesario para evitar que la imagen sea recolectada por el GC
imagen_reproduccion.grid(row=1, column=1, columnspan=4, pady=20, padx=20)

# Botones de control de musica, vinculando a los métodos de la clase
load_button = tk.Button(root, text="Cargar y Reproducir", command=player.load_music)
load_button.grid(row= 0, column= 0, sticky='n')

#Boton detener
stop_button = tk.Button(root, text="⏹︎", command=player.stop_music, width=5, height=2)
stop_button.grid(row=3, column=1)

#Boton anterior cancion
previous_button = tk.Button(root, text="⏮︎", command=player.previous_song, width=5, height=2)
previous_button.grid(row=3, column=2)

#Boton reproducir/pausar
play_button = tk.Button(root, text="⏸︎", command=player.play_music, width=5, height=2)
play_button.grid(row= 3, column= 3)

#Boton siguiente cancion
next_button = tk.Button(root, text="⏭︎", command=player.next_song, width=5, height=2)
next_button.grid(row=3, column=4)

# Iniciar el bucle de la interfaz gráfica
root.mainloop()
