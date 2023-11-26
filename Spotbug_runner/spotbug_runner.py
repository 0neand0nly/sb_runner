import subprocess
import os
import argparse

# Set the path to the SpotBugs executable jar
spotbugs_path = 'spotbugs-4.8.0/lib/spotbugs.jar'

def find_jar_files(directory):
    """
    Searches through the directory to find all .jar files.
    """
    jar_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.jar'):
                jar_files.append(os.path.join(root, file))
    return jar_files

def run_spotbugs_on_jar_files(jar_files):
    for jar_file in jar_files:
        report_filename = os.path.basename(jar_file).replace('.jar', '.xml')
        # Ensure that the XML output is directed to a file
        command = [
            'java', '-jar', spotbugs_path,
            '-textui', f'-xml:withMessages={report_filename}',
            '-low',
            jar_file
        ]
        subprocess.run(command, check=True)

if __name__ == "__main__":
    # Set up the argument parser
    parser = argparse.ArgumentParser(description='Run SpotBugs on JAR files.')
    parser.add_argument('target_directory', help='The directory where the JAR files to analyze are located.')

    # Parse the arguments
    args = parser.parse_args()

    # Find and run SpotBugs on all JAR files in the target directory
    jar_files = find_jar_files(args.target_directory)
    run_spotbugs_on_jar_files(jar_files)
