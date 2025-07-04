#Build a File Organizer for html Files

import os
import shutil

# get downloads directory
downloads = os.path.expanduser("~/Downloads")

# log entries of moving files (great in automation tasks)
log_file = os.path.join(downloads, 'html_log.txt')

# list all files in the downloads directory
files = os.listdir(downloads)

# filtering out html files
htmlFiles = list(filter(lambda x: x.endswith('.html'), files))

# create a subfolder for html files
html_folder = os.path.join(downloads, 'html_files')
os.makedirs(html_folder, exist_ok=True)

# appending log entries to the log file
with open(log_file, 'a') as log:
    #move html files to the subfolder
    for file in htmlFiles:
        source = os.path.join(downloads, file)
        shutil.move(source, html_folder)
        log.write(f"Moved {file} to {html_folder}\n")
        print(f"Moved {file} to {html_folder}")


# Move files based on their extensions to respective folders
# for file in files:
#     if os.path.isfile(os.path.join(downloads, file)):
#         _, ext = os.path.splitext(file)
#         ext = ext.lower().strip('.')

#         if ext:  # skip files without extension
#             target_folder = os.path.join(downloads, ext + "_files")
#             os.makedirs(target_folder, exist_ok=True)
#             shutil.move(os.path.join(downloads, file), os.path.join(target_folder, file))
#             print(f"Moved {file} to {target_folder}")
