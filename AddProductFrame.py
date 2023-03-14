import tkinter as tk

from GPFISCoordinator import GPFISCoordinator
from Product import ProductObj
from Product import ProductObjEnum

class AddProductFrame():

    #Static Settings
    #Controls the number and name of form elements
    product_compositional_elements = ['Product Number: ', 'Name: ', 'Description: ', 'Price: ', 'Note: ', 'Case Style: ']
    #Color theme
    bg_color = '#395144'
    label_color = '#4E6C50'
    data_color = '#AA8B56'
    header_color = '#F0EBCE'
    #Fonts
    title_font = 'Haettenschweiler'
    header_font = 'Haettenschweiler'
    label_font = 'Haettenschweiler'
    data_font = 'MS Sans Serif'
    #Controls the title of the frame.
    frame_title = "Add Product"

    def __init__(self, parent_frame):
        self.base_frame = parent_frame
        self.coordinator = GPFISCoordinator()
        #self.my_frame = tk.Frame(parent_frame, bd=2, bg='green')
        #self.btn = tk.Button(self.my_frame, text="Save", width=40)
        #self.btn.configure(command=self.save_product_info_to_db)
        #self.my_frame.pack(side="top", fill="both", expand=True)

    def set_up_frame(self):
        self.my_frame = tk.Frame(self.base_frame, bd=2, bg=self.bg_color)
        self.btn = tk.Button(self.my_frame, text="Save", width=40, bg=self.data_color)
        self.btn.configure(command=self.save_product_info_to_db)

    def save_product_info_to_db(self):
        oProduct = ProductObj(productList = self.get_entry_elements_as_list())

        self.coordinator.insert_product(ProductObj = oProduct)

        self.clear_product_data()

    def add_title_label(self):
        self.title = tk.Label(self.my_frame, text=self.frame_title, bg=self.label_color)
        self.title.config(font=(self.title_font,25))
        self.title.grid(row=0, column = 0, columnspan=3, ipady=5, pady=5, sticky="N,S,E,W")
        self.my_frame.grid_columnconfigure(0, weight=1)
        self.my_frame.grid_columnconfigure(1, weight=1)
        self.my_frame.grid_columnconfigure(2, weight=1)

    def create_product_frame(self):
        self.product_id_lbl = tk.Label(self.my_frame, text = "Product ID:", font=(self.data_font, 12, 'bold'), bg=self.bg_color)
        self.product_id_entry = tk.Entry(self.my_frame, width=40, font=(self.data_font, 12))
        self.product_id_lbl.grid(row = 1, column = 0, sticky='W')
        self.product_id_entry.grid(row = 1, column= 1, sticky='E,W')

        self.product_name_lbl = tk.Label(self.my_frame, text = "Product Name:", font=(self.data_font, 12, 'bold'), bg=self.bg_color)
        self.product_name_entry = tk.Entry(self.my_frame, width=40, font=(self.data_font, 12))
        self.product_name_lbl.grid(row = 2, column = 0, sticky='W')
        self.product_name_entry.grid(row = 2, column= 1, sticky='E,W')

        self.product_description_lbl = tk.Label(self.my_frame, text = "Product Description:", font=(self.data_font, 12, 'bold'), bg=self.bg_color)
        self.product_description_entry = tk.Entry(self.my_frame, width=40, font=(self.data_font, 12))
        self.product_description_lbl.grid(row = 3, column = 0, sticky='W')
        self.product_description_entry.grid(row = 3, column= 1, sticky='E,W')

        self.product_price_lbl = tk.Label(self.my_frame, text = "Unit Price:", font=(self.data_font, 12, 'bold'), bg=self.bg_color)
        self.product_price_entry = tk.Entry(self.my_frame, width=40, font=(self.data_font, 12))
        self.product_price_lbl.grid(row = 4, column = 0, sticky='W')
        self.product_price_entry.grid(row = 4, column= 1, sticky='E,W')

        self.product_note_lbl = tk.Label(self.my_frame, text = "Note:", font=(self.data_font, 12, 'bold'), bg=self.bg_color)
        self.product_note_entry = tk.Entry(self.my_frame, width=40, font=(self.data_font, 12))
        self.product_note_lbl.grid(row = 5, column = 0, sticky='W')
        self.product_note_entry.grid(row = 5, column= 1, sticky='E,W')

        self.product_case_style_lbl = tk.Label(self.my_frame, text = "Case Style:", font=(self.data_font, 12, 'bold'), bg=self.bg_color)
        self.product_case_style_entry = tk.Entry(self.my_frame, width=40, font=(self.data_font, 12))
        self.product_case_style_lbl.grid(row = 6, column = 0, sticky='W')
        self.product_case_style_entry.grid(row = 6, column= 1, sticky='E,W')

        self.btn.grid(row = 7, column = 0, columnspan=3, ipadx=10, padx=5, pady=40)

        self.my_frame.pack(side='top', fill='both', expand='true')

    def build_frame(self):
        self.clear_display_frame()
        self.set_up_frame()
        self.add_title_label()
        self.create_product_frame()

    def get_entry_elements_as_list(self):
        list = []
        list.insert(ProductObjEnum.PRODUCT_ID.value, self.product_id_entry.get().strip())
        list.insert(ProductObjEnum.PRODUCT_NAME.value, self.product_name_entry.get().strip())
        list.insert(ProductObjEnum.DESCRIPTION.value, self.product_description_entry.get().strip())
        list.insert(ProductObjEnum.UNIT_PRICE.value, self.product_price_entry.get().strip())
        list.insert(ProductObjEnum.CASE_STYLE.value, self.product_case_style_entry.get().strip())
        list.insert(ProductObjEnum.NOTE.value, self.product_note_entry.get().strip())
        return list

    def clear_product_data(self):
        self.product_id_entry.delete(0, tk.END)
        self.product_name_entry.delete(0, tk.END)
        self.product_description_entry.delete(0, tk.END)
        self.product_price_entry.delete(0, tk.END)
        self.product_note_entry.delete(0, tk.END)
        self.product_case_style_entry.delete(0, tk.END)


    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy()