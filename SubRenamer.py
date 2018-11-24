import os
import re

"""
Author: Wilson.Zhang
Date: 2018/11/18
Usage: Load files inside given folder and rename every subtitles based on chapter (if it has),
or just simply rename it.
"""

path = input("Show me the path: ")
print("The path is:", path)
try:
    dirs = os.listdir(path)
except IOError:
    print("Invalid path")
else:
    os.chdir(path)  # Change working folder
    sub = []
    video = []
    for index in range(len(dirs)):
        # if re.match(".mkv", dirs[index][-4:]):
        if re.match(".mkv|.mp4|.avi", dirs[index][-4:]):
            print("We got video file: ", dirs[index])
            video.append(dirs[index])
        elif re.match(".ass|.ssa|.sub|.srt", dirs[index][-4:]):
            print("We got subtitle: ", dirs[index])
            sub.append(dirs[index])

        # in case we don't have files:
        if index == (len(dirs)-1) and (len(video) == 0 or len(sub) == 0):
            print("Hey! No video or sub file! I gonna go...")  # EXIT 1!
            exit()
    # Alright, let's get rid of sth we don't need...
    delist = []
    MultiChap = False
    for index in range(len(video)):
        if re.search("sample", video[index], re.I):
            delist.append(video[index])

        if re.match(".\n*\[[0-9]{2}\].\n*", video[index], re.I) or len(video) >= 10:
            MultiChap = True
    video = list(set(video).difference(set(delist)))
    # print(MultiChap)
    """
    remain unsolved:
    mode 1: if there is no "[0-9]" sub or video file num is less than 2, just rename all the sub files...
    mode 2: if video file num is more than 1, then rename sub according to acquired chapter, like [01] -> [01]......
    """
    # Mode 1
    newsublist = []
    if MultiChap is False and len(video) < 2:
        videoname = video[0][:-4]
        pattern = re.compile(r"\.+")
        for index in range(len(sub)):
            tmp = pattern.split(sub[index])
            # Let's assume all sub maker is warmhearted enough to follow '.lang.sub' rule
            lang = tmp[len(tmp) - 2]
            tmp = videoname + "." + lang + "." + tmp[len(tmp)-1]
            print("Old file name: ", sub[index], "This is the new name of your sub: ", tmp)
            newsublist.append(tmp)
        situ = input("Do you want to proceed? [Y/N]")
        if situ == "Y" and len(newsublist) == len(sub):  # in case sth's wrong!
            for index in range(len(sub)):
                try:
                    os.renames(sub[index], newsublist[index])
                except IOError:
                    print("Something's wrong with you sub file...")  # EXIT 2!
                    exit()
                else:
                    print("Successfully replace ", sub[index], " into ", newsublist[index])
            print("Done, exit...")  # EXIT 3!
            exit()
        else:
            print("Better luck next time!")  # EXIT 3!
            exit()
    elif MultiChap is True:
        exit()
    else:
        exit()
