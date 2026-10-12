import pygame
import sys
import os
import subprocess # for file running

pygame.init()

screen = pygame.display.set_mode((640,1080))
pygame.display.set_caption("Untitled Rhythm Game")

font = pygame.font.Font(None, 32)

button_rect = pygame.Rect(screen.get_width() // 2 - 100, screen.get_height() // 2 - 25, 200, 50)

running = True

while running:
    screen.fill("mediumorchid4")

    title_text = font.render("Untitled Rhythm Game", True, "white")
    screen.blit(title_text, (100, 100))

    mouse_pos = pygame.mouse.get_pos()
    pygame.draw.rect(screen, "green", button_rect)

    button_text = font.render("Play", True, "white")
    screen.blit(button_text, (button_rect.x, button_rect.y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                pygame.quit()
                venv_python = os.path.join (".venv", "bin", "python")
                subprocess.run([venv_python, "client/game.py"])
                sys.exit()
    
    pygame.display.flip()