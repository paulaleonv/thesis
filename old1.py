import json
#esto es un modulo (biblioteca, libreria)
import glob
import random
from vidpy import Clip, Composition
from pprint import pprint

#array of videos in sequence order,
#to create the composition concatenate sequence
# beggining = []
# development = []
# climax = []
# symbolicElement = []
# preending = []
# ending = []

remix = []

# cd to the folder
# source env/bin/activate

def videoRemixer(pickedColor, pickedTag):

    # load the json file
    with open('videosWater.json') as json_data:
        allVideos = json.load(json_data)
        json_data.close()
        allVideos= allVideos["videos"]
        #print allVideos

    # sequence order for remixed video
    #sequence = ["beginning", "development", "climax", "symbolicElement", "preending", "ending"]

    # empty array for videos to be picked and stored


    # select all the videos that match the color
    colorMatch = []

    for video in allVideos:
        for color in video["color"]:
            if color == pickedColor:
                colorMatch.append(video)


        #print colorMatch

    # pick a beginning video in colorMatch that has the pickedTag
    for video in colorMatch:
        for tag in video["tags"]:
            if (tag == pickedTag and len(remix) == 0):
                #print(topic)
                #beggining.append(video)
                remix.append(video)
                #print remix
                #print beggining

    # pick a development video that has one topic in common with beginning
    for video in colorMatch:
        for sequencePosition in video["sequencePosition"]:
            #print sequencePosition
            if sequencePosition == "development":
                for tag in video["tags"]:
                    if (tag in remix[0]["tags"] and len(remix) == 1) :
                            remix.append(video)
                #     #     remix.append(video)
                #     if topic in beggining["topic"]:
                #         remix.append(video)
                #         development.append(video)
                #         print development


    for video in colorMatch:
        for sequencePosition in video["sequencePosition"]:
            if sequencePosition == "climax":
                for tag in video["tags"]:
                    if (tag in remix[0]["tags"] and len(remix) == 2) :
                            remix.append(video)

    for video in colorMatch:
        for sequencePosition in video["sequencePosition"]:
            if sequencePosition == "symbolicElement":
                for tag in video["tags"]:
                    if ((tag in remix[0]["tags"] or tag in remix[1]["tags"] or remix[2]["tags"]) and len(remix) == 3) :
                            remix.append(video)


    for video in colorMatch:
        for sequencePosition in video["sequencePosition"]:
            if sequencePosition == "preending":
                for tag in video["tags"]:
                    if ((tag in remix[0]["tags"] or tag in remix[1]["tags"] or remix[2]["tags"] or remix[3]["tags"]) and len(remix) == 4) :
                            remix.append(video)

    for video in colorMatch:
        for sequencePosition in video["sequencePosition"]:
            if sequencePosition == "ending":
                for tag in video["tags"]:
                    if ((tag in remix[0]["tags"] or tag in remix[1]["tags"] or remix[2]["tags"] or remix[3]["tags"] or remix[4]["tags"] or remix[5]["tags"]) and len(remix) == 5) :
                            remix.append(video)

    print len(remix)

#     # pick an video for climax  that has one topic in common with development or beggining
#     #is this a toooo analog way of doing it??
#     for video in colorMatch:
#         for sequencePosition in video["sequencePosition"]:
#             if sequencePosition == ["climax"]:
#                 for topic in video["topic"]:
#                     print(topic)
#                     # if topic in remix.["topic"]:
#                     #     remix.append(video)
#                     if topic in development ["topic"] or beggining["topic"]:
#                         remix.append(video)
#                         climax.append(video)
#                         print climax
#
# # pick an video for symbolicElement that has one topic in common with development or beggining
#
#     for video in colorMatch:
#         for sequencePosition in video["sequencePosition"]:
#             if sequencePosition == ["symbolicElement"]:
#                 for topic in video["topic"]:
#                     print(topic)
#                     # if topic in remix.["topic"]:
#                     #     remix.append(video)
#                     if topic in climax["topic"] or development["topic"] or beggining["topic"]:
#                         remix.append(video)
#                         symbolicElement.append(video)
#                         print symbolicElement
#
# # pick an video for preending that has one topic in common with development, beggining, climax or symbolicEmement
#     for video in colorMatch:
#         for sequencePosition in video["sequencePosition"]:
#             if sequencePosition == ["preending"]:
#                 for topic in video["topic"]:
#                     print(topic)
#                     # if topic in remix.["topic"]:
#                     #     remix.append(video)
#                     if topic in symbolicElement["topic"] or climax["topic"] or development["topic"] or beggining["topic"]:
#                         remix.append(video)
#                         preending.append(video)
#                         print preending
#
# # pick an video for preending that has one topic in common with development, beggining or symbolicEmement
#     for video in colorMatch:
#         for sequencePosition in video["sequencePosition"]:
#             if sequencePosition == ["ending"]:
#                 for topic in video["topic"]:
#                     print(topic)
#                     # if topic in remix.["topic"]:
#                     #     remix.append(video)
#                     if topic in preending["topic"] or symbolicElement["topic"] or climax["topic"] or development["topic"] or beggining["topic"]:
#                         remix.append(video)
#                         preending.append(video)
#                         print ending
#     #print remix


    #propuesta de crisV para hacerlo
    # # add remix (que es un conjunto de imgs, al tipo de secuencia que es)
    # for video in allVideos:
    #     for secuencia in video["sequencePosition"]:
    #         if (secuencia == 'climax'):
    #             climax.append(remix)
    #         elif (secuencia == 'symbolicElement'):
    #           symbolicElement.append(remix)
        #     elif (secuencia == 'preending'):
        #       preending.append(remix)
            #     elif (secuencia == 'ending'):
            #       ending.append(remix)

    #

