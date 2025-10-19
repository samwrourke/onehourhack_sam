import numpy
import pygame
import sys

textwidth = 100
textheight = 100

def main():
    pygame.mixer.init()

    sf = input("Enter the sound file you wish to transform:")
    sound = pygame.mixer.Sound(sf)

    array = pygame.sndarray.array(sound)
    floatarray = numpy.zeros(array.shape[0],dtype = float)
    largest = array.max() * 1.5

    for i in range(array.shape[0]):
        floatarray[i] = array[i][0] / largest

    text = ""
    for i in numpy.linspace(0,array.shape[0],textwidth,dtype = int,endpoint = False):
        ntext =  " " * int(((floatarray[i] * textwidth) + textwidth) / 2) + "S"
        text += ntext + "\n"

    print(text)
    
    pygame.mixer.quit()

main()
