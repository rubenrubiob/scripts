# Scripts
Here I will be adding some system scripts that I find useful. List of scripts:
- [periodic-backup-files.py](#periodic-backup-files-py)

## periodic-backup-files.py

This Python script is meant to perform a periodic backup of some folder within a filesystem —it can be a network disc, if it is mounted on the system— into another folder —that can also be a network disc, on a periodic basis, leaving only a concrete number of copies. This is useful, for example, when you have to make a periodic backup of virtual machines’ files within your local network, so then you can simply `rsync` the backed up folder to a remote resource.

Given a structure like this:
- origin folder
	- subfolder 1
		- file 1
		- file 2
	- subfolder 2
		- file 3
		- file 4
	- subfolder 3
		- file 5
		- file 6

It copies the content to the destination folder as it follows:
- destination-folder
	- subfolder 1
		- daily
			- ymd-hhmmss
				- file 1
				- file 2
	- subfolder 2
		- daily
			- ymd-hhmmss
				- file 3
				- file 4
	- subfolder 3
		- daily
			- ymd-hhmmss
				- file 5
				- file 6

Usage:

	$ python periodic-backup-files.py -h
	usage: periodic-backup-files.py [-h] -i INPUT_FOLDER -d DESTINATION_FOLDER [-m {daily,weekly,monthly}] [-n NUMBER]

	Command to save files keeping only a concrete number of files per folder.

	optional arguments:
  	-h, —help            show this help message and exit
	  -i INPUT_FOLDER, —input-folder INPUT_FOLDER
                        The folder to get the files from.
  	-d DESTINATION_FOLDER, —destination-folder DESTINATION_FOLDER
                        The folder to save the files to.
	  -m {daily,weekly,monthly}, —mode {daily,weekly,monthly}
                        The mode of saving files.
  	-n NUMBER, —number NUMBER
                        The number of copies to keep.

### Example 1

Copy the contents of the /backup/path into the /destination/path folder on a daily basis, keeping only 3 copies:

	$ python periodic-backup-files.py -i /backup/path -d /destination/path

### Example 2

Copy the contents of the /backup/path into the /destination/path folder on a monthly basis, keeping 5 copies:

	$ python periodic-backup-files.py -i /backup/path -d /destination/path -m monthly -n 5
