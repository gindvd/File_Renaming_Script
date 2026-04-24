import os
import argparse
import re
import math

from PIL import Image

from src.progress_bar import ProgressBar

def rename_files(args):
  target_directory = args.directory
  append_resolution = args.resolution
  remove_punctuation = args.rm_punctuation
  capitalize = args.capitalize

  progress_bar = ProgressBar()
  file_count = 0
  total_files = scan_dir(target_directory)

  for item in os.scandir(target_directory):
    # Checks if item is file and not a folder / directory
    if os.path.isfile(item):

      base_name = os.path.basename(item)
      # Splits file name from file extenstion
      name, ext = os.path.splitext(base_name)

      new_name = replace_with_underscores(name)
      new_name = remove_empty_strings(new_name)

      if remove_punctuation:
        new_name = remove_punctuation_characters(new_name)

      if append_resolution:
        new_name = append_image_resolution(item, new_name)

      if capitalize:
        new_name = capitalize_words(new_name)

      new_basename = new_name + ext
      new_filename = os.path.join(target_directory, new_basename)

      try:
        os.rename(item, new_filename)
      except FileExistsError:
        os.remove(item)
      
      file_count += 1
      percentage = math.floor(file_count / total_files) * 100

      progress_bar.update(percentage)

def valid_image_file(file: os.Pathlike) -> bool:
  try:
    with Image.open(file) as img:
      img.verify()
      return True
  except (IOError, SyntaxError):
    return False

def replace_with_underscores(filename):
  string = ""
  for char in filename:
    if char == "-" or char == " ":
      char = "_"
    
    string += char

  return string	

def remove_empty_strings(string_list):
  list = []

  for word in string_list:
    if word != "":
      list.append(word)

  return list

def remove_punctuation_characters(filename):
  string = ""

  for char in filename:
    if char.isalnum() or char == "_":
      string += char

  return string

def append_image_resolution(item, name):
  if not valid_image_file(item):
    return name

  split_name = name.split("_")

  with Image.open(item) as image:
    width, height = image.size

  resolution = str(width) + "x" + str(height)

  # Only adds the files resolution if it's not already in the filename
  if resolution not in split_name:
    return name + "_" + resolution

  return name

def capitalize_words(name):
  split_name = name.split("_")

  new_name = []

  for word in split_name:
    if re.match("[a-zA-Z]", word[:1]):
      word = word.capitalize()
    
    new_name.append(word)
  
  return "_".join(new_name)

def scan_dir(target_directory):
  files = 0
  for root, dirnames, filenames in os.walk(target_directory):
    files += len(filenames)
  return files

def parse_args():
  parser = argparse.ArgumentParser(prog='Rename Files Script', 
                                  description='Script renames all files in a given directory.')

  parser.add_argument('directory', help='Directory to scan, and rename all files')

  parser.add_argument('-r','--resolution', action='store_true', 
                      help="Append image resolution to file's name.")
  
  
  parser.add_argument("-rp", "--rm_punctuation", action="store_true",
                      help="Remove all non-alphanumeric characters from filename")
  
  parser.add_argument("-c", "--capitalize", action="store_true",
                      help="Capitalize all words in files_name")
      
  return parser.parse_args()

def main():
  args = parse_args()

  if not os.path.isdir(args.directory):
    print("{} does not exist.".format(args.directory))
    return

  rename_files(args)

if __name__ == "__main__":
  main()    