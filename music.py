import pygame


class Music:
    def __init__(self):
        self.musique = {
            pygame.mixer.music.load("/sounds/zelda.ogg")
            pygame.mixer.music.load("sounds/dungeon.ogg")

        }

    def Play_music(self, name, map):
        self.name = name
        map = self.current_map
