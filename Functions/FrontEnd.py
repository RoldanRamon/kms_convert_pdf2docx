import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

def convert_rules():
    message.config(text='Great! Have fun playing!')

def merge_rules():
    message.config(text='Too bad! We hope you change your mind and decide to play by the rules.')

def rotate_documents():
    message.config(text='Great! Have fun playing!')

# Function to load an image and resize it
def load_image(file_name, width, height):
    image = Image.open(file_name)
    image = image.resize((width, height))
    return ImageTk.PhotoImage(image)

# Creating the main window
window = tk.Tk()
window.title('')

# Style for the buttons
button_style = ttk.Style()
button_style.configure('Button.TButton', font=('Arial', 12, 'bold'))

# Frame for the upper buttons
upper_buttons_frame = tk.Frame(window)
upper_buttons_frame.pack()

# Loading icons
convert_icon = load_image('Images/word.ico', 30, 30)
merge_icon = load_image('Images/merge.png', 30, 30)
rotate_icon = load_image('Images/rotate.png', 30, 30)

# Button to Convert pdf2docx
convert_button = ttk.Button(upper_buttons_frame, text='Converter PDF para Word', image=convert_icon, compound=tk.LEFT, command=convert_rules, style='Button.TButton')
convert_button.pack(side=tk.LEFT, padx=5, pady=5)  # Positions the button to the left

# Button to Merge PDFs
merge_button = ttk.Button(upper_buttons_frame, text='Juntar PDFs', image=merge_icon, compound=tk.LEFT, command=merge_rules, style='Button.TButton')
merge_button.pack(side=tk.LEFT, padx=5, pady=5)  # Positions the button to the left

# Frame for the lower buttons
lower_buttons_frame = tk.Frame(window)
lower_buttons_frame.pack()

# Button to Rotate PDF
rotate_button = ttk.Button(lower_buttons_frame, text='Girar PDF', image=rotate_icon, compound=tk.LEFT, command=rotate_documents, style='Button.TButton')
rotate_button.pack(side=tk.LEFT, padx=5, pady=5)  # Positions the button to the left


# Feedback message
message = tk.Label(window, text='')
message.pack()

# Running the GUI
window.mainloop()
