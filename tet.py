from threading import *
from playsound import playsound
import time
import pygame
from pygame import mixer
import subprocess
from pynput.keyboard import Key, Listener
from gtts import gTTS
import os
import psutil
score = 0
over = False
i = 0  # flag variable for proceeding to next level 
check = False
btn_run = True
exit_val = False
running = True
stop_song = 0

loading = pygame.image.load("Resources/wrong.jpg")
def background():
    playsound("background.mp3")

_bg = Thread(target=background)
_bg.start()

current_system_pid = os.getpid()
def First_level():
            pygame.init() # Initialising pygame module
            window = pygame.display.set_mode((1700,900)) # Window Setup
            pygame.display.set_caption("DiGi-Myth")  # Application title
            icon = pygame.image.load('Resources/icon.png') # Setting game's ICON
            bg = pygame.image.load('Resources/background.jpg') #
            pygame.display.set_icon(icon) # Display icon
            ques = pygame.image.load('Resources/Q1.png')

            next_level = False

             # FOr going to next level
            # For switching off buttons

            g = 0
            ques  = pygame.image.load("Resources/lvl_1_1.png")
            ############################################################################



            def button(screen, position, text):
                font = pygame.font.SysFont("Arial", 50)
                text_render = font.render(text, 1, (255, 0, 0))
                x, y, w , h = text_render.get_rect()
                x, y = position
                pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
                pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
                pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
                pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
                pygame.draw.rect(screen, (100, 100, 100), (x, y, w , h))
                return screen.blit(text_render, (x, y))
            def Marich():
                global check
                check = True
                global btn_run
                btn_run = False


            ###################################################################################
            playerImg = pygame.image.load('Resources/Ram2.png')
            playerX=0                                        # Ram's character setup
            playerY=400

            arrowp = pygame.image.load('Resources/resized.png')
            player1X=400             # Arrow's Setup
            player1Y=490

            monster =  pygame.image.load('Resources/monster.png')
            monX = 1400
            monY = 400
            monter2 =  pygame.image.load('Resources/monster.png')
            MonX2 = 1100
            MonY2 = 400

            monster3 =  pygame.image.load('Resources/monster.png')
            MonX3 = 800
            MonY3 = 400



            blood = pygame.image.load('Resources/bloodstain.png')
            bx = 1400
            by = 450

            overscr = pygame.image.load('Resources/gameover.jpg')
            mcq1 = pygame.image.load('Resources/mcq1.png')
            mcq2 = pygame.image.load('Resources/mcq2.png')
            mcq3 = pygame.image.load('Resources/mcq3.png')

            #####################################################################################





            def start_song():
                time.sleep(1)
                playsound('Resources/Theme.mp3')
            def next_level():
                global check
                global next_level

                while True:
                    if check:
                        time.sleep(11)
                        next_level = True
                        break
            nxr = Thread(target = next_level)
            nxr.start()

            def next_audio():
                time.sleep(13)
                playsound("next.mp3")
            def laugh():
                time.sleep(1)
                playsound('Resources/laughing.wav')
            def arrow_sound():
                playsound('Resources/wind.wav')
            def scream():
               playsound('Resources/scream.mp3')
            def player(): # Player's function
                window.blit(playerImg,(playerX,playerY))
            def arrow(): # Arrow's function
                window.blit(arrowp,(player1X, player1Y))
            def monsterR():
               window.blit(monster,(monX,monY))
               window.blit(monter2 , (MonX2,MonY2))
               window.blit(monster3 ,(MonX3,MonY3))
            def bloodstain():
                window.blit(blood , (bx,by))
            def gameover():
                window.blit()

            ######################################################################################

            screamTh = Thread(target=scream)  # The demons scream thread
            sc = 0 # for starting the Scream thread


            demon_laugh = Thread(target=laugh)
            demon_laugh.start()

            nxt_aud = Thread(target=next_audio)
            global over



            ovr = 1 # For Playing game over audio



            def key_monitor():
                 def show(key):

                    global exit_val
                    global running
                    global next_level

                    try:

                        if next_level:

                            if key == key.shift:
                                running = False
                                exit_val = True
                                exit()
                    except:
                        _ = Exception




                 with Listener(on_press=show) as listener:
                       listener.join()
            key_mon = Thread(target=key_monitor)
            key_mon.start()

            global score
            global current_system_pid
            global btn_run
            global  loading
            global running

            while running:

                   for event in pygame.event.get():
                      if event.type == pygame.QUIT:
                          print("Thanks for playing ")
                          ThisSystem = psutil.Process(current_system_pid)
                          ThisSystem.terminate()
                      if btn_run:
                          if event.type == pygame.KEYDOWN:
                              if event.key == pygame.K_ESCAPE:
                                  Marich()
                                  btn_run = False
                              key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                              if key_to_start:
                                  btn_run = False
                                  over = True
                          if event.type == pygame.MOUSEBUTTONDOWN:
                              if b1.collidepoint(pygame.mouse.get_pos()):
                                  Marich()

                              elif b2.collidepoint(pygame.mouse.get_pos()):
                                  btn_run = False
                                  over = True
                              elif b3.collidepoint(pygame.mouse.get_pos()):
                                  btn_run = False
                                  over = True

                   window.blit(bg, (0, 0))
                   player()


                   monsterR()
                   b1 = button(window, (1450, 300), "Marich")  # 1640 200
                   b2 = button(window, (1100, 300), "Subahu")
                   b3 = button(window, (850, 300), "Tarka")

                   window.blit(ques , (100 , -270))

                   window.blit(mcq1 , (1240,270))
                   window.blit(mcq2 , (900,270))
                   window.blit(mcq3, (650, 270))
                   score_dis = button(window , (0,0) , str(score))
                   if over:
                       window.blit(loading , (0,0))

                       pygame.display.update()
                       if ovr == 1:
                           running = False

                           playsound("Resources/game_over_laugh.mp3")
                           ovr +=1


                   if check:
                       arrow()
                       if player1X != 1200:
                         player1X += 50
                       if player1X == 1200:
                         bloodstain()


                         if sc == 0:
                          screamTh.start()
                          score +=1

                          try:
                              theme = Thread(target=start_song)

                              theme.start()
                              nxt_aud.start()

                          except Exception:
                              _ = Exception
                          sc = 2
                   pygame.display.update()



First_level()