import os
import shutil
from sklearn.model_selection import train_test_split

# Define paths
cropped_images_path = 'C:/Users/Rushil/Desktop/Major Project/Cropped_Images'
train_path = os.path.join(cropped_images_path, 'train')
val_path = os.path.join(cropped_images_path, 'val')
test_path = os.path.join(cropped_images_path, 'test')

# Ensure the directory structure
for path in [train_path, val_path, test_path]:
    if not os.path.exists(path):
        os.makedirs(path)

# Get a list of all files
all_files = [f for f in os.listdir(cropped_images_path) if os.path.isfile(os.path.join(cropped_images_path, f))]

# Split the dataset
train_files, test_files = train_test_split(all_files, test_size=0.3, random_state=42)
val_files, test_files = train_test_split(test_files, test_size=0.5, random_state=42)

# Function to copy files
def copy_files(files, source_dir, target_dir):
    for file in files:
        shutil.copy(os.path.join(source_dir, file), os.path.join(target_dir, file))

# Copy the files
copy_files(train_files, cropped_images_path, train_path)
copy_files(val_files, cropped_images_path, val_path)
copy_files(test_files, cropped_images_path, test_path)

print("Dataset split and copied into train, validation, and test sets.")
