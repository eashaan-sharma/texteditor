import sys                               # Imports sys to access sys-specific param and func(version_info)
v = sys.version_info                     # Version of current interpreter
              
  
# \users\easha\onedrive\desktop\texteditor.py
  
  
from tkinter import *            
# Imports Tk class from the Tkinter library to create main window

# Check py vers for compatibility
#if "2.7" in v: # Check if sys ver = 2.7
#   from Tkinter import * #Imports Tkinter lib for py 2.7
#   import tkFileDialog
    
#elif "3.3" in v or "3.4" in v: # 3.3 or 3.4
#   from tkinter import filedialog
    
if v[0] == 2:  # Python 2.x
    from Tkinter import *
    import tkFileDialog as filedialog  # Rename for consistency
else:  # Python 3.x
    from tkinter import *
    from tkinter.font import Font
    from tkinter import filedialog
    
root = Tk()  # Create Tkinter window with title in "" 
root.title("Text Editor")

text = Text(root)   # Init text widget
text.grid()    

#def saveas():
#       
#       t = text.get("1.0", "end-1c")
#       savelocation = tkFileDialog.asksaveasfilename()
#       file1 = open(savelocation, "w+")
#       file1.write(t)
#       file1.close()

def saveas():
             # No need for global (text same hai, reassign nahi hoti uski value)
    t = text.get("1.0", "end-1c")  # Get all text from the widget
    savelocation = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if savelocation:  # Proceed only if the user selects a file
        with open(savelocation, "w") as file1:  # Safely open the file
            file1.write(t)  # Write text to file

button = Button(root, text = "Save", command = saveas)
button.grid()

def FontHelvetica():                                    # Define the font classes
        
        text.config(font = "Helvetica")
        
def FontCourier():
        
        text.config(font = "Courier")

def FontCenturyGothic():
        
        text.config(font = "Century Gothic")
        
def FontCambria():
        
        text.config(font = "Cambria")

bold_font = Font(text, text.cget("font"))       # Gets current font
bold_font.configure(weight = "bold")    # Configure text as bold

def FormatBold():
      current_font = text.cget("font")          # Gets current font
      if str(current_font) == str(bold_font):           # If already bold, reset to normal else turn bold
            text.config(font = ("Helvetica"))
      else:
            text.config(font = bold_font)  

# Button for the bold toggle
bold_button = Button(root, text = "Bold", command = FormatBold)
bold_button.grid()


font = Menubutton(root, text = "Font")
font.grid()
font.menu = Menu(font, tearoff = 0)
font["menu"] = font.menu
helvetica = IntVar()
courier = IntVar()
centurygothic = IntVar()
cambria = IntVar()

font.menu.add_checkbutton(label = "Courier", variable = courier,
command = FontCourier)
font.menu.add_checkbutton(label = "Helvetica", variable = helvetica,
command = FontHelvetica)
font.menu.add_checkbutton(label = "Cambria", variable = cambria,
command = FontCambria)
font.menu.add_checkbutton(label = "Century Gothic", variable = centurygothic,
command = FontCenturyGothic)

   
root.mainloop()     # Starts Tkinter event loop to keep window open

