import tkinter as tk
from tkinter import filedialog
import pygame

# Inicializar pygame mixer
pygame.mixer.init()

# Funciones para controlar la música
def load_music():
    file = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    if file:
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        music_label.config(text="Reproduciendo: " + file.split("/")[-1])

def play_music():
    pygame.mixer.music.unpause()

def pause_music():
    pygame.mixer.music.pause()

def stop_music():
    pygame.mixer.music.stop()
    music_label.config(text="")

# Crear la ventana principal
root = tk.Tk()
root.title("Reproductor de Música")

# Etiqueta para mostrar la canción actual
music_label = tk.Label(root, text="No hay música reproduciéndose")
music_label.pack(pady=10)

# Botones de control de música
load_button = tk.Button(root, text="Cargar y Reproducir", command=load_music)
load_button.pack(pady=5)

play_button = tk.Button(root, text="Reanudar", command=play_music)
play_button.pack(pady=5)

pause_button = tk.Button(root, text="Pausar", command=pause_music)
pause_button.pack(pady=5)

stop_button = tk.Button(root, text="Detener", command=stop_music)
stop_button.pack(pady=5)

# Iniciar el bucle de la interfaz gráfica
root.mainloop()
