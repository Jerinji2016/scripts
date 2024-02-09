import xmltodict
import json
import sys

def kml_to_json(kml_file_path, json_file_path):
    # Read the KML file
    with open(kml_file_path, 'r') as kml_file:
        kml_content = kml_file.read()
    
    # Convert KML content to a Python dictionary
    kml_dict = xmltodict.parse(kml_content)
    
    # Convert the Python dictionary to JSON
    json_content = json.dumps(kml_dict, indent=4)
    
    # Write the JSON content to a file
    with open(json_file_path, 'w') as json_file:
        json_file.write(json_content)

    print(f"Converted KML to JSON and saved to {json_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python kml-json-converter.py <input_kml_file_path> <output_json_file_path>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    
    kml_to_json(input_file_path, output_file_path)
