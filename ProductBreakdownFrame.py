import tkinter as tk
from GPFISCoordinator import GPFISCoordinator
from Product import ProductObj

class ProductBreakdownFrame():

    def __init__(self, parent_frame, canvas, root):
        self.base_frame = parent_frame
        self.canvas = canvas
        self.root = root
        self.coordinator = GPFISCoordinator()
        self.productObjList = []
        self.monthsDict = {1: "January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
        self.entryList = []
        self.totalsEntryList = []


    def setup_frame(self):
        self.product_breakdown_frame = tk.Frame(self.base_frame)

        self.product_length = len(self.productObjList)
        self.months_length = len(self.monthsDict)

        self.product_breakdown_frame.grid_columnconfigure((0), weight=1, uniform='column')

        col = 0
        row = 0

        lbl = tk.Label(self.product_breakdown_frame, text=' ', anchor='w')
        lbl.grid(row=0, column=0)

        col = 1
        row = 0

        for months in list(self.monthsDict.values()):
            self.product_breakdown_frame.grid_columnconfigure((col), weight=1, uniform='column')
            lbl = tk.Label(self.product_breakdown_frame, text=months, wraplength=100)
            lbl.grid(row=row, column=col)
            col += 1

        col = 0
        row = 1
        for products in self.productObjList:
            #self.customer_board_frame.grid_rowconfigure((row), weight=1)
            lbl = tk.Label(self.product_breakdown_frame, text=products.getName(), anchor='w')
            lbl.grid(row=row ,column=col, rowspan=2)
            row += 2
    
        col = 1
        row = 1
        self.product_length = len(self.productObjList)
        self.months_length = len(self.monthsDict)
        print(self.months_length, " MONTHS LENGTH")
        print(self.product_length, " PRODUCT LENGTH")
        for x in range(1, self.product_length+1):
            for y in range(0, self.months_length):
                dollar_entry = tk.Entry(self.product_breakdown_frame)
                quantity_entry = tk.Entry(self.product_breakdown_frame)
                #SET THE ENTRY BOX TO DATA FROM DATABASE
                #e.g. total for product id 1 for month of january, feb, march, april, ..etc
                dollar_entry.grid(row=x * 2 - 1, column=y+1)
                quantity_entry.grid(row=x * 2, column=y+1)
                self.set_entry_text(dollar_entry, "0")
                self.set_entry_text(quantity_entry, "0")
                self.entryList.append(dollar_entry)
                self.entryList.append(quantity_entry)

            #totals_entry = tk.Entry(self.product_breakdown_frame)
            #self.totalsEntryList.append(totals_entry)
            #totals_entry.grid(row = x+1, column=self.months_length+1)
            #self.product_breakdown_frame.grid_columnconfigure((x+1), weight=1, uniform='column')
        
        print(len(self.entryList), " ENTRY LIST")
        print(self.entryList)
        for x in range(0, self.months_length):
            self.set_entry_text(self.entryList[x], "edit")
        
        self.product_breakdown_frame.pack(expand=True, fill='both', ipady=20)
        self.update_scroll_region()

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
        self.cache_sales_data()
        self.setup_frame()
        #self.populate_ui()
    
    def cache_product_data(self):
        print("Product Breakdown Frame")
        print("#####Caching Product Data#####")
        self.productObjList = self.coordinator.get_products()
        print("Cached Product List: ", self.productObjList)

    def cache_sales_data(self):
        print("Product Breakdown Frame")
        print("#####Caching Sales Data#####")
        self.sales_data = self.coordinator.get_product_sales_data_by_month()
        print("Cached Product Sales Data: ", self.sales_data)

    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy()