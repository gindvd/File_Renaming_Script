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

			#filename = dashesToUnderscores(filename)
			#filename = removePunctuation(filename)
			#filename = formatWords(filename, file_ext)

			print(original_filename)
			new_filename = str(filename) + str(file_ext)
			print(new_filename)
			os.rename(os.path.join(cwd, original_filename), os.path.join(cwd, new_filename))
			

def dashesToUnderscores(filename):
	pass
	#replace dashes with underscores
  # loop through all characters
  # find dashes, replace with underscores

def removePunctuation(filename):
	pass
	#remove punctuation
  # split file name via underscore
  # iterate through all characters
  # remove character if no alphanumeric value

def formatWords(filename, file_ext):
	pass
  # split name via underscore
  # check file extenion

  # if file extension image, gif, vide or text file 
    # capitalize each word in name

  #else
    # toLower() each word


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
    