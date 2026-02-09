from pathlib import Path
import getopt, sys
import os

# start loop that iterates through all files in the directory 
	# for each file, call the following functions:

def rename_files(cwd):

	for item in cwd.iterdir():
		if item.is_file():
			original_filename = os.path.basename(item)
			filename, file_ext = os.path.splitext(original_filename)

			filename = addUnderscores(filename)
			filename = removePunctuation(filename)
			filename = formatWords(filename, file_ext)

			new_filename = filename + file_ext
			os.rename(os.path.join(cwd, original_filename), os.path.join(cwd, new_filename))
			

def addUnderscores(filename):
	new_filename = ""

	for char in filename:
		if char == "-" or char == " ":
			char = "_"
		new_filename += char

	return new_filename	

def removePunctuation(filename):
	new_filename = ""

	for char in filename:
		if char.isalnum() or char == "_":
			new_filename += char

	return new_filename

def formatWords(filename, file_ext):
	media_file_ext = [".gif", ".mp4", ".jpg", ".jpeg", ".png", ".bmp", ".webp", ".jfif"]
	split_name = filename.split("_")
	formatted_words = []

	for word in split_name:
		if file_ext in media_file_ext:
			word = word.capitalize()
		else:
			word.lower()

		formatted_words.append(word)

	return "_".join(formatted_words) 


def getCWD():
  args = sys.argv[1:]
  options = "d:"
  long_options = ["Directory="]

  try:
    arguments, values = getopt.getopt(args, options, long_options)
    for currentArgs, currentVal in arguments:
      if currentArgs in ("-d", "--Directory"):
        return Path(currentVal)

  except getopt.error as err:
    print(str(err))

def main():
	cwd = getCWD()
  
	# If no directory is given, sets default path to the current working directory
	if cwd == None:
		cwd = Path.cwd()

	rename_files(cwd)

if __name__ == "__main__":
  main()    
    