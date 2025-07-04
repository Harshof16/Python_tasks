# categorize files in a folder based on their extensions

# Steps
# 1. Define the structure of the folders with their listed extensions. (in Dictionary)
# 2. Scan for all the files in the specified folder.
# 3. check the selected file extension.
# 4. If extension matches with any of the defined extensions, move/copy the file to the corresponding folder.
# 5. Create the folder if it does not exist.
# 6. Also log the moved/copied files in a log file within the respective folder.

import os
import shutil

# dict
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Archives": [".zip", ".rar", ".7z"],
    "Videos": [".mp4", ".mov", ".mkv"],
    "Code": [".py", ".js", ".html", ".css"]
}

def categorize_files(folder_path):
    files = os.listdir(folder_path)
    for file in files:
        _, ext = os.path.splitext(file)
        file_path = os.path.join(folder_path, file)
        #check if it is a file
        if os.path.isfile(file_path):
            for folder, extensions in file_types.items(): # same like entries in js
                if ext in extensions:
                    target_folder = os.path.join(folder_path, folder)
                    os.makedirs(target_folder, exist_ok=True) # creating the extension folder if it does not exist
                    log_file = os.path.join(target_folder, f'{folder}_log.txt')
                    shutil.copy(file_path, target_folder)
                    with open(log_file, 'a') as log:
                        log.write(f"Copied {file} to {target_folder}\n")
                    print(f"Copied {file} to {target_folder}")
                    break  # break to avoid copying the same file multiple times
                    

# Example usage
if __name__ == "__main__":
    folder_path = r"c:\Users\harsh\Downloads"  # Change this to your target folder
    categorize_files(folder_path)
