import os
import sys
import argparse

from pathlib import Path
from PIL import Image

IMG_EXT = [".jpeg", ".jpg", ".jfif", ".pjpeg", ".pjpg", 
           ".png", ".apng", ".webp", ".gif", ".bmp", 
           ".svg", ".tiff", ".tif", ".avif", ".ico", ".cur"]

VID_EXT = [".mp4", ".mov", ".mkv" , ".wmv", ".avi", "webm", ".mpg", ".mpeg"]

AUD_EXT = [".m4a", ".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".aiff"]

def rename_files(target_directory):

	for object in os.scandir(target_directory):
		if os.path.isfile(object):
			basename = os.path.basename(object)
			filename, extension = os.path.splitext(basename)

			filename = replace_with_underscores(filename)
			filename = remove_punctuation_characters(filename)
			filename = format_words(filename, extension)

			new_basename = filename + extension
			new_filename = os.path.join(target_directory, new_basename)
			print(new_filename)
			os.rename(object, new_filename)		

def replace_with_underscores(filename):
	string = ""

	for char in filename:
		if char == "-" or char == " ":
			char = "_"
		string += char

	return string	

def remove_punctuation_characters(filename):
	string = ""

	for char in filename:
		if char.isalnum() or char == "_":
			string += char

	return string

def format_words(filename, extension):
	media_file_ext = IMG_EXT + VID_EXT + AUD_EXT
	split_name = filename.split("_")
	formatted_words = []

	for word in split_name:
		if extension in media_file_ext:
			word = word.capitalize()
		else:
			word = word.lower()

		formatted_words.append(word)

	return "_".join(formatted_words) 

def main():
	target_directory = sys.argv[1]

	if not os.path.isdir(target_directory):
		print("{} does not exist.".format(target_directory))
		return

	rename_files(target_directory)

if __name__ == "__main__":
  main()    
    