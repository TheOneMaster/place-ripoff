import tkinter as tk
from pixel import Pixel
import random

root = tk.Tk()
root.geometry("512x512")
root.title("Proof of Concept")
root.resizable(False, False)

number_of_pixels = 32
size_of_pixel = 512/32


def create_grid(parent, number_of_pixels, pixel_size):

    pixel_grid = [i for i in range(number_of_pixels**2)]

    for i in pixel_grid:

        column = (i % number_of_pixels) * size_of_pixel
        row = (i // number_of_pixels) * size_of_pixel

        pixel = Pixel(parent, i, (size_of_pixel, size_of_pixel))
        pixel.place(x=column, y=row)

        i = pixel
    
    return pixel_grid

def reset_all(event):

    for i in pixel_grid:

        i.update_color(new_color="blue")

    root.update_idletasks()

pixel_grid = create_grid(root, 32, 16)

root.bind("<space>", reset_all)

root.mainloop()