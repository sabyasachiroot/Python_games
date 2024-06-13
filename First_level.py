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
score = 0          # 
qu = 0

stop_song = 0

loading = pygame.image.load("Resources/wrong.jpg")
def background():
    playsound("background.mp3")

_bg = Thread(target=background)
_bg.start()

current_system_pid = os.getpid()
def questions():

        def show(key):

            global qu
            try:
                if qu == 1:
                    if key == key.tab:
                        playsound("Question1.mp3")
                if qu == 2:
                    if key == key.tab:
                        playsound("Question2.mp3")
                if qu == 3:
                    if key == key.tab:
                      playsound("Question3.mp3")
                if qu == 4:
                    if key == key.tab:
                        playsound("Question4.mp3")
                if qu == 5:
                    if key == key.tab:
                        playsound("Question5.mp3")
                if qu == 6:
                    if key == key.tab:
                        playsound("Question6.mp3")
                if qu == 7:
                    if key == key.tab:
                      playsound("Question7.mp3")
                if qu == 8:
                    if key == key.tab:
                        playsound("Question8.mp3")
                if qu == 9:
                    if key == key.tab:
                        playsound("Question9.mp3")
                if qu == 10:
                    if key == key.tab:
                        playsound("Question10.mp3")
            except Exception:
                _ = Exception


        with Listener(on_press=show) as listener:
            listener.join()

ques = Thread(target = questions)
ques.start()
def appearance():
    pygame.init()  # Initialising pygame module
    window = pygame.display.set_mode((1700, 900))  # Window Setup
    pygame.display.set_caption("DiGi-Myth")  # Application title
    icon = pygame.image.load('Resources/icon.png')  # Setting game's ICON
    bg1 = pygame.image.load('Resources/launcher_bg.jpg')  #
    play = pygame.image.load('Resources/play_button.png')

    pygame.display.set_icon(icon)  # Display icon

    running = True
    global current_system_pid

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



    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Thanks for playing ")
                ThisSystem = psutil.Process(current_system_pid)
                ThisSystem.terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                if key_to_start:
                   running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    running = False


        window.blit(bg1, (0, 0))
        b1 = button(window, (800, 800), "    Play Now    ")

        window.blit(play , (720,780))

        pygame.display.update()
appearance()
qu +=1
over = False
i = 0  # flag variable for proceeding to next level 
check = False
btn_run = True
exit_val = False
running = True
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
qu +=1

running = True

check = False
next_level = False
btn_run = True  # For switching off buttons
exit_val = False
def Second_level():
    pygame.init()  # Initialising pygame module
    window = pygame.display.set_mode((1700, 900))  # Window Setup
    pygame.display.set_caption("DiGi-Myth")  # Application title
    icon = pygame.image.load('Resources/icon.png')  # Setting game's ICON
    bg = pygame.image.load('Resources/background_2.jpg')  #
    pygame.display.set_icon(icon)  # Display icon
    s = 0

    ques = pygame.image.load("Resources/lvl_1_2.png")
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

    def Tarka():
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
    monY = 400
    monter2 = pygame.image.load('Resources/monster.png')
    MonX2 = 1100
    MonY2 = 400

    monster3 = pygame.image.load('Resources/monster.png')
    MonX3 = 800
    MonY3 = 400

    blood = pygame.image.load('Resources/bloodstain.png')
    bx = 800
    by = 470



    overscr = pygame.image.load('Resources/gameover.jpg')

    #####################################################################################
    mcq1 = pygame.image.load("Resources/mcq3.png")
    mcq2 = pygame.image.load("Resources/mcq4.jpg")
    mcq3 =  pygame.image.load("Resources/mcq5.jpg")




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
    def start_song():
        playsound('Resources/Theme.mp3')

    def laugh():
        time.sleep(1)
        playsound('Resources/laughing.wav')


    def next_audio():
        time.sleep(8)
        playsound("next.mp3")

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


    def Key_monitor():
        global next_level
        def show(key):
            try:

                if next_level:
                    if key == key.shift:
                        global running
                        running = False
                        exit()
            except Exception:
                _ = Exception

        with Listener(on_press=show) as listener:
            listener.join()

    key_mon = Thread(target=Key_monitor)
    key_mon.start()
    global over
    over = False
    ovr = 1  # For Playing game over audio
    global running
    global score
    global current_system_pid
    global btn_run
    i = 0
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Thanks for playing ")
                ThisSystem = psutil.Process(current_system_pid)
                ThisSystem.terminate()
            if btn_run:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        over = True
                        btn_run = False
                    key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                    if key_to_start:
                        over = True
                        btn_run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if b1.collidepoint(pygame.mouse.get_pos()):
                        over = True
                        btn_run = False
                    elif b2.collidepoint(pygame.mouse.get_pos()):
                        over = True
                        btn_run = False
                    elif b3.collidepoint(pygame.mouse.get_pos()):
                        Tarka()



        window.blit(bg, (0, 0))

        player()

        monsterR()

        b1 = button(window, (1450, 300), "Vibhisan")  # 1640 200
        b2 = button(window, (1100, 300), "Laxman")
        b3 = button(window, (850, 300), "Tarka")
        window.blit(mcq1 , (650,270))
        window.blit(mcq2, (1100, 270))
        window.blit(mcq3 , (1440 , 270))

        window.blit(ques , (100,-270))
        score_dis = button(window , (0,0) , str(score))

        if over:
            window.blit(loading, (0, 0))
            pygame.display.update()
            if ovr == 1:

                running = False
                playsound("Resources/game_over_laugh.mp3")
                ovr += 1
        if i == 0:
            pygame.display.update()

            i +=1
        if check:
            arrow()
            if player1X != 650:
                player1X += 50
            if player1X == 650:
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