#make Composition
#begginingClip= Clip(remix[0]["id"])
#print begginingClip

def make_video():
    #call the videos
    clips=[]

    for vid in remix:
        print vid

        clip = Clip(vid['id'], start=vid['start'], end= vid['end'])
        clip.glow()
        clips.append(clip)

        #begginingClip= Clip(remix[0]["id"])
        #print begginingClip
        # #clips =['remix[0]','remix[1]','remix[2]','remix[3]','remix[4]','remix[5]']
        #clips =[remix[0]["id"],remix[1]["id"],remix[2]["id"],remix[3]["id"],remix[4]["id"],remix[5]["id"]]
        #clips =[Clip(remix[0]["id"]),Clip(remix[1]["id"]),Clip(remix[2]["id"]),Clip(remix[3]["id"]),Clip(remix[4]["id"]),Clip(remix[5]["id"])]
        print remix[0]["id"]
    composition = Composition(clips,singletrack=True)
    #composition.save('firstDream_grey_ocean.mp4')
    composition.save('a_a_a_3Video.mp4')



    #pick each video from start to end

    #apply glow effect to each video

    # add effects
    # #         beginning.glow()         # add a glow effect
    # #         development.glow()
    # #         climax.glow()
    # #         symbolic.glow()
    # #         preending.glow()
    # #         ending.glow()
    # #         ending.fadeout(0.5)

# play selected videos in the sequence order
    # composition(orVideo) = Composition ([beginning,development,climax,symbolicElement,preending,ending])
        #composition.preview()
    #composition(orVideo).save('firstDream_output.mp4')





# print beggining
# print development
# print climax
# print symbolicElement

#calling the function
videoRemixer("black","water")
#videoRemixer("white", "cities")
#videoRemixer("white", "industrialization")
#create the sequence
make_video()



#OLD PROGRAM FOR REFERENCES
# # def createVideos(videos=1):
# #
# #     for counter in range(videos):
# #
# #         # import videos
# #         beginning = glob.glob("videos_golden/beginning/*.mp4")
# #         beginningClip = Clip(random.choice(beginning))
# #         development = glob.glob("videos_golden/development/*.mp4")
# #         developmentClip = Clip(random.choice(development))
# #         climax = glob.glob("videos_golden/climax/*.mp4")
# #         climaxClip = Clip(random.choice(climax))
# #         symbolicElement = glob.glob("videos_golden/symbolicElement/*.mp4")
# #         symbolicClip = Clip(random.choice(symbolicElement))
# #         preEnding = glob.glob("videos_golden/preEnding/*.mp4")
# #         preEndClip = Clip(random.choice(preEnding))
# #         ending = glob.glob("videos_golden/ending/*.mp4")
# #         endClip = Clip(random.choice(ending))
# #
# #         # add effects
# #         beginningClip.glow()         # add a glow effect
# #         developmentClip.glow()
# #         climaxClip.glow()
# #         symbolicClip.glow()
# #         preEndClip.glow()
# #         endClip.glow()
# #         endClip.fadeout(0.5)
# #
# #         # list of clips
# #         clips = [beginningClip,developmentClip,climaxClip,symbolicClip,preEndClip,endClip]
# #
# #         composition = Composition(clips,singletrack=True)
# #         #composition.preview()
# #         filename = 'dream' + str(counter) + '.mp4'
# #         composition.save(filename)
#
# # uncomment this to call the function
# #createVideos(3)
#
#
# # MAKES A LIST OF CLIPS FOR EVERY VIDEO IN THE BEGGINING FOLDER
# # clipsBeggining = []
# # for filename in begginings:
# #     print filename
# #     vid = Clip(filename)
# #     clipsBeggining.append(vid)
# #
# # random.shuffle(clipsBeggining)
# # comp = Composition()
# # comp.preview()
