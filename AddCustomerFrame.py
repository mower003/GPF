import tkinter as tk
import random as rd

class AddCustomerFrame():

    #Static Settings
    #Controls the number and name of form elements
    customer_compositional_elements = ['Customer Number: ', 'Name: ', 'Address: ', 'City: ', 'State: ', 'Zip: ']
    #Color theme
    customer_bg_color = '#395144'
    customer_label_color = '#4E6C50'
    customer_data_color = '#AA8B56'
    customer_header_color = '#F0EBCE'
    #Fonts
    customer_title_font = 'Haettenschweiler'
    customer_header_font = 'Haettenschweiler'
    customer_label_font = 'Haettenschweiler'
    customer_data_font = 'MS Sans Serif'
    #Controls the title of the frame.
    frame_title = "Add Customer"

    def __init__(self, parent_frame):
        self.base_frame = parent_frame
        self.thebgcolor = 'grey'
        self.lbl_list = []
        self.entry_list = []
        #self.my_frame = tk.Frame(parent_frame, bd=2, bg='green')
        #self.btn = tk.Button(self.my_frame, text="Save", width=40)
        #self.btn.configure(command=self.save_customer_info_to_db)
        #self.my_frame.pack(side="top", fill="both", expand=True)

    def set_up_frame(self):
        self.my_frame = tk.Frame(self.base_frame, bd=2, bg=self.customer_bg_color)
        self.btn = tk.Button(self.my_frame, text="Save", width=40, bg=self.customer_data_color)
        self.btn.configure(command=self.save_customer_info_to_db)

    def save_customer_info_to_db(self):
        self.get_entry_elements_as_tuple()

    def add_title_label(self):
        self.title = tk.Label(self.my_frame, text=self.frame_title, bg=self.customer_label_color)
        self.title.config(font=(self.customer_title_font,25))
        self.title.grid(row=0, column = 0, columnspan=3, ipady=5, pady=5, sticky="E,W")
        self.my_frame.grid_columnconfigure(0, weight=1)
        self.my_frame.grid_columnconfigure(1, weight=1)
        self.my_frame.grid_columnconfigure(2, weight=1)

    def get_entry_elements_as_tuple(self):
        entry_elements = []
        for element in self.entry_list:
            entry_elements.append(element.get())
        if entry_elements[0].isnumeric():
            entry_elements[0] = int(entry_elements[0]) 
        entry_elements = tuple(entry_elements)
        print(entry_elements)
        return entry_elements

    def create_add_form(self):
        row = 1
        col = 0
        for element in self.customer_compositional_elements:
            lbl = tk.Label(self.my_frame, text= element, font=(self.customer_data_font, 12, 'bold'), bg=self.customer_bg_color)
            entry = tk.Entry(self.my_frame, width=40, font=(self.customer_data_font, 12))
            lbl.grid(row=row, column=col, sticky="W")
            entry.grid(row = row, column=col+1, sticky="E,W")
            self.lbl_list.append(lbl)
            self.entry_list.append(entry)
            row += 1
        self.btn.grid(row=row+1, column = 0, columnspan= 3, ipadx=10, padx=5, pady=40)
        self.my_frame.pack(side="top", fill="both", expand=True)

    def build_frame(self):
        self.clear_display_frame()
        self.set_up_frame()
        self.add_title_label()
        self.create_add_form()

    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy()
