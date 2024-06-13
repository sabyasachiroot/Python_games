from threading import *
from playsound import playsound

import pygame
from pygame import mixer
from pynput.keyboard import Key, Listener

import os
import psutil

loading = pygame.image.load("Resources/wrong.jpg")
qu = 0
energy = 0
current_system_pid = os.getpid()
loading = pygame.image.load("Resources/wrong.jpg")
btn_run = True
next = pygame.image.load("Resources/next.png")
song_stop = False
ghost = pygame.image.load("ghost.png")

def bg_song():

    playsound("background.mp3")

_bgsong = Thread(target = bg_song)
_bgsong.start()



def questions():
    def show(key):

        global qu
        try:
            if qu == -1:
                print("Nothing")
            if qu == 0:
                if key == key.tab:
                    playsound("instruction.mp3")
            if qu == 1:
                if key == key.tab:
                    playsound("Question1_2.mp3")
            if qu == 2:
                if key == key.tab:
                    playsound("Question2_2.mp3")
            if qu == 3:
                if key == key.tab:
                    playsound("Question3_2.mp3")
            if qu == 4:
                if key == key.tab:
                    playsound("Question4_2.mp3")
            if qu == 5:
                if key == key.tab:
                    playsound("Question5_2.mp3")
        except Exception:
            _ = Exception

    with Listener(on_press=show) as listener:
        listener.join()


ques = Thread(target=questions)
ques.start()
i = False
def app():
    pygame.init()  # Initialising pygame module
    window = pygame.display.set_mode((1500, 900))  # Window Setup
    pygame.display.set_caption("DiGi-Myth")  # Application title
    icon = pygame.image.load('Resources/icon.png')  # Setting game's ICON
    bg1 = pygame.image.load('Resources/level_2.jpg')  #
    play = pygame.image.load('Resources/play_button.png')

    pygame.display.set_icon(icon)  # Display icon
    def ins():
        playsound("instruction.mp3")
        global i
        i = True
    ini = Thread(target = ins)
    ini.start()
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
                     if i:
                       running = False

        window.blit(bg1, (0, 0))

        b1 = button(window, (800, 800), "    Play Now    ")

        window.blit(play, (720, 780))

        pygame.display.update()


app()

comm = 1

def forest():
    pygame.init()  # Initialising pygame module
    window = pygame.display.set_mode((1500, 900))  # Window Setup
    pygame.display.set_caption("DiGi-Myth")  # Application title
    icon = pygame.image.load('Resources/icon.png')  # Setting game's ICON
    bg1 = pygame.image.load('Resources/forest.jpg')  #
    pygame.display.set_icon(icon)  # Display icon
    player = pygame.image.load('Resources/Ram_2.png')
    come1 = pygame.image.load('Resources/comm1.png')
    come2 = pygame.image.load('Resources/comm3.png')
    come3 = pygame.image.load('Resources/comm4.png')
    come4 = pygame.image.load('Resources/comm5.png')
    X = 500
    Y = 500
    running = True
    global current_system_pid
    global energy
    global next

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

    def start():
        global comm
        comm +=1
    global comm

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
                    start()
            if event.type == pygame.MOUSEBUTTONDOWN:

                if b1.collidepoint(pygame.mouse.get_pos()):
                   start()

        window.blit(bg1, (0, 0))

        if comm == 1:

          window.blit(come1 , (10,0))

        elif comm == 2:
         window.blit(come2 , (10,0))
        elif comm == 3:
            window.blit(come3, (10, 0))
        elif comm==4:
            window.blit(come4, (10, 0))
        elif comm == 5:
            running = False
        b1 = button(window , (1400 , 80 ),"Nex")
        window.blit(next, (1320, 0))
        window.blit(player, (X, Y))


        pygame.display.update()
