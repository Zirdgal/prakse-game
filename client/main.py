import pygame
import sys
import os
import subprocess # for file running
import json

pygame.init()

screen = pygame.display.set_mode((640,1080))
pygame.display.set_caption("Zird Rhythm Game")

font = pygame.font.Font(None, 32)

button1_rect = pygame.Rect(screen.get_width() // 2 - 100, screen.get_height() // 2 - 25, 200, 50)
button2_rect = pygame.Rect(screen.get_width() // 2 - 100, screen.get_height() // 2 + 75, 200, 50)

running = True

while running:
    screen.fill("mediumorchid4")

    title_text = font.render("Zird Rhythm Game", True, "white")
    screen.blit(title_text, (100, 100))

    mouse_pos = pygame.mouse.get_pos()

    pygame.draw.rect(screen, "green", button1_rect)
    pygame.draw.rect(screen, "green", button2_rect)
    button1_text = font.render("Play Track 1", True, "white")
    screen.blit(button1_text, (button1_rect.x, button1_rect.y))
    button2_text = font.render("Play Track 2", True, "white")
    screen.blit(button2_text, (button2_rect.x, button2_rect.y))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button1_rect.collidepoint(event.pos):
                path = os.path.realpath(__file__)
                root = os.getcwd()



                f = open(root + "/game/data.json", "r+")
                data = json.load(f)
                data.update({"selectedTrack": 1})
                f.seek(0)
                json.dump(data, f, indent=4)
                f.close()



                pygame.quit()
                venv_python = os.path.join (".venv", "bin", "python")
                subprocess.run([venv_python, "client/game.py"])
                sys.exit()
            if button2_rect.collidepoint(event.pos):
                path = os.path.realpath(__file__)
                root = os.getcwd()
                f = open(root + "/game/data.json", "r+")
                data = json.load(f)
                data.update({"selectedTrack": 2})
                f.seek(0)
                json.dump(data, f, indent=4)
                f.close()



                pygame.quit()
                venv_python = os.path.join (".venv", "bin", "python")
                subprocess.run([venv_python, "client/game.py"])
                sys.exit()
    
    pygame.display.flip()