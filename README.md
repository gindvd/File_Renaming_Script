# File Renaming Script

## Description:

Use this script to mass rename filenames to a consistent format. The formatting
is based on my personal file naming conventions. 

All spaces and bashes are replaced with underscores, and punctuation characters are removed.
For image, audio and video files, each word is capitalized, and for all other files, every
word is lowercased.

An optional argumant can be set to add an images resolution to the file's name. Use for keeping 
easy track of file resolutions for wallpapers.


## How To Use:

This script requires the pillow third party library.

To istall use: pip3 install pillow <br>
It is recommended to set up a python virtual environmnt inside the directory where 
this script is store then install pip to this virtual environmnt.

The script requires a directory path as an argument when launching the script.

Examples of command to run script: <br>
For Windows: python3 rename_file.py C:\Users\USERNAME\Pictures\Wallpaper <br>
For Linux: python3 rename_file.py /home/USERNAME/Pictures/Wallpaper <br>

Optinal arguments:

Adding -ir or --include-resolution to the run command will add image resolution to image file's name.<br>
Ex: python3 rename_file.py /home/USERNAME/Pictures/Wallpaper --include-resolution <br>

For Linux and other Unix-like operating-systems, the file contains a sheband so the script's permission can be 
changed to execute with the chmod +x rename_file.py commannd.

If the script has an associated virtual environment, change the shebang to point to the virtual environment.

##How To Add Optional Progress Bar

A CLI rendered progress bar can be added to this script to get a visual representation of files iterated over. <br>
The progress bar script can be cloned from: https://github.com/gindvd/CLI_progress_bar

Once file is cloned, add the progress_bar.py file into the same directory that this script resides. <br>
Then the following lines in the rename_file.py script can be uncommented by deleteing the # symbol at the start of the line:<br>
Line 9<br>Line 23<br>Line 47<br>Line 49