forest()
comm = 1
def round_tree():
    pygame.init()  # Initialising pygame module
    window = pygame.display.set_mode((1500, 900))  # Window Setup
    pygame.display.set_caption("DiGi-Myth")  # Application title
    icon = pygame.image.load('Resources/icon.png')  # Setting game's ICON
    bg1 = pygame.image.load('Resources/round_tree.jpg')  #
    pygame.display.set_icon(icon)  # Display icon
    player = pygame.image.load('Resources/Ram_2.png')
    come1 = pygame.image.load('Resources/comm1_2.png')
    come2 = pygame.image.load('Resources/comm3_2.png')
    come3 = pygame.image.load('Resources/comm5_2.png')
    come4 = pygame.image.load('Resources/comm6_2.png')
    th = pygame.image.load("Resources/th1.png")

    mcq1 = pygame.image.load("Resources/mcq26.png")
    mcq2 = pygame.image.load("Resources/mcq27.png")
    mcq3 = pygame.image.load("Resources/mcq28.png")

    def correc():
        playsound("corre.wav")
    def wro():
        playsound("wro.wav")
    _ro = Thread(target=wro)
    _co = Thread(target = correc)
    co_s = 0 # for starting _co thread
    ro_s = 0 #for starting the _ro thread
    X = 500
    Y = 500
    q = 0 # flag for question
    running = True
    global current_system_pid
    global comm
    global next
    global qu
    def start():
        global comm
        if comm == 0:
            comm = 10
        comm +=1
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
    global energy
    global btn_run
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
                    start()
            if event.type == pygame.MOUSEBUTTONDOWN:
              if btn_run:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    start()
                    if comm == 0:
                        running = False
                    if comm == 5:
                        running = False
              elif b2.collidepoint(pygame.mouse.get_pos()):
                    start()
              elif b3.collidepoint(pygame.mouse.get_pos()):
                    comm = 0
              elif b4.collidepoint(pygame.mouse.get_pos()):
                    comm = 0

        window.blit(bg1, (0, 0))

        b1 = button(window, (1400, 80), "Nex")
        window.blit(next, (1320, 0))

        window.blit(player, (X, Y))
        if comm == 1:
            window.blit(come1 , (10,0))
        if comm == 2:
            window.blit(th , (600,400))
        if comm == 3:
            window.blit(come2 , (10,0))
            btn_run = False
            if q == 0:
                qu =1
                q +=1
            b2 = button(window, (10, 160), "Dark Blue As")   # Dark Blue as a lotus
            b3 = button(window, (10, 260), "Purple as the sunset")
            b4 = button(window, (10, 450), "Brown a")   # Brown as the sacred earth
            window.blit(mcq1 , (0,30))
            window.blit(mcq2 , (0,350))
            window.blit(mcq3 , (-10,170))
        if comm == 0:
            global loading
            if ro_s == 0:
                _ro.start()
                ro_s +=1
            window.blit(come4 , (10,0))
            btn_run = True
        if comm == 4:
            window.blit(come3, (10, 0))
            energy +=1
            btn_run = True
            if co_s == 0:
                _co.start()
                co_s +=1
        if comm == 10:
            running = False
        if comm == 11:
            running = False

        pygame.display.update()
