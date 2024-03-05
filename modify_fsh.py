import binascii
import os
import shutil

def hex_edit_file(file_path, search_hex, replace_hex, address):
    with open(file_path, 'rb') as file:
        binary_data = bytearray(file.read())

    # Convert hex strings to bytes
    search_bytes = binascii.unhexlify(search_hex)
    replace_bytes = binascii.unhexlify(replace_hex)

    # Find and replace the hex pattern at the specified address
    address_index = binary_data.find(search_bytes, int(address, 16))
    if address_index != -1:
        binary_data[address_index:address_index+len(search_bytes)] = replace_bytes

        # Write the modified data back to the file
        with open(file_path, 'wb') as file:
            file.write(binary_data)

def copy_fsh_files_to_folder(source_folder, target_folder, key):
    # Create the target folder if it doesn't exist
    target_path = os.path.join(target_folder, f'plyrprts~{key}')
    os.makedirs(target_path, exist_ok=True)

    # Copy the .fsh file to the target folder
    source_fsh = os.path.join(source_folder, f'{key}.fsh')
    target_fsh = os.path.join(target_path, f'{key}.fsh')
    shutil.copy2(source_fsh, target_fsh)
