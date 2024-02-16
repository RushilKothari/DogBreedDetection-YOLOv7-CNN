import os
import xml.etree.ElementTree as ET
from PIL import Image

# Paths
annotations_path = 'C:/Users/Rushil/Desktop/Major Project/Annotations'
images_path = 'C:/Users/Rushil/Desktop/Major Project/Images'
cropped_images_path = 'C:/Users/Rushil/Desktop/Major Project/Cropped_Images'

# Make sure the cropped images directory exists
if not os.path.exists(cropped_images_path):
    os.makedirs(cropped_images_path)

def crop_image(image_path, output_path, bbox):
    """Crop the image to the specified bounding box and save it."""
    with Image.open(image_path) as image:
        cropped_image = image.crop(bbox)  # Crop
        cropped_image.save(output_path)  # Save

for annotation_file in os.listdir(annotations_path):
    annotation_path = os.path.join(annotations_path, annotation_file)
    tree = ET.parse(annotation_path)
    root = tree.getroot()
    
    # Assuming filename does not include the extension
    filename_without_extension = root.find('filename').text
    # Assuming images are in .jpg format; change as necessary
    filename_with_extension = filename_without_extension + '.jpg'
    
    image_path = os.path.join(images_path, filename_with_extension)
    
    if not os.path.isfile(image_path):
        print(f"Warning: File does not exist - {image_path}")
        continue  # Skip this iteration if the file doesn't exist
    
    for obj in root.findall('object'):
        bbox = obj.find('bndbox')
        xmin = int(bbox.find('xmin').text)
        ymin = int(bbox.find('ymin').text)
        xmax = int(bbox.find('xmax').text)
        ymax = int(bbox.find('ymax').text)
        
        # Define the output path for the cropped image
        # This example overwrites images with the same name from different annotations. 
        # You might want to adjust this behavior to suit your needs.
        output_path = os.path.join(cropped_images_path, filename_with_extension)
        
        # Crop and save the image
        crop_image(image_path, output_path, (xmin, ymin, xmax, ymax))

print("Cropping completed.")
