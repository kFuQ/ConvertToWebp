import os
import random
import string
from shutil import rmtree
from tkinter import Tk, filedialog, messagebox, Button, Text, Frame, Menu, Label, Toplevel
import webbrowser
from PIL import Image

# Global variables
source_directory = ""
output_directory = ""
conversion_in_progress = False

# Function to handle the conversion process
def convert_images():
    global conversion_in_progress

    for file_name in os.listdir(source_directory):
        if not conversion_in_progress:
            break

        file_path = os.path.join(source_directory, file_name)
        if os.path.isfile(file_path):
            filename, file_extension = os.path.splitext(file_name)
            filename_lowercase = filename.lower()
            random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=18))
            output_file = os.path.join(output_directory, random_name + ".webp")

            # Use PIL library to convert the image to WebP format
            img = Image.open(file_path)
            img.save(output_file, "webp")

            # Update the status in the terminal
            status_text.insert("end", f"Converted: {file_name}\n")
            status_text.see("end")

    conversion_in_progress = False
    status_text.insert("end", "Conversion completed.\n")
    messagebox.showinfo("Conversion Completed", "Images converted successfully!")

# Function to handle the directory selection
def select_directory():
    global source_directory, output_directory

    source_directory = filedialog.askdirectory(title="Select Source Directory")
    if source_directory:
        output_directory = os.path.join(source_directory, "WebP")

        if os.path.exists(output_directory):
            rmtree(output_directory)

        os.makedirs(output_directory)

        status_text.delete("1.0", "end")
        status_text.insert("end", "Converting images...\n")

        start_button.config(state="normal")
        stop_button.config(state="normal")

        # Update the label with the selected input directory
        directory_label.config(text=f"Input Directory: {source_directory}")

        # Update the label with the ouput directory
        directory_label.config(text=f"Input Directory: {output_directory}")

# Function to start the conversion process
def start_conversion():
    global conversion_in_progress
    conversion_in_progress = True
    start_button.config(state="disabled")
    stop_button.config(state="normal")
    convert_images()

# Function to stop the conversion process
def stop_conversion():
    global conversion_in_progress
    conversion_in_progress = False
    start_button.config(state="normal")
    stop_button.config(state="disabled")

# Function to show the about window
def show_about_window():
    about_window = Toplevel(root)
    about_window.title("About")
    about_window.geometry("210x210")
    about_label = Label(about_window, text="WebP Image Conversion Tool\n\nVersion 0.6.9\n\nby kFuQ")
    about_label.pack(pady=20)
    # Function to open the URL
    def open_url():
        webbrowser.open("https://www.kfuq.net")

    url_label = Label(about_window, text="https://www.kfuq.net", fg="blue", cursor="hand2")
    url_label.pack()
    url_label.bind("<Button-1>", lambda event: open_url())


# Function to show the about window
def show_help_window():
    about_window = Toplevel(root)
    about_window.title("Help")
    about_window.geometry("420x420")
    about_label = Label(about_window, text="Step 1:  Click on the file menu and click on 'Select Directory'\n\nStep 2: Click on 'Start Conversion\n\nStep 3: Kick back and wait for your images to be processed' ")
    about_label.pack(pady=20)

# Create the GUI window
root = Tk()
root.title("WebP Image Conversion Tool")
root.geometry("420x420")

# Create the menu bar
menubar = Menu(root)
root.config(menu=menubar)

# Create the File menu
file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Select Directory", command=select_directory)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create the Help menu
help_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=show_about_window)
help_menu.add_command(label="Help", command=show_help_window)
# Create a frame for the start and stop buttons
button_frame = Frame(root)
button_frame.pack(pady=10)

# Create the start button
start_button = Button(button_frame, text="Start Conversion", command=start_conversion, state="disabled")
start_button.pack(side="left", padx=5)

# Create the stop button
stop_button = Button(button_frame, text="Stop Conversion", command=stop_conversion, state="disabled")
stop_button.pack(side="left", padx=5)

# Create a label to display the selected input directory
directory_label = Label(root, text="Input Directory: ")
directory_label.pack(pady=10)

# Create the status terminal window
status_text = Text(root, height=20, width=50)
status_text.pack()

# Run the GUI event loop
root.mainloop()