Second_level()
qu +=1
running = True
next_level = False
check = False
over = False
btn_run = True  # For switching off buttons
exit_val = False
F = 0
def Third_level():
    pygame.init()  # Initialising pygame module
    window = pygame.display.set_mode((1700, 900))  # Window Setup
    pygame.display.set_caption("DiGi-Myth")  # Application title
    icon = pygame.image.load('Resources/icon.png')  # Setting game's ICON
    bg = pygame.image.load('Resources/Question3_bg.jpg')  #
    pygame.display.set_icon(icon)  # Display icon

    ques = pygame.image.load("Resources/lvl_1_3.png")

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

    def Demon_clan():
        global check
        check = True
        global btn_run
        btn_run = False

    ###################################################################################
    Ravan = pygame.image.load("Resources/ravana.png")
    Rx = 400
    Ry = 300
    Game_finish = pygame.image.load("Resources/yes-you-are-correct.jpg")
    gx = 300
    gy = 50

    overscr = pygame.image.load('Resources/gameover.jpg')

    mcq1 =  pygame.image.load("Resources/mcq6.jpg")
    mcq2 =  pygame.image.load("Resources/mcq7.jpg")
    mcq3 =  pygame.image.load("Resources/mcq8.jpg")
    #####################################################################################




    def Key_monitor():
        global next_level

        def show(key):

            try:


                if key == key.shift:
                    if  next_level:
                        global running
                        running = False
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
        global  next_level

        while True:
            if check:
                time.sleep(12)
                next_level = True
                break

    nxr = Thread(target=next_level)
    nxr.start()

    def next_audio():
        time.sleep(10)
        playsound("next.mp3")


    def Ravana():
        window.blit(Ravan, (Rx, Ry))

    def correct():
        window.blit(Game_finish, (gx, gy))

    ######################################################################################

    sc = 1  # for starting the Scream thread

    sn0 = 0
    nxt_aud = Thread(target=next_audio)
    global over

    ovr = 1  # For Playing game over audio
    i = 0  # for incremnting sc
    global running
    global score
    global current_system_pid
    global btn_run
    global loading
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Thanks for playing ")
                ThisSystem = psutil.Process(current_system_pid)
                ThisSystem.terminate()
            if btn_run:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Demon_clan()
                    key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                    if key_to_start:
                        Demon_clan()
                        btn_run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if b1.collidepoint(pygame.mouse.get_pos()):
                        over = True
                        btn_run = False
                    elif b2.collidepoint(pygame.mouse.get_pos()):
                        over = True
                        btn_run = False
                    elif b3.collidepoint(pygame.mouse.get_pos()):
                        Demon_clan()


        window.blit(bg, (0, 0))
        Ravana()

        b1 = button(window, (850, 400), " 3. Demon Clan ")  # 1640 200
        b2 = button(window, (850, 300), " 2. sun clan ")
        b3 = button(window, (850, 200), " 1. Rishi Pulatsya ")
        window.blit(mcq1 , (850,390))
        window.blit(mcq2 , (850, 190))
        window.blit(mcq3 , (850,290))
        window.blit(ques, (100, -310))

        score_dis = button(window , (0,0),str(score))
        if check:
            correct()
            if i == 0:
                sc = 0
                i += 1

        if over:
            window.blit(loading ,(0,0))
            pygame.display.update()
            if ovr == 1:
                running = False

                playsound("Resources/game_over_laugh.mp3")
                ovr += 1

        if sc == 0:
            score +=1
            try:
                theme = Thread(target=start_song)

                theme.start()
                nxt_aud.start()

            except Exception:
                _ = Exception

            sc += 2
        pygame.display.update()

