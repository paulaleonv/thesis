import json
#esto es un modulo (biblioteca, libreria)
import glob
import random
from random import shuffle
from vidpy import Clip, Composition
from pprint import pprint

#The program I want to do:

#1.Create dreamSequence

#a.Select the beggining Video of the sequence related to a tag people will select in a screen. Take the video from videosWater.json in the folder videos
#b.Select a development video related to any tag in the previous beggining video, and with a color in common with previous video..
#c.Select a climax, symbolicElement, preending and ending video for the sequence with tag & color in common with previous video.

#2.create nightSequence =[]

#a.select a random audiofile from randomSounds.json (audios are in the folder assets), play it over a black screen (with fade in and fade out).append it to nightSequence
#b.select a random video from videosWater.json with the tag "abstract", append it to nightSequence.
#c.select a random audio from the file audio_thoughts.json, append it to  nightSequence
# append dreamSequence to nightSequence.

#3.Then apply Effects
#(with fade in and fade out)
#glow
#etc

dreamSequence = []
# cd to the folder
# source env/bin/activate

def createDreamSequence(pickedTag):
    # load the json file
    with open('videosWater.json') as json_data:
        allVideos = json.load(json_data)
        json_data.close()

        allVideos = allVideos["videos"]
        #print allVideos

    selectedTagVideos=[]
    #select videos with the selected tag
    for video in allVideos:
        for tag in video["tags"]:
            if tag == pickedTag:
                selectedTagVideos.append(video)

    shuffle(selectedTagVideos)
    #print selectedTagVideos

    #select video for beggining
    beginVideos = []

    for video in selectedTagVideos:
        for sequencePosition in video["sequencePosition"]:
            if sequencePosition == "beginning":
                beginVideos.append(video)

                #print dreamSequence[0]

    beginning = random.choice(beginVideos)
    dreamSequence.append(beginning)

    # select video for development, with same color as previous video & a tag in common

    colorMatch=[]

    for video in dreamSequence:
        for color in video["color"]:
            colorMatch.append(color)

            print color

    #selectedColor = random.choice(colorMatch)

    #to create relation with all the tags
    beginningTags= []
    #acumulativeTags= []
    #select all the tags of beggining video
    for video in dreamSequence:
        for tag in video["tags"]:
            beginningTags.append(tag)

            #print beginningTags



    #to select a development video
    developmentVideos = []
    for video in allVideos:
        for tag in video["tags"]:
            for sequencePosition in video["sequencePosition"]:
                for color in video['color']:
                    if tag in beginningTags and sequencePosition == "development" and color in colorMatch:
                        developmentVideos.append(video)

    development = random.choice(developmentVideos)
    dreamSequence.append(development)

    #for video in development:
    #    for tag in video["tags"]:
    #        acumulativeTags.append(tag)


#continue like this for the other parts of the sequence ?

    #select all the tags of beggining video
    #for video in dreamSequence:
    #    for tag in video["tags"]:
    #        beginningTags.append(tag)

    #        print beginningTags

    acumulativeTags= []
    #select all the tags of development video + begginingTags
    for video in dreamSequence:
        for tag in video["tags"]:
            acumulativeTags.append(tag)
            #acumulativeTags.append(beginningTags)

            print acumulativeTags

    climaxVideos = []
    for video in allVideos:
        for tag in video["tags"]:
            for sequencePosition in video["sequencePosition"]:
                for color in video['color']:
                    if tag in acumulativeTags and sequencePosition == "climax" and color in colorMatch:
                        climaxVideos.append(video)

    climax = random.choice(climaxVideos)
    dreamSequence.append(climax)

    symbolicElementVideos = []
    for video in allVideos:
        for tag in video["tags"]:
            for sequencePosition in video["sequencePosition"]:
                for color in video['color']:
                    if tag in beginningTags and sequencePosition == "symbolicElement" and color in colorMatch:
                        symbolicElementVideos.append(video)

    symbolicElement = random.choice(symbolicElementVideos)
    dreamSequence.append(symbolicElement)

    preendingVideos = []
    for video in allVideos:
        for tag in video["tags"]:
            for sequencePosition in video["sequencePosition"]:
                for color in video['color']:
                    if tag in beginningTags and sequencePosition == "preending" and color in colorMatch:
                        preendingVideos.append(video)

    preending = random.choice(preendingVideos)
    dreamSequence.append(preending)

    endingVideos = []
    for video in allVideos:
        for tag in video["tags"]:
            for sequencePosition in video["sequencePosition"]:
                for color in video['color']:
                    if tag in beginningTags and sequencePosition == "ending" and color in colorMatch:
                        endingVideos.append(video)

    ending = random.choice(endingVideos)
    dreamSequence.append(ending)

#print len(dreamSequence)

#function to create the video dreamSequence
def make_video():
    clips=[]

    for video in dreamSequence:

        #print each video of the sequence and tagsself.and colors

        filename = "./videos/" + video['id']
        #print video
        #print filename
        clip = Clip(filename, start=video['start'], end= video['end'])
        clip.glow()
        clips.append(clip)
        print dreamSequence[0]["id"]
        composition = Composition(clips,singletrack=True)
        composition.save('a_13Video.mp4')

#calling function
createDreamSequence("nature")
#create the sequence
make_video()
