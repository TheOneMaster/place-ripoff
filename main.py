import tkinter as tk
from pixel import Pixel
import random

root = tk.Tk()
root.geometry("512x512")
root.title("Proof of Concept")
root.resizable(False, False)

number_of_pixels = 32
size_of_pixel = 512/32

pixel_grid = ['blue' for i in range(number_of_pixels**2)]
colors = ['blue', 'red', 'green', 'yellow', 'orange']

for index, color in enumerate(pixel_grid):
    
    column = (index%number_of_pixels)*16
    row = (index//number_of_pixels)*16

    pixel = Pixel(root, index, (size_of_pixel, size_of_pixel), color=color)
    pixel.place(x=column, y=row)

    pixel_grid[index] = pixel

def reset_all(event):

    for i in pixel_grid:

        i.update_color(new_color="blue")

    root.update_idletasks()

root.bind("<space>", reset_all)

root.mainloop()