Third_level()
qu +=1

running = True
check = False
next_level = False  # FOr going to next level
btn_run = True  # For switching off buttons
exit_val = False
def Fourth_qestion():
    pygame.init()  # Initialising pygame module
    window = pygame.display.set_mode((1700, 900))  # Window Setup
    pygame.display.set_caption("DiGi-Myth")  # Application title
    icon = pygame.image.load('Resources/icon.png')  # Setting game's ICON
    bg = pygame.image.load('Resources/Question3_bg.jpg')  #
    pygame.display.set_icon(icon)  # Display icon
    s = 0


    ques = pygame.image.load("Resources/lvl_1_4.png")

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

    def Demon_clan():
        global check
        check = True
        global btn_run
        btn_run = False

    ###################################################################################

    Rx = 400
    Ry = 200
    Game_finish = pygame.image.load("Resources/yes-you-are-correct.jpg")
    gx = 300
    gy = 50



    overscr = pygame.image.load('Resources/gameover.jpg')

    #####################################################################################

    mcq1 = pygame.image.load("Resources/mcq9.png")
    mcq2 = pygame.image.load("Resources/mcq4.jpg")
    mcq3 = pygame.image.load("Resources/mcq10.png")

    lax = pygame.image.load("Resources/lacman.png")
    han = pygame.image.load("Resources/hanuman.png")
    ram = pygame.image.load("Resources/Ram2.png")
    def Key_monitor():
        global next_level

        def show(key):
            try:

                if key == key.shift:
                    if next_level:
                        global running
                        running = False
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
                time.sleep(12)
                next_level = True
                break

    nxr = Thread(target=next_level)
    nxr.start()

    def next_audio():
        time.sleep(10)
        playsound("next.mp3")



    def correct():
        window.blit(Game_finish, (gx, gy))

    ######################################################################################

    sc = 1  # for starting the Scream thread

    sn0 = 0
    nxt_aud = Thread(target=next_audio)
    global over
    over = False
    ovr = 1  # For Playing game over audio
    i = 0  # for incremnting sc
    global running
    global current_system_pid
    global score
    global btn_run
    global loading
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Thanks for playing ")
                ThisSystem = psutil.Process(current_system_pid)
                ThisSystem.terminate()
            if btn_run:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Demon_clan()
                    key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                    if key_to_start:
                        over = True
                        btn_run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if b1.collidepoint(pygame.mouse.get_pos()):
                        over = True
                        btn_run = False

                    elif b2.collidepoint(pygame.mouse.get_pos()):
                          Demon_clan()
                    elif b3.collidepoint(pygame.mouse.get_pos()):
                        over = True
                        btn_run = False


        window.blit(bg, (0, 0))

        b1 = button(window,(160, 350) , " 3. Rama ")  # 1640 200
        b2 = button(window, (630, 380), " 2. Laxmana ")
        b3 = button(window, (1110, 380), " 1. Hanumana ")
        window.blit(ques , (127 , -290))
        window.blit(mcq1, (130, 280))
        window.blit(mcq2, (600, 350))
        window.blit(mcq3, (1100, 300))
        window.blit(lax , (550 , 480))
        window.blit(han , (1000,450))
        window.blit(ram ,(110,400))
        score_dis = button(window,(0,0),str(score))
        if check:
            correct()
            if i == 0:
                sc = 0
                i += 1

        if over:
            window.blit(loading, (0, 0))
            pygame.display.update()

            if ovr == 1:

                running = False
                playsound("Resources/game_over_laugh.mp3")
                ovr += 1
        if exit_val:
            running = False
        if sc == 0:

            try:
                score +=1
                theme = Thread(target=start_song)

                theme.start()
                nxt_aud.start()

            except Exception:
                _ = Exception

            sc += 2
        pygame.display.update()

