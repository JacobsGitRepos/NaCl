import pygame
import sys
from pathlib import Path
from settings_manager import SettingsManager

# Initialize Pygame
pygame.init()
pygame.display.set_caption("NaCl - Main Menu")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
FONT_PATH = BASE_DIR / "assets" / "fonts" / "Bleach.ttf"

# Load font
if FONT_PATH.exists():
    font = pygame.font.Font(str(FONT_PATH), 48)
    print("Loaded custom font:", FONT_PATH)
else:
    print("Font not found, using default.")
    font = pygame.font.SysFont(None, 48)

# Settings
settings = SettingsManager()
settings.load()

# Allowed characters for display
ALLOWED_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@+-/()? "

# Menu items
menu_items = ["START GAME", "LOAD GAME", "SETTINGS", "EXIT"]
selected_index = 0

def render_text(text, selected=False):
    # Only render allowed characters
    text = "".join([c if c in ALLOWED_CHARS else "?" for c in text])
    color = (255, 255, 0) if selected else (255, 255, 255)
    return font.render(text, True, color)

def draw_menu():
    screen.fill((0, 0, 0))

    # --- Header line ---
    header_text = "WELCOME TO NACL"
    header_surface = font.render(header_text, True, (255, 255, 255))
    header_y = 10  # top padding
    screen.blit(header_surface, (50, header_y))

    # --- Menu items ---
    line_height = font.get_height()
    menu_start_y = header_y + int(line_height * 1.5)  # header + half-line buffer

    for i, item in enumerate(menu_items):
        text_surface = render_text(item, selected=(i == selected_index))
        y = menu_start_y + i * int(line_height * 1.5)  # half-line spacing between items
        screen.blit(text_surface, (50, y))


def main():
    global selected_index
    running = True
    while running:
        draw_menu()
        pygame.display.flip()  # <- update display after drawing

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_index = (selected_index - 1) % len(menu_items)
                elif event.key == pygame.K_DOWN:
                    selected_index = (selected_index + 1) % len(menu_items)
                elif event.key == pygame.K_RETURN:
                    choice = menu_items[selected_index]
                    if choice == "EXIT":
                        running = False
                    else:
                        print(f"Selected: {choice}")
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
