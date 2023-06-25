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
            running = False