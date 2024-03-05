import os
import glob
import shutil
import binascii

def get_image_files_dict(directory):
    # Define the file extensions for images you want to consider
    image_extensions = ['jpg', 'jpeg', 'png', 'gif', 'bmp']

    # Use glob to get a list of files matching the specified extensions
    image_files = []
    for ext in image_extensions:
        pattern = os.path.join(directory, f'*.{ext}')
        image_files.extend(glob.glob(pattern))

    # Create a dictionary with filenames without extensions as keys and full filenames as values
    image_dict = {os.path.splitext(os.path.basename(file))[0]: file for file in image_files}

    return image_dict

# Edit ***.ebo files for each portrait
def string_edit_file(replace_str):
    file_path = f"plyrprts~{replace_str}\{replace_str}.ebo"
    with open(file_path, 'rb') as file:
        binary_data = bytearray(file.read())

    address = '4F0'
    # Convert hex strings to bytes
    search_text = "kobryan"
    search_hex = search_text.encode('utf-8').hex()
    replace_hex = replace_str.lower().encode('utf-8').hex()

    search_bytes = binascii.unhexlify(search_hex)
    replace_bytes = binascii.unhexlify(replace_hex)

    # Find and replace the hex pattern at the specified address
    address_index = binary_data.find(search_bytes, int(address, 16))
    if address_index != -1:
        binary_data[address_index:address_index+len(search_bytes)] = replace_bytes

        # Write the modified data back to the file
        with open(file_path, 'wb') as file:
            file.write(binary_data)

# For each image, copy sample.apt, sample.const and sample.ebo as ***.apt, ***.const, ***.ebo
def copy_files_to_folders(key):
    # Specify the paths to the source and target folders
    source_folder = ''
    target_folder = ''

    # Define the file extensions for the files you want to copy
    file_extensions = ['apt', 'const', 'ebo']

    # Create the target folder if it doesn't exist
    target_path = os.path.join(target_folder, f'plyrprts~{key}')
    os.makedirs(target_path, exist_ok=True)

    # Copy each file to the target folder
    for ext in file_extensions:
        source_file = os.path.join(source_folder, f'sample.{ext}')
        target_file = os.path.join(target_path, f'{key}.{ext}')
        shutil.copy2(source_file, target_file)