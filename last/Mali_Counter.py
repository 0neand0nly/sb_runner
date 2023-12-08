import os
import xml.etree.ElementTree as ET
import argparse

def check_xml_files_for_malicious_code(directory):
    # List all the xml files in the specified directory
    xml_files = [file for file in os.listdir(directory) if file.endswith('.xml')]
    
    # Initialize the counter for malicious code occurrences
    malicious_code_counter = 0

    # Function to check for malicious code in an XML file
    def check_for_malicious_code(file_path):
        try:
            # Parse the XML file
            tree = ET.parse(file_path)
            root = tree.getroot()

            # Search for the 'MALICIOUS_CODE' string in the XML file
            if 'MALICIOUS_CODE' in ET.tostring(root, encoding='utf8', method='xml').decode():
                return True
            if 'Security' in ET.tostring(root, encoding='utf8', method='xml').decode():
                return True
            else:
                return False
        except ET.ParseError as e:
            # Print out the error and file path if an error occurs
            print(f"Error parsing {file_path}: {e}")
            return False
        except Exception as e:
            # Catch-all for any other exceptions
            print(f"An error occurred with {file_path}: {e}")
            return False

    # Iterate over each file and check for malicious code
    for xml_file in xml_files:
        full_path = os.path.join(directory, xml_file)
        if check_for_malicious_code(full_path):
            malicious_code_counter += 1
            # Print out each file that contains malicious code
            print(f"'MALICIOUS_CODE' found in {xml_file}")

    # Print the total number of checked XML files
    print(f"Total number of XML files checked: {len(xml_files)}")

    # Return the total count of files containing malicious code
    return malicious_code_counter

if __name__ == "__main__":
    # Set up the argument parser
    parser = argparse.ArgumentParser(description='Check XML files for malicious code.')
    parser.add_argument('directory', help='The directory where the XML files are located.')

    # Parse the arguments
    args = parser.parse_args()

    # Run the function and print the result
    malicious_code_count = check_xml_files_for_malicious_code(args.directory)
    print(f"Total files containing 'MALICIOUS_CODE': {malicious_code_count}")
