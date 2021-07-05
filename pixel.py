from tkinter import Frame

class Pixel(Frame):

    COLORS = ['blue', 'red', 'green', 'yellow', 'orange']
    _SELECTED_PIXEL = None


    def __init__(self, root, position, size, color='blue', **kwargs):
        super().__init__(root)

        self.config(background=color, width=size[0], height=size[1])
        self.root = root
        self.color = color
        self.position = position
        self.size = size

        self.bind("<Button-1>", self.mouse_click)
        self.bind("<B1-Motion>", self.on_hover)

    def update_color(self, new_color=None):
                        
        if new_color is None:
            current_index = Pixel.COLORS.index(self.color)
            new_index = (current_index+1)%5
            new_color = Pixel.COLORS[new_index]

        self.color = new_color
        self.config(background=new_color)
        # self.update()
        last_pixel = self

    def mouse_click(self, input):

        self.update_color()
        Pixel._SELECTED_PIXEL = self
        self.update_idletasks()
    
    def on_hover(self, event):

        x = event.x_root
        y = event.y_root

        pixel = self.root.winfo_containing(x, y)

        # The mouse hover is outside the bounds of the window
        if pixel is None:
            return

        if Pixel._SELECTED_PIXEL != pixel:
            pixel.update_color()
            Pixel._SELECTED_PIXEL = pixel
            pixel.update_idletasks()
