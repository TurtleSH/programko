import sys
import pygame

pygame.init()

# Nastavení okna
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Icy Tower - Hlavní menu")

# Barvy
WHITE = (255, 255, 255)
BLUE = (0, 120, 215)
RED = (200, 50, 50)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 40)


def draw_text(text, font, color, surface, x, y):
  textobj = font.render(text, True, color)
  textrect = textobj.get_rect()
  textrect.topleft = (x, y)
  surface.blit(textobj, textrect)


def main_menu():
  while True:
    screen.fill(WHITE)
    draw_text("Ice Tower 2.0", font, BLACK, screen, 210, 150)

    # Tlačítka
    start_button = pygame.Rect(200, 350, 200, 50)
    exit_button = pygame.Rect(200, 450, 200, 50)

    pygame.draw.rect(screen, BLUE, start_button)
    pygame.draw.rect(screen, RED, exit_button)

    draw_text("SPUSTIT HRU", font, WHITE, screen, 210, 360)
    draw_text("UKONČIT", font, WHITE, screen, 235, 460)

    click = False
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          pos = pygame.mouse.get_pos()
          if start_button.collidepoint(pos):
            print("Spouštím hru...")  
          if exit_button.collidepoint(pos):
            pygame.quit()
            sys.exit()

    pygame.display.update()


if __name__ == "__main__":
  main_menu()