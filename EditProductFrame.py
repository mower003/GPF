import tkinter as tk

from GPFISCoordinator import GPFISCoordinator
from Product import ProductObj
from Product import ProductObjEnum
class EditProductFrame():

    #Static Settings
    product_compositional_elements = ['Product Number: ', 'Name: ', 'Description: ', 'Price: ', 'Note: ', 'Case Style: ']
    #Color theme
    bg_color = '#FFFFFF'
    label_color = '#4E6C50'
    data_color = '#AA8B56'
    header_color = '#F0EBCE'
    #Fonts
    title_font = 'Haettenschweiler'
    header_font = 'Haettenschweiler'
    label_font = 'Haettenschweiler'
    data_font = 'MS Sans Serif'
    #Controls the title of the frame.
    frame_title = "Edit Product Frame"

    def __init__(self, parent_frame, product_list):
        self.base_frame = parent_frame
        self.coordinator = GPFISCoordinator()
        self.product_list = product_list
        self.build_frame()

    def set_up_frame(self):
        self.edit_product_frame = tk.Toplevel(bd=2, bg=self.bg_color)
        self.btn = tk.Button(self.edit_product_frame, text="Save", width=40, bg=self.data_color, command=lambda: self.save_product_info_to_db())

    def save_product_info_to_db(self):
        oProduct = ProductObj(productList = self.getEntryElements())
        #print(oProduct.asListForDBUpdate())
        self.coordinator.update_product(ProductObj = oProduct)

        
        self.edit_product_frame.update()
        self.edit_product_frame.destroy()

    def add_title_label(self):
        self.title = tk.Label(self.edit_product_frame, text=self.frame_title, bg=self.label_color)
        self.title.config(font=(self.title_font,25))
        self.title.grid(row=0, column = 0, columnspan=3, ipady=5, pady=5, sticky="N,S,E,W")
        self.edit_product_frame.grid_columnconfigure(0, weight=1)
        self.edit_product_frame.grid_columnconfigure(1, weight=1)
        self.edit_product_frame.grid_columnconfigure(2, weight=1)

    def create_product_frame(self):
        self.product_id_lbl = tk.Label(self.edit_product_frame, text = "Product ID:", font=(self.data_font, 12, 'bold'), bg=self.bg_color)
        self.product_id_entry = tk.Entry(self.edit_product_frame, width=40, font=(self.data_font, 12))
        self.product_id_entry.insert(0, self.product_list[ProductObjEnum.PRODUCT_ID.value])
        self.product_id_entry.config(state='disabled')
        self.product_id_lbl.grid(row = 1, column = 0, sticky='W')
        self.product_id_entry.grid(row = 1, column= 1, sticky='E,W')

        self.product_name_lbl = tk.Label(self.edit_product_frame, text = "Product Name:", font=(self.data_font, 12, 'bold'), bg=self.bg_color)
        self.product_name_entry = tk.Entry(self.edit_product_frame, width=40, font=(self.data_font, 12))
        self.product_name_entry.insert(0, self.product_list[ProductObjEnum.PRODUCT_NAME.value])
        self.product_name_entry.config(state='disabled')
        self.product_name_lbl.grid(row = 2, column = 0, sticky='W')
        self.product_name_entry.grid(row = 2, column= 1, sticky='E,W')

        self.product_description_lbl = tk.Label(self.edit_product_frame, text = "Product Description:", font=(self.data_font, 12, 'bold'), bg=self.bg_color)
        self.product_description_entry = tk.Entry(self.edit_product_frame, width=40, font=(self.data_font, 12))
        self.product_description_entry.insert(0, self.product_list[ProductObjEnum.DESCRIPTION.value])
        self.product_description_entry.config(state='disabled')
        self.product_description_lbl.grid(row = 3, column = 0, sticky='W')
        self.product_description_entry.grid(row = 3, column= 1, sticky='E,W')

        self.product_price_lbl = tk.Label(self.edit_product_frame, text = "Unit Price:", font=(self.data_font, 12, 'bold'), bg=self.bg_color)
        self.product_price_entry = tk.Entry(self.edit_product_frame, width=40, font=(self.data_font, 12))
        self.product_price_entry.insert(0, self.product_list[ProductObjEnum.UNIT_PRICE.value])
        self.product_price_lbl.grid(row = 4, column = 0, sticky='W')
        self.product_price_entry.grid(row = 4, column= 1, sticky='E,W')

        self.product_note_lbl = tk.Label(self.edit_product_frame, text = "Note:", font=(self.data_font, 12, 'bold'), bg=self.bg_color)
        self.product_note_entry = tk.Entry(self.edit_product_frame, width=40, font=(self.data_font, 12))
        self.product_note_entry.insert(0, self.product_list[ProductObjEnum.NOTE.value])
        self.product_note_lbl.grid(row = 5, column = 0, sticky='W')
        self.product_note_entry.grid(row = 5, column= 1, sticky='E,W')

        self.product_case_style_lbl = tk.Label(self.edit_product_frame, text = "Case Style:", font=(self.data_font, 12, 'bold'), bg=self.bg_color)
        self.product_case_style_entry = tk.Entry(self.edit_product_frame, width=40, font=(self.data_font, 12))
        self.product_case_style_entry.insert(0, self.product_list[ProductObjEnum.CASE_STYLE.value])
        self.product_case_style_lbl.grid(row = 6, column = 0, sticky='W')
        self.product_case_style_entry.grid(row = 6, column= 1, sticky='E,W')

        self.btn.grid(row = 7, column = 0, columnspan=3, ipadx=10, padx=5, pady=40)


    def build_frame(self):
        self.set_up_frame()
        self.add_title_label()
        self.create_product_frame()
        #self.populate_form()

    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy()

    def getEntryElements(self):
        prod_list = []
        prod_list.append(self.product_id_entry.get().strip())
        prod_list.append(self.product_name_entry.get().strip())
        prod_list.append(self.product_description_entry.get().strip())
        prod_list.append(self.product_price_entry.get().strip())
        prod_list.append(self.product_case_style_entry.get().strip())
        prod_list.append(self.product_note_entry.get().strip())

        return prod_list
