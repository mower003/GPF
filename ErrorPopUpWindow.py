import tkinter as tk

class ErrorPopUpWindow():

    def __init__(self, parent_frame=None):
        self.base_frame = parent_frame

    def create_error_window(self, e):
        window_width = 300
        window_height = 200

        if self.base_frame is None:
            self.errorWindow = tk.Toplevel()
            # get the screen dimension
            screen_width = self.errorWindow.winfo_screenwidth()
            screen_height = self.errorWindow.winfo_screenheight()
            # find the center point
            center_x = int(screen_width/2 - window_width / 2)
            center_y = int(screen_height/2 - window_height / 2)
            self.errorWindow.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
            self.errorWindow.title("Error")
            self.tempError = tk.Label(self.errorWindow, text=e)
            self.tempError.pack()
            self.b = tk.Button(self.errorWindow, text="Close", command=self.errorWindow.destroy)
            self.b.pack()
        else:
            self.errorWindow = tk.Toplevel(self.base_frame)
            # get the screen dimension
            screen_width = self.errorWindow.winfo_screenwidth()
            screen_height = self.errorWindow.winfo_screenheight()
            # find the center point
            center_x = int(screen_width/2 - window_width / 2)
            center_y = int(screen_height/2 - window_height / 2)
            self.errorWindow.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
            self.errorWindow.title("Error")
            self.tempError = tk.Label(self.errorWindow, text=e)
            self.tempError.pack()
            self.b = tk.Button(self.errorWindow, text="Close", command=self.errorWindow.destroy)
            self.b.pack()