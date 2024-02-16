import shutil
import os 

# Base directory where your project is located
base_dir = 'C:/Users/Rushil/Desktop/Major Project'

# Directories for images
image_dirs = {
    'train': os.path.join(base_dir, 'train'),
    'val': os.path.join(base_dir, 'val'),
    'test': os.path.join(base_dir, 'test')
}

# Directories for annotations
annotation_src_dir = os.path.join(base_dir, 'YOLO_Annotations')
annotation_dirs = {
    'train': os.path.join(base_dir, 'train', 'annotations'),
    'val': os.path.join(base_dir, 'val', 'annotations'),
    'test': os.path.join(base_dir, 'test', 'annotations')
}

# Create annotation directories if they don't exist
for dir_path in annotation_dirs.values():
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def distribute_annotations(image_dir, annotation_src_dir, annotation_dest_dir):
    """
    Moves annotation files to the corresponding set directory based on the presence of image files.
    """
    # List all image files in the directory
    image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]
    
    for image_file in image_files:
        # Construct the corresponding annotation file name
        annotation_file = os.path.splitext(image_file)[0] + '.txt'
        src_annotation_path = os.path.join(annotation_src_dir, annotation_file)
        
        # Check if the annotation file exists
        if os.path.exists(src_annotation_path):
            # Move the annotation file
            shutil.move(src_annotation_path, annotation_dest_dir)
        else:
            print(f"Warning: Annotation file does not exist for {image_file}")

# Distribute annotations for each set
for set_name, img_dir in image_dirs.items():
    distribute_annotations(img_dir, annotation_src_dir, annotation_dirs[set_name])

print("Annotation files have been distributed.")