import tkinter as tk

from EditProductFrame import EditProductFrame
from GPFISCoordinator import GPFISCoordinator
from Product import ProductObj
from Product import ProductObjEnum

class ProductLineItemWidget():

    #Static Settings
    #Color theme
    #bg_color = '#395144'
    bg_color = '#D3D3D3'
    #bg_color = '#E5E4E2'
    label_color = '#4E6C50'
    data_color = '#AA8B56'
    header_color = '#F0EBCE'
    #Fonts
    title_font = 'Haettenschweiler'
    header_font = 'Haettenschweiler'
    label_font = 'MS Sans Serif'
    data_font = 'MS Sans Serif'
    #Controls the title of the frame.
    frame_title = "Product Line Item Widget"

    def __init__(self, parent_frame, vpf, product_id = -999, name = '', description = '', price = 0.00, case_style = '', note = '', *, productObj=None):
        self.base_frame = parent_frame
        self.coordinator = GPFISCoordinator()
        self.viewproductclass = vpf
        if productObj is None:
            self.product_id = tk.Text(self.base_frame, bg=self.bg_color, font=(self.label_font, 12), width=20, height=2, wrap=tk.WORD)
            self.product_id.insert("1.0", product_id)

            self.name = tk.Text(self.base_frame, bg=self.bg_color, font=(self.label_font, 12), width=20, height=2, wrap=tk.WORD)
            self.name.insert("1.0", name)

            self.description = tk.Text(self.base_frame, bg=self.bg_color, font=(self.label_font, 12), width=20, height=2, wrap=tk.WORD)
            self.description.insert("1.0", description)

            self.price = tk.Text(self.base_frame, bg=self.bg_color, font=(self.label_font, 12), width=20, height=2, wrap=tk.WORD)
            self.price.insert("1.0", price)

            self.note = tk.Text(self.base_frame, bg=self.bg_color, font=(self.label_font, 12), width=20, height=2, wrap=tk.WORD)
            self.note.insert("1.0", note)

            self.case_style = tk.Text(self.base_frame, bg=self.bg_color, font=(self.label_font, 12), width=20, height=2, wrap=tk.WORD)
            self.case_style.insert("1.0", case_style)

            self.edit_button = tk.Button(self.base_frame, text="Edit", command=lambda: self.spawn_edit_window())

            self.product_id.config(state='disabled')
            self.name.config(state='disabled')
            self.description.config(state='disabled')
            self.price.config(state='disabled')
            self.case_style.config(state='disabled')
            self.note.config(state='disabled')
        else:
            self.product_id = tk.Text(self.base_frame, bg=self.bg_color, font=(self.label_font, 12), width=20, height=2, wrap=tk.WORD)
            self.product_id.insert("1.0", productObj.getID())

            self.name = tk.Text(self.base_frame, bg=self.bg_color, font=(self.label_font, 12), width=20, height=2, wrap=tk.WORD)
            self.name.insert("1.0", productObj.getName())

            self.description = tk.Text(self.base_frame, bg=self.bg_color, font=(self.label_font, 12), width=20, height=2, wrap=tk.WORD)
            self.description.insert("1.0", productObj.getDescription())

            self.price = tk.Text(self.base_frame, bg=self.bg_color, font=(self.label_font, 12), width=20, height=2, wrap=tk.WORD)
            self.price.insert("1.0", productObj.getUnitPrice())

            self.note = tk.Text(self.base_frame, bg=self.bg_color, font=(self.label_font, 12), width=20, height=2, wrap=tk.WORD)
            self.note.insert("1.0", productObj.getNote())

            self.case_style = tk.Text(self.base_frame, bg=self.bg_color, font=(self.label_font, 12), width=20, height=2, wrap=tk.WORD)
            self.case_style.insert("1.0", productObj.getCaseStyle())

            self.edit_button = tk.Button(self.base_frame, text="Edit", command=lambda: self.spawn_edit_window(productObj))

            self.product_id.config(state='disabled')
            self.name.config(state='disabled')
            self.description.config(state='disabled')
            self.price.config(state='disabled')
            self.case_style.config(state='disabled')
            self.note.config(state='disabled')

    def place_product_line(self, theRow):
        self.product_id.grid(row=theRow, column=ProductObjEnum.PRODUCT_ID.value, sticky='N,E,W', pady=2)
        self.name.grid(row=theRow, column=ProductObjEnum.PRODUCT_NAME.value, sticky='N,E,W', pady=2)
        self.description.grid(row=theRow, column=ProductObjEnum.DESCRIPTION.value, sticky='N,E,W', pady=2)
        self.price.grid(row=theRow, column=ProductObjEnum.UNIT_PRICE.value, sticky='N,E,W', pady=2)
        self.note.grid(row=theRow, column=ProductObjEnum.NOTE.value, sticky='N,E,W', pady=2)
        self.case_style.grid(row=theRow, column=ProductObjEnum.CASE_STYLE.value, sticky='N,E,W', pady=2)
        self.edit_button.grid(row=theRow, column=6, sticky='N,E,W')

    def spawn_edit_window(self, productObj=None):
        if productObj is None:
            self.ep = EditProductFrame(self.base_frame, self.get_product_as_list())
        else:
            self.ep = EditProductFrame(self.base_frame, productObj.asList(), self.viewproductclass)
            #self.clear_display_frame()

    def get_product_line_info(self):
        the_str = str(self.product_id.get("1.0", tk.END)) + " " + str(self.name.get("1.0", tk.END)) + " " + str(self.description.get("1.0", tk.END)) + " " + str(self.price.get("1.0", tk.END)) + " " + str(self.case_style.get("1.0", tk.END)) + " " + str(self.note.get("1.0", tk.END))
        return the_str

    def get_product_as_list(self):
        product_list = []
        product_list.append(str(self.product_id.get("1.0", tk.END)))
        product_list.append(str(self.name.get("1.0", tk.END)))
        product_list.append(str(self.description.get("1.0", tk.END)))
        product_list.append(str(self.price.get("1.0", tk.END)))
        product_list.append(str(self.case_style.get("1.0", tk.END)))
        product_list.append(str(self.note.get("1.0", tk.END)))
        return product_list

    def set_product_info(self, productObj):
        self.product_id = tk.Text(self.base_frame, bg=self.bg_color, font=(self.label_font, 12), width=20, height=2, wrap=tk.WORD)
        self.product_id.insert("1.0", productObj.getID())

        self.name = tk.Text(self.base_frame, bg=self.bg_color, font=(self.label_font, 12), width=20, height=2, wrap=tk.WORD)
        self.name.insert("1.0", productObj.getName())

        self.description = tk.Text(self.base_frame, bg=self.bg_color, font=(self.label_font, 12), width=20, height=2, wrap=tk.WORD)
        self.description.insert("1.0", productObj.getDescription())

        self.price = tk.Text(self.base_frame, bg=self.bg_color, font=(self.label_font, 12), width=20, height=2, wrap=tk.WORD)
        self.price.insert("1.0", productObj.getUnitPrice())

        self.note = tk.Text(self.base_frame, bg=self.bg_color, font=(self.label_font, 12), width=20, height=2, wrap=tk.WORD)
        self.note.insert("1.0", productObj.getNote())

        self.case_style = tk.Text(self.base_frame, bg=self.bg_color, font=(self.label_font, 12), width=20, height=2, wrap=tk.WORD)
        self.case_style.insert("1.0", productObj.getCaseStyle())

    def update_product_info(self, productObj):
        print("update product info called")
        self.enable_product_boxes()

        self.price.delete("1.0", tk.END)
        self.note.delete("1.0", tk.END)
        self.case_style.delete("1.0", tk.END)

        self.price.insert("1.0", productObj.getUnitPrice())
        self.note.insert("1.0", productObj.getNote())
        self.case_style.insert("1.0", productObj.getCaseStyle())

        self.disable_product_boxes()

    def enable_product_boxes(self):
        self.product_id.config(state='normal')
        self.name.config(state='normal')
        self.description.config(state='normal')
        self.price.config(state='normal')
        self.case_style.config(state='normal')
        self.note.config(state='normal')

    def disable_product_boxes(self):
        self.product_id.config(state='disabled')
        self.name.config(state='disabled')
        self.description.config(state='disabled')
        self.price.config(state='disabled')
        self.case_style.config(state='disabled')
        self.note.config(state='disabled')

    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy()