# Modified code to include printing the total number of checked XML files

import os
import xml.etree.ElementTree as ET

# This function assumes that XML files are present in the directory.
# Since the files are not actually present in this environment, this code will not run here.

def check_xml_files_for_malicious_code():
    # List all the xml files in the current directory
    xml_files = [file for file in os.listdir() if file.endswith('.xml')]
    
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
        if check_for_malicious_code(xml_file):
            malicious_code_counter += 1
            # Print out each file that contains malicious code
            print(f"'MALICIOUS_CODE' found in {xml_file}")

    # Print the total number of checked XML files
    print(f"Total number of XML files checked: {len(xml_files)}")

    # Return the total count of files containing malicious code
    return malicious_code_counter

# Run the function and print the result
malicious_code_count = check_xml_files_for_malicious_code()
print(f"Total files containing 'MALICIOUS_CODE': {malicious_code_count}")
