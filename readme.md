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

To istall use: pip3 install pillow
It is recommended to set up a python virtual environmnt inside the directory where 
this script is store then install pip to this virtual environmnt.

The script requires a directory path as an argument when launching the script.

Examples of command to run script: 
For Windows: python3 rename_file.py C:\Users\USERNAME\Pictures\Wallpaper
For Linux: python3 rename_file.py /home/USERNAME/Pictures/Wallpaper

Optinal arguments:

Adding -ir or --include-resolution to the run command will add image resolution to image file's name.
Ex: python3 rename_file.py /home/USERNAME/Pictures/Wallpaper --include-resolution

For Linux and Unix-like operating-systems, the file contains a sheband so the script's permission can be 
changed to execute.

If the script has an associated virtual environment, change the shbang to point to the virtual environment.