Fourth_qestion()

qu +=1


running = True
check = False
next_level = False  # FOr going to next level
btn_run = True  # For switching off buttons
exit_val = False
def Fifth_question():
    pygame.init()  # Initialising pygame module
    window = pygame.display.set_mode((1700, 900))  # Window Setup
    pygame.display.set_caption("DiGi-Myth")  # Application title
    icon = pygame.image.load('Resources/icon.png')  # Setting game's ICON
    bg = pygame.image.load('Resources/Question3_bg.jpg')  #
    pygame.display.set_icon(icon)  # Display icon
    s = 0
    ques = pygame.image.load("Resources/lvl_1_10.png")
    _luv = pygame.image.load("Luv_kush.png")
    _lax = pygame.image.load("lax_bha.png")
    _luv_sh = pygame.image.load("Resources/luv_bha.png")
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

    def Shisupal():
        global check
        check = True
        global btn_run
        btn_run = False

    ###################################################################################

    Game_finish = pygame.image.load("Resources/yes-you-are-correct.jpg")
    gx = 300
    gy = 50

    mcq1 = pygame.image.load("Resources/mcq22.png")
    mcq2 = pygame.image.load("Resources/mcq23.jpg")
    mcq3 = pygame.image.load("Resources/mcq23.png")

    overscr = pygame.image.load('Resources/gameover.jpg')

    #####################################################################################

    def Key_monitor():
        global next_level

        def show(key):
            try:

                if key == key.shift:
                    if next_level:
                        global running
                        running = False
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
                time.sleep(12)
                next_level = True
                break

    nxr = Thread(target=next_level)
    nxr.start()

    def next_audio():
        global running
        time.sleep(10)

        playsound("next.mp3")

    def correct():
        window.blit(Game_finish, (gx, gy))

    ######################################################################################

    sc = 1  # for starting the Scream thread

    sn0 = 0
    nxt_aud = Thread(target=next_audio)
    global over
    over = False
    ovr = 1  # For Playing game over audio
    i = 0  # for incremnting sc
    global running
    global score
    global btn_run
    global current_system_pid
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Thanks for playing ")
                ThisSystem = psutil.Process(current_system_pid)
                ThisSystem.terminate()
            if btn_run:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Shisupal()
                    key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                    if key_to_start:
                        over = True
                        btn_run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if b1.collidepoint(pygame.mouse.get_pos()):
                        over = True
                        btn_run = False
                    elif b2.collidepoint(pygame.mouse.get_pos()):
                        Shisupal()
                    elif b3.collidepoint(pygame.mouse.get_pos()):
                        over = True
                        btn_run = False

        window.blit(bg, (0, 0))
        window.blit(ques, (127, -290))
        b1 = button(window, (630, 300), " 3. Laxma ")  # 1640 200
        b2 = button(window, (150, 450), " 2. Lav and  ")
        b3 = button(window, (1200, 300), " 1.  Shatrughan a")
        window.blit(mcq1, (130, 380))
        window.blit(mcq2 , (600,220))
        window.blit(mcq3 , (1100 , 230))

        window.blit(_luv , (100,500))
        window.blit(_lax ,(500,300))
        window.blit(_luv_sh , (1100 , 430))
        score_dis = button(window, (0, 0), str(score))
        if check:
            correct()
            if i == 0:
                sc = 0
                i += 1

        if over:
            window.blit(loading, (0, 0))

            pygame.display.update()
            if ovr == 1:
                playsound("Resources/game_over_laugh.mp3")
                running = False
                ovr += 1

        if sc == 0:

            try:
                score += 1
                theme = Thread(target=start_song)
                theme.start()
                nxt_aud.start()



            except Exception:
                _ = Exception

            sc += 2
        pygame.display.update()

