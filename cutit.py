import os

import moviepy.editor as mp
import argparse as arp
from pytube import YouTube
import sys
import atexit


def init():
    parser = arp.ArgumentParser()
    parser.add_argument("-o", "--offline", help="Parse an already downloaded file", action="store_true")
    parser.add_argument("-s", "--splitontimes", help="Split the input video into songs based on the starting time of "
                                                     "each song in the provided input file")
    parser.add_argument("filename", help="The input video file from a local source, or the video slug from youtube")
    parser.add_argument("output", help="The directory to output the audio files to")
    args = parser.parse_args()
    return args


def main():
    #atexit.register(exit_handler)
    args = init()
    tmp = parse_time(args.splitontimes)
    time = tmp[0]
    names = tmp[1]
    if args.offline:
        clip = mp.VideoFileClip(args.filename).subclip(time[len(list(time.keys()))])
        write_clip(args.filename, args.output, time, names, len(list(time.keys())), clip)
    else:
        getvid(args.filename)
        print("Download Finished Successfully")
        clip = mp.VideoFileClip("tmp.mp4").subclip(0)
        write_clip("tmp.mp4", args.output, time, names, len(list(time.keys())), clip)


def getvid(fname):
    yt = YouTube("http://www.youtube.com/watch?v=" + fname)
    tmp = dict()
    for v in yt.get_videos():
        if v.video_codec == "H.264":
            tmp[v.resolution] = v
    video = yt.get('mp4', tmp[max(tmp.keys())].resolution)
    print("Downloading video: " + str(tmp[max(tmp.keys())]))
    video.download('tmp.mp4')


def parse_time(fname):
    tmpdict = dict()
    namedict = dict()
    try:
        with open(fname, mode='r') as ins:
            count = 0
            for i in ins:
                count += 1
                tmp = i.split(':')
                tmp2 = tmp[1].split(" ", 1)
                time = int(tmp[0]) * 60 + int(tmp2[0])
                tmpdict[count] = time
                namedict[count] = tmp2[1].strip()
    except FileNotFoundError:
        sys.stderr.write("Error: " + fname + " does not exist")
        exit()
    return [tmpdict, namedict]


def write_clip(fname, opath, times, names, starttime, clip):
    if starttime <= 0:
        print("Done Converting video.")
        return True
    else:
        tmpclip = clip.subclip(times[starttime])
        if len(names[starttime]) > 0:
            tmp = str(opath) + "/" + str(starttime) + " " + str(names[starttime]) + ".mp3"
            tmpclip.audio.write_audiofile(filename=tmp, nbytes=2, bitrate="320k")
        else:
            tmpclip.audio.write_audiofile(filename=str(opath + "/" + str(starttime) + ".mp3"), nbytes=2, bitrate="320k")
        write_clip(fname, opath, times, names, starttime - 1, mp.VideoFileClip(fname).subclip(0, times[starttime]))

"""
def exit_handler():
    if os.path.exists("tmp.mp4"):
        os.remove("tmp.mp4")
"""

if __name__ == '__main__':
    main()
