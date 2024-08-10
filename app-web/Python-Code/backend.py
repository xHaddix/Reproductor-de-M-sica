import pygame
from tkinter import filedialog

class MusicPlayer:
    def __init__(self, label):
        pygame.mixer.init()
        self.music_label = label

    def load_music(self):
        file = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if file:
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            self.music_label.config(text="Reproduciendo: " + file.split("/")[-1])

    def play_music(self):
        pygame.mixer.music.unpause()

    def pause_music(self):
        pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()
        self.music_label.config(text="")
