#Importing required modules
import psutil
import playsound

run = True
while run:
    power = psutil.sensors_battery()
    if power.percent<=20 and power.power_plugged==False:
        playsound("E:\battery_charged_alert\Binks Sake - Japanese ! Bgm ! Theme.mp3")
        run = False