Fifth_question()
qu +=1
running = True
check = False
next_level = False  # FOr going to next level
btn_run = True  # For switching off buttons
exit_val = False
def Sixth_question():
    pygame.init()  # Initialising pygame module
    window = pygame.display.set_mode((1700, 900))  # Window Setup
    pygame.display.set_caption("DiGi-Myth")  # Application title
    icon = pygame.image.load('Resources/icon.png')  # Setting game's ICON
    bg = pygame.image.load('Resources/background_4.jpg')  #
    pygame.display.set_icon(icon)  # Display icon

    # FOr going to next level
    # For switching off buttons

    g = 0
    ques = pygame.image.load("Resources/lvl_1_5.png")
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

    def Surpanakha():

        global check
        check = True
        global btn_run
        btn_run = False

    ###################################################################################
    playerImg = pygame.image.load('Resources/Ram2.png')
    playerX = 0  # Ram's character setup
    playerY = 300

    arrowp = pygame.image.load('Resources/resized.png')
    player1X = 400  # Arrow's Setup
    player1Y = 400

    monster = pygame.image.load('Resources/monster.png')
    monX = 1400
    monY = 320
    monter2 = pygame.image.load('Resources/monster.png')
    MonX2 = 1100
    MonY2 = 320

    monster3 = pygame.image.load('Resources/monster.png')
    MonX3 = 800
    MonY3 = 320

    blood = pygame.image.load('Resources/bloodstain.png')
    bx = 800
    by = 380

    mcq1 = pygame.image.load("Resources/mcq11.png")
    mcq2 = pygame.image.load("Resources/mcq1.png")
    mcq3 = pygame.image.load("Resources/mcq12.png")

    #####################################################################################
    def Key_monitor():
        global next_level

        def show(key):
            try:

                if next_level:

                    if key == key.shift:
                        global running
                        running = False
                        exit()
            except Exception:
                _ = Exception

        with Listener(on_press=show) as listener:
            listener.join()

    key_mon = Thread(target=Key_monitor)
    key_mon.start()
    def next_level():
        global check
        global next_level

        while True:
            if check:
                time.sleep(12)
                next_level = True
                break

    nxr = Thread(target=next_level)
    nxr.start()

    def start_song():
        time.sleep(1)
        playsound('Resources/Theme.mp3')

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

    global over
    over = False
    ovr = 1  # For Playing game over audio
    global score
    global running
    global current_system_pid
    global btn_run
    global loading
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Thanks for playing ")
                ThisSystem = psutil.Process(current_system_pid)
                ThisSystem.terminate()
            if btn_run:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Surpanakha()
                    key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                    if key_to_start:
                        over = True
                        btn_run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if b1.collidepoint(pygame.mouse.get_pos()):
                        over = True
                        btn_run = False
                    elif b2.collidepoint(pygame.mouse.get_pos()):
                        over = True
                        btn_run = False
                    elif b3.collidepoint(pygame.mouse.get_pos()):
                        Surpanakha()


        window.blit(bg, (0, 0))
        player()

        monsterR()

        b1 = button(window, (1440, 240), "Marich")  # 1640 200
        b2 = button(window, (1100, 240), "Subahu")
        b3 = button(window, (800, 240), "Surpnakha")

        window.blit(mcq1, (1050, 170))
        window.blit(mcq2, (1260, 220))
        window.blit(mcq3, (720, 170))
        window.blit(ques , (100 , -270))
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
            if player1X != 650:
                player1X += 50
            if player1X == 650:
                bloodstain()


                if sc == 0:
                    screamTh.start()

                    score += 1
                    try:
                        theme = Thread(target=start_song)

                        theme.start()
                        nxt_aud = Thread(target=next_audio)
                        nxt_aud.start()

                    except Exception:
                        _ = Exception
                    sc += 2
        pygame.display.update()

Sixth_question()
qu +=1
running = True
check = False
next_level = False  # FOr going to next level
btn_run = True  # For switching off buttons
exit_val = False

