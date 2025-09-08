import pygame
from settings_manager import SettingsManager  # local import

def boot():
    pygame.init()
    print("Pygame initialized!")
    
    # Load settings
    settings = SettingsManager()
    settings.load()
    print("Settings loaded!")

    # Placeholder for main game loop
    print("Game would start here...")

if __name__ == "__main__":
    boot()
