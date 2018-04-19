import json
#esto es un modulo (biblioteca, libreria)
import glob
import random
from random import shuffle
from vidpy import Clip, Composition
from pprint import pprint
import datetime





simpleThoughts = json.load(open('audio_thougths.json', 'r'))
simpleThoughts = simpleThoughts["jsonThoughts"]
#print simpleThoughts
randomSounds = json.load(open('randomSounds.json'))
randomSounds = randomSounds["jsonSounds"]
allVideos = json.load(open('videos.json'))
allVideos = allVideos["videos"]

shuffle(randomSounds)
shuffle(simpleThoughts)

nightSequence = []
dreamSequence = []
mergeSequence = []
beginning = []
ending = []
# cd to the folder
# source env/bin/activate


def createMergeSequence(pickedTag):
    # load the json file with all videos
    with open('videos.json') as json_data:
        allVideos = json.load(json_data)
        json_data.close()
        allVideos = allVideos["videos"]
        #print allVideos
    mergeSequence.append(random.choice(randomSounds))
    #print (mergeSequence)
    abstractVideos = [video for video in allVideos if "abstract" in video["tags"]]
    print (abstractVideos)
    shuffle(abstractVideos)
    abstractSelected = random.choice(abstractVideos)
    #abstractSelected2 = random.choice(abstractVideos)
    #print abstractSelected
    #nightSequence.append(random.choice(abstractVideos))
    mergeSequence.append(abstractSelected)
    mergeSequence.append(random.choice(simpleThoughts))
    #print (nightSequence)



    selectedTagVideos=[]
    #select videos with the pickedTag
    for video in allVideos:
        for tag in video["tags"]:
            if tag == pickedTag:
                selectedTagVideos.append(video)

    shuffle(selectedTagVideos)
    #porque no me imprime esto?
    #print (selectedTagVideos)


        #select video for beginning
    beginVideos = []

    for video in selectedTagVideos:
        if "beginning" in video["sequencePosition"]:
                beginVideos.append(video)


                #for video in allVideos:
                #    if "abstract" in video["tags"]:
                #        abstractVideos.append(video)

                            #print abstractVideos

                    #print (mergeSequence)
    shuffle(beginVideos)
    beginning = random.choice(beginVideos)
    mergeSequence.append(beginning)
    print (beginning)


    #print beginVideos

    colorMatch = beginning.get('color')
    print (colorMatch)

    beginningTags= []
                #acumulativeTags= []
                #select all the tags of beginning video
    for video in mergeSequence:
        for tag in video["tags"]:
            beginningTags.append(tag)
            #why this is notprinting
    print (beginningTags)


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
        for color in video["color"]:
            if color in colorMatch:
                developmentVideosAux2.append(video)
    #print developmentVideosAux2


    developmentVideosAux3 = []
    for video in developmentVideosAux2:
        if tag in beginningTags:
            developmentVideosAux3.append(video)
    print (developmentVideosAux2)

    development = random.choice(developmentVideosAux3)
    mergeSequence.append(development)
    #print development

    acumulativeTagsAux1= []

    # -*- coding: latin-1 -*-
    #select all the tags of the previous selected videos. para hacerlo mas simple intente for video in development, pero no acepta
    for video in mergeSequence:
        for tag in video["tags"]:
                acumulativeTagsAux1.append(tag)
            #acumulativeTags.append(beginningTags)

    print (acumulativeTagsAux1)
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
        for color in video["color"]:
            if color in colorMatch:
                climaxVideosAux2.append(video)
    #print climaxVideosAux2


    climaxVideosAux3 = []
    for video in climaxVideosAux2:
        if tag in acumulativeTagsAux1:
            climaxVideosAux3.append(video)
    #print climaxVideosAux3

    climax = random.choice(climaxVideosAux3)
    mergeSequence.append(climax)
    print (climax)


    acumulativeTagsAux2= []

    # -*- coding: latin-1 -*-
    #select all the tags of the previous selected videos. para hacerlo mas simple intente for video in development, pero no acepta
    for video in mergeSequence:
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
        for color in video["color"]:
            if color in colorMatch:
                symbolicElementVideosAux2.append(video)
    #print climaxVideosAux2


    symbolicElementVideosAux3 = []
    for video in symbolicElementVideosAux2:
        if tag in acumulativeTagsAux2:
            symbolicElementVideosAux3.append(video)
    #print symbolicElementVideosAux3

    symbolicElement = random.choice(symbolicElementVideosAux3)
    mergeSequence.append(symbolicElement)
    print (symbolicElement)


    acumulativeTagsAux3= []

    # -*- coding: latin-1 -*-
    #select all the tags of the previous selected videos. para hacerlo mas simple intente for video in development, pero no acepta
    for video in mergeSequence:
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
        for color in video["color"]:
            if color in colorMatch:
                preendingVideosAux2.append(video)
    #print climaxVideosAux2

    preendingVideosAux3 = []
    for video in preendingVideosAux2:
        if tag in acumulativeTagsAux3:
            preendingVideosAux3.append(video)
    #print symbolicElementVideosAux3

    preending = random.choice(preendingVideosAux3)
    mergeSequence.append(preending)
    #print symbolicElement


    acumulativeTagsAux4= []

    # -*- coding: latin-1 -*-
    #select all the tags of the previous selected videos. para hacerlo mas simple intente for video in development, pero no acepta
    for video in mergeSequence:
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
        for color in video["color"]:
            if color in colorMatch:
                endingVideosAux2.append(video)
    #print climaxVideosAux2


    endingVideosAux3 = []
    for video in endingVideosAux2:
        if tag in acumulativeTagsAux4:
            endingVideosAux3.append(video)
    #print symbolicElementVideosAux3

    ending = random.choice(endingVideosAux3)
    mergeSequence.append(ending)
    #print ending
    mergeSequence.append(random.choice(randomSounds))




#function to create the video mergeSequence
def make_video():

    clips=[]

    for video in mergeSequence:
        #print mergeSequence
    #print each video of the sequence and tagsself.and colors

    #filename = "./videos/" + video['id']
        filename = video["path"]
    #print video
    #print filename
        clip = Clip(filename, start=video['start'], end= video['end'])
        if "abstract" in video["tags"]:
            clip.fadein(1)
            clip.fadeout(1.5)
        for video in beginning:
            clip.fadein(3)
        for video in ending:
            clip.fadeout(1.5)
        for video in randomSounds:
            clip.fadein(1)
            clip.fadeout(1.5)


        clip.glow()
        clips.append(clip)
        print (mergeSequence[0]["id"])

    composition = Composition(clips,singletrack=True, width=800, height=800)
    videoName = "render/videoMergeClassic" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") +".mp4"
    composition.save(videoName)
    #composition.preview()

        # for tag in video["tags"]:
        #     for sequencePosition in video["sequencePosition"]:
        #         for color in video['color']:
        #             if tag in beginningTags and sequencePosition == "development" and color in colorMatch:
        #                 developmentVideos.append(video)


        #print development

        #for video in development:
        #    for tag in video["tags"]:
        #        acumulativeTags.append(tag)


    #continue like this for the other parts of the sequence ?

        #select all the tags of beginning video
        #for video in mergeSequence:
        #    for tag in video["tags"]:
        #        beginningTags.append(tag)

        #        print beginningTags




#    print beginning
#    print development
#    print climax
#    print symbolicElement
#    print preending
#    print ending


#pendientes
# fade in and out/
# agregar un negro.





            #calling function
createMergeSequence("sea")
            #create the sequence

make_video()
