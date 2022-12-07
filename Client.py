
import socket
import time as sleep
import pygame
import sys
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((300,200))

print("Kører klienten\n")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = "172.20.10.10"
port = 5454

def send(msg):
    dataKodet = msg.encode("UTF-8")
    s.sendto(dataKodet, (host, port))
    print(msg)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
        send("frem")

    elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
        send("stop")
      
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
        send("tilbage")
    
    elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
        send("stop")
        
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
        send("venstre")
        
    elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
        send("stop")
        
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
        send("højre")
        
    elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
        send("stop")
        

        


