# Auto-delete Temporary Files
# Write a Python script that automatically scans a folder and deletes files with specific extensions (tmp, log, bak, cache, old) commonly used for temporary or debug content.

def clean_temp_files(folder_path):
    import os