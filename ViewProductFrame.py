import tkinter as tk
from tkinter import font
class ViewProductFrame():

    #Static Settings
    #Controls the number and name of form elements
    product_compositional_elements = ['Product ID ', 'Name ', 'Description ', 'Price ', 'Note ', 'Case Style ']
    #Color theme
    product_bg_color = '#395144'
    product_label_color = '#4E6C50'
    product_data_color = '#AA8B56'
    product_header_color = '#F0EBCE'
    #Fonts
    product_title_font = 'Haettenschweiler'
    product_header_font = 'Haettenschweiler'
    product_label_font = 'Haettenschweiler'
    product_data_font = 'MS Sans Serif'
    #Controls the title of the frame.
    frame_title = "Product List"

    def __init__(self, parent_frame):
        self.base_frame = parent_frame
        self.lbl_list = []
        self.delete_btn_list = []
        self.view_btn_list = []
        #self.my_frame = tk.Frame(parent_frame, bd=2, bg='grey')
        #self.my_frame.pack(side="top", fill="both", expand=True)

    def set_up_frame(self):
        self.my_frame = tk.Frame(self.base_frame, bd=2, bg=self.product_bg_color)
        
    def create_view_form(self, form_rows):
        row = 1
        col = 0
        for headers in self.product_compositional_elements:
            lbl = tk.Label(self.my_frame, text = headers, font=(self.product_header_font,20), bg=self.product_header_color)
            lbl.grid(row = row, column = col, sticky = "W,E")
            self.my_frame.grid_columnconfigure(col, weight=1)
            col += 1
        
        row = 2
        col = 0
        index = 0
        for element in form_rows:
            for item in element:
                lbl = tk.Label(self.my_frame, text = item, borderwidth=2, relief="solid", font=(self.product_data_font, 12),bg=self.product_data_color)
                lbl.grid(row = row, column = col, sticky = "W,E")
                self.lbl_list.append(lbl)
                col += 1
            view_btn = tk.Button(self.my_frame, text="Edit", padx=5, bg= self.product_data_color)
            delete_btn = tk.Button(self.my_frame, text="Delete", padx=5)
            view_btn.grid(row=row, column=col+1)
            #delete_btn.grid(row=row, column=col+2)
            self.view_btn_list.append(view_btn)
            self.delete_btn_list.append(delete_btn)
            row += 1
            col = 0
            index += 1
        
        self.my_frame.pack(side="top", fill="both", expand=True)

    def add_title_label(self):
        self.title = tk.Label(self.my_frame, text=self.frame_title)
        self.title.config(font=(self.product_title_font,38),bg=self.product_label_color)
        self.title.grid(row=0, column = 0, columnspan=len(self.product_compositional_elements)+2, ipady=5, pady=5, sticky="E,W")

    def build_frame(self):
        self.clear_display_frame()
        self.set_up_frame()
        self.add_title_label()
        #A call to a class that fetches product data should be put here
        #the returned result should be passed into create_view_form as a list of tuples IIRC
        form_rows = [(77, ' Negi', 'Jumbo Negi', 2.75, 'A Spot for a note', '24 per box')]
        self.create_view_form(form_rows)

    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy()