from playsound import playsound
import os as os
import random as random

path = 'music/'

def removeSpaces(string):
    return string.replace(" ", "%20")



#create list of mp3 files
upSongFiles = []
downSongFiles = []

for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".mp3"):
            fullPath = (os.path.join(root, file))
            if "up/" in fullPath:
                upSongFiles.append(fullPath)
            else:
                downSongFiles.append(fullPath)

#print("A random up song: " + random.choice(upSongFiles))
#print("A random down song: " + random.choice(downSongFiles))

#random iterates through a list randomly - do not need a for loop
def up():
    playsound(removeSpaces(random.choice(upSongFiles)))
    #for upSong in upSongFiles:
        #playsound(removeSpaces(upSong))


def down():
    playsound(removeSpaces(random.choice(downSongFiles)))
    #for downSong in downSongFiles:
        #playsound(removeSpaces(downSong))



'''

downSongs = ['music/down/Crazy Train.mp3', 'music/down/Master_of_Puppets.mp3', 'music/down/Metallica_One.mp3']
upSongs = ['music/up/Move Your Feet.mp3']

def up():
    for upSong in upSongs:
        playsound(removeSpaces(upSong))

def down():
    for downSong in downSongs:
        playsound(removeSpaces(downSong))


'''