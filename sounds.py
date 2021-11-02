import pygame


class SoundManager:
    def __init__(self):
        self.sounds = {
            "zelda": pygame.mixer.Sound("../sounds/zelda.ogg"),
            "dungeon": pygame.mixer.Sound("../sounds/dungeon.ogg")
        }

    def play(self, name):
        self.sounds[name].play()
