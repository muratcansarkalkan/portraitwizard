import subprocess

def big_import(key):
    cmd = fr'.\big_from_dir.exe plyrprts~{key}.big plyrprts~{key}'  # Use raw string (r) for Windows paths
    subprocess.run(cmd, shell=True)
