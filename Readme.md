# File Organization Automation
1. Project Overview
This Python script automates the task of organizing files in the specified directory (e.g., Downloads) by sorting them into subfolders based on their file extensions.

# Requirements
Python 3.x: Make sure Python is installed on your machine.
# Installation Instructions
Download and install Python from python.org.
Open your preferred text editor or IDE (like VSCode, PyCharm, etc.).
Create a new file named file_organization.py.
Copy and paste the provided code into this file.
# How to Use
Update the source_dir variable in the script to point to the directory you want to organize (e.g., Downloads).
Open a terminal or command prompt.
Navigate to the directory where file_organization.py is located.
Run the script using the command:
bash
Copy code
python file_organization.py
The script will organize your files into specified folders based on their file extensions.
# Code Explanation
Importing Libraries:

The script uses the os library for file system operations and the shutil library for moving files.
Folder Mapping:

A dictionary that maps folder names to their corresponding file extensions is defined for organizing files.
Creating Folders:

The script checks if the specified folders exist and creates them if they don't.
Moving Files:

It iterates through the files in the source directory and moves them to the appropriate folders based on their extensions.
# Contribution
If you want to contribute to this project, feel free to fork the repository and submit a pull request with your improvements or suggestions.

# License
This project is licensed under the MIT License.