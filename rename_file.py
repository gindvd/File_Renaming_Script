from pathlib import Path
import getopt, sys

# take file directory as an argument or use cwd

# start loop that iterates through all files in the directory 

# for each file, call the following functions: 

# get file extension
  # remove file extension
  # save file extension is separate value
  # return file name with no extension
    

#replace dashes with underscores
  # loop through all characters
  # find dashes, replace with underscores

#remove punctuation
  # split file name via underscore
  # iterate through all characters
  # remove character if no alphanumeric value

# lower or capitalize words
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
        directory = Path(currentVal)
				# Returns the full path of the driectory
        return directory.resolve()

  except getopt.error as err:
    print(str(err))

def main():
	cwd = getCWD()
  
	# If no directory is given, sets default path to the current working directory
	if cwd == None:
		cwd = Path.cwd()

	print(cwd)

if __name__ == "__main__":
  main()    
    