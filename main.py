import gettarget
import export_fsh
import import_fsh
import modify_fsh
import import_big
import os
import shutil

# Specify the path to the subdirectory
subdirectory_path = '.\portraits'

# Crashing and working hex addresses
start_works = '5368704680000100000000010000002200000030000100503100473432370000000042757920455254530000000000007D01000020'
start_crash = '5368704680000100000000010000002200000030000000503100473234370000000042757920455254530000000000007D01000000'
end_works = '0100000000000020000000100000000000000000000000020000000100000080000000700000000000000000000000'
end_crash = '1000000000000020000000100000000000000000000000020000000100000000000000000000000000000000000000'

# Get the dictionary of image filenames in the subdirectory
image_dict = gettarget.get_image_files_dict(subdirectory_path)

# Print the dictionary of image filenames
print("List of player portraits to be created:")
for key, value in image_dict.items():
    print(f"{key}: {value}")

# Copy files to folders based on the dictionary
for key, value in image_dict.items():
    gettarget.copy_files_to_folders(key)
    gettarget.string_edit_file(key)
print("apt, const and ebo files are copied successfully.")

# Copy sample.fsh for each key in the dictionary
for key, value in image_dict.items():
    export_fsh.copy_fsh_files(key)
print("fsh files are copied successfully.")

for key, value in image_dict.items():
    export_fsh.fshline_export(f"{key}")
    import_fsh.copy_and_rename_images('', key, value)
print("Images are replaced successfully.")

for key, value in image_dict.items():
    import_fsh.fshline_import(key)
    modify_fsh.hex_edit_file(f"{key}.fsh", start_crash, start_works, '0x0')
    modify_fsh.hex_edit_file(f"{key}.fsh", end_crash, end_works, '0x10051')
print("fsh files are imported successfully.")

for key, value in image_dict.items():
    modify_fsh.copy_fsh_files_to_folder('', '', f"{key}")

for key, value in image_dict.items():
    import_big.big_import(key)
    # Cleanup
    shutil.rmtree(f'{key}')
    shutil.rmtree(fr'plyrprts~{key}')
    os.remove(f'{key}.fsh')

move_big = input("Do you want to move created portraits to SGSM? (yes/no): ").lower()

if move_big in ['yes', 'y']:
    big_files = [file for file in os.listdir() if file.endswith('.big')]
    target_folder = input("Copy paste your SGSM target folder.")
    for big_file in big_files:
        source_big = os.path.join('', big_file)
        target_big = os.path.join(target_folder, big_file)
        shutil.move(source_big, target_big)

    print("big files moved successfully. All done!")
else:
    print("All done!")
