from pygame import *
mixer.init()
mixer.music.load('F:\College\DSA\dsa project\sunny sunny.ogg')
mixer.music.play()

while mixer.music.get_busy():
    time.Clock().tick(10)
