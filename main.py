import pygame
from tkinter import simpledialog
import json
pygame.init()
white = (255,255,255)
audiobackground = pygame.mixer.Sound("Space_Machine_Power.mp3")
audiobackground.play(-1)
audiobackground.set_volume(0.2)
clock = pygame.time.Clock()
background = pygame.image.load("fundo.jpg")
icon = pygame.image.load("icone.png")
screen = pygame.display.set_mode((1200,720))
pygame.display.set_caption("Space Marker")
pygame.display.set_icon(icon)
starF = pygame.font.Font(None,24)
font = pygame.font.Font(None,28)
running = True
pos = (0,0)
starName = None
counter = 0
counterstarName = 0
points = {}
def save_pos():
     with open("star.json","w") as file:
          json.dump(points,file)
def load_pos():
    global points
    try:
        with open("star.json","r") as file:
            points = json.load(file)
    except:
        with open("star.json","w") as file:
            json.dump(points,file)
def delete_pos():
     points.clear()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_pos()
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            save_pos()
            running = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            pos = pygame.mouse.get_pos()
            starName = simpledialog.askstring("Space", "Nome da estrela:")
            if starName == "":
                starName = "Desconhecido"
                if "Desconhecido" in points:
                    counter = counter + 1
                    starName = "Desconhecido" + str(counter)
            elif starName in points:
                counterstarName = counterstarName + 1
                starName = starName + str(counterstarName)
            elif starName is None:
                    continue
            points[starName]= pos
            print(counterstarName)
            print(points)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F10:
            save_pos()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            load_pos()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F12:
            delete_pos()
    screen.blit(background, (0,0))
    for key in points:
        pos = points[key]
        pygame.draw.circle(screen,white,(pos),5)
        starNamePrint = starF.render(key + str(pos),True,white)
        screen.blit(starNamePrint,(pos))
    keys = list(points.keys())
    for i in range(len(keys)-1):
         currentKey = keys[i]
         nextKey = keys[i + 1]
         currentPoint = points[currentKey]
         nextPoint = points[nextKey]
         pygame.draw.line(screen,white,currentPoint,nextPoint)
    f10 = font.render("Pressione F10 para salvar as marcações",True,white)
    f11 = font.render("Pressione F11 para carregar as marcações salvas",True,white)
    f12 = font.render("Pressione F12 para deletar as marcações",True,white)
    screen.blit(f10,(10,10))
    screen.blit(f11,(10,35))
    screen.blit(f12,(10,60))
    pygame.display.update()
    clock.tick(180)
pygame.quit()
