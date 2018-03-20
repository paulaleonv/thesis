import json
#esto es un modulo (biblioteca, libreria)
import glob
import random
from vidpy import Clip, Composition
from pprint import pprint

#The program I want to do:
#2.create nightSequence =[]

#a.select a random audiofile from randomSounds.json (audios are in the folder assets), play it over a black screen (with fade in and fade out).append it to nightSequence
#b.select a random video from videosWater.json with the tag "abstract", append it to nightSequence.
#c.select a random audio from the file audio_thoughts.json, append it to  nightSequence
# append dreamSequence to nightSequence.

#3.Then apply Effects
#(with fade in and fade out)
#glow
#etc

#pprint(data)
#With data, you can now also find values like so:
#data["masks"]["id"]
#data["om_points"]

#loading jsons
#load audio_thoughts.json_data

#data = json.load(open('data.json'))
simpleThoughts = json.load(open('audio_thougths.json', 'r'))
simpleThoughts = simpleThoughts["jsonThoughts"]
#print simpleThoughts
randomSounds = json.load(open('randomSounds.json'))
randomSounds = randomSounds["jsonSounds"]
allVideos = json.load(open('videosWater.json'))
allVideos = allVideos["videos"]


nightSequence = []

def createNightSequence():
    # load the json file

    #for audio in randomSounds:
    #    random.choice(audio)
    #    nightSequence.append(audio)
    nightSequence.append(random.choice(simpleThoughts))
    nightSequence.append(random.choice(randomSounds))
    print nightSequence


    abstractVideos = []
    for video in allVideos:
        for tag in video["tags"]:
            if tag == "abstract":
                abstractVideos.append(video)

                print abstractVideos


    #abstractSelected = random.choice(abstractVideos)
    #nightSequence.append(random.choice(abstractVideos))
    #nightSequence.append(abstractSelected)


#function to create the video dreamSequence
def makeFirstSequence():


    clips=[]


    for video in nightSequence:

        #filename = "./videos/" + video['id']
        filename = video["path"]
        #"./assets/randomSounds" + video['id']
        #

        #print video
        #print filename
        clip = Clip(filename, start=video['start'], end= video['end'])
        #clip.glow()
        clips.append(clip)
        #print nightSequence[0]["id"]
        composition = Composition(clips,singletrack=True)
        composition.save('a_firtsSequence2.mp4')
        #composition.preview('a_firtsSequence1.mp4')

#calling function
createNightSequence()
#create the sequence
makeFirstSequence()
