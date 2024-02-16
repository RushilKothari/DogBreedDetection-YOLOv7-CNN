import os
import shutil

# Define the directory containing the subfolders
main_folder = "Annotation"

# Iterate over each subfolder
for folder_name in os.listdir(main_folder):
    folder_path = os.path.join(main_folder, folder_name)

    # Check if the entry is a directory
    if os.path.isdir(folder_path):
        # Iterate over each file in the subfolder
        for filename in os.listdir(folder_path):
            # Move the file to the main folder
            src = os.path.join(folder_path, filename)
            dst = os.path.join(main_folder, filename)
            shutil.move(src, dst)
            print(f"Moved: {src} -> {dst}")

print("All files moved to the main folder.")