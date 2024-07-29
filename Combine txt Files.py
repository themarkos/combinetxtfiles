import os

# Use the specified input folder path
input_folder_path = r"CHOOSE INPUT FOLDER"

# Specify the output file name
output_file = 'title_list.txt'

# Get a list of all txt files in the folder
txt_files = [f for f in os.listdir(input_folder_path) if f.endswith('.txt')]

# Combine the contents of all txt files
with open(os.path.join(input_folder_path, output_file), 'w', encoding='utf-8') as outfile:
    for txt_file in txt_files:
        with open(os.path.join(input_folder_path, txt_file), 'r', encoding='utf-8') as infile:
            outfile.write(infile.read())
            outfile.write('\n')  # Add a newline between files

print(f"All txt files have been combined into {output_file}")