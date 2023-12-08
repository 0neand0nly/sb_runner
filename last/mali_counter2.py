import os
import xml.etree.ElementTree as ET
import argparse
import sys
import contextlib

# Context manager for redirecting stdout to a file
@contextlib.contextmanager
def redirect_stdout_to_file(file_path):
    original_stdout = sys.stdout
    with open(file_path, 'w', encoding='utf-8') as file:
        sys.stdout = file
        yield
        sys.stdout = original_stdout

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

            # Search for specific strings in the XML file
            xml_string = ET.tostring(root, encoding='utf8', method='xml').decode()
            if 'MALICIOUS_CODE' in xml_string or 'Security' in xml_string:
                return True
            else:
                return False
        except ET.ParseError as e:
            print(f"Error parsing {file_path}: {e}")
            return False
        except Exception as e:
            print(f"An error occurred with {file_path}: {e}")
            return False

    # Iterate over each file and check for malicious code
    for xml_file in xml_files:
        full_path = os.path.join(directory, xml_file)
        if check_for_malicious_code(full_path):
            malicious_code_counter += 1
            print(f"'MALICIOUS_CODE' found in {xml_file}")

    print(f"Total number of XML files checked: {len(xml_files)}")
    return malicious_code_counter

def run_snyk_analysis(directory):
    # Set the folder path containing the .txt files
    folder_path = directory  # Use the provided directory

    # Text to search for
    search_text = "Tested 1 dependencies for known issues, no vulnerable paths found."

    # Initialize counts and file names lists
    count_without = 0
    file_names_without = []
    count_with = 0
    file_names_with = []

    # Iterate over all files in the folder
    for file in os.listdir(folder_path):
        if file.endswith('.txt'):
            file_path = os.path.join(folder_path, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                file_content = f.read()
                if search_text not in file_content:
                    count_without += 1
                    file_names_without.append(file)
                else:
                    count_with += 1
                    file_names_with.append(file)

    # Write the results to new files
    output_file_without = os.path.join(directory, 'files_with_vulnerability_report.txt')
    output_file_with = os.path.join(directory, 'files_without_vulnerability_report.txt')

    with open(output_file_without, 'w', encoding='utf-8') as f:
        f.write(f"Number of files without the line '{search_text}': {count_without}\n")
        f.write("File names:\n")
        for name in file_names_without:
            f.write(name + '\n')

    with open(output_file_with, 'w', encoding='utf-8') as f:
        f.write(f"Number of files with the line '{search_text}': {count_with}\n")
        f.write("File names:\n")
        for name in file_names_with:
            f.write(name + '\n')

    print(f"Analysis completed. Results saved in {output_file_without} and {output_file_with}")

if __name__ == "__main__":
    # Set up the argument parser
    parser = argparse.ArgumentParser(description='Run security analysis tools.')
    parser.add_argument('-sn', '--snyk', action='store_true', help='Run Snyk analysis on .txt files')
    parser.add_argument('-sp', '--spotbugs', action='store_true', help='Run SpotBugs analysis on XML files')
    parser.add_argument('directory', help='The directory where the files are located.')

    # Parse the arguments
    args = parser.parse_args()

    # Output file for logging
    log_file_path = os.path.join(args.directory, 'analysis_log.txt')

    # Redirect stdout to a file
    with redirect_stdout_to_file(log_file_path):
        # Check which argument was passed and run the corresponding function
        if args.snyk:
            run_snyk_analysis(args.directory)
        elif args.spotbugs:
            malicious_code_count = check_xml_files_for_malicious_code(args.directory)
            print(f"Total files containing 'MALICIOUS_CODE': {malicious_code_count}")
        else:
            print("Please select an option: -sn for Snyk analysis or -sp for SpotBugs analysis.")

    print(f"Analysis completed. Log saved in {log_file_path}")
