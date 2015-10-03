import argparse
import subprocess
import os
import shutil
from datetime import datetime

# Get command line options
parser = argparse.ArgumentParser(description='Command to save files keeping only a concrete number of files per folder.')
parser.add_argument('-i', '--input-folder', help='The folder to get the files from.', required=True)
parser.add_argument('-d', '--destination-folder', help='The folder to save the files to.', required=True)
parser.add_argument('-m', '--mode', choices=['daily', 'weekly', 'monthly'], help='The mode of saving files.', default='daily', required=False)
parser.add_argument('-n', '--number', help='The number of copies to keep.', type=int, default=3, required=False)
args = parser.parse_args()


# Get all subfolders within input folder
input_subfolders = subprocess.check_output(['find', args.input_folder.rstrip('/'), '-type', 'd', '-print'], universal_newlines=True)
input_subfolders = input_subfolders.rstrip().split('\n')[1:]

# Set date, so it is common to all subfolders
datetime_now_string = datetime.now().strftime('%Y%m%d-%H%M%S')

# Set the destination folder, without trailing slash
parent_destination_folder = args.destination_folder.rstrip('/')

for input_subfolder in input_subfolders:
    # Get subfolder name. We need it to replicate it within the destination folder
    folder_name = os.path.basename(input_subfolder)
    
    # Get the list of files we have to copy
    files_to_copy = subprocess.check_output(['find', input_subfolder.rstrip('/'), '-type', 'f', '-print'], universal_newlines=True)
    files_to_copy = files_to_copy.rstrip().split('\n')
    
    # Destination folder has the structure: destination/folder_name/mode/date_time/
    base_destination_folder = '%s/%s/%s' % (parent_destination_folder, folder_name, args.mode)
    destination_folder = '%s/%s' % (base_destination_folder, datetime_now_string)

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        
    # Copy files
    for file_to_copy in files_to_copy:
        destination_file = '%s/%s' % (destination_folder, os.path.basename(file_to_copy))
        shutil.copy2(file_to_copy, destination_file)
        
    # Remove existing files, if needed

        
    # Keep only number files
    existing_files = subprocess.check_output(['find', base_destination_folder.rstrip('/'), '-type', 'd', '-print'], universal_newlines=True)
    existing_files = existing_files.rstrip().split('\n')[1:]
    existing_files.sort(reverse=True)
    
    if len(existing_files) > 0:
        existing_files = existing_files[args.number:]
        
        for existing_file in existing_files:
            shutil.rmtree(existing_file)