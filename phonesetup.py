import board
import neopixel
import time
import random
import numpy as np
import cv2

##use for first process through only

numPix = 150

pixels = neopixel.NeoPixel(board.D18,numPix,brightness = 1,auto_write = True)

def cameraRun():
        
    for loop in range(1,numPix+1):
        pixels[loop-1] = (255,0,0)
        time.sleep(1)
        pixels[loop-1] = (0,0,0)

cameraRun()


