from playsound import playsound




def removeSpaces(string):
    return string.replace(" ","%20")

downSongs = ['music/down/Crazy Train.mp3', 'music/down/Master_of_Puppets.mp3', 'music/down/Metallica_One.mp3']
upSongs = ['music/up/Move Your Feet.mp3']

def up():
    for upSong in upSongs:
        playsound(removeSpaces(upSong))



def down():
   for downSong in downSongs:
       playsound(removeSpaces(downSong))

