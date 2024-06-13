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
import sys
next = pygame.image.load("Resources/next.png")
score = 15
current_system_pid = os.getpid()


check = False
next_level = False  # FOr going to next level
btn_run = True  # For switching off buttons
exit_val = False
running = True
def ninth_questions():
    pygame.init()  # Initialising pygame module
    window = pygame.display.set_mode((1700, 900))  # Window Setup
    pygame.display.set_caption("DiGi-Myth")  # Application title
    icon = pygame.image.load('Resources/icon.png')  # Setting game's ICON
    bg = pygame.image.load('Resources/background.jpg')  #
    pygame.display.set_icon(icon)  # Display icon

    ques = pygame.image.load("Resources/lvl_1_7.png")

    # FOr going to next level
    # For switching off buttons

    g = 0

    ############################################################################

    def button(screen, position, text):
        font = pygame.font.SysFont("Arial", 50)
        text_render = font.render(text, 1, (255, 0, 0))
        x, y, w, h = text_render.get_rect()
        x, y = position
        pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w, y), 5)
        pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
        pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
        pygame.draw.line(screen, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
        pygame.draw.rect(screen, (100, 100, 100), (x, y, w, h))
        return screen.blit(text_render, (x, y))

    def Marich():
        global check
        check = True
        global btn_run
        btn_run = False

    ###################################################################################
    playerImg = pygame.image.load('Resources/Ram2.png')
    playerX = 0  # Ram's character setup
    playerY = 400

    arrowp = pygame.image.load('Resources/resized.png')
    player1X = 400  # Arrow's Setup
    player1Y = 490

    monster = pygame.image.load('Resources/monster.png')
    monX = 1400
    monY = 350
    monter2 = pygame.image.load('Resources/monster.png')
    MonX2 = 1100
    MonY2 = 350

    monster3 = pygame.image.load('krishna.png')
    MonX3 = 800
    MonY3 = 350

    blood = pygame.image.load('Resources/bloodstain.png')
    bx = 1400
    by = 470

    mcq1 = pygame.image.load("Resources/mcq16.png")
    mcq2 = pygame.image.load("Resources/mcq17.png")
    mcq3 = pygame.image.load("Resources/mcq18.png")

    #####################################################################################

    def Key_monitor():
        global next_level

        def show(key):
            global exit_val

            global running


            try:
                if key == key.shift:
                    if next_level:
                        running = False
                        exit_val = True
                        exit()
            except Exception:
                _ = Exception
        with Listener(on_press=show) as listener:
            listener.join()

    key_mon = Thread(target=Key_monitor)
    key_mon.start()

    def start_song():
        time.sleep(1)
        playsound('Resources/Theme.mp3')

    def next_level():
        global check
        global next_level

        while True:
            if check:
                time.sleep(13)
                next_level = True
                break

    nxr = Thread(target=next_level)
    nxr.start()

    def next_audio():
        time.sleep(13)
        playsound("next.mp3")

    def laugh():
        time.sleep(1)
        playsound('Resources/laughing.wav')



    def scream():
        playsound('Resources/scream.mp3')

    def player():  # Player's function
        window.blit(playerImg, (playerX, playerY))

    def arrow():  # Arrow's function
        window.blit(arrowp, (player1X, player1Y))

    def monsterR():
        window.blit(monster, (monX, monY))
        window.blit(monter2, (MonX2, MonY2))
        window.blit(monster3, (MonX3, MonY3))

    def bloodstain():
        window.blit(blood, (bx, by))



    ######################################################################################

    screamTh = Thread(target=scream)  # The demons scream thread
    sc = 0  # for starting the Scream thread

    demon_laugh = Thread(target=laugh)
    demon_laugh.start()

    nxt_aud = Thread(target=next_audio)
    global over
    over = False
    ovr = 1  # For Playing game over audio
    global score
    global current_system_pid
    global btn_run
    global loading
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
                    key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                    if key_to_start:
                        over = True
                        btn_run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if b1.collidepoint(pygame.mouse.get_pos()):
                        Marich()
                    elif b2.collidepoint(pygame.mouse.get_pos()):
                        over = True
                        btn_run = False
                    elif b3.collidepoint(pygame.mouse.get_pos()):
                        over = True
                        btn_run = False


        window.blit(bg, (0, 0))
        player()

        monsterR()

        b1 = button(window, (1450, 240), "Viradha")  # 1640 200
        b2 = button(window, (1100, 240), "Kaushalya")
        b3 = button(window, (850, 240), "Krishna")
        window.blit(ques , (100 , -270))
        window.blit(mcq1, (750, 180))
        window.blit(mcq2, (1040, 180))
        window.blit(mcq3, (1370, 180))

        score_dis = button(window, (0, 0), str(score))
        if over:
            window.blit(loading, (0, 0))

            pygame.display.update()
            if ovr == 1:
                running = False

                playsound("Resources/game_over_laugh.mp3")
                ovr += 1

        if check:
            arrow()
            if player1X != 1200:
                player1X += 50
            if player1X == 1200:
                bloodstain()


                if sc == 0:
                    screamTh.start()
                    score += 1
                    try:
                        theme = Thread(target=start_song)

                        theme.start()
                        nxt_aud.start()

                    except Exception:
                        _ = Exception
                    sc = 2
        pygame.display.update()
ninth_questions()