round_tree()
comm = 1
running = True
btn_run = True
qu = -1
def mayani():
    pygame.init()  # Initialising pygame module
    window = pygame.display.set_mode((1500, 900))  # Window Setup
    pygame.display.set_caption("DiGi-Myth")  # Application title
    icon = pygame.image.load('Resources/icon.png')  # Setting game's ICON
    Ram =pygame.image.load('Resources/Ram_2.png')
    bg1 = pygame.image.load('Resources/level_2_1.jpg')
    mayani = pygame.image.load('Resources/mayani.png')
    pygame.display.set_icon(icon)

    come1 = pygame.image.load('Resources/th2.png')
    th = pygame.image.load('Resources/th32.png')
    come2 = pygame.image.load('Resources/defea.png')
    come3 = pygame.image.load('Resources/dedea2.png')

    mcq1 = pygame.image.load("Resources/mcq29.png")
    mcq2 = pygame.image.load("Resources/mcq30.png")
    mcq3 = pygame.image.load("Resources/mcq31.png")
    global ghost
    global next
    global qu
    g = 0 # for the ghost image
    q =0
    def correc():
        playsound("corre.wav")
    def wro():
        playsound("wro.wav")
    _ro = Thread(target=wro)
    _co = Thread(target = correc)
    co_s = 0 # for starting _co thread
    ro_s = 0 #for starting the _ro thread
    def start():
        global comm
        if comm == 0:
            comm = 10
        comm += 1
    global comm
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

    global energy
    global current_system_pid
    global  running
    global btn_run
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
                    start()
            if event.type == pygame.MOUSEBUTTONDOWN:
             if btn_run:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    start()
                    if comm == 0:
                        running = False
                    if comm == 5:
                        running = False
                    if comm == 4:
                        running = False
             elif b2.collidepoint(pygame.mouse.get_pos()):
                    comm = 0

             elif b3.collidepoint(pygame.mouse.get_pos()):
                    start()
                    g = 1
             elif b4.collidepoint(pygame.mouse.get_pos()):
                    comm = 0

        window.blit(bg1 , (0,0))
        if g==0:
            window.blit(mayani , (500,30))
        if g==1:
            window.blit(ghost , (500,30))

        window.blit(Ram , (500,430))
        b1 = button(window, (1400, 80), "Nex")
        window.blit(next, (1320, 0))
        if comm == 1:
            window.blit(come1 , (10,0))
        if comm == 2:
            window.blit(th , (10,0))
            if q == 0:
                qu =2
                q +=1
            btn_run = False
            b2 = button(window, (10, 170), "A demon from") # Demon from birth
            b3 = button(window, (10, 250), "Cursed to be")
            b4 = button(window, (10, 350), "A Holy Sage")
            window.blit(mcq1 , (0,290))
            window.blit(mcq2 , (0,100))
            window.blit(mcq3 , (0,190))
        if comm == 3:
            window.blit(come2 , (10,0))
            if co_s == 0:
                _co.start()
                co_s += 1
            energy += 1
            btn_run = True
        if comm == 0:
            global loading
            if ro_s == 0:
                _ro.start()
                ro_s +=1
            window.blit(come3 , (10,0))
            btn_run = True


        if comm == 11:
            running = False
        if comm == 10:
            running = False

        pygame.display.update()

mayani()
comm = 1
running = True
btn_run = True
qu = -1
def dense_forest():
    pygame.init()  # Initialising pygame module
    window = pygame.display.set_mode((1500, 900))  # Window Setup
    pygame.display.set_caption("DiGi-Myth")  # Application title
    icon = pygame.image.load('Resources/icon.png')  # Setting game's ICON
    Ram = pygame.image.load('Resources/Ram_2.png')
    bg1 = pygame.image.load('Resources/dense_canopy.jpg')
    werewolf =  pygame.image.load('Resources/werewolf.png')
    pygame.display.set_icon(icon)

    come1 = pygame.image.load('Resources/th4.png')
    th = pygame.image.load('Resources/qu1.png')
    come2 = pygame.image.load('Resources/qu3.png')
    come3 = pygame.image.load('Resources/th56.png')

    mcq1 = pygame.image.load("Resources/mcq32.png")
    mcq2 = pygame.image.load("Resources/mcq33.png")
    mcq3 = pygame.image.load("Resources/mcq34.png")
    global ghost
    g = 0
    global running
    global btn_run
    global next
    global qu
    q = 0

    def correc():
        playsound("corre.wav")

    def wro():
        playsound("wro.wav")

    _ro = Thread(target=wro)
    _co = Thread(target=correc)
    co_s = 0  # for starting _co thread
    ro_s = 0  # for starting the _ro thread
    def start():
        global comm
        if comm == 0:
            comm = 10
        comm += 1
    global comm
    global  energy
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
                    start()
            if event.type == pygame.MOUSEBUTTONDOWN:
               if btn_run:
                    if b1.collidepoint(pygame.mouse.get_pos()):
                        start()
                        if comm == 0:
                            running = False
                        if comm == 5:
                            running = False
                        if comm == 4:
                            running = False
               elif b2.collidepoint(pygame.mouse.get_pos()):
                   start()
                   g = 1
               elif b3.collidepoint(pygame.mouse.get_pos()):
                    comm = 0
               elif b4.collidepoint(pygame.mouse.get_pos()):
                    comm = 0
        window.blit(bg1 , (0,0))

        b1 = button(window, (1400, 80), "Nex")
        window.blit(next, (1320, 0))
        if g==0:
            window.blit(werewolf , (520,125))
        if g==1:
            window.blit(ghost, (520, 125))
        window.blit(Ram, (500, 550))
        if comm == 1:
            window.blit(come1, (10, 0))
        if comm == 2:
            window.blit(th, (10, 0))
            btn_run = False
            if q == 0:
                qu = 3
                q +=1
            b2 = button(window, (10, 170), "Lord Brahma")
            b3 = button(window, (10, 250), "Lord Shiva")
            b4 = button(window, (10, 350), "Lord Indra")
            window.blit(mcq1 , (0,100))
            window.blit(mcq2 , (0,270))
            window.blit(mcq3 , (0,183))
        if comm == 3:
            window.blit(come2, (10, 0))
            energy += 1
            if co_s == 0:
                _co.start()
                co_s += 1
            btn_run = True
        if comm == 0:
            global loading
            window.blit(come3, (10, 0))
            if ro_s == 0:
                _ro.start()
                ro_s +=1
            btn_run = True

        if comm == 11:
            running = False
        if comm == 10:
            running = False
        pygame.display.update()

