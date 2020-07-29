import stream, instrument
import requests
import pygame, sys
from pygame import mixer
pygame.mixer.init()
pygame.init()

pygame.pre_init(frequency=44100, size=-16, channels=4, buffer=512, devicename=Peedrum, fadeout=5000, fadein_length=5000)

for instruments in (Soundictionary):
Soundictionary = {'1' : 'Loop1.wav'
                  '2' : 'Loop2.wav'
                  '3' : 'Loop3.wav'
                  '4' : 'Loop4.wav' }

                
    for instrument, drumbeat.beat:
        if 
        play[instrument] = sound

K_1 = '1'
K_2 = '2'
K_3 = '3'
K_4 = '4'

def manage_audio(boolean, input):
    while True:
        for event in pygame.event.get():
            
            try:
                if (event.type == KEYDOWN and event.key == K_1):	
		            if boolean:
			            pygame.mixer.Channel(0).set_volume(0.0, 1.0)
			            pygame.mixer.Channel(0).play(pygame.mixer.Sound(), loops = -1, fade_ms = fadein_length)
		            else:
			            pygame.mixer.Channel(0).fadeout(fadeout_length)
	              
                if (event.type == KEYDOWN and event.key == K_2):	
		            if boolean:
			            pygame.mixer.Channel(1).set_volume(0.0, 1.0)
			            pygame.mixer.Channel(1).play(pygame.mixer.Sound(), loops = -1, fade_ms = fadein_length)
		            else:
			            pygame.mixer.Channel(1).fadeout(fadeout_length)
	              
                if (event.type == KEYDOWN and event.key == K_3):	
		            if boolean:
			            pygame.mixer.Channel(2).set_volume(0.0, 1.0)
			            pygame.mixer.Channel(2).play(pygame.mixer.Sound(), loops = -1, fade_ms = fadein_length)
		            else:
			            pygame.mixer.Channel(2).fadeout(fadeout_length)
                
                if (event.type == KEYDOWN and event.key == K_4):	
		            if boolean:
			            pygame.mixer.Channel(3).set_volume(0.0, 1.0)
			            pygame.mixer.Channel(3).play(pygame.mixer.Sound(), loops = -1, fade_ms = fadein_length)
		            else:
			            pygame.mixer.Channel(3).fadeout(fadeout_length)
    except:
            pass

    manage_audio()
class instrument:
  def __init__(self, name):
    self.drum = name

