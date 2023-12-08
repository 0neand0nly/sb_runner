import os

# Set the folder path containing the .txt files
folder_path = './snyk_results'  # Replace with your folder path

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
output_file_without = 'files_with_vulnerability_report.txt'
with open(output_file_without, 'w', encoding='utf-8') as f:
    f.write(f"Number of files without the line '{search_text}': {count_without}\n")
    f.write("File names:\n")
    for name in file_names_without:
        f.write(name + '\n')

output_file_with = 'files_without_vulnerability_report.txt'
with open(output_file_with, 'w', encoding='utf-8') as f:
    f.write(f"Number of files with the line '{search_text}': {count_with}\n")
    f.write("File names:\n")
    for name in file_names_with:
        f.write(name + '\n')

print(f"Analysis completed. Results saved in {output_file_without} and {output_file_with}")