dense_forest()

comm = 1
running = True
btn_run = True
qu = -1
def heavy():
    pygame.init()  # Initialising pygame module
    window = pygame.display.set_mode((1500, 900))  # Window Setup
    pygame.display.set_caption("DiGi-Myth")  # Application title
    icon = pygame.image.load('Resources/icon.png')  # Setting game's ICON
    Ram = pygame.image.load('Resources/Ram_2.png')
    bg1 = pygame.image.load('Resources/bg_1500x900.jpg')
    werewolf = pygame.image.load('Resources/heavy.png')
    pygame.display.set_icon(icon)

    come1 = pygame.image.load('Resources/comm2.png')
    th = pygame.image.load('Resources/qe2 .png')
    come2 = pygame.image.load("Resources/qe21.png")
    come3 = pygame.image.load('Resources/th56.png')

    mcq1 = pygame.image.load("Resources/mcq35.png")
    mcq2 = pygame.image.load("Resources/mcq37.png")
    mcq3 = pygame.image.load("Resources/mcq38.png")

    global ghost
    global running
    global btn_run
    global next
    g = 0
    q = 0
    def correc():
        playsound("corre.wav")

    def wro():
        playsound("wro.wav")

    _ro = Thread(target=wro)
    _co = Thread(target=correc)
    co_s = 0  # for starting _co thread
    ro_s = 0  # for starting the _ro thread
    def start():
        global comm
        if comm == 0:
            comm = 10
        comm += 1

    global comm
    global energy
    global qu
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
                    start()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_run:
                    if b1.collidepoint(pygame.mouse.get_pos()):
                        start()
                        if comm == 0:
                            running = False
                        if comm == 5:
                            running = False
                        if comm == 4:
                            running = False
                elif b2.collidepoint(pygame.mouse.get_pos()):
                    comm = 0
                elif b3.collidepoint(pygame.mouse.get_pos()):
                    comm = 0
                elif b4.collidepoint(pygame.mouse.get_pos()):
                    start()
                    g = 1
        window.blit(bg1, (0, 0))

        b1 = button(window, (1400, 80), "Nex")
        window.blit(next, (1320, 0))
        if g==0:
            window.blit(werewolf, (520, 125))
        if g==1:
            window.blit(ghost , (520,125))
        window.blit(Ram, (500, 550))
        if comm == 1:
            window.blit(come1, (10, 0))
        if comm == 2:
            window.blit(th, (10, 0))
            btn_run = False
            if q == 0:
                qu = 4
                q +=1
            b2 = button(window, (10, 170), "He didn't had the")  # He didn't has the time to do so
            b3 = button(window, (10, 300), "due to lakshman Rekha")
            b4 = button(window, (10, 420), "Due to a curse")
            window.blit(mcq1 , (-10,320))
            window.blit(mcq2 ,(-10,100))
            window.blit(mcq3 , (-10,218))
        if comm == 3:
            window.blit(come2, (10, 0))
            energy += 1
            if co_s == 0:
                _co.start()
                co_s += 1
            btn_run = True
        if comm == 0:
            global loading
            window.blit(come3, (10, 0))
            btn_run = True
            if ro_s == 0:
                _ro.start()
                ro_s +=1

        if comm == 11:
            running = False
        if comm == 10:
            running = False
        pygame.display.update()
