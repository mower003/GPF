import tkinter as tk
import locale
from GPFISCoordinator import GPFISCoordinator
from Product import ProductObj

class ProductBreakdownFrame():
    locale.setlocale(locale.LC_ALL, 'en_US')
    def __init__(self, parent_frame, canvas, root):
        self.base_frame = parent_frame
        self.canvas = canvas
        self.root = root
        self.coordinator = GPFISCoordinator()

        self.productObjList = []
        self.monthsDict = {1: "January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
        self.dollar_amount_entry_list = []
        self.quantity_entry_list = []

    def setup_frame(self):
        self.product_breakdown_frame = tk.Frame(self.base_frame)
        self.product_length = len(self.productObjList)
        if self.product_length == 0:
            self.create_no_data_display()
            return
        self.months_length = len(self.monthsDict)
        self.product_breakdown_frame.grid_columnconfigure((0), weight=1, uniform='column')

        #Create an empty space for the upper left corner of the table.
        col = 0
        row = 0
        lbl = tk.Label(self.product_breakdown_frame, text=' ', anchor='w')
        lbl.grid(row=0, column=0)

        self.create_month_columns()
        self.create_product_rows()

        for x in range(1, self.product_length+1):
            for y in range(0, self.months_length):
                dollar_entry = tk.Entry(self.product_breakdown_frame, bg='#E5E4E2')
                quantity_entry = tk.Entry(self.product_breakdown_frame)
                dollar_entry.grid(row=x * 2 - 1, column=y+1)
                quantity_entry.grid(row=x * 2, column=y+1, padx=5, pady=5)
                self.set_entry_text(dollar_entry, "$0.00")
                self.set_entry_text(quantity_entry, "0.00")
                self.dollar_amount_entry_list.append(dollar_entry)
                self.quantity_entry_list.append(quantity_entry)

        self.populate_sales_data()
        
        self.product_breakdown_frame.pack(expand=True, fill='both', ipady=20)
        self.update_scroll_region()

    def create_month_columns(self):
        col = 1
        row = 0

        for months in list(self.monthsDict.values()):
            self.product_breakdown_frame.grid_columnconfigure((col), weight=1, uniform='column')
            lbl = tk.Label(self.product_breakdown_frame, text=months, wraplength=100)
            lbl.grid(row=row, column=col)
            col += 1

    def create_product_rows(self):
        col = 0
        row = 1
        for products in self.productObjList:
            #self.customer_board_frame.grid_rowconfigure((row), weight=1)
            lbl = tk.Label(self.product_breakdown_frame, text=products.getName(), anchor='w')
            lbl.grid(row=row ,column=col, rowspan=2)
            row += 2

    def create_no_data_display(self):
        no_data = tk.Label(self.product_breakdown_frame, text="NO PRODUCT DATA AVAILABLE", anchor='center', font=('',32, 'bold'))
        no_data.grid(row=0, column=0)
        self.product_breakdown_frame.pack(expand=True, fill='both', ipady=20)

    def populate_sales_data(self):
        #entry index is used to index elements for each list. Entry list length should be months_length * number of products.
        entry_index = 0
        for products in self.productObjList:
            for x in range(0, self.months_length):
                self.fetch_monthly_sales_data(products.getID(),x+1)
                if self.month_sales_data[0][0] is None:
                    self.set_entry_text(self.dollar_amount_entry_list[entry_index], self.month_sales_data[0][1])
                    self.set_entry_text(self.quantity_entry_list[entry_index], self.month_sales_data[0][2])
                else:
                    #print(self.month_sales_data)
                    self.set_entry_text(self.dollar_amount_entry_list[entry_index], locale.currency(round(float(self.month_sales_data[0][1]),2), True, True, False))
                    self.set_entry_text(self.quantity_entry_list[entry_index], locale.currency(round(float(self.month_sales_data[0][2]),2), False, True, False))
                entry_index += 1

    def update_scroll_region(self):
        #Canvas holding scroll bar needs to be resized to fit line items.
        self.product_breakdown_frame.update()
        self.base_frame.update()

        lines_height = self.product_breakdown_frame.winfo_reqheight()
        lines_width = self.product_breakdown_frame.winfo_reqwidth()

        total_height = lines_height
        total_width = lines_width
        screen_width = self.root.winfo_screenwidth()

        #print("l        " + str(lines_height) + " w      " + str(lines_width))
        #bbox is bound by topmost coords (0,0) and bottom rightmost coords (frame width, frame height)
        self.canvas.config(scrollregion=(0,0, total_width, total_height))

    def set_entry_text(self, entry_widg, text):
        entry_widg.delete(0,tk.END)
        entry_widg.insert(0,str(text))
        return
    
    def build_frame(self):
        self.clear_display_frame()
        self.cache_product_data()
        #self.cache_sales_data()
        self.setup_frame()
        #self.populate_ui()
    
    def cache_product_data(self):
        print("Product Breakdown Frame")
        print("#####Caching Product Data#####")
        self.productObjList = self.coordinator.get_products()
        print("Cached Product List: ", self.productObjList)

    def fetch_monthly_sales_data(self, product_id, month_num):
        self.month_sales_data = self.coordinator.get_product_sales_data_by_month(product_id, month_num)
        #print(self.month_sales_data)

    def cache_sales_data(self):
        print("Product Breakdown Frame")
        print("#####Caching Sales Data#####")
        self.sales_data = self.coordinator.get_product_sales_data_by_month()
        print("Cached Product Sales Data: ", self.sales_data)

    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy()