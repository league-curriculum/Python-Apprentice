import os

def remove_lines_with_special_comment(input_file_path, output_file_path):
    # Check if the file exists
    if not os.path.exists(input_file_path):
        print(f"File not found: {input_file_path}")
        return

    # Read the file
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    # Filter lines that don't end with '#;'
    filtered_lines = [line for line in lines if not line.rstrip().endswith('# ;')]

    # Write the modified content to the new file
    with open(output_file_path, 'w') as file:
        file.writelines(filtered_lines)

    print(f"Lines with '#;' removed from {input_file_path}\nNew file created at {output_file_path}")


# Add your file path here
# input_file_path = "Path\\to\\file"
# output_file_path = "Path\\to\\file"

remove_lines_with_special_comment(input_file_path,
                                  output_file_path)