def Seventh_Question():
    pygame.init()  # Initialising pygame module
    window = pygame.display.set_mode((1700, 900))  # Window Setup
    pygame.display.set_caption("DiGi-Myth")  # Application title
    icon = pygame.image.load('Resources/icon.png')  # Setting game's ICON
    bg = pygame.image.load('Resources/Question3_bg.jpg')  #
    pygame.display.set_icon(icon)  # Display icon
    s = 0

    ques = pygame.image.load("Resources/lvl_1_9.png")

    mcq1 = pygame.image.load("Resources/mcq19.png")
    mcq2 = pygame.image.load("Resources/mcq20.png")
    mcq3 = pygame.image.load("Resources/mcq21.png")


    img1 = pygame.image.load("Sita.png")
    img2 = pygame.image.load("kau.png")
    img3 = pygame.image.load("bh.png")
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

    def Demon_clan():
        global check
        check = True
        global btn_run
        btn_run = False

    ###################################################################################

    Rx = 400
    Ry = 200
    Game_finish = pygame.image.load("Resources/yes-you-are-correct.jpg")
    gx = 300
    gy = 50



    overscr = pygame.image.load('Resources/gameover.jpg')

    #####################################################################################





    def Key_monitor():
        global next_level

        def show(key):
            try:

                if key == key.shift:
                    if next_level:
                        global running
                        running = False
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
                time.sleep(12)
                next_level = True
                break

    nxr = Thread(target=next_level)
    nxr.start()

    def next_audio():
        time.sleep(10)
        playsound("next.mp3")



    def correct():
        window.blit(Game_finish, (gx, gy))

    ######################################################################################

    sc = 1  # for starting the Scream thread

    sn0 = 0
    nxt_aud = Thread(target=next_audio)
    global over
    over = False
    ovr = 1  # For Playing game over audio
    i = 0  # for incremnting sc
    global running
    global current_system_pid
    global score
    global btn_run
    global loading
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Thanks for playing ")
                ThisSystem = psutil.Process(current_system_pid)
                ThisSystem.terminate()
            if btn_run:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Demon_clan()
                    key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                    if key_to_start:
                        over = True
                        btn_run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if b1.collidepoint(pygame.mouse.get_pos()):
                        over = True
                        btn_run = False

                    elif b2.collidepoint(pygame.mouse.get_pos()):
                        over = True
                        btn_run = False
                    elif b3.collidepoint(pygame.mouse.get_pos()):

                        Demon_clan()


        window.blit(bg, (0, 0))

        b1 = button(window, (500, 400), " 3. Kaushalya ")  # 1640 200
        b2 = button(window, (850, 300), " 2. Bharat ")
        b3 = button(window, (180, 400), " 1. Sita ")
        window.blit(ques , (127 , -290))
        window.blit(mcq1, (150, 320))
        window.blit(mcq3, (830, 240))

        window.blit(mcq2, (480, 325))

        window.blit(img1 , (100,400))
        window.blit(img2 , (360,470))
        window.blit(img3 , (780 , 400))
        score_dis = button(window,(0,0),str(score))
        if check:
            correct()
            if i == 0:
                sc = 0
                i += 1

        if over:
            window.blit(loading, (0, 0))
            pygame.display.update()

            if ovr == 1:

                running = False
                playsound("Resources/game_over_laugh.mp3")
                ovr += 1
        if exit_val:
            running = False
        if sc == 0:

            try:
                score +=1
                theme = Thread(target=start_song)

                theme.start()
                nxt_aud.start()

            except Exception:
                _ = Exception

            sc += 2
        pygame.display.update()

