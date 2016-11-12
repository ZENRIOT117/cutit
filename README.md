==================================
CutIt.py (c) 2016 Zachary Nichols
==================================

This is a tool to help users download a YouTube video of a "full album" (all songs from a musical album condensed into a single video with no overlap or extra time added) and format it into a folder of the individual songs on the album. THIS TOOL IS MEANT TO HELP USERS WHO HAVE PERMISSION TO USE THE CONTENT OF OTHERS. I WILL NOT BE HELD ACCOUNTABLE FOR ANY COPYRIGHT INFRINGING ACTIVITY THAT MAY IMPLEMENT THIS TOOL.

==================================
INSTALLATION
==================================
1. Extract all files from the archive to an empty directory. This will be your "Working directory".
2. The application requires the user to have python installed and uses several libraries, if you do not have all of these installed, follow the links below to download and install them.

	+ https://www.python.org/downloads/
	+ http://zulko.github.io/moviepy/
	+ https://github.com/nficano/pytube

==================================
USING THE TOOL
==================================
1. Once you have the files extracted and all of the proper dependencies installed, you are ready to use the tool.
2. You will need to define an output directory for the tool to place the files in. One has been provided for you ( the 'out' folder ), but if you wish to use your own output directory, you are free to do so. Remember the path to this directory as you will need it later when you are executing the program.
3. Now, find an album on YouTube that you wish to download. Copy the video slug ( everything after 'v=' and before the next '&' if there is one) and paste it somewhere for the moment. If you have already downloaded the video, simply make note of the file path/name.
4. Next, find the "starting points" of each song within the video. These can usually be found in the description of the video, or in some helpful comment in the comment section. If you cannot find them there, you can easily look up the album and compute each offset manually. Place these "start points" into a text file ( One called 'tracks.txt' has been provided for your use) in the order of their occurrence. You can also include song names, if you so choose. Format the file exactly like this:
	
	With song names:
	```
	0:00 Mountain Heart 
	6:02 Black Slug 
	11:06 Movements In The Sky 
	14:36 Answers In Your Soul 
	18:33 Is Satan Real 
	22:51 Watch It Grow 
	26:50 Evil In Your Eye
	```
	Without song names:
	```
	0:00
	6:02
	11:06
	14:36
	18:33
	22:51
	26:50
	```
5. Now that you have completed your setup, you can run the command line application. The usage for the program is as follows:

   	To download and extract songs from a video:
	```
	python cutit.py -s <track list file> <YouTube slug> <output directory>
	```
	To extract songs from a previously downloaded video:
	```
	python cutit.py -o -s <track list file> <input video file name> <output directory>
	```
