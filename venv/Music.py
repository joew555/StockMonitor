from playsound import playsound




def removeSpaces(string):
    return string.replace(" ","\ ")

downSongs = ['music/down/Crazy_Train.mp3', 'music/down/Master_of_Puppets.mp3', 'music/down/Metallica_One.mp3']
upSongs = ['music/up/Move_Your_Feet.mp3']

def up():
    for upSong in upSongs:
        playsound(upSong)



def down():
   for downSong in downSongs:
       playsound(downSong)

