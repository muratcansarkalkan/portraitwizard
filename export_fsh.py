import os
import shutil
import subprocess

def copy_fsh_files(key):
    # Specify the paths to the source and target folders
    source_folder = ''
    target_folder = ''

    # Define the source and target file paths
    source_file = os.path.join(source_folder, 'sample.fsh')
    target_file = os.path.join(target_folder, f'{key}.fsh')

    # Copy the file to the target folder
    shutil.copy2(source_file, target_file)

def fshline_export(key):
    cmd = fr'.\fshline.exe {key}.fsh -getidx -nfs'  # Use raw string (r) for Windows paths
    subprocess.run(cmd, shell=True)
