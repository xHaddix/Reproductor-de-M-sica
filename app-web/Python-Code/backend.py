import pygame
from tkinter import filedialog, Listbox, END

class MusicPlayer:
    def __init__(self, label, listbox):
        pygame.mixer.init()
        self.music_label = label
        self.listbox = listbox
        self.playlist = []

        # Vincular la selección de una canción en el Listbox con el método play_selected_music
        self.listbox.bind('<<ListboxSelect>>', self.play_selected_music)

    def load_music(self):
        files = filedialog.askopenfilenames(filetypes=[("MP3 files", "*.mp3")])
        if files:
            for file in files:
                self.playlist.append(file)
                self.listbox.insert(END, file.split("/")[-1])

    def play_selected_music(self, event=None):
        selected_song_index = self.listbox.curselection()
        if selected_song_index:
            file = self.playlist[selected_song_index[0]]
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            self.music_label.config(text="" + file.split("/")[-1])

    def play_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    def stop_music(self):
        pygame.mixer.music.stop()
        self.music_label.config(text="Sin reproducción")

    def next_song(self):
        current_selection = self.listbox.curselection()
        if current_selection:
            next_index = current_selection[0] + 1
            if next_index < self.listbox.size():
                self.listbox.selection_clear(0, END)
                self.listbox.selection_set(next_index)
                self.listbox.activate(next_index)
                self.play_selected_music()

    def previous_song(self):
        current_selection = self.listbox.curselection()
        if current_selection:
            prev_index = current_selection[0] - 1
            if prev_index >= 0:
                self.listbox.selection_clear(0, END)
                self.listbox.selection_set(prev_index)
                self.listbox.activate(prev_index)
                self.play_selected_music()