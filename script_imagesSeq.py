import json
#esto es un modulo (biblioteca, libreria)
import glob
import random
from random import shuffle
from vidpy import Clip, Composition
from pprint import pprint

#The program I want to do:

#1.Create dreamSequence

#a.Select the beginning Video of the sequence related to a tag people will select in a screen. Take the video from videosWater.json in the folder videos
#b.Select a development video related to any tag in the previous beginning video, and with a color in common with previous video..
#c.Select a climax, symbolicElement, preending and ending video for the sequence with tag & color in common with previous videos.

#3.Then apply Effects
#(with fade in and fade out)
#glow
#etc

dreamSequence = []
# cd to the folder
# source env/bin/activate


#REFERENCE TO MAKE IT MORE simple

#    abstractVideos = [video for video in allVideos if "abstract" in #video["tags"]]
#    print abstractVideos
    #for video in allVideos:
    #    if "abstract" in video["tags"]:
    #        abstractVideos.append(video)

                #print abstractVideos

def createDreamSequence(pickedTag):
    # load the json file with all videos
    with open('videos.json') as json_data:
        allVideos = json.load(json_data)
        json_data.close()

        allVideos = allVideos["videos"]
        #print allVideos

    selectedTagVideos=[]
    #select videos with the pickedTag
    for video in allVideos:
        for tag in video["tags"]:
            if tag == pickedTag:
                selectedTagVideos.append(video)

    shuffle(selectedTagVideos)
    #porque no me imprime esto?
    #print selectedTagVideos


        #select video for beginning
    beginVideos = []

    for video in selectedTagVideos:
        if "beginning" in video["sequencePosition"]:
                beginVideos.append(video)


                #for video in allVideos:
                #    if "abstract" in video["tags"]:
                #        abstractVideos.append(video)

                            #print abstractVideos

                    #print dreamSequence
    shuffle(beginVideos)
    beginning = random.choice(beginVideos)
    dreamSequence.append(beginning)
    #print beginning


    #print beginVideos


        # select video for development, with same color as previous video & a  a tag in common

    colorMatch=[]

    for video in dreamSequence:
        for color in video["color"]:
            colorMatch.append(color)

            print color


    #selectedColor = random.choice(colorMatch)

    #array to content the tags of the selected video, to create relation with the tags of next videos.

    beginningTags= []
                #acumulativeTags= []
                #select all the tags of beginning video
    for video in dreamSequence:
        for tag in video["tags"]:
            beginningTags.append(tag)
            #why this is notprinting
    #print beginningTags


            #to select a development video
    developmentVideosAux1 = []

    for video in allVideos:
        for sequencePosition in video["sequencePosition"]:
            if sequencePosition == "development":
            #if "sequencePosition"=="development":
                developmentVideosAux1.append(video)
            #why this is notprinting
    #print developmentVideosAux1


    developmentVideosAux2 = []
    for video in developmentVideosAux1:
        if color in colorMatch:
            developmentVideosAux2.append(video)
    #print developmentVideosAux2


    developmentVideosAux3 = []
    for video in developmentVideosAux2:
        if tag in beginningTags:
            developmentVideosAux3.append(video)
    #print developmentVideosAux2

    development = random.choice(developmentVideosAux3)
    dreamSequence.append(development)
    #print development

    acumulativeTagsAux1= []

    # -*- coding: latin-1 -*-
    #select all the tags of the previous selected videos. para hacerlo mas simple intente for video in development, pero no acepta
    for video in dreamSequence:
        for tag in video["tags"]:
                acumulativeTagsAux1.append(tag)
            #acumulativeTags.append(beginningTags)

    print acumulativeTagsAux1
    shuffle(acumulativeTagsAux1)

    #to select a climax video
    climaxVideosAux1 = []

    for video in allVideos:
        for sequencePosition in video["sequencePosition"]:
            if sequencePosition == "climax":
                climaxVideosAux1.append(video)

    #print climaxVideosAux1

    climaxVideosAux2 = []
    for video in climaxVideosAux1:
        if color in colorMatch:
            climaxVideosAux2.append(video)
    #print climaxVideosAux2


    climaxVideosAux3 = []
    for video in climaxVideosAux2:
        if tag in acumulativeTagsAux1:
            climaxVideosAux3.append(video)
    #print climaxVideosAux3

    climax = random.choice(climaxVideosAux3)
    dreamSequence.append(climax)
    #print climax

    acumulativeTagsAux2= []

    # -*- coding: latin-1 -*-
    #select all the tags of the previous selected videos. para hacerlo mas simple intente for video in development, pero no acepta
    for video in dreamSequence:
        for tag in video["tags"]:
                acumulativeTagsAux2.append(tag)
            #acumulativeTags.append(beginningTags)

    #print acumulativeTagsAux2
    shuffle(acumulativeTagsAux2)


    #to select a symbolicElement video
    symbolicElementVideosAux1 = []

    for video in allVideos:
        for sequencePosition in video["sequencePosition"]:
            if sequencePosition == "symbolicElement":
                symbolicElementVideosAux1.append(video)

    #print symbolicElementVideosAux1

    symbolicElementVideosAux2 = []
    for video in symbolicElementVideosAux1:
        if color in colorMatch:
            symbolicElementVideosAux2.append(video)
    #print climaxVideosAux2


    symbolicElementVideosAux3 = []
    for video in symbolicElementVideosAux2:
        if tag in acumulativeTagsAux2:
            symbolicElementVideosAux3.append(video)
    #print symbolicElementVideosAux3

    symbolicElement = random.choice(symbolicElementVideosAux3)
    dreamSequence.append(symbolicElement)
    #print symbolicElement

    acumulativeTagsAux3= []

    # -*- coding: latin-1 -*-
    #select all the tags of the previous selected videos. para hacerlo mas simple intente for video in development, pero no acepta
    for video in dreamSequence:
        for tag in video["tags"]:
                acumulativeTagsAux3.append(tag)
            #acumulativeTags.append(beginningTags)

    #print acumulativeTagsAux3
    shuffle(acumulativeTagsAux3)


    #to select a preending video
    preendingVideosAux1 = []

    for video in allVideos:
        for sequencePosition in video["sequencePosition"]:
            if sequencePosition == "preending":
                preendingVideosAux1.append(video)

    #print preendingVideosAux1

    preendingVideosAux2 = []
    for video in preendingVideosAux1:
        if color in colorMatch:
            preendingVideosAux2.append(video)
    #print climaxVideosAux2


    preendingVideosAux3 = []
    for video in preendingVideosAux2:
        if tag in acumulativeTagsAux3:
            preendingVideosAux3.append(video)
    #print symbolicElementVideosAux3

    preending = random.choice(preendingVideosAux3)
    dreamSequence.append(preending)
    #print symbolicElement

    acumulativeTagsAux4= []

    # -*- coding: latin-1 -*-
    #select all the tags of the previous selected videos. para hacerlo mas simple intente for video in development, pero no acepta
    for video in dreamSequence:
        for tag in video["tags"]:
                acumulativeTagsAux4.append(tag)
            #acumulativeTags.append(beginningTags)

    #print acumulativeTagsAux3
    shuffle(acumulativeTagsAux4)

    #to select a ending video
    endingVideosAux1 = []

    for video in allVideos:
        for sequencePosition in video["sequencePosition"]:
            if sequencePosition == "ending":
                endingVideosAux1.append(video)

    #print preendingVideosAux1

    endingVideosAux2 = []
    for video in endingVideosAux1:
        if color in colorMatch:
            endingVideosAux2.append(video)
    #print climaxVideosAux2


    endingVideosAux3 = []
    for video in endingVideosAux2:
        if tag in acumulativeTagsAux4:
            endingVideosAux3.append(video)
    #print symbolicElementVideosAux3

    ending = random.choice(endingVideosAux3)
    dreamSequence.append(ending)
    #print ending





    for video in allVideos:
        for sequencePosition in video["sequencePosition"]:
            if sequencePosition == "beginning":
                for tag in video["tags"]:
                    print tag




    #print beginning
    #print development
    #print climax
    #print symbolicElement
    #print preending
    #print ending
























#function to create the video dreamSequence
def make_video():

    clips=[]

    for video in dreamSequence:
        #print dreamSequence
    #print each video of the sequence and tagsself.and colors

    #filename = "./videos/" + video['id']
        filename = video["path"]
    #print video
    #print filename
        clip = Clip(filename, start=video['start'], end= video['end'])
        clip.glow()
        clips.append(clip)
        print dreamSequence[0]["id"]

    composition = Composition(clips,singletrack=True)
    composition.save('a_Video_feets1.mp4')
    composition.preview()



#calling function
createDreamSequence("feets")
#create the sequence

make_video()
