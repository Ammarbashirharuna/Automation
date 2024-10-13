import os
import shutil

# Define the source directory (Downloads folder)
source_dir = 'C:\\Users\\Ammar\\Downloads'  # Double backslashes
 # Update this path

# Define the target directories
target_dirs = {
    'images': os.path.join(source_dir, 'Images'),
    'documents': os.path.join(source_dir, 'Documents'),
    'videos': os.path.join(source_dir, 'Videos'),
    'others': os.path.join(source_dir, 'Others')
}

# Create target directories if they don't exist
for directory in target_dirs.values():
    if not os.path.exists(directory):
        os.makedirs(directory)

# Move files to their respective directories
for filename in os.listdir(source_dir):
    # Skip directories
    if os.path.isdir(os.path.join(source_dir, filename)):
        continue
    
    # Check the file extension
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        shutil.move(os.path.join(source_dir, filename), target_dirs['images'])
    elif filename.lower().endswith(('.pdf', '.doc', '.docx', '.txt')):
        shutil.move(os.path.join(source_dir, filename), target_dirs['documents'])
    elif filename.lower().endswith(('.mp4', '.avi', '.mov')):
        shutil.move(os.path.join(source_dir, filename), target_dirs['videos'])
    else:
        shutil.move(os.path.join(source_dir, filename), target_dirs['others'])

print("Files have been organized.")
