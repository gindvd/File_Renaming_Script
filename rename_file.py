import os, sys
import argparse

from pathlib import Path
from PIL import Image

IMG_EXT = [".jpeg", ".jgp", ".jfif", ".pjpeg", ".pjpg", 
           ".png", ".apng", ".webp", ".gif", ".bmp", 
           ".svg", ".tiff", ".tif", ".avif", ".ico", ".cur"]

VID_EXT = [".mp4", ".mov", ".mkv" , ".wmv", ".avi", "webm", ".mpg", ".mpeg"]

AUD_EXT = [".m4a", ".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".aiff"]

def rename_files(target_directory, add_resolution):

	for item in target_directory.iterdir():
		if item.is_file():
			original_filename = os.path.basename(item)
			filename, file_ext = os.path.splitext(original_filename)

			filename = replace_with_underscores(filename)
			filename = remove_punctuation(filename)
			filename = format_words(filename, file_ext)

			new_filename = filename + file_ext
			os.rename(os.path.join(target_directory, original_filename), os.path.join(target_directory, new_filename))
			
# Replaces spaces and dashes with underscores
def replace_with_underscores(filename):
	new_filename = ""

	for char in filename:
		if char == "-" or char == " ":
			char = "_"
		new_filename += char

	return new_filename	

def remove_punctuation(filename):
	new_filename = ""

	for char in filename:
		if char.isalnum() or char == "_":
			new_filename += char

	return new_filename

def format_words(filename, file_ext):
	media_file_ext = IMG_EXT + VID_EXT + AUD_EXT
	split_name = filename.split("_")
	formatted_words = []

	for word in split_name:
		if file_ext in media_file_ext:
			word = word.capitalize()
		else:
			word.lower()

		formatted_words.append(word)

	return "_".join(formatted_words) 

def main():
	parser = argparse.ArgumentParser(description='Set target directory, and options to rename files')

	parser.add_argument('target_directory', type=str, help="The target directory storing the files to be renamed.")
	parser.add_argument('-r', '--resolution', action='store_true', help="Add image resolution to the file's name.")

	if os.path.isdir(args.target_directory):
		target_directory = args.target_directory
	elif args.target_directory == "":
		target_directory = os.getcwd()
	else:
		# Exits script if the directory doesn't exist
		print("{} does not exist!".format(args.target_directory))
		sys.exit(1)

	add_resolution = args.resolution

	rename_files(target_directory, add_resolution)

if __name__ == "__main__":
  main()    
    