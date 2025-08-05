
#### Main Code (Kayo-FileOrganizer.py):
```python
import os
import shutil
import sys

# Custom mapping for extensions to folder names (extend as needed)
extension_map = {
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.gif': 'Images',
    '.pdf': 'Documents',
    '.arw': 'Raw',
    '.mp4': 'Video',
    '.mov': 'Video',
    '.docx': 'Documents',
    '.txt': 'Documents',
    '.py': 'Scripts',
    '.csv': 'Data',
    # Add more as needed
}

def organize_files(directory):
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist!")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Skip directories and hidden files
        if os.path.isdir(file_path) or filename.startswith('.'):
            continue
        
        # Get extension
        _, ext = os.path.splitext(filename)
        ext = ext.lower()
        
        if ext:
            # Get folder name from map or default to uppercase extension + 's'
            folder_name = extension_map.get(ext, ext[1:].upper() + 's')
            folder_path = os.path.join(directory, folder_name)
            
            # Create folder if it doesn't exist
            os.makedirs(folder_path, exist_ok=True)
            
            # Move file
            dest_path = os.path.join(folder_path, filename)
            shutil.move(file_path, dest_path)
            print(f"Moved '{filename}' to '{folder_name}'")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python organizer.py <directory_path>")
        sys.exit(1)
    
    dir_path = sys.argv[1]
    organize_files(dir_path)
