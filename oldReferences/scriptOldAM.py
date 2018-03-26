# script.py
# to run it, first activate the virtualenv
# source env/bin/activate
# after working, close the environment
# deactivate

# depedencies
import json
import glob
import random
from vidpy import Clip, Composition
from pprint import pprint

# empty array for the remix
remix = []

sequence = ["beginning", "development", "climax", "symbolicElement", "preending", "ending"]

def videoRemixer(pickedTag):

    # retrieve videos from videos.json
    allVideos = loadJson('videos.json')

    # select all the videos that match the color
    colorMatchVideos = colorMatcher(allVideos, pickedColor)
    # print colorMatchVideos

    # take the already filtered videos by color,
    # and pass them to the topicMatcher
    colorTopicMatchVideos = topicMatcher(colorMatchVideos, pickedTopic)
    #print colorTopicMatchVideos

    #beginning, development, climax, symbolicElement, preEnding, ending

    # find all of the videos that are beginnings
    begin = beginPicker(colorTopicMatchVideos)
    #print begin

    #append a random begin to the remix
    #remix.append(random.choice(begin))
    #print remix


###########################
####auxiliary functions####
###########################


def loadJson(filename):
    # load the json file
    with open(filename) as json_data:
        retrievedVideos = json.load(json_data)
        json_data.close()
        # parsing
        retrievedVideos= retrievedVideos["jsonVideos"]
        return retrievedVideos

def colorMatcher(videos, theColor):
    videosMatchColor = []
    for video in videos:
        for color in video["color"]:
            if color == theColor:
                videosMatchColor.append(video)
    return videosMatchColor

def topicMatcher(videos, theTopic):
    videosMatchTopic = []
    for video in videos:
        for topic in video["topic"]:
            if topic == theTopic:
            # if (topic == pickedTopic and len(remix) == 0):
                videosMatchTopic.append(video)
    return videosMatchTopic


def beginPicker(videos):
    beginVideos = []
    for video in videos:
        for sequencePosition in video["sequencePosition"]:
            if sequencePosition == "beginning":
                beginVideos.append(video)

    return beginVideos

# def sequencePicker(videos, position, match1, match2):
#     sequenceVideos = []
#     for video in videos:
#         for sequencePosition in video["sequencePosition"]:
#             if sequencePosition == position:
#                 for matching1 in video[match1]:
#                     if sequencePosition in  position:
#
#                 sequenceVideos.append(video)
#
#
#     return sequenceVideos



###########################
####execute the program####
###########################

#calling the function
videoRemixer("white","water")
