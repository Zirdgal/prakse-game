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

logInButton_rect = pygame.Rect(200, 400, 100, 40)

loggedIn = False
userText = ""
inputActive = False
inputRect = pygame.Rect(200,300,100,30)
color_active = pygame.Color("lightskyblue3")
color_inactive = pygame.Color("chartreuse4")
color = color_inactive

running = True

while running:
    screen.fill("mediumorchid4")

    title_text = font.render("Zird Rhythm Game", True, "white")
    screen.blit(title_text, (100, 100))

    mouse_pos = pygame.mouse.get_pos()

    if loggedIn == True:
        pygame.draw.rect(screen, "green", button1_rect)
        pygame.draw.rect(screen, "green", button2_rect)
        button1_text = font.render("Play Track 1", True, "white")
        screen.blit(button1_text, (button1_rect.x, button1_rect.y))
        button2_text = font.render("Play Track 2", True, "white")
        screen.blit(button2_text, (button2_rect.x, button2_rect.y))
        
        usernameText = font.render("Username: " + userText, True, "white")
        screen.blit(usernameText, (100, 200))
    else:
        logInText = font.render("Please log in!", True, "white")
        screen.blit(logInText, (100, 200))
        pygame.draw.rect(screen, color, inputRect)
        text_surface = font.render(userText, True, "white")
        screen.blit(text_surface, (inputRect.x+5, inputRect.y+5))
        inputRect.w = max(100, text_surface.get_width()+10)

        logInButtonText = font.render("LogIn", True, "white")
        pygame.draw.rect(screen, "green", logInButton_rect)
        screen.blit(logInButtonText, (logInButton_rect.x, logInButton_rect.y))



    if inputActive:
        color = color_active
    else:
        color = color_inactive

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if inputRect.collidepoint(event.pos):
                inputActive = True
            else:
                inputActive = False

            if logInButton_rect.collidepoint(event.pos) and loggedIn == False and userText != "":
                loggedIn = True

            if button1_rect.collidepoint(event.pos) and loggedIn == True:
                path = os.path.realpath(__file__)
                root = os.getcwd()



                f = open(root + "/api/gameData.json", "r+")
                data = json.load(f)
                data.update({"selectedTrack": 1})
                f.seek(0)
                json.dump(data, f, indent=4)
                f.close()



                pygame.quit()
                venv_python = os.path.join (".venv", "bin", "python")
                subprocess.run([venv_python, "client/game.py"])
                sys.exit()
            if button2_rect.collidepoint(event.pos) and loggedIn == True:
                path = os.path.realpath(__file__)
                root = os.getcwd()
                f = open(root + "/api/gameData.json", "r+")
                data = json.load(f)
                data.update({"selectedTrack": 2})
                f.seek(0)
                json.dump(data, f, indent=4)
                f.close()



                pygame.quit()
                venv_python = os.path.join (".venv", "bin", "python")
                subprocess.run([venv_python, "client/game.py"])
                sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                userText = userText[:-1]
            else:
                userText += event.unicode
    
    pygame.display.flip()