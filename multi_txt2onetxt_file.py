
# This Python script performs the following tasks:

# 1. **Imports**: Imports the `os` module for operating system-related functionalities.

# 2. **Variables**:
#    - `input_folder`: Specifies the folder name (`"savilles_fix"`) where input `.txt` files are located.
#    - `output_file`: Specifies the output file name (`"savilles_full.txt"`) where the combined content will be saved.

# 3. **List comprehension**:
#    - `txt_files`: Creates a list of filenames (`f`) in the `input_folder` directory that end with `.txt`.

# 4. **Combining File Contents**:
#    - Initializes an empty string `combined_content` to store the concatenated content of all input files.

# 5. **File Processing Loop**:
#    - Iterates through each file (`input_file`) in the `txt_files` list.
#    - Constructs the full path (`input_file_path`) to each file using `os.path.join()` with `input_folder`.
#    - Opens each file (`input_file_path`) in read mode (`"r"`), reads its content using `f.read()`, and stores it in the `content` variable.
#    - Appends the `content` of each file to the `combined_content` string.

# 6. **Output**:
#    - Opens the `output_file` in write mode (`"w"`).
#    - Writes the entire `combined_content` string to the `output_file`.
#    - Prints a confirmation message indicating where the combined content has been saved.

# ### Summary:
# This script essentially reads all `.txt` files from a specified input folder (`"villes_fix"`), combines their contents 
# into a single string (`combined_content`), and then writes this combined content to an output file (`"villes_full.txt"`).
# It's useful for consolidating text data spread across multiple files into one cohesive file.



import os

# Define the input and output folders
input_folder = "villes_fix"
output_file = "villes_full.txt"

# List all .txt files in the input folder
txt_files = [f for f in os.listdir(input_folder) if f.endswith(".txt")]

# Initialize an empty string to store the combined content
combined_content = ""

# Loop through each .txt file and concatenate their contents
for input_file in txt_files:
    # Construct the full input file path
    input_file_path = os.path.join(input_folder, input_file)

    # Read the content of the input file
    with open(input_file_path, "r") as f:
        content = f.read()

    # Append the content to the combined_content string
    combined_content += content

# Write the combined content to the output file
with open(output_file, "w") as f:
    f.write(combined_content)

print("Combined content saved to", output_file)
