# Portrait Creation Wizard

The Portrait Creation Wizard is a Python-based tool for generating 128x128 portraits for a game. It simplifies the process by automating the creation of portraits based on the player's name.

## Prerequisites

- Python 3.10

## How to Use

1. **Download the Project:**
   - Click on the "Code" button and select "Download ZIP".
   - Extract the contents to your desired location.

2. **Prepare Images:**
   - Create player portraits in .png format. The images should have a size of 128x128. You can take a look at base.psd in Photoshop and format your image based on this template.
   - Place the images in the "portraits" folder. Image names should consist of letters and underscores only.
   - The recommended naming convention is the first 2 letters of the player's first name, followed by the first 5 letters of their last name.

3. **Run the Script:**
   - Open a command prompt.
   - Navigate to the project directory.
   - Type the following command:
     ```bash
     python main.py
     ```

4. **Post-Processing:**
   - After the process is complete, the script will prompt you to copy the folders.
   - Type "yes" to proceed and enter the destination folder (ideally the sgsm folder of the game).
   - Type "no" to exit if you don't want to copy the files.

## Example:

```bash
$ python main.py
... (processing)
Do you want to copy the folders? (yes/no): yes
Enter the destination folder: path/to/sgsm
```

## Credits:

- NBA2KStuff/Denis Auroux for FSHLINE
- Dmitri for big import/export tool