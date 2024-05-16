#make sure you install playsound module and save the song file name in the same directory
import datetime
from playsound import playsound
alarmHour = int(input("Enter the hour: "))
alarmMin = int(input("Enter the minutes: "))
alarmperiod = input("Select from AM or PM: ").lower()  
if alarmperiod == "pm":
    alarmHour += 12
while True:
    if alarmHour == datetime.datetime.now().hour and alarmMin == datetime.datetime.now().minute:
        print("Play")
        playsound('nijamene.mp3')
        break
