import tkinter as tk

class ErrorPopUpWindow():

    def __init__(self, parent_frame=None):
        self.base_frame = parent_frame

    def create_error_window(self, e):
        if self.base_frame is None:
            self.errorWindow = tk.Toplevel()
            self.errorWindow.title("Error")
            self.tempError = tk.Label(self.errorWindow, text=e)
            self.tempError.pack()
            self.b = tk.Button(self.errorWindow, text="Close", command=self.errorWindow.destroy)
            self.b.pack()
        else:
            self.errorWindow = tk.Toplevel(self.base_frame)
            self.errorWindow.title("Error")
            self.tempError = tk.Label(self.errorWindow, text=e)
            self.tempError.pack()
            self.b = tk.Button(self.errorWindow, text="Close", command=self.errorWindow.destroy)
            self.b.pack()