import pygame
import os
import sys
import subprocess
import json

# bsSpawnerTimer = 1
# pygame setup
pygame.init()
screen = pygame.display.set_mode((640,1080))
pygame.display.set_caption("Zird Rhythm Game")
clock = pygame.time.Clock()
running = True
songOver = False
delta_time = 0
NOTE_SIZE = 60
NOTE_SPEED = 475
INPUT_COOLDOWN = 15

superMeter = 0
SUPER_METER_INCREASE = 15
SUPER_METER_MULT = 1
superMeterActive = False

comboMeter = 0
COMBO_METER_INCREASE = 0.1
COMBO_METER_MULT = 1
comboMeterActive = False


# files 
path = os.path.realpath(__file__)
direc = os.path.dirname(path)

root = os.getcwd()

f = open(root + "/game/data.json")
data = json.load(f)
print(data)
SONG_ID_SELECTED = data["selectedTrack"]
print(SONG_ID_SELECTED)
print(data["selectedTrack"])
f.close()
song = open(direc + "/charts/" + str(SONG_ID_SELECTED) + "/song.txt", "r")
songContent = song.readlines()
songData = open(direc + "/charts/" + str(SONG_ID_SELECTED) + "/data.txt", "r")
songDataContent = songData.readlines()
songSpeed = int(songDataContent[1]) # second line
songSpeedCounter = 1
songLineCounter = 1
songMaxLines = len(songContent)


player_score = 0

BASE_SCORE_INCREASE = 1

font = pygame.font.Font(None, 32)
text = font.render("Score: " + str(round(player_score, 3)), True, "white")

lane1_input_cooldown = INPUT_COOLDOWN
lane2_input_cooldown = INPUT_COOLDOWN
lane3_input_cooldown = INPUT_COOLDOWN
lane4_input_cooldown = INPUT_COOLDOWN

lane1_input_boolean = False
lane2_input_boolean = False
lane3_input_boolean = False
lane4_input_boolean = False

lane1_input = pygame.Vector2(90, screen.get_height() / 1.2)
lane2_input = pygame.Vector2(242, screen.get_height() / 1.2)
lane3_input = pygame.Vector2(394, screen.get_height() / 1.2)
lane4_input = pygame.Vector2(546, screen.get_height() / 1.2)
lane1_input_text = font.render("A", True, "white")
lane2_input_text = font.render("W", True, "white")
lane3_input_text = font.render("S", True, "white")
lane4_input_text = font.render("D", True, "white")

note_list = []
lane1_list = []
lane2_list = []
lane3_list = []
lane4_list = []

class Note: 
    def __init__ (self, colour, x, y, lane):
        self.size = NOTE_SIZE
        self.colour = colour
        self.x = x
        self.y = y
        self.lane = lane

    def update (self):
        self.y += NOTE_SPEED * delta_time

    def draw (self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size)
    
    def create_note (self):
        Note = pygame.Vector2(self.x, self.y)
        
        pygame.draw.circle(screen, self.colour, Note, self.size)

# inherits from Note class
class Lane1_Note(Note):
    def __init__ (self):
        super().__init__("red", 90, 0, 1)

class Lane2_Note(Note):
    def __init__ (self):
        super().__init__("yellow", 242, 0, 2)
    
class Lane3_Note(Note):
    def __init__ (self):
        super().__init__("green", 394, 0, 3)

class Lane4_Note(Note):
    def __init__ (self):
        super().__init__("pink", 546, 0, 4)
    
