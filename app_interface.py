import tkinter as tk  # Importing the Tkinter library

# Function to handle button click
def on_button_click():
    label.config(text="Button clicked!")  # Update label text when button is clicked

# Create the main window
root = tk.Tk()
root.title("Simple App Interface")  # Set the title of the window
root.geometry("300x200")  # Set the dimensions of the window

# Create a label widget
label = tk.Label(root, text="Welcome to the App", font=("Arial", 14))
label.pack(pady=20)  # Add padding to the label and place it in the window

# Create a button widget
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)  # Add padding to the button and place it in the window

# Run the application
root.mainloop()
