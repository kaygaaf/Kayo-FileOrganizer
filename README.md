# Automatic File Organizer 🗂️

A Python script to automatically sort files in a directory into subfolders based on their extensions. Say goodbye to cluttered folders!
I personally use this after photo and videoshoots to automatically sort raw/jpg and video files by letting it auto run when connecting the SD card.

<img width="366" height="314" alt="Screenshot 2025-08-05 at 15 40 55" src="https://github.com/user-attachments/assets/59ab7f52-e571-49d8-b9c3-dc2c5cb66a90" />


## Features
- Scans a directory for files.
- Creates subfolders for each file type (e.g., "Images" for .jpg, .png).
- Moves files into the appropriate folders.
- Ignores directories and hidden files.
- Customizable extensions and folder names.

## Installation
1. Clone the repo: `git clone https://github.com/kaygaaf/Kayo-FileOrganizer`
2. Navigate to the directory: `cd Kayo-FileOrganizer`

## Usage
Edit the extension_map dictionary in Kayo-FileOrganizer.py to group extensions (e.g., combine .jpg and .png into "Images").

Run the script with a directory path:
```bash
python Kayo-FileOrganizer.py /path/to/your/directory
