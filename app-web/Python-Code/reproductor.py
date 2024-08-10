import tkinter as tk
import pygame
from backend import MusicPlayer  # Importa la clase MusicPlayer

# Inicializar pygame mixer (esto también se puede hacer en el __init__ de la clase MusicPlayer)
pygame.mixer.init()

# Crear la ventana principal
root = tk.Tk()
root.title("Reproductor de Música")

# Etiqueta para mostrar la canción actual
music_label = tk.Label(root, text="No hay música reproduciéndose")
music_label.pack(pady=10)

# Crear una instancia de la clase MusicPlayer y pasar la etiqueta como argumento
player = MusicPlayer(music_label)

# Botones de control de música, vinculando a los métodos de la clase
load_button = tk.Button(root, text="Cargar y Reproducir", command=player.load_music)
load_button.pack(pady=5)

play_button = tk.Button(root, text="Reanudar", command=player.play_music)
play_button.pack(pady=5)

pause_button = tk.Button(root, text="Pausar", command=player.pause_music)
pause_button.pack(pady=5)

stop_button = tk.Button(root, text="Detener", command=player.stop_music)
stop_button.pack(pady=5)

# Iniciar el bucle de la interfaz gráfica
root.mainloop()