Seventh_Question()
qu +=1
running = True
check = False
next_level = False  # FOr going to next level
btn_run = True  # For switching off buttons
exit_val = False
def eigth_question():
    pygame.init()  # Initialising pygame module
    window = pygame.display.set_mode((1700, 900))  # Window Setup
    pygame.display.set_caption("DiGi-Myth")  # Application title
    icon = pygame.image.load('Resources/icon.png')  # Setting game's ICON
    bg = pygame.image.load('Resources/background_4.jpg')  #
    pygame.display.set_icon(icon)  # Display icon

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

    def Surpanakha():
        global next_level
        next_level = True
        global check
        check = True
        global btn_run
        btn_run = False

    ###################################################################################
    playerImg = pygame.image.load('Resources/Ram2.png')
    playerX = 0  # Ram's character setup
    playerY = 300

    arrowp = pygame.image.load('Resources/resized.png')
    player1X = 400  # Arrow's Setup
    player1Y = 400

    monster = pygame.image.load('Resources/monster.png')
    monX = 1400
    monY = 320
    monter2 = pygame.image.load('Resources/monster.png')
    MonX2 = 1100
    MonY2 = 320

    monster3 = pygame.image.load('Resources/monster.png')
    MonX3 = 800
    MonY3 = 320

    blood = pygame.image.load('Resources/bloodstain.png')
    bx = 800
    by = 380

    ques = pygame.image.load("Resources/lvl_1_6.png")

    mcq1 = pygame.image.load("Resources/mcq13.png")
    mcq2 = pygame.image.load("Resources/mcq14.png")
    mcq3 = pygame.image.load("Resources/mcq15.png")
    #####################################################################################
    def Key_monitor():
        global next_level

        def show(key):

            try:

                if key == key.shift:
                    if next_level:
                        global running
                        running = False
                        exit()
            except Exception:
                _ = Exception
        with Listener(on_press=show) as listener:
            listener.join()

    key_mon = Thread(target=Key_monitor)
    key_mon.start()
    def next_level1():
        global check
        global next_level

        while True:
            if check:
                time.sleep(12)
                next_level = True
                break

        nxr = Thread(target=next_level1)
        nxr.start()

    def start_song():
        time.sleep(1)
        playsound('Resources/Theme.mp3')

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

    global over
    over = False
    ovr = 1  # For Playing game over audio
    global score
    global running
    global current_system_pid
    global btn_run
    global  loading
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Thanks for playing ")
                ThisSystem = psutil.Process(current_system_pid)
                ThisSystem.terminate()
            if btn_run:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Surpanakha()
                    key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                    if key_to_start:
                        over = True
                        btn_run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if b1.collidepoint(pygame.mouse.get_pos()):
                        over = True
                        btn_run = False
                    elif b2.collidepoint(pygame.mouse.get_pos()):
                        over = True
                        btn_run = False
                    elif b3.collidepoint(pygame.mouse.get_pos()):
                        Surpanakha()


        window.blit(bg, (0, 0))
        player()

        monsterR()

        b1 = button(window, (1440, 240), "Dushan")  # 1640 200
        b2 = button(window, (1170, 240), "Yashoda")
        b3 = button(window, (800, 240), "Kumbkaran")
        window.blit(ques ,(100 , -270))

        window.blit(mcq1, (780, 170))
        window.blit(mcq2, (1100, 198))
        window.blit(mcq3, (1400, 170))

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
            if player1X != 650:
                player1X += 50
            if player1X == 650:
                bloodstain()


                if sc == 0:
                    screamTh.start()

                    score += 1
                    try:
                        theme = Thread(target=start_song)

                        theme.start()
                        nxt_aud = Thread(target=next_audio)
                        nxt_aud.start()

                    except Exception:
                        _ = Exception
                    sc = 2
        pygame.display.update()
eigth_question()
qu +=1
running = True
check = False
next_level = False  # FOr going to next level
btn_run = True  # For switching off buttons
exit_val = False
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