heavy()
comm = 1
running = True
btn_run = True
qu = -1
def last():
    pygame.init()  # Initialising pygame module
    window = pygame.display.set_mode((1500, 900))  # Window Setup
    pygame.display.set_caption("DiGi-Myth")  # Application title
    icon = pygame.image.load('Resources/icon.png')  # Setting game's ICON
    Ram = pygame.image.load('Resources/Ram_2.png')
    bg1 = pygame.image.load('Resources/dense_canopy.jpg')
    werewolf = pygame.image.load('Resources/mon2.png')
    pygame.display.set_icon(icon)

    come1 = pygame.image.load('Resources/comm67.png')
    th = pygame.image.load('Resources/com121.png')
    come2 = pygame.image.load("Resources/qe21.png")
    come3 = pygame.image.load('Resources/th56.png')

    mcq1 = pygame.image.load("Resources/mcq39.png")
    mcq2 = pygame.image.load("Resources/mcq40.png")
    mcq3 = pygame.image.load("Resources/mcq41.png")


    global running
    global btn_run
    global next
    def start():
        global comm
        if comm == 0:
            comm = 10
        comm += 1
    global ghost
    global comm
    global energy
    global qu
    g = 0
    q  = 0
    def correc():
        playsound("corre.wav")

    def wro():
        playsound("wro.wav")

    _ro = Thread(target=wro)
    _co = Thread(target=correc)
    co_s = 0  # for starting _co thread
    ro_s = 0  # for starting the _ro thread
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
                    start()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_run:
                    if b1.collidepoint(pygame.mouse.get_pos()):
                        start()
                        if comm == 0:
                            running = False
                        if comm == 5:
                            running = False
                        if comm == 4:
                            running = False
                elif b2.collidepoint(pygame.mouse.get_pos()):
                    comm = 0
                elif b3.collidepoint(pygame.mouse.get_pos()):
                    comm = 0
                elif b4.collidepoint(pygame.mouse.get_pos()):
                    start()
                    g = 1
        window.blit(bg1, (0, 0))

        b1 = button(window, (1400, 80), "Nex")
        window.blit(next, (1320, 0))
        if g==0:
            window.blit(werewolf, (520, 125))
        if g==1:
            window.blit(ghost, (520, 125))
        window.blit(Ram, (500, 550))
        if comm == 1:
            window.blit(come1, (10, 0))
        if comm == 2:
            window.blit(th, (10, 0))
            btn_run = False
            if q == 0:
                qu = 5
                q +=1
            b2 = button(window, (10, 170), "Durbhasha")
            b3 = button(window, (10, 250), "Valmiki")
            b4 = button(window, (10, 350), "Gautam Rishi")
            window.blit(mcq1 , (-10,190))
            window.blit(mcq2 , (-10,100))
            window.blit(mcq3 , (-10,280))
        if comm == 3:
            window.blit(come2, (10, 0))
            energy += 1
            if co_s == 0:
                _co.start()
                co_s += 1
            btn_run = True
        if comm == 0:
            global loading
            if ro_s == 0:
                _ro.start()
                ro_s += 1
            window.blit(come3, (10, 0))
            btn_run = True

        if comm == 11:
            running = False
        if comm == 10:
            running = False
        pygame.display.update()

last()
running = True
song_stop = True
qu = -1
def checking():
    global energy
    global running


    def win():
        playsound("win.mp3")
    def loose():
            playsound("game_over.mp3")
    win_song = Thread(target=win)
    lose_song= Thread(target=loose)
    if energy >=4:
        pygame.init()  # Initialising pygame module
        window = pygame.display.set_mode((1500, 900))  # Window Setup
        pygame.display.set_caption("DiGi-Myth")  # Application title
        icon = pygame.image.load('Resources/icon.png')  # Setting game's ICON
        bg = pygame.image.load('Resources/game_win__2.jpg')  #
        pygame.display.set_icon(icon)  # Display icon
        win_song.start()
        global _bgsong

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Thanks for playing ")

                    ThisSystem = psutil.Process(current_system_pid)
                    ThisSystem.terminate()
            window.blit(bg , (0,0))
            pygame.display.update()
    else:
        pygame.init()  # Initialising pygame module
        window = pygame.display.set_mode((1500, 900))  # Window Setup
        pygame.display.set_caption("DiGi-Myth")  # Application title
        icon = pygame.image.load('Resources/icon.png')  # Setting game's ICON
        bg = pygame.image.load('Resources/gameover_.jpg')  #
        pygame.display.set_icon(icon)  # Display icon
        lose_song.start()
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