import os, sys, argparse
import math

from PIL import Image

from progress_bar import ProgressBar

IMG_EXT = [".jpeg", ".jpg", ".jfif", ".pjpeg", ".pjpg", 
           ".png", ".apng", ".webp", ".gif", ".bmp", 
           ".svg", ".tiff", ".tif", ".avif", ".ico", ".cur"]

VID_EXT = [".mp4", ".mov", ".mkv" , ".wmv", ".avi", "webm", ".mpg", ".mpeg"]

AUD_EXT = [".m4a", ".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".aiff"]

def rename_files(args):
  target_directory = args.directory
  set_res_option = args.include_resolution
  
  progress_bar = ProgressBar()
  file_count = 0
  total_files = scan_dir(target_directory)

	for object in os.scandir(target_directory):
    # Checks if object is file and not a folder / directory
		if os.path.isfile(object):
      # Separaetes file name and file extension from full path
			basename = os.path.basename(object)
      # Splits file name from file extenstion
			filename, extension = os.path.splitext(basename)

			filename = replace_with_underscores(filename)
			filename = remove_punctuation_characters(filename)
			filename = format_words(filename, extension)
            
      if set_res_option: 
        filename = append_resolution(object, filename, extension)

			new_basename = filename + extension
			new_filename = os.path.join(target_directory, new_basename)
			print(new_filename)
			os.rename(object, new_filename)
            
      file_count++
      percentage = math.floor((file_count / total_files) * 100)
      
      progress_bar.update(percentage)

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

def append_resolution(object, filename, extension):  
  if extension in IMG_EXT:
    with Image.open(object) as image:
      width, height = image.size
          
      return (filename += "_" + str(width) + "x" + str(height))
  # If not an image file, returns file name with no changes
  return filename  

def scan_dir(target_directory):
  for root, dirnames, filenames in os.walk(target_directory):
    files += len(filenames)
  return files

def parse_args():
  parser = argparse.ArgumentParser(prog='Rename Files Script', 
                                  description='Script renames all files in a given directory.')
  
  parser.add_argument('directory', help='Give the directory where files to be renamed reside.')
  parser.add_argument('-ir','--include-resolution', action='store_true', 
                      help='When set, tells script to include the images resolution in the file name.')
      
  return parser.parse_args()

def main():
  args = parse_args()
  
  if not os.path.isdir(args.directory):
  print("{} does not exist.".format(args.directory))
  return

rename_files(args)

if __name__ == "__main__":
  main()    
    