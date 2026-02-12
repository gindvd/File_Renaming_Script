import os
import sys
import argparse

from pathlib import Path
from PIL import Image

IMG_EXT = [".jpeg", ".jgp", ".jfif", ".pjpeg", ".pjpg", 
           ".png", ".apng", ".webp", ".gif", ".bmp", 
           ".svg", ".tiff", ".tif", ".avif", ".ico", ".cur"]

VID_EXT = [".mp4", ".mov", ".mkv" , ".wmv", ".avi", "webm", ".mpg", ".mpeg"]

AUD_EXT = [".m4a", ".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".aiff"]

def rename_files(target_directory):

	for object in os.scandir(target_directory):
		if os.path.isfile(object):
			basename = os.path.basename(object)
			filename, extension = os.path.splitext(basename)

def main():
	target_directory = sys.argv[1]

	if not os.path.isdir(target_directory):
		print("{} does not exist.".format(target_directory))
		return

	rename_files(target_directory)

if __name__ == "__main__":
  main()    
    