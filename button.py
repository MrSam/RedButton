#!/usr/bin/python
import RPi.GPIO as GPIO
import os
import random
import time
import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(7, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
GPIO.output(7,False)


print('Started the supper button')


temp_list = {
        "1_berg.mp3": "baby there ain't no :mountain: high enough",
        "2_crazyfrog.mp3":"Trrriinnngg triiinnggg :frog: :frog: :frog: ",
        "3_kwekkwek.mp3":"Kwek kweek kwek kwaaak kwaaak kwaaaak :hatched_chick: :hatched_chick: :hatched_chick:",
        "4_oh_lala.mp3": "Den :octopus: is vertrokken!",
        "42_Toeter.mp3": "Tooeeet toeeet tooeeeet :postal_horn: :postal_horn: :postal_horn: ",
        "43_Blijven_Zitten_Tijdens_Het_Draaie.mp3": "Blijven zittteeeennnn",
        "44_Let_sGogogogo.mp3" : "GOGOGOGOGOGOOOOOOOOO :dancingorange: :dancingorange:",
        "45_Alweer_Een_Winnaar.mp3" : "We hebben alweer een winnaar :crown: :crown: :crown:",
        "46_Alejupa.mp3" : "Alejuplaaaa :partyparrot: :partyparrot: :partyparrot: ",
        "47_Gaan_Met_Die_Banaan.mp3": "Gaaaan met die banaaaaan :dancingmonkey: :dancingmonkey: :dancingmonkey: ",
        "48_Handjes_In_De_Lucht.mp3": "Haaandjees in de lucht :raised_hands: :raised_hands: :raised_hands: ",
        "49_He_Schatje_Gaan_We_Eens_Botsen.mp3" : "Heyy schatje, gaan we eens botsen ? :pbjt: :pbjt: :pbjt:",
        "50_Roulez_Roulez.mp3" : "Roulezzz rouleeezzzz :champagne: :champagne: :champagne:",
        "51_Jaaaaa.mp3" : "Jaaaaaaa :owyeah: :owyeah: :owyeah:",
        }


lastpress = datetime.datetime.now()
soundfile, slackmsg = random.choice(list(temp_list.items()))

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print slackmsg
        GPIO.output(7,True)
        os.system('killall -9 mpg123')
        os.system('mpg123 -q /home/pi/media/'+ soundfile +' &')

        if lastpress < datetime.datetime.now()-datetime.timedelta(seconds=20):
            os.system('/root/slack.sh "'+ slackmsg +'"')
            soundfile, slackmsg = random.choice(list(temp_list.items()))
            lastpress = datetime.datetime.now()

        time.sleep(0.2)
        GPIO.output(7,False)
