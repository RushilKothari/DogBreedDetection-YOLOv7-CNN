import os
import xml.etree.ElementTree as ET
from PIL import Image
import json

# Directories
annotations_path = 'C:/Users/Rushil/Desktop/Major Project/Annotations'
images_path = 'C:/Users/Rushil/Desktop/Major Project/Images'
yolo_annotations_path = 'C:/Users/Rushil/Desktop/Major Project/YOLO_Annotations'
mapping_file = 'C:/Users/Rushil/Desktop/Major Project/breed_to_id.json'  # Path to the mapping file

# Ensure YOLO annotations directory exists
if not os.path.exists(yolo_annotations_path):
    os.makedirs(yolo_annotations_path)

# Load the breed_to_id mapping from the JSON file
with open(mapping_file, 'r') as f:
    breed_to_id = json.load(f)

def convert_bbox_to_yolo(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

for xml_file in os.listdir(annotations_path):
    base_file_name = os.path.splitext(xml_file)[0]
    xml_path = os.path.join(annotations_path, xml_file)
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    img_file = root.find('filename').text + '.jpg'
    img_path = os.path.join(images_path, img_file)
    
    # Error handling: Check if the image file exists before attempting to open it
    if not os.path.exists(img_path):
        print(f"Warning: Image file does not exist - {img_path}")
        continue  # Skip to the next file if the current image file doesn't exist
    
    img = Image.open(img_path)
    
    yolo_file = os.path.join(yolo_annotations_path, base_file_name + '.txt')
    
    with open(yolo_file, 'w') as f:
        for obj in root.iter('object'):
            breed = obj.find('name').text
            if breed not in breed_to_id:
                print(f"Warning: Breed '{breed}' not found in mapping. Skipping object.")
                continue  # Skip objects with breeds not found in the mapping
            class_id = breed_to_id[breed]
            
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text),
                 float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
            bb = convert_bbox_to_yolo(img.size, b)
            
            f.write(f"{class_id} {bb[0]} {bb[1]} {bb[2]} {bb[3]}\n")

print("YOLO annotations have been generated.")
