import pytest
import tkinter as tk
from number_entry import IntEntry
from tkinter import Frame, Label, Button

def main (): # This is the main function that will be called when the program is run.
    root = tk.Tk() # This line will create the main window of the program.
    # root.geometry("400x400") # This line will set the size of the main window.
    # root.title("Rectangle Area Calculator") # This line will set the title of the main window.
    frm_main = Frame(root)
    frm_main.master.title("Rectangle Area Calculator")
    frm_main = tk.Frame(root) # This line will create the main window of the program.

    frm_main.pack(padx = 4, pady = 3, fill = tk.BOTH, expand = 1) # This line will pack the main window.
    
    populate_winui(frm_main) # This line will call the populate_winui function and pass the root as an argument.
    root.mainloop()

def populate_winui(frm_main):
    width_label = tk.Label(frm_main, text = "Width: ") # This line will create a label that displays "Width:".
    
    width_entry = tk.Entry(frm_main) # This line will create an entry box where the user will enter the width of the rectangle.

    height_label = tk.Label(frm_main, text="height: ") # This line will create a label that displays "Height:".

    height_entry = tk.Entry(frm_main) # This line will create an entry box where the user will enter the height of the rectangle.

    calc_btn = tk.Button(frm_main, text = "Calculate") # This line will create a button that the user will click to calculate the area of the rectangle.

    clear_btn = tk.Button(frm_main, text = "Clear")

    result_label = tk.Label(frm_main, text = "Result: ") # This line will create a label that displays "Area:".

    status_label = tk.Label(frm_main, text = "Status: ") # This line will create a label that displays "Status:".

    result_display = tk.Label(frm_main, width = 5)

    status_display = tk.Label(frm_main, width = 20)

    width_label.grid(padx=10, pady=10, row=0, column=0) # This line will place the width label in the main window.
    width_entry.grid(padx=10, pady=10, row=0, column=1) # This line will place the width entry box in the main window.
    height_label.grid(padx=10, pady=10, row=1, column=0) # This line will place the height label in the main window
    height_entry.grid(padx=10, pady=10, row=1, column=1) # This line will place the height entry box in the main window.
    calc_btn.grid(padx=10, pady=10, row=2, column=0) # This line will place the calculate button in the main window.
    clear_btn.grid(padx=10, pady=10, row=2, column=1) # This line will place the clear button in the main window.
    result_label.grid(padx=10, pady=10, row=3, column=0) # This line will place the result label in the main window.
    status_label.grid(padx=10, pady=10, row=4, column=0) # This line will place the status label in the main window.
    result_display.grid(padx=10, pady=10, row=3, column=1) # This line will place the result display in the main window.
    status_display.grid(padx=10, pady=10, row=4, column=1) # This line will place the status display in the main window.


    def handle_calculations ():
        try:
            width_str = width_entry.get()
            height_str = height_entry.get()

            width = float(width_str)
            height = float(height_str)

            area = width * height

            result_display.config(text= f"{area}")
        except:
            if not ValueError:
                pass
            else:
                error = "Enter numerics"
                result_display.config(text="")
                status_display.config(text= f"{error}")

    def clear():
        
        width_entry.delete(0, tk.END)
        height_entry.delete(0, "end")
        result_display.config(text = "")
        status_display.config(text = "")

    calc_btn.config(command=handle_calculations)
    clear_btn.config(command= clear)

if __name__ == "__main__":
    main()