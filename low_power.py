#Importing required modules
import psutil
from playsound import playsound

run = True
while run:
    power = psutil.sensors_battery()
    if power.percent<=20 and power.power_plugged==False:
        playsound("Binks Sake - Japanese ! Bgm ! Theme.mp3")
        run = False