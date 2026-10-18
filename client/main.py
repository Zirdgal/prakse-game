import pygame
import sys
import os
import subprocess # for file running
import json

# initialization
pygame.init()
screen = pygame.display.set_mode((640,1000))
pygame.display.set_caption("Zird Rhythm Game")

# fonts
titleFont = pygame.font.Font(None, 80)
headerFont = pygame.font.Font(None, 48)
font = pygame.font.Font(None, 32)


# track buttons
button1_text = font.render("Play Track 1\nLatvijas Himna", True, "white")
button1_rect = pygame.Rect(screen.get_width() // 2 - button1_text.get_width() // 2, screen.get_height() // 2 - 25, button1_text.get_width() + 30, button1_text.get_height() + 10)
button2_text = font.render("Play Track 2\nThrough Patches of Violet\nMili", True, "white")
button2_rect = pygame.Rect(screen.get_width() // 2 - button2_text.get_width() // 2, screen.get_height() // 2 + 50, button2_text.get_width() + 30, button2_text.get_height() + 10)


# keybind buttons
keybind1Rect = pygame.Rect(100, 900, 50, 30)
keybind2Rect = pygame.Rect(200, 900, 50, 30)
keybind3Rect = pygame.Rect(300, 900, 50, 30)
keybind4Rect = pygame.Rect(400, 900, 50, 30)
keybindSuperRect = pygame.Rect(500, 900, 100, 30)

# keybindings.json
root = os.getcwd()
keyBindingsFile = open(root + "/api/keybindings.json", "r")
keyBindingsData = json.load(keyBindingsFile) # saved as Dict

keyBindingsFile.close()

# used for telling if user is trying to change keybind
keybindRectInactiveCol = "deeppink4"
keybindRectActiveCol = "deeppink2"
keybind1RectActive = False
keybind1RectCol = keybindRectInactiveCol
keybind2RectActive = False
keybind2RectCol = keybindRectInactiveCol
keybind3RectActive = False
keybind3RectCol = keybindRectInactiveCol
keybind4RectActive = False
keybind4RectCol = keybindRectInactiveCol
keybindSuperRectActive = False
keybindSuperRectCol = keybindRectInactiveCol

# for login
userText = ""
loggedIn = False
inputActive = False
# check if user isnt already logged in (the user data gets deleted on closing the application)
usf = open(root + "/api/userData.json", "r")
usdata = json.load(usf)

if (usdata["username"] != ""):
    userText = usdata["username"]
    loggedIn = True

usf.close()

logInButton_rect = pygame.Rect(screen.get_width() // 2 - 50, 800, 100, 30)
inputRect = pygame.Rect(screen.get_width() // 2 - 50,700,100,30)   
color_active = pygame.Color("deeppink2")
color_inactive = pygame.Color("deeppink4")
color = color_inactive


# program loop
running = True


# function for handling switcing python programs
def handleSwitchingScenes(trackID: int):
    
    # read and write into gameData.json which handles which level the player is using on a local level
    f = open(root + "/api/gameData.json", "r+")
    data = json.load(f)
    data["selectedTrack"] = trackID
    data.update(data)
    f.seek(0)
    json.dump(data, f, indent=4)
    f.close()

    # save keybindings into keybindings.json
    kf = open(root + "/api/keybindings.json", "r+")
    kdata = json.load(kf)
    kdata.update(keyBindingsData)
    kf.seek(0)
    json.dump(kdata, kf, indent=4)
    kf.close()

    # save username into userData.json
    uf = open(root + "/api/userData.json", "w") # w is added because i want to overwrite data
    # make new data to overwrite it
    userDataDict = {
        "username" : userText,
        "score": 0,
        "level": trackID
    }
    # set cursor to 0 position
    uf.seek(0)
    # update the file
    json.dump(userDataDict, uf, indent=4)
    uf.close()


    pygame.quit()
    venv_python = os.path.join (".venv", "bin", "python")
    subprocess.run([sys.executable, "client/game.py"])
    sys.exit()

while running:
    # background colour mediumorchid4 
    screen.fill("mediumorchid4")

    # NOT program name, its rendered text on screen
    title_text = titleFont.render("Zird Rhythm Game", True, "white")
    screen.blit(title_text, (screen.get_width() // 2  - title_text.get_width() // 2, 250))

    # mouse pos
    mouse_pos = pygame.mouse.get_pos()

    if loggedIn == True:
        # draws the track buttons
        pygame.draw.rect(screen, "deeppink", button1_rect)
        pygame.draw.rect(screen, "deeppink", button2_rect)
        screen.blit(button1_text, (button1_rect.x + 5, button1_rect.y + 5))
        screen.blit(button2_text, (button2_rect.x + 5, button2_rect.y + 5))
        
        usernameText = font.render("Username: " + userText, True, "white")
        screen.blit(usernameText, (screen.get_width() // 2 - usernameText.get_width() // 2, 350))

        pygame.draw.rect(screen, keybind1RectCol, keybind1Rect)
        keybind1Text = font.render(keyBindingsData["lane1"], True, "white")
        screen.blit(keybind1Text, (keybind1Rect.x + 5, keybind1Rect.y + 5))
        pygame.draw.rect(screen, keybind2RectCol, keybind2Rect)
        keybind2Text = font.render(keyBindingsData["lane2"], True, "white")
        screen.blit(keybind2Text, (keybind2Rect.x + 5, keybind2Rect.y + 5))
        pygame.draw.rect(screen, keybind3RectCol, keybind3Rect)
        keybind3Text = font.render(keyBindingsData["lane3"], True, "white")
        screen.blit(keybind3Text, (keybind3Rect.x + 5, keybind3Rect.y + 5))
        pygame.draw.rect(screen, keybind4RectCol, keybind4Rect)
        keybind4Text = font.render(keyBindingsData["lane4"], True, "white")
        screen.blit(keybind4Text, (keybind4Rect.x + 5, keybind4Rect.y + 5))
        pygame.draw.rect(screen, keybindSuperRectCol, keybindSuperRect)
        keybindSuperText = font.render(keyBindingsData["super"], True, "white")
        screen.blit(keybindSuperText, (keybindSuperRect.x + 5, keybindSuperRect.y + 5))



    else:
        logInText = headerFont.render("Please log in!", True, "white")
        screen.blit(logInText, (screen.get_width() // 2 - logInText.get_width() // 2, 600))
        
         
        pygame.draw.rect(screen, color, inputRect)
        text_surface = font.render(userText, True, "white")
        screen.blit(text_surface, (inputRect.x+5, inputRect.y+5))
        inputRect.w = max(100, text_surface.get_width()+10)

        
        logInButtonText = font.render("LogIn", True, "white")
        pygame.draw.rect(screen, "deeppink", logInButton_rect)
        screen.blit(logInButtonText, (logInButton_rect.x + 5, logInButton_rect.y + 5))



    if inputActive:
        color = color_active
    else:
        color = color_inactive
    
    if keybind1RectActive:
        keybind1RectCol = keybindRectActiveCol
    else:
        keybind1RectCol = keybindRectInactiveCol
    
    if keybind2RectActive:
        keybind2RectCol = keybindRectActiveCol
    else:
        keybind2RectCol = keybindRectInactiveCol
    
    if keybind3RectActive:
        keybind3RectCol = keybindRectActiveCol
    else:
        keybind3RectCol = keybindRectInactiveCol
    
    if keybind4RectActive:
        keybind4RectCol = keybindRectActiveCol
    else:
        keybind4RectCol = keybindRectInactiveCol
    
    if keybindSuperRectActive:
        keybindSuperRectCol = keybindRectActiveCol
    else:
        keybindSuperRectCol = keybindRectInactiveCol

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            # clear username on program end
            uf = open(root + "/api/userData.json", "w") # w is added because i want to overwrite data
            # make new data to overwrite it
            userDataDict = {
                "username" : "",
                "runs" : []
            }
            # set cursor to 0 position
            uf.seek(0)
            # update the file
            json.dump(userDataDict, uf, indent=4)
            uf.close()

            running = False

        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if inputRect.collidepoint(event.pos):
                inputActive = True
            else:
                inputActive = False

            if logInButton_rect.collidepoint(event.pos) and loggedIn == False and userText != "":
                loggedIn = True

            if keybind1Rect.collidepoint(event.pos):
                keybind1RectActive = True
            else:
                keybind1RectActive = False
            
            if keybind2Rect.collidepoint(event.pos):
                keybind2RectActive = True
            else:
                keybind2RectActive = False
            
            if keybind3Rect.collidepoint(event.pos):
                keybind3RectActive = True
            else:
                keybind3RectActive = False

            if keybind4Rect.collidepoint(event.pos):
                keybind4RectActive = True
            else:
                keybind4RectActive = False
            
            if keybindSuperRect.collidepoint(event.pos):
                keybindSuperRectActive = True
            else:
                keybindSuperRectActive = False

            if button1_rect.collidepoint(event.pos) and loggedIn == True:
                handleSwitchingScenes(1)
            if button2_rect.collidepoint(event.pos) and loggedIn == True:
                handleSwitchingScenes(2)
        
        if event.type == pygame.KEYDOWN:
            if inputActive == True:
                if event.key == pygame.K_BACKSPACE:
                    userText = userText[:-1]
                else:
                    userText += event.unicode
            
            if keybind1RectActive == True:
                keyBindingsData["lane1"] = event.unicode
            
            if keybind2RectActive == True:
                keyBindingsData["lane2"] = event.unicode

            if keybind3RectActive == True:
                keyBindingsData["lane3"] = event.unicode

            if keybind4RectActive == True:
                keyBindingsData["lane4"] = event.unicode
            
            if keybindSuperRectActive == True:
                lanekeyBindingsData["super"] = event.unicode

    
    pygame.display.flip()

pygame.quit()