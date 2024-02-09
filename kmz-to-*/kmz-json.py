import xmltodict
import json
import zipfile
import os
import sys

def extract_kml_from_kmz(kmz_file_path):
    # Create a temporary directory to extract the KMZ contents
    temp_dir = "temp_kml"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    with zipfile.ZipFile(kmz_file_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)
        # Assuming there's only one KML file in the KMZ
        for file in os.listdir(temp_dir):
            if file.endswith(".kml"):
                return os.path.join(temp_dir, file)

def kml_to_json(kml_file_path, json_file_path):
    with open(kml_file_path, 'r') as kml_file:
        kml_content = kml_file.read()
    kml_dict = xmltodict.parse(kml_content)
    with open(json_file_path, 'w') as json_file:
        json.dump(kml_dict, json_file, indent=4)
    # Clean up: remove the KML file and temporary directory
    os.remove(kml_file_path)
    os.rmdir(os.path.dirname(kml_file_path))
    print(f"Converted KMZ to JSON and saved to {json_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_kmz_file_path> <output_json_file_path>")
        sys.exit(1)

    input_kmz_file_path = sys.argv[1]
    output_json_file_path = sys.argv[2]

    # Extract KML from KMZ
    kml_file_path = extract_kml_from_kmz(input_kmz_file_path)
    
    # Convert KML to JSON
    kml_to_json(kml_file_path, output_json_file_path)
