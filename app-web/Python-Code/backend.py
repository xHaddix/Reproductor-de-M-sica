# Funciones para controlar la música
import pygame
from tkinter import filedialog
class backend(): 

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