running = True
check = False
next_level = False  # FOr going to next level
btn_run = True  # For switching off buttons
exit_val = False
qu +=1
def tenth_question():
    pygame.init()  # Initialising pygame module
    window = pygame.display.set_mode((1700, 900))  # Window Setup
    pygame.display.set_caption("DiGi-Myth")  # Application title
    icon = pygame.image.load('Resources/icon.png')  # Setting game's ICON
    bg = pygame.image.load('Resources/Question3_bg.jpg')  #
    pygame.display.set_icon(icon)  # Display icon
    s = 0
    ques = pygame.image.load("Resources/lvl_1_8.png")

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

    def Kaushalya():
        global check
        check = True
        global btn_run
        btn_run = False

    ###################################################################################

    Game_finish = pygame.image.load("Resources/yes-you-are-correct.jpg")
    gx = 300
    gy = 50

    mcq1 = pygame.image.load("Resources/mcq24.png")
    mcq2 = pygame.image.load("Resources/mcq20.png")

    mcq3 = pygame.image.load("Resources/mcq25.png")

    overscr = pygame.image.load('Resources/gameover.jpg')

    img1 = pygame.image.load("kau.png")
    img2 = pygame.image.load("sum.png")
    img3 = pygame.image.load("Resources/kai.png")
    #####################################################################################

    def Key_monitor():
        global next_level

        def show(key):
            try:

                if key == key.shift:
                    if next_level:
                        global running
                        running = False
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
                time.sleep(12)
                next_level = True
                break

    nxr = Thread(target=next_level)
    nxr.start()

    def next_audio():
        global running
        time.sleep(10)

        playsound("finish.mp3")

    def correct():
        window.blit(Game_finish, (gx, gy))

    ######################################################################################

    sc = 1  # for starting the Scream thread

    sn0 = 0
    nxt_aud = Thread(target=next_audio)
    global over
    over = False
    ovr = 1  # For Playing game over audio
    i = 0  # for incremnting sc
    global running
    global score
    global btn_run
    global current_system_pid
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Thanks for playing ")
                ThisSystem = psutil.Process(current_system_pid)
                ThisSystem.terminate()
            if btn_run:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Kaushalya()
                    key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                    if key_to_start:
                        over = True
                        btn_run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if b1.collidepoint(pygame.mouse.get_pos()):
                        over = True
                        btn_run = False
                    elif b2.collidepoint(pygame.mouse.get_pos()):
                        over = True
                        btn_run = False

                    elif b3.collidepoint(pygame.mouse.get_pos()):
                        Kaushalya()

        window.blit(bg, (0, 0))

        window.blit(ques, (100, -270))
        b1 = button(window, (1160, 230), " 3. Sumitra ")  # 1640 200
        b2 = button(window, (590, 400), " 2. kaikeyi ")
        b3 = button(window, (200, 370), " 1. Kaushalya")
        window.blit(mcq1 , (570 , 320))
        window.blit(mcq2 , (180 , 310)) #Kaushalya
        window.blit(mcq3 , (1100,150))
        window.blit(img1 ,(120 , 470))
        window.blit(img2 , (1000,270))
        window.blit(img3 , (570,475))
        score_dis = button(window, (0, 0), str(score))
        if check:
            correct()
            if i == 0:
                sc = 0
                i += 1

        if over:
            window.blit(loading, (0, 0))

            pygame.display.update()
            if ovr == 1:
                playsound("Resources/game_over_laugh.mp3")
                running = False
                ovr += 1

        if sc == 0:

            try:
                score += 1
                theme = Thread(target=start_song)
                theme.start()
                nxt_aud.start()



            except Exception:
                _ = Exception

            sc += 2
        pygame.display.update()

tenth_question()


def checking():
    global score
    global current_system_pid
    running = True

    def win():
        mixer.init()

        mixer.music.load("win.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()

    win_song = Thread(target=win)
    def loose():
        mixer.init()

        mixer.music.load("game_over.mp3")
        mixer.music.set_volume(0.3)
        mixer.music.play()
    loose_song = Thread(target=loose)
    if score >=6:
        pygame.init()  # Initialising pygame module
        window = pygame.display.set_mode((1700, 900))  # Window Setup
        pygame.display.set_caption("DiGi-Myth")  # Application title
        icon = pygame.image.load('Resources/icon.png')  # Setting game's ICON
        bg = pygame.image.load('Resources/game_win.jpg')  #
        pygame.display.set_icon(icon)  # Display icon
        win_song.start()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Thanks for playing ")
                    os.startfile("Second_level.exe")
                    ThisSystem = psutil.Process(current_system_pid)
                    ThisSystem.terminate()
            window.blit(bg , (0,0))
            pygame.display.update()
    else:
        pygame.init()  # Initialising pygame module
        window = pygame.display.set_mode((1700, 900))  # Window Setup
        pygame.display.set_caption("DiGi-Myth")  # Application title
        icon = pygame.image.load('Resources/icon.png')  # Setting game's ICON
        bg = pygame.image.load('Resources/gameover.jpg')  #
        pygame.display.set_icon(icon)  # Display icon
        loose_song.start()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Thanks for playing ")
                    ThisSystem = psutil.Process(current_system_pid)
                    ThisSystem.terminate()
            window.blit(bg, (0, 0))
            pygame.display.update()


checking()