while running:
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
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
            if event.key == pygame.K_a and lane1_input_cooldown == 0 and len(lane1_list) > 0: 
                lane_note = None
                highestY = -1
                for note in lane1_list:
                    if (note.y > highestY):
                        highestY = note.y
                        lane_note = note

                if (lane_note and lane_note.y < lane1_input.y + 100 and lane_note.y > lane1_input.y - 100):

                    player_score += BASE_SCORE_INCREASE * SUPER_METER_MULT * COMBO_METER_MULT

                    if (superMeter < 100 and superMeterActive == False):
                        superMeter += SUPER_METER_INCREASE

                    COMBO_METER_MULT += COMBO_METER_INCREASE
                    comboMeter += 1
                    
                    lane1_list.remove(lane_note)
                    note_list.remove(lane_note)
                else:
                    player_score -= 1
                    COMBO_METER_MULT = 1
                    comboMeter = 0
                lane1_input_cooldown = INPUT_COOLDOWN

        # 2nd note
            if event.key == pygame.K_w and lane2_input_cooldown == 0: 
                lane_note = None
                highestY = -1
                for note in lane2_list:
                    if (note.y > highestY):
                        highestY = note.y
                        lane_note = note

                if (lane_note and lane_note.y < lane2_input.y + 100 and lane_note.y > lane2_input.y - 100):

                    player_score += BASE_SCORE_INCREASE * SUPER_METER_MULT * COMBO_METER_MULT

                    if (superMeter < 100 and superMeterActive == False):
                        superMeter += SUPER_METER_INCREASE

                    COMBO_METER_MULT += COMBO_METER_INCREASE
                    comboMeter += 1

                    lane2_list.remove(lane_note)
                    note_list.remove(lane_note)
                else:
                    player_score -= 1
                    COMBO_METER_MULT = 1
                    comboMeter = 0
                lane2_input_cooldown = INPUT_COOLDOWN

            # 3rd note
            if event.key == pygame.K_s and lane3_input_cooldown == 0: 
                lane_note = None
                highestY = -1
                for note in lane3_list:
                    if (note.y > highestY):
                        highestY = note.y
                        lane_note = note

                if (lane_note and lane_note.y < lane3_input.y + 100 and lane_note.y > lane3_input.y - 100):

                    player_score += BASE_SCORE_INCREASE * SUPER_METER_MULT * COMBO_METER_MULT

                    if (superMeter < 100 and superMeterActive == False):
                        superMeter += SUPER_METER_INCREASE
                    
                    COMBO_METER_MULT += COMBO_METER_INCREASE
                    comboMeter += 1

                    lane3_list.remove(lane_note)
                    note_list.remove(lane_note)
                else:
                    player_score -= 1
                    COMBO_METER_MULT = 1
                    comboMeter = 0
                lane3_input_cooldown = INPUT_COOLDOWN
            
            # 4th note
            if event.key == pygame.K_d and lane4_input_cooldown == 0: 
                lane_note = None
                highestY = -1
                for note in lane4_list:
                    if (note.y > highestY):
                        highestY = note.y
                        lane_note = note

                if (lane_note and lane_note.y < lane4_input.y + 100 and lane_note.y > lane4_input.y - 100):

                    player_score += BASE_SCORE_INCREASE * SUPER_METER_MULT * COMBO_METER_MULT

                    if (superMeter < 100):
                        superMeter += SUPER_METER_INCREASE

                    COMBO_METER_MULT += COMBO_METER_INCREASE
                    comboMeter += 1
                    
                    lane4_list.remove(lane_note)
                    note_list.remove(lane_note)
                else:
                    player_score -= 1
                    COMBO_METER_MULT = 1
                    comboMeter = 0
                lane4_input_cooldown = INPUT_COOLDOWN
            
            # Super Meter (SPACE)
            if event.key == pygame.K_SPACE and superMeter >= 100 and superMeterActive == False:
                superMeterActive = True
                SUPER_METER_MULT = 5


    if songOver:
        endingText = font.render("You finished with a score of: " + str(round(player_score, 3)), True, "white")
        screen.blit(endingText, (screen.get_width()/4, screen.get_height()/2))

        button_rect = pygame.Rect(screen.get_width() // 2 - 100, screen.get_height() // 2 + 50, 200, 50)
        pygame.draw.rect(screen, "green", button_rect)
        button_text = font.render("Play Again", True, "white")
        screen.blit(button_text, (button_rect.x, button_rect.y))

        button2_rect = pygame.Rect(screen.get_width() // 2 - 100, screen.get_height() // 2 + 150, 200, 50)
        pygame.draw.rect(screen, "green", button2_rect)
        button2_text = font.render("MainMenu", True, "white")
        screen.blit(button2_text, (button2_rect.x, button2_rect.y))
        
    else:
    
        screen.fill("mediumorchid4")

        pygame.draw.circle(screen, "brown2", lane1_input, NOTE_SIZE)
        pygame.draw.circle(screen, "lightgoldenrod", lane2_input, NOTE_SIZE)
        pygame.draw.circle(screen, "lightgreen", lane3_input, NOTE_SIZE)
        pygame.draw.circle(screen, "lightpink2", lane4_input, NOTE_SIZE)

        screen.blit(lane1_input_text, (90, screen.get_height() / 1.2))
        screen.blit(lane2_input_text, (242, screen.get_height() / 1.2))
        screen.blit(lane3_input_text, (394, screen.get_height() / 1.2))
        screen.blit(lane4_input_text, (546, screen.get_height() / 1.2))

        screen.blit(text, (screen.get_width()/2.35, screen.get_height() /1.1))

        superText = font.render("Super Meter: " + str(superMeter), True, "white")
        screen.blit(superText, (screen.get_width()/2.35, screen.get_height() /1.07))
        comboText = font.render("Combo Meter: " + str(comboMeter), True, "white")
        screen.blit(comboText, (screen.get_width()/2.35, screen.get_height() /1.04))


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
            j = 0
            for i in songContent[songLineCounter]:

                if (i == "0"):
                    if (j == 0):
                        new_note = Lane1_Note()
                        note_list.append(new_note)
                        lane1_list.append(new_note)
                    elif (j == 1):
                        new_note = Lane2_Note()
                        note_list.append(new_note)
                        lane2_list.append(new_note)
                    elif (j == 2):
                        new_note = Lane3_Note()
                        note_list.append(new_note)
                        lane3_list.append(new_note)
                    elif (j == 3):
                        new_note = Lane4_Note()
                        note_list.append(new_note)
                        lane4_list.append(new_note)
                j += 1


            songLineCounter += 1
            songSpeedCounter = 0

    songSpeedCounter += 1
     
     # the [:] signifies that its a copy of the original list because this snippet of code will delete objects from the actual list - slice notation start:stop:step
    for note in note_list[:]:
        note.update()
        note.draw()

        if (note.y > screen.get_height()):
            player_score -= 1
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
    
    if (superMeter >= 100 and superMeterActive == False):
        superMeter = 100
    if (superMeterActive == True and superMeter > 0):
        superMeter -= 0.5
    if (superMeter == 0 ):
        SUPER_METER_MULT = 1
        superMeterActive = False

    delta_time = clock.tick(60) / 1000 # 60 tps

song.close()
pygame.quit()
