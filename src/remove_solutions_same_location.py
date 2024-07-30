import os

def remove_lines_with_special_comment(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return


    # Read the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Filter lines that don't end with '#;'
    filtered_lines = [line for line in lines if not line.rstrip().endswith('# ;')]

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.writelines(filtered_lines)

    print(f"Lines with '#;' removed from {file_path}")


# Add your file path here
file_path = "Path\\to\\file"


remove_lines_with_special_comment(file_path)
