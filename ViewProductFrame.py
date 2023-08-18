import tkinter as tk
from tkinter import font

from GPFISCoordinator import GPFISCoordinator
from ProductLineItemWidget import ProductLineItemWidget

class ViewProductFrame():
    #Static Settings
    #Controls the number and name of form elements
    product_compositional_elements = ['Product ID ', 'Name ', 'Description ', 'Price ', 'Case Style ', 'Note ', '']
    #Color theme
    #bg_color = '#395144'
    bg_color = '#cccccc'
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
    frame_title = "Product List"

    def __init__(self, parent_frame, canvas, root):
        self.base_frame = parent_frame
        self.canvas = canvas
        self.root = root
        self.coordinator = GPFISCoordinator()
        self.product_list = []
        self.product_lines_list = []

    def set_up_frame(self):
        self.title_frame = tk.Frame(self.base_frame, bd=2, bg= self.bg_color)
        self.product_lines_frame = tk.Frame(self.base_frame, bg = self.bg_color, padx=10)
        self.product_lines_frame.grid_columnconfigure((0,1,2,3,4,5,6), weight=1, uniform='column')
        #self.product_lines_frame.grid_rowconfigure((0), weight=1)


    def create_product_lines(self):
        row = 1
        for products in self.product_list:
            print(products.asList())
            po = ProductLineItemWidget(self.product_lines_frame, self, productObj = products)
            po.place_product_line(row)
            self.product_lines_list.append(po)
            #self.product_lines_frame.grid_rowconfigure((row), weight=1)
            #print("from create product lines", po.get_product_line_info())
            row += 1
     
    def create_view_form(self, form_rows):
        row = 0
        col = 0
        for headers in self.product_compositional_elements:
            lbl = tk.Label(self.product_lines_frame, text = headers, font=(self.header_font,20), bg=self.bg_color)
            lbl.grid(row = row, column = col, sticky = "W,E")
            col += 1
        self.create_product_lines()
        self.update_scroll_region()
        
        self.title_frame.pack(side='top', fill='x')
        self.product_lines_frame.pack(side='top', fill='both', expand=True)

    def add_title_label(self):
        self.title = tk.Label(self.title_frame, text=self.frame_title)
        self.title.config(font=(self.title_font,38),bg=self.bg_color)
        self.title.pack(side='top', fill='x')

    def update_scroll_region(self):
        #Canvas holding scroll bar needs to be resized to fit line items.
        self.product_lines_frame.update()
        self.base_frame.update()

        header_height = self.title_frame.winfo_reqheight()
        header_width = self.title_frame.winfo_reqwidth()
        lines_height = self.product_lines_frame.winfo_reqheight()
        lines_width = self.product_lines_frame.winfo_reqwidth()

        total_height = header_height + lines_height
        total_width = header_width + lines_width
        screen_width = self.root.winfo_screenwidth()

        print("h         " + str(header_height) + "l        " + str(lines_height) + " w      " + str(lines_width))

        #self.canvas.itemconfig("baseFrame_2", height=total_height, width=screen_width)
        #self.canvas.update_idletasks()
        #self.wrapper_frame.update()
        #self.entity_lines_frame.update_idletasks()
        #self.base_frame.update_idletasks()
        #bbox = self.base_frame.bbox("all")
        #bboxa = self.entity_lines_frame.bbox("all")

        #print("bbox   " + str(bbox) + "   bboxa     " + str(bboxa))
        #bbox is bound by topmost coords (0,0) and bottom rightmost coords (frame width, frame height)
        self.canvas.config(scrollregion=(0,0,screen_width, total_height))
        #self.canvas.config(scrollregion=(self.entity_lines_frame.bbox("all")))

    def build_frame(self):
        self.clear_display_frame()
        self.cache_product_data()
        self.set_up_frame()
        self.add_title_label()
        #self.add_title_label()
        #A call to a class that fetches product data should be put here
        #the returned result should be passed into create_view_form as a list of tuples IIRC

        product_rows = []
        #print("product list: ",self.product_list)
        for products in self.product_list:
            product_rows.append(products.asList())

        #print(product_rows)
        self.create_view_form(product_rows)

    def cache_product_data(self):
        self.product_list = self.coordinator.get_products()

    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy()