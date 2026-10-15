import pygame
import os
import sys
import subprocess
import json
from api_client import send_score


# pygame setup
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((640,1080))
pygame.display.set_caption("Zird Rhythm Game")
clock = pygame.time.Clock()
running = True
songOver = False
delta_time = 0
NOTE_SIZE = 60
NOTE_SPEED = 475 # 475
INPUT_COOLDOWN = 15

superMeter = 0
SUPER_METER_INCREASE = 15
SUPER_METER_MULT = 1
SUPER_METER_DECAY = 0.3
superMeterActive = False

comboMeter = 0
COMBO_METER_INCREASE = 0.1
COMBO_METER_MULT = 1
comboMeterActive = False


# files 
root = os.getcwd()
f = open(root + "/api/gameData.json")
data = json.load(f)
SONG_ID_SELECTED = data["selectedTrack"]
f.close()
song = open(root + "/client/charts/" + str(SONG_ID_SELECTED) + "/song.txt", "r")
songContent = song.readlines()
songData = open(root + "/client/charts/" + str(SONG_ID_SELECTED) + "/data.txt", "r")
songDataContent = songData.readlines()
songSpeed = int(songDataContent[1]) # second line
songSpeedCounter = 1
songLineCounter = 1
songMaxLines = len(songContent)

pygame.mixer.music.load(root + "/music/song" + str(SONG_ID_SELECTED) + ".mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play()


# images
lane1InputImg = pygame.image.load(root + "/img/lane1input.png").convert()
lane1InputImg.set_colorkey((0, 255, 255))
lane1InputImgPos = pygame.Vector2(30, screen.get_height() / 1.3)

lane2InputImg = pygame.image.load(root + "/img/lane2input.png").convert()
lane2InputImg.set_colorkey((0, 255, 255))
lane2InputImgPos = pygame.Vector2(182, screen.get_height() / 1.3)

lane3InputImg = pygame.image.load(root + "/img/lane3input.png").convert()
lane3InputImg.set_colorkey((0, 255, 255))
lane3InputImgPos = pygame.Vector2(334, screen.get_height() / 1.3)

lane4InputImg = pygame.image.load(root + "/img/lane4input.png").convert()
lane4InputImg.set_colorkey((0, 255, 255))
lane4InputImgPos = pygame.Vector2(486, screen.get_height() / 1.3)

# note images

lane1NoteImg = pygame.image.load(root + "/img/lane1note.png").convert()
lane1NoteImg.set_colorkey((0, 255, 255))
lane2NoteImg = pygame.image.load(root + "/img/lane2note.png").convert()
lane2NoteImg.set_colorkey((0, 255, 255))
lane3NoteImg = pygame.image.load(root + "/img/lane3note.png").convert()
lane3NoteImg.set_colorkey((0, 255, 255))
lane4NoteImg = pygame.image.load(root + "/img/lane4note.png").convert()
lane4NoteImg.set_colorkey((0, 255, 255))



player_score = 0
savedScore = False

BASE_SCORE_INCREASE = 1

font = pygame.font.Font(None, 32)
text = font.render("Score: " + str(round(player_score, 3)), True, "white")

inputTimingFont = pygame.font.Font(None, 80)
INPUT_TEXT_EXPIRE_DURATION = 25
textInputExpireTimer = 0
textInputType = 0
badInputText = inputTimingFont.render("BAD :C", True, "firebrick1")
okInputText = inputTimingFont.render("OK!", True, "deepskyblue")
perfectInputText = inputTimingFont.render("!!!PERFECT!!!", True, "gold")
missInputText = inputTimingFont.render("X MISS X", True, "red")


# keyboard input

keyBindingsFile = open(root + "/api/keybindings.json", "r")
keyBindingsData = json.load(keyBindingsFile)
lane1Keybinding = keyBindingsData["lane1"]
lane2Keybinding = keyBindingsData["lane2"]
lane3Keybinding = keyBindingsData["lane3"]
lane4Keybinding = keyBindingsData["lane4"]
superKeybinding = keyBindingsData["super"]
keyBindingsFile.close()

lane1_input_cooldown = INPUT_COOLDOWN
lane2_input_cooldown = INPUT_COOLDOWN
lane3_input_cooldown = INPUT_COOLDOWN
lane4_input_cooldown = INPUT_COOLDOWN
lane1_input_boolean = False
lane2_input_boolean = False
lane3_input_boolean = False
lane4_input_boolean = False

note_list = []
lane1_list = []
lane2_list = []
lane3_list = []
lane4_list = []

class Note: 
    def __init__ (self, colour, x, y, lane):
        self.size = NOTE_SIZE
        self.colour = colour
        self.pos = pygame.Vector2(x, y)
        self.lane = lane

    def update (self):
        self.pos.y += NOTE_SPEED * delta_time

    def draw (self):
        #pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size)
        if (self.lane == 1):
            screen.blit(lane1NoteImg, self.pos)
        elif(self.lane == 2):
            screen.blit(lane2NoteImg, self.pos)
        elif(self.lane == 3):
            screen.blit(lane3NoteImg, self.pos)
        elif(self.lane == 4):
            screen.blit(lane4NoteImg, self.pos)
    
# inherits from Note class
class Lane1_Note(Note):
    def __init__ (self):
        super().__init__("red", 30, 0, 1)

class Lane2_Note(Note):
    def __init__ (self):
        super().__init__("yellow", 182, 0, 2)
    
class Lane3_Note(Note):
    def __init__ (self):
        super().__init__("green", 334, 0, 3)

class Lane4_Note(Note):
    def __init__ (self):
        super().__init__("pink", 486, 0, 4)
    
while running:

    if (superMeterActive == False):
        screen.fill("mediumorchid4")
    else:
        screen.fill("darkgoldenrod2")

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

        if event.type == pygame.MOUSEBUTTONDOWN and songOver:
                if button_rect.collidepoint(event.pos):
                   os.execv(sys.executable, ["python"] + sys.argv)
                if button2_rect.collidepoint(event.pos):
                    pygame.quit()
                    venv_python = os.path.join (".venv", "bin", "python")
                    subprocess.run([venv_python, "client/main.py"])
                    sys.exit()
            # 1st note
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.key.key_code(lane1Keybinding) and lane1_input_cooldown == 0 and len(lane1_list) > 0: 
                lane_note = None
                highestY = -1
                for note in lane1_list:
                    if (note.pos.y > highestY):
                        highestY = note.pos.y
                        lane_note = note

                if (lane_note and lane_note.pos.y < lane1InputImgPos.y + 100 and lane_note.pos.y > lane1InputImgPos.y - 100):
                    player_score += BASE_SCORE_INCREASE * SUPER_METER_MULT * COMBO_METER_MULT

                    if (superMeter < 100 and superMeterActive == False):
                        superMeter += SUPER_METER_INCREASE

                    
                    comboMeter += 1

                    lane1_list.remove(lane_note)
                    note_list.remove(lane_note)
                    if (5,lane_note.pos.y < lane1InputImgPos.y + 50 and lane_note.pos.y > lane1InputImgPos.y - 50):
                        if (lane_note.pos.y < lane1InputImgPos.y + 20 and lane_note.pos.y > lane1InputImgPos.y - 20):
                            textInputType = 2
                            textInputExpireTimer = INPUT_TEXT_EXPIRE_DURATION
                            COMBO_METER_MULT += COMBO_METER_INCREASE * 3
                        else:
                            textInputType = 1
                            textInputExpireTimer = INPUT_TEXT_EXPIRE_DURATION
                            COMBO_METER_MULT += COMBO_METER_INCREASE * 2
                    else:
                        textInputType = 0
                        textInputExpireTimer = INPUT_TEXT_EXPIRE_DURATION
                        COMBO_METER_MULT += COMBO_METER_INCREASE
                else:
                    player_score -= 1
                    COMBO_METER_MULT = 1
                    comboMeter = 0
                lane1_input_cooldown = INPUT_COOLDOWN

        # 2nd note
            if event.key == pygame.key.key_code(lane2Keybinding) and lane2_input_cooldown == 0: 
                lane_note = None
                highestY = -1
                for note in lane2_list:
                    if (note.pos.y > highestY):
                        highestY = note.pos.y
                        lane_note = note

                if (lane_note and lane_note.pos.y < lane2InputImgPos.y + 100 and lane_note.pos.y > lane2InputImgPos.y - 100):

                    player_score += BASE_SCORE_INCREASE * SUPER_METER_MULT * COMBO_METER_MULT

                    if (superMeter < 100 and superMeterActive == False):
                        superMeter += SUPER_METER_INCREASE

                    comboMeter += 1

                    lane2_list.remove(lane_note)
                    note_list.remove(lane_note)
                    if (lane_note.pos.y < lane2InputImgPos.y + 50 and lane_note.pos.y > lane2InputImgPos.y - 50):
                        if (lane_note.pos.y < lane2InputImgPos.y + 20 and lane_note.pos.y > lane2InputImgPos.y - 20):
                            textInputType = 2
                            textInputExpireTimer = INPUT_TEXT_EXPIRE_DURATION
                            COMBO_METER_MULT += COMBO_METER_INCREASE * 3
                        else:
                            textInputType = 1
                            textInputExpireTimer = INPUT_TEXT_EXPIRE_DURATION
                            COMBO_METER_MULT += COMBO_METER_INCREASE * 2
                    else:
                        textInputType = 0
                        textInputExpireTimer = INPUT_TEXT_EXPIRE_DURATION
                        COMBO_METER_MULT += COMBO_METER_INCREASE
                else:
                    player_score -= 1
                    COMBO_METER_MULT = 1
                    comboMeter = 0
                lane2_input_cooldown = INPUT_COOLDOWN

            # 3rd note
            if event.key == pygame.key.key_code(lane3Keybinding) and lane3_input_cooldown == 0: 
                lane_note = None
                highestY = -1
                for note in lane3_list:
                    if (note.pos.y > highestY):
                        highestY = note.pos.y
                        lane_note = note

                if (lane_note and lane_note.pos.y < lane3InputImgPos.y + 100 and lane_note.pos.y > lane3InputImgPos.y - 100):

                    player_score += BASE_SCORE_INCREASE * SUPER_METER_MULT * COMBO_METER_MULT

                    if (superMeter < 100 and superMeterActive == False):
                        superMeter += SUPER_METER_INCREASE
                    
                    comboMeter += 1

                    lane3_list.remove(lane_note)
                    note_list.remove(lane_note)
                    if (lane_note.pos.y < lane3InputImgPos.y + 50 and lane_note.pos.y > lane3InputImgPos.y - 50):
                        if (lane_note.pos.y < lane3InputImgPos.y + 20 and lane_note.pos.y > lane3InputImgPos.y - 20):
                            textInputType = 2
                            textInputExpireTimer = INPUT_TEXT_EXPIRE_DURATION
                            COMBO_METER_MULT += COMBO_METER_INCREASE * 3
                        else:
                            textInputType = 1
                            textInputExpireTimer = INPUT_TEXT_EXPIRE_DURATION
                            COMBO_METER_MULT += COMBO_METER_INCREASE * 2
                    else:
                        textInputType = 0
                        textInputExpireTimer = INPUT_TEXT_EXPIRE_DURATION
                        COMBO_METER_MULT += COMBO_METER_INCREASE
                else:
                    player_score -= 1
                    COMBO_METER_MULT = 1
                    comboMeter = 0
                lane3_input_cooldown = INPUT_COOLDOWN
            
            # 4th note
            if event.key == pygame.key.key_code(lane4Keybinding) and lane4_input_cooldown == 0: 
                lane_note = None
                highestY = -1
                for note in lane4_list:
                    if (note.pos.y > highestY):
                        highestY = note.pos.y
                        lane_note = note

                if (lane_note and lane_note.pos.y < lane4InputImgPos.y + 100 and lane_note.pos.y > lane4InputImgPos.y - 100):

                    player_score += BASE_SCORE_INCREASE * SUPER_METER_MULT * COMBO_METER_MULT

                    if (superMeter < 100):
                        superMeter += SUPER_METER_INCREASE

                    comboMeter += 1
                    
                    lane4_list.remove(lane_note)
                    note_list.remove(lane_note)
                    if (lane_note.pos.y < lane4InputImgPos.y + 50 and lane_note.pos.y > lane4InputImgPos.y - 50):
                        if (lane_note.pos.y < lane4InputImgPos.y + 20 and lane_note.pos.y > lane4InputImgPos.y - 20):
                            textInputType = 2
                            textInputExpireTimer = INPUT_TEXT_EXPIRE_DURATION
                            COMBO_METER_MULT += COMBO_METER_INCREASE * 3
                        else:
                            textInputType = 1
                            textInputExpireTimer = INPUT_TEXT_EXPIRE_DURATION
                            COMBO_METER_MULT += COMBO_METER_INCREASE * 2
                    else:
                        textInputType = 0
                        textInputExpireTimer = INPUT_TEXT_EXPIRE_DURATION
                        COMBO_METER_MULT += COMBO_METER_INCREASE
                else:
                    player_score -= 1
                    COMBO_METER_MULT = 1
                    comboMeter = 0
                lane4_input_cooldown = INPUT_COOLDOWN
            
            # Super Meter (SPACE)
            if event.key == pygame.key.key_code(superKeybinding) and superMeter >= 100 and superMeterActive == False:
                superMeterActive = True
                SUPER_METER_MULT = 5


    if songOver == True:

        # save the run to userData.json file
        if savedScore == False:
            uf = open(root + "/api/userData.json", "r+")
            udata = json.load(uf)
            udata["score"] = round(player_score, 3)
            udata.update(udata)
            uf.seek(0)
            json.dump(udata, uf, indent=4)
            # send score to api
            send_score(udata)
            uf.close()
            savedScore = True



        endingText = font.render("You finished with a score of: " + str(round(player_score, 3)), True, "white")
        screen.blit(endingText, (screen.get_width()//2 - endingText.get_width() // 2, screen.get_height()/2))

        button_rect = pygame.Rect(screen.get_width() // 2 - 100, screen.get_height() // 2 + 50, 200, 50)
        pygame.draw.rect(screen, "green", button_rect)
        button_text = font.render("Play Again", True, "white")
        screen.blit(button_text, (button_rect.x + 5, button_rect.y +5))

        button2_rect = pygame.Rect(screen.get_width() // 2 - 100, screen.get_height() // 2 + 150, 200, 50)
        pygame.draw.rect(screen, "green", button2_rect)
        button2_text = font.render("MainMenu", True, "white")
        screen.blit(button2_text, (button2_rect.x + 5, button2_rect.y + 5))
        
    else:

        screen.blit(lane1InputImg, lane1InputImgPos)
        screen.blit(lane2InputImg, lane2InputImgPos)
        screen.blit(lane3InputImg, lane3InputImgPos)
        screen.blit(lane4InputImg, lane4InputImgPos)

        screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, screen.get_height() /1.1))

        superText = font.render("Super Meter: " + str(round(superMeter, 3)), True, "white")
        screen.blit(superText, (screen.get_width() // 2 - superText.get_width() // 2, screen.get_height() /1.07))
        comboText = font.render("Combo Meter: " + str(comboMeter), True, "white")
        screen.blit(comboText, (screen.get_width() // 2 - comboText.get_width() // 2, screen.get_height() /1.04))

        if (textInputExpireTimer > 0):
            if (textInputType == 0):
                screen.blit(badInputText, (screen.get_width() // 2 - badInputText.get_width() // 2, screen.get_height() / 4))
            elif(textInputType == 1):
                screen.blit(okInputText, (screen.get_width() // 2 - okInputText.get_width() // 2, screen.get_height() / 4))
            elif(textInputType == 2):
                screen.blit(perfectInputText, (screen.get_width() // 2 - perfectInputText.get_width() // 2, screen.get_height() / 4))
            elif(textInputType == 3):
                screen.blit(missInputText, (screen.get_width() // 2 - missInputText.get_width() // 2, screen.get_height() / 4))


    if (lane1_input_cooldown > 0):
        lane1_input_cooldown -= 1
    
    if (lane2_input_cooldown > 0):
        lane2_input_cooldown -= 1

    if (lane3_input_cooldown > 0):
        lane3_input_cooldown -= 1

    if (lane4_input_cooldown > 0):
        lane4_input_cooldown -= 1

    ###NOTE SPAWNING

    if songSpeedCounter > songSpeed:

        if (songLineCounter >= songMaxLines):
            if (len(note_list) > 0):
                pass
            else:
                songOver = True
        else:
            laneCounter = 0
            for i in songContent[songLineCounter]:

                if (i == "0"):
                    if (laneCounter == 0):
                        new_note = Lane1_Note()
                        note_list.append(new_note)
                        lane1_list.append(new_note)
                    elif (laneCounter == 1):
                        new_note = Lane2_Note()
                        note_list.append(new_note)
                        lane2_list.append(new_note)
                    elif (laneCounter == 2):
                        new_note = Lane3_Note()
                        note_list.append(new_note)
                        lane3_list.append(new_note)
                    elif (laneCounter == 3):
                        new_note = Lane4_Note()
                        note_list.append(new_note)
                        lane4_list.append(new_note)
                laneCounter += 1


            songLineCounter += 1
            songSpeedCounter = 0

    songSpeedCounter += 1
     
     # the [:] signifies that its a copy of the original list because this snippet of code will delete objects from the actual list - slice notation start:stop:step
    for note in note_list[:]:
        note.update()
        note.draw()

        if (note.pos.y > screen.get_height()):
            player_score -= 1
            comboMeter = 0

            textInputType = 3
            textInputExpireTimer = INPUT_TEXT_EXPIRE_DURATION

            note_list.remove(note)
            if (note.lane == 1 ):
                lane1_list.remove(note)
            elif (note.lane == 2):
                lane2_list.remove(note)
            elif (note.lane == 3):
                lane3_list.remove(note)
            elif (note.lane == 4):
                lane4_list.remove(note)
    
    text = font.render("Score: " + str(round(player_score, 3)), True, "white")
    pygame.display.flip()
    
    if (textInputExpireTimer > 0):
        textInputExpireTimer -= 1

    if (superMeter >= 100 and superMeterActive == False):
        superMeter = 100
    if (superMeterActive == True and superMeter > 0):
        superMeter -= SUPER_METER_DECAY
    if (superMeter <= 0 ):
        SUPER_METER_MULT = 1
        superMeter = 0
        superMeterActive = False

    delta_time = clock.tick(60) / 1000 # 60 tps

song.close()
songData.close()
pygame.quit()
