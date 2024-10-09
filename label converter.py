import os

# Function to extract and convert icon names into labels from a folder
def convert_to_label_from_folder(folder_path, output_file):
    labels = []
    prefix = "-icon-service-"
    
    # List all files in the folder
    for filename in os.listdir(folder_path):
        # Check if filename contains the prefix
        if prefix in filename:
            # Extract the part after the prefix and before the extension
            label = filename.split(prefix)[-1].split('.')[0]
            # Remove any remaining dashes from the label
            label = label.replace('-', ' ')
            labels.append(label)
    
    # Write labels to the output file
    with open(output_file, 'w') as file:
        for label in labels:
            file.write(label + '\n')
    
    print(f"Labels saved to {output_file}")

# Folder path containing the files
folder_path = "/Users/siddhnat/Desktop/Icons"
# Output file name
output_file = "output_labels.txt"

# Call the function and print the labels
convert_to_label_from_folder(folder_path, output_file)
