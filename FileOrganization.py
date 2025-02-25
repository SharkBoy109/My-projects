import os
import shutil

def organize_files(directory):
    # Create folders for different file types
    extensions = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'Audio': ['.mp3', '.wav', '.aac'],
        'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
        'Archives': ['.zip', '.rar', '.tar', '.gz'],
    }
    
    # Create directories for each type if they don't exist
    for folder in extensions:
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
    
    # Iterate through all files in the given directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Get file extension
        _, file_extension = os.path.splitext(filename)
        
        # Move file to the appropriate folder
        moved = False
        for folder, exts in extensions.items():
            if file_extension.lower() in exts:
                shutil.move(file_path, os.path.join(directory, folder, filename))
                moved = True
                break
        
        # Optionally, move files without extensions into 'Others'
        if not moved:
            others_folder = os.path.join(directory, 'Others')
            if not os.path.exists(others_folder):
                os.mkdir(others_folder)
            shutil.move(file_path, os.path.join(others_folder, filename))

# Usage
organize_files('/path/to/your/folder')
