Simple Text Editor using Tkinter
This project is a simple text editor built with Python's Tkinter library. It allows users to type, save text files, and customize the font (that have been classified).

Features
📝 Type and edit text.
💾 Save your text to a file with the "Save" button.
🔤 Choose between multiple fonts to personalize your text.



How to Run the Project

Prerequisites:
Install Python.
Ensure Tkinter is installed (it comes bundled with Python).

Run the Code:
Save the file as texteditor.py.
Open the terminal/command prompt.
Navigate to the directory where texteditor.py is saved.
Run the script with: "python pathto/texteditor.py"

Using the Application:

Type or edit text in the window.
Use the Save button to save your text as a .txt file.
Change the text font using the Font menu.



Code Explanation
The project uses Python's Tkinter library to create a graphical user interface (GUI). Here's a breakdown:

Main Window:
The Tk() class creates the main application window.
Text Widget:
The Text widget allows users to type and edit text.
Save Function:
A file dialog (asksaveasfilename) lets users save their text input to a file.
Font Menu:
The Menu widget creates a dropdown menu with font options.
The text font is updated dynamically using the config() method.



Dependencies
This project relies on Python's standard libraries:
Tkinter (for GUI)
filedialog (for save file functionality)



Future (maybe):
Open File Functionality: Add a feature to open and edit existing text files.
Text Formatting: Include options like Bold, Italics, and Underline.
Theme Support: Add light and dark mode options for the editor.

