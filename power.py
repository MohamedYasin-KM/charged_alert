#Importing required modules
import psutil
from playsound import playsound

#Initializing Variable to make the while loop to run infinitely until the condition satisfied.
run = True
while run:
    power = psutil.sensors_battery() #Instance to access battery status
    if power.percent==100 and power.power_plugged==True:
        playsound("Binks Sake - Japanese ! Bgm ! Theme.mp3")#Path of the tone
        run = False