import tkinter as tk
from GPFISCoordinator import GPFISCoordinator
from Product import ProductObj
from Entity import EntityObj

class OrderBoardFrame():

    def __init__(self, parent_frame):
        self.base_frame = parent_frame
        self.coordinator = GPFISCoordinator()
        self.productObjList = []
        self.customerObjList = []
        self.num_products = 0
        self.num_customers = 0

    def setup_frame(self):
        self.customer_board_frame = tk.Frame(self.base_frame)
        col = 0
        row = 0

        for customers in self.customerObjList:
            lbl = tk.Label(self.customer_board_frame, text=customers.getName(), anchor='center')
            lbl.grid(row=row, column=col, columnspan=2)
            row += 1
            for products in self.productObjList:
                lbl = tk.Label(self.customer_board_frame, text=products.getName(), anchor='w')
                entry = tk.Entry(self.customer_board_frame)
                lbl.grid(row=row, column=col)
                entry.grid(row=row, column=col+1)
                row += 1
            row = 0
            col += 2

        

        self.customer_board_frame.pack(expand=True, fill='both')

    def populate_ui(self):
        pass

    def build_frame(self):
        self.clear_display_frame()
        self.cache_product_data()
        self.cache_customer_data()
        self.setup_frame()
        self.populate_ui()

    def cache_product_data(self):
        print("ORDER BOARD FRAME")
        print("#####Caching Product Data#####")
        self.productObjList = self.coordinator.get_products()
        print("Cached Product List: ", self.productObjList)

    def cache_customer_data(self):
        print("ORDER BOARD FRAME")
        print("##########Caching Customer Data######")
        self.customerObjList = self.coordinator.get_entities()
            
        print("CACHED  CUSTOMER LIST: ", self.customerObjList)

    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy()

