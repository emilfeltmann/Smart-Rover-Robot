import socket
import RPi.GPIO as G
from time import sleep

host = "172.20.10.10"
port = 5454

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
print("Kører serveren\n")

G.setwarnings(False)
G.setmode(G.BCM)
pinlist = [16,20,21,26]
G.setup(pinlist, G.OUT)

Motor1f = G.PWM(16, 100)
Motor1b = G.PWM(20, 100)
Motor2f = G.PWM(26, 100)
Motor2b = G.PWM(21, 100)

Motor1f.start(0)
Motor1b.start(0)
Motor2f.start(0)
Motor2b.start(0)

def frem():
    Motor1f.ChangeDutyCycle(30)
    Motor2f.ChangeDutyCycle(30)
    Motor1b.ChangeDutyCycle(0)
    Motor2b.ChangeDutyCycle(0)

def tilbage():
    Motor1f.ChangeDutyCycle(0)
    Motor2f.ChangeDutyCycle(0)
    Motor1b.ChangeDutyCycle(30)
    Motor2b.ChangeDutyCycle(30)

def venstre():
    Motor1f.ChangeDutyCycle(0)
    Motor2f.ChangeDutyCycle(30)
    Motor1b.ChangeDutyCycle(0)
    Motor2b.ChangeDutyCycle(0)

def højre():
    Motor1f.ChangeDutyCycle(30)
    Motor2f.ChangeDutyCycle(0)
    Motor1b.ChangeDutyCycle(0)
    Motor2b.ChangeDutyCycle(0)

def stop():
    Motor1f.ChangeDutyCycle(0)
    Motor2f.ChangeDutyCycle(0)
    Motor1b.ChangeDutyCycle(0)
    Motor2b.ChangeDutyCycle(0)


while True:
    data, adresse = s.recvfrom(1024)
    dataDekodet = data.strip().decode("UTF-8")
    print(dataDekodet)        
    if dataDekodet == "Frem":
        frem()
        sleep(0.2)
    elif dataDekodet == "tilbage":
        tilbage()
        sleep(0.2)
    elif dataDekodet == "venstre":
        venstre()
        sleep(0.2)
    elif dataDekodet == "højre":
        højre()
        sleep(0.2)   
    elif dataDekodet == "Stop":
        stop()
        sleep(0.2)
                
    s.close()
    G.cleanup()
