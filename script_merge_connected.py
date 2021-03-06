import json
#esto es un modulo (biblioteca, libreria)
import glob
import random
from random import shuffle
from vidpy import Clip, Composition
from pprint import pprint
from pythonosc import osc_message_builder
from pythonosc import udp_client
import datetime



simpleThoughts = json.load(open('audio_thougths.json', 'r'))
simpleThoughts = simpleThoughts["jsonThoughts"]
#print simpleThoughts
randomSounds = json.load(open('randomSounds.json'))
randomSounds = randomSounds["jsonSounds"]
allVideos = json.load(open('videos.json'))
allVideos = allVideos["videos"]

nightSequence = []
dreamSequence = []
mergeSequence = []
beginning = []
ending = []


def restart():
    shuffle(randomSounds)
    shuffle(simpleThoughts)

    nightSequence = []
    dreamSequence = []
    mergeSequence = []
    beginning = []
    ending = []
    # cd to the folder
    # source env/bin/activate


def processTag(pickedTag):
#def processTag(allDreamWordAsCSVstring):
    print (allDreamWordAsCSVstring)
    # process tags
    # what should I do if tags are more than one and with commas
    allBeginningsTags = []
    allWordsInDream = []

    #from allVideos sequence position, get beginning tags, makes them an array
    with open('videos.json') as json_data:
        allVideos = json.load(json_data)
        json_data.close()
        allVideos = allVideos["videos"]

    for video in allVideos:
        if "beginning" in video["sequencePosition"]:
            for tags in video["tags"]:
                allBeginningsTags.append(tags)
                #print (allBeginningsTags)

    print (pickedTag)
    shuffle(allBeginningsTags)

    #if one word of picked tag is in allBeginningsTags, that word is tag (or pickedtag?)

    for tags in allBeginningsTags:
        for tag in newVideoTags:
            if tag in allBeginningsTags:
                tag = pickedTag
            #this "tag" is confusing with the finally selected tag

    #if not,
    #if any word in that array allWordsInDream is in allBeginningsTags, select that word and that word is tag.

    # if not, shuffle and pick a radom word from tag from allBeginningTags., ans that word is tag.
    #
    # check if video exits etc
    #
    # assuming pickedTag is cow for which videos dont exist
    # youd prbably want to return a different tag

    #tag = "fire"
    #return tag


def findTag(words):
    #words = [w.lower().strip() for w in words]

    allBeginningsTags = []
    with open('videos.json') as json_data:
        allVideos = json.load(json_data)
        allVideos = allVideos["videos"]
        #print allVideos
    allBeginningVideos = [video for video in allVideos if "beginning" in video["sequencePosition"]]

    for video in allBeginningVideos:
        allBeginningsTags = allBeginningsTags + video['tags']

    randomTag = random.choice(allBeginningsTags)

    for word in words:
        if word in allBeginningsTags:
            return word

    return randomTag



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
    #print (abstractVideos)
    shuffle(abstractVideos)
    abstractSelected = random.choice(abstractVideos)
    #abstractSelected2 = random.choice(abstractVideos)
    #print abstractSelected
    #nightSequence.append(random.choice(abstractVideos))
    #mergeSequence.append(abstractSelected)
    mergeSequence.append(random.choice(simpleThoughts))
    #print nightSequence



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

                    #print mergeSequence
    shuffle(beginVideos)
    beginning = random.choice(beginVideos)
    mergeSequence.append(beginning)
    #print (beginning)


    #print beginVideos

    colorMatch = beginning.get('color')
    #print (colorMatch)

    beginningTags= []
                #acumulativeTags= []
                #select all the tags of beginning video
    for video in mergeSequence:
        for tag in video["tags"]:
            beginningTags.append(tag)
            #why this is notprinting
    #print (beginningTags)


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
    #print (developmentVideosAux2)

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

    #print (acumulativeTagsAux1)
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
    #print (climax)


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
    #print (symbolicElement)


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
def make_video(tag):

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
        if video in beginning:
            clip.fadein(3)
        if video in ending:
            clip.fadeout(1.5)
        if video in randomSounds:
            clip.fadein(1)
            clip.fadeout(1.5)

        clip.glow()
        clips.append(clip)
        #print (mergeSequence[0]["id"])

    composition = Composition(clips,singletrack=True, width=800, height=800)
    #videoName = "render/videoConnected10" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") +".mp4"
    # videoName = "render/video_" + tag +  datetime.datetime.now().strftime("%Y%m%d%H%M%S") +".mp4"
    videoName = "render/video_" + tag +  datetime.datetime.now().strftime("%Y%m%d%H%M%S") +".mov"
    composition.save(videoName)
    #composition.save(videoName)
    #datetime.datetime.now().strftime("%Y%m%d%H%M&S")

    #setup a client (api adress, localhost)
    client = udp_client.UDPClient("127.0.0.1",8000)
    print ("testing message")

    #composition.preview()

    #now built the messagingSenderId
    msg = osc_message_builder.OscMessageBuilder(address="/video")
    msg.add_arg("nature")
    msg = msg.build()
    client.send(msg)



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

#def createNewVideoSequence(allDreamWordAsCSVstring):
def createNewVideoSequence(allDreamWordAsCSVstring):
    # print(allDreamWordAsCSVstring)
    # allWords = allDreamWordAsCSVstring.split(",")
    # print("i am in the python script here are the words I am dealing with")
    # print(allWords)
    # restart()
    #
    #print ("the original tag from the user is ", tag)
    # #calling function
    #
    #processedTag = processTag(tag)
    #print ("the tag i will use is ", processedTag)
    #
    #createMergeSequence(tag)
    # createMergeSequence("sea")
    # #create the sequence
    #
    allWords = allDreamWordAsCSVstring.split(",")
    allWords = [w.strip().lower() for w in allWords]
    allWords = [w for w in allWords if w != ""]
    tag = findTag(allWords)
    createMergeSequence(tag)
    make_video(tag)


import sys

#createMergeSequence("nature")
#createNewVideoSequence(sys.argv[1])

if __name__ == '__main__':
    createNewVideoSequence(sys.argv[1])

    # processTag("nature")
