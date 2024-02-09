import xmltodict
import zipfile
import os
import sys
from openpyxl import Workbook

def extract_kml_from_kmz(kmz_file_path):
    # Extract KML from KMZ
    with zipfile.ZipFile(kmz_file_path, 'r') as zip_ref:
        zip_ref.extractall("temp_kml")
        # Assuming there's only one kml file in the KMZ
        for file in os.listdir("temp_kml"):
            if file.endswith(".kml"):
                return os.path.join("temp_kml", file)

def parse_kml_to_data(kml_file_path):
    # Parse KML and extract data
    with open(kml_file_path, 'r') as kml_file:
        kml_content = kml_file.read()
    
    kml_dict = xmltodict.parse(kml_content)
    # Example: Extracting place names and coordinates; adjust as needed
    places = []
    for placemark in kml_dict['kml']['Document']['Folder']['Placemark']:
        name = placemark['name']
        coordinates = placemark['Point']['coordinates']
        places.append({'name': name, 'coordinates': coordinates})
    
    # Clean up temporary files
    os.remove(kml_file_path)
    return places

def create_xlsx_file(data, output_file_path):
    workbook = Workbook()
    sheet = workbook.active
    sheet.append(['Name', 'Coordinates'])
    
    for item in data:
        sheet.append([item['name'], item['coordinates']])
    
    workbook.save(filename=output_file_path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_kmz_file_path> <output_xlsx_file_path>")
        sys.exit(1)

    input_kmz_file_path = sys.argv[1]
    output_xlsx_file_path = sys.argv[2]
    
    # Extract KML from KMZ
    kml_file_path = extract_kml_from_kmz(input_kmz_file_path)
    
    # Parse KML and extract data
    data = parse_kml_to_data(kml_file_path)
    
    # Generate .xlsx file with extracted data
    create_xlsx_file(data, output_xlsx_file_path)
    
    # Remove the temporary directory
    os.rmdir("temp_kml")

    print(f"Data extracted and saved to {output_xlsx_file_path}")
