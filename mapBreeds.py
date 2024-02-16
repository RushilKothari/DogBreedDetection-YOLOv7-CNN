import os
import xml.etree.ElementTree as ET
import json

# Path to the Annotations directory
annotations_path = 'C:/Users/Rushil/Desktop/Major Project/Annotations'
mapping_file = 'C:/Users/Rushil/Desktop/Major Project/breed_to_id.json'  # Path to save the mapping

# Initialize an empty dictionary to store breed to ID mapping
breed_to_id = {}
current_id = 0  # Starting ID

# Iterate over annotation files to build the mapping
for annotation_file in os.listdir(annotations_path):
    xml_path = os.path.join(annotations_path, annotation_file)
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    # Extract breed name
    breed_name = root.find('object/name').text
    
    # Check if the breed is already in the dictionary
    if breed_name not in breed_to_id:
        breed_to_id[breed_name] = current_id
        current_id += 1  # Increment ID for the next unique breed

# Save the mapping to a JSON file
with open(mapping_file, 'w') as f:
    json.dump(breed_to_id, f)

print("Breed to ID mapping saved.")
