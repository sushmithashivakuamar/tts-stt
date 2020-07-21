#!/usr/bin/env python
import numpy as np
import sys
import os
from playsound import playsound

from gtts import gTTS
import os

print ("Enter the Text :")
str=input()
print (str)
lag = 'en'
myobj = gTTS(text=str, lang=lag, slow =False)
myobj.save("hi.mp3")
playsound("hi.mp3")
os.system("mpg321 test.mp3")
