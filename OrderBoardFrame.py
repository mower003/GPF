import tkinter as tk
from GPFISCoordinator import GPFISCoordinator
from Product import ProductObj
from Entity import EntityObj

class OrderBoardFrame():

    def __init__(self, parent_frame):
        self.base_frame = parent_frame
        self.coordinator = GPFISCoordinator()
        self.entryList = []
        self.totalsEntryList = []
        self.productObjList = []
        self.customerObjList = []

    def setup_frame(self):
        self.customer_board_frame = tk.Frame(self.base_frame)

        customer_object_length = len(self.customerObjList)
        products_object_length = len(self.productObjList)

        self.customer_board_frame.grid_columnconfigure((0), weight=1, uniform='column')
        #self.customer_board_frame.grid_rowconfigure((0), weight=1)

        col = 0
        row = 0

        lbl = tk.Label(self.customer_board_frame, text=' ', anchor='w')
        lbl.grid(row=0, column=0)

        col = 1
        row = 0

        for customers in self.customerObjList:
            self.customer_board_frame.grid_columnconfigure((col), weight=1, uniform='column')
            lbl = tk.Label(self.customer_board_frame, text=customers.getName(), wraplength=100)
            lbl.grid(row=row, column=col)
            col += 1

        totals_lbl = tk.Label(self.customer_board_frame, text="Totals")
        totals_lbl.grid(row = 0, column= customer_object_length+1)

        col = 0
        row = 1
        for products in self.productObjList:
            #self.customer_board_frame.grid_rowconfigure((row), weight=1)
            lbl = tk.Label(self.customer_board_frame, text=products.getName(), anchor='w')
            lbl.grid(row=row, column=col)
            row += 1

        col = 1
        row = 1
        customer_object_length = len(self.customerObjList)
        products_object_length = len(self.productObjList)


        for x in range(0, products_object_length):
            for y in range(0, customer_object_length):
                entry = tk.Entry(self.customer_board_frame)
                entry.bind("<KeyRelease>", self.sum_entry_boxes)
                #entry.bind("<Button-1>", lambda  event, x = entry: self.delete_on_click(x))
                entry.grid(row=x+1, column=y+1)
                self.set_entry_text(entry, "0")
                self.entryList.append(entry)

            totals_entry = tk.Entry(self.customer_board_frame)
            self.totalsEntryList.append(totals_entry)
            totals_entry.grid(row = x+1, column=customer_object_length+1)
            self.customer_board_frame.grid_columnconfigure((x+1), weight=1, uniform='column')
        
        self.customer_board_frame.pack(expand=True, fill='both')

        #self.sum_entry_boxes()

    def delete_on_click(self, entry_widg):
        entry_widg.delete(0,tk.END)
        entry_widg.insert(0, "0")
        return

    def sum_entry_boxes(self, e):
        customer_object_length = len(self.customerObjList)
        entry_list_length = len(self.entryList)

        totalIndex = 0
        total = 0
        counter = 1

        for x in range(0,entry_list_length):
            total += int(self.entryList[x].get())
            if counter == customer_object_length:
                self.set_entry_text(self.totalsEntryList[totalIndex], total)
                total = 0
                counter = 0
                totalIndex += 1
            counter += 1

    def set_entry_text(self, entry_widg, text):
        entry_widg.delete(0,tk.END)
        entry_widg.insert(0,str(text))
        return

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
        self.remove_GPF_from_list()
        print("CACHED  CUSTOMER LIST: ", self.customerObjList)

    def remove_GPF_from_list(self):
        tempList = list(self.customerObjList)
        foundInd=0
        for i in range(0, len(tempList)):
            print(tempList[i].getID())
            if tempList[i].getID() == 33:   
                foundInd = i
        tempList.remove(tempList[foundInd])
        self.customerObjList.clear()
        self.customerObjList = tuple(tempList)


    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy()

