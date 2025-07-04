# Auto-delete Temporary Files
# Write a Python script that automatically scans a folder and deletes files with specific extensions (tmp, log, bak, cache, old) commonly used for temporary or debug content.

def clean_temp_files(folder_path):
    import os

    #create a log file to log deleted files
    log_file = os.path.join(folder_path, 'deleted_files_log.txt')

    #list all the files in the specified folder
    files = os.listdir(folder_path)

    #extensions to be deleted
    temp_extensions = ['.tmp', '.log', '.bak', '.cache', '.old']

    #open log file in append mode
    with open(log_file , 'a') as log:
        for file in files:
            file_path = os.path.join(folder_path, file)
            #check if it is a file
            if not os.path.isfile(file_path):
                continue
            #check if file has temp extension
            _, ext = os.path.splitext(file)
            if ext in temp_extensions:
                os.remove(file_path)
                log.write(f'Deleted: {file}\n')
                print(f"Deleted: {file}")

# Example usage
clean_temp_files(r"c:\Users\harsh\Downloads")

# to remove the files from the subfolders as well, you can use os.walk
#  for root, dirs, files in os.walk(folder_path):
#     for file in files: