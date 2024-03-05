import os
import shutil
import subprocess

def copy_and_rename_images(source_folder, key, value):
    # Create the target folder if it doesn't exist
    target_path = os.path.join(source_folder, key)
    os.makedirs(target_path, exist_ok=True)

    # Copy the image to the target folder and rename it to 1.png
    target_file = os.path.join(target_path, '1.png')
    shutil.copy2(value, target_file)

def fshline_import(key):
    os.remove(fr'{key}\1.dds')
    cmd = fr'.\fshline.exe {key}\index.fsh -setidx'  # Use raw string (r) for Windows paths
    subprocess.run(cmd, shell=True)