import tkinter as tk
from sqlite3 import Error
from ErrorPopUpWindow import ErrorPopUpWindow
from GPFISCoordinator import GPFISCoordinator

class InvoiceLineItemWidget():

    product_dict = {"77":"Tokyo Negi", "78": "Kabu (Packed in bags)", "1": "Cucumber (Kyuuri)(Loose 50 lb box)"}
    price_dict = {"77":2.53, "78": 2.03, "1": 1.85}

    def __init__(self, parent_frame):
        self.base_frame = parent_frame
        self.productObjList = []
        self.errorPrompt = ErrorPopUpWindow(self.base_frame)
        self.line_id = -999
        self.quantity_entry = tk.Entry(self.base_frame, width=7, background='#E5E4E2')
        self.cases_entry = tk.Entry(self.base_frame, width=10, background='#E5E4E2')
        self.item_no_entry = tk.Entry(self.base_frame, width=5, background='#E5E4E2')
        self.description_entry = tk.Text(self.base_frame, width=20, height=2, background='#E5E4E2', wrap= tk.WORD)
        self.note_entry = tk.Text(self.base_frame, width=20, height=2, background='#E5E4E2', wrap= tk.WORD)
        self.price_entry = tk.Entry(self.base_frame, width=10, background='#E5E4E2')
        self.line_total_entry = tk.Entry(self.base_frame, width=10, background='#E5E4E2')

        self.description_entry.config(state='disabled')
        self.line_total_entry.config(state='disabled')

        self.price_entry.bind("<KeyRelease>", self.monitor_search_box)
        self.quantity_entry.bind("<KeyRelease>", self.monitor_search_box)
        self.item_no_entry.bind("<KeyRelease>", self.product_lookup)

        self.cache_product_data()

    def place_line_item(self, theRow):
        self.line_id = theRow
        self.quantity_entry.grid(row=theRow, column=0, sticky='N,E,W', pady=2, ipady=8)
        self.cases_entry.grid(row=theRow, column=1, sticky='N,E,W',pady=2, ipady=8)
        self.item_no_entry.grid(row=theRow, column=2, sticky='N,E,W', ipady=8, pady=2)
        self.description_entry.grid(row=theRow, column=3, sticky='N,E,W', pady=2)
        self.note_entry.grid(row=theRow, column=4, sticky='N,E,W', pady=2)
        self.price_entry.grid(row=theRow, column=5, sticky='N,E,W', ipady=8, pady=2)
        self.line_total_entry.grid(row=theRow, column=6, sticky='N,E,W', ipady=8, pady=2)

    def get_line_elements_as_list(self):
        try:
            if self.quantity_entry.get() == '':
                element_list = ['']
            else:
                element_list = []
                element_list.append(int(self.line_id))
                element_list.append(int(self.quantity_entry.get()))
                element_list.append(str(self.cases_entry.get()))
                element_list.append(int(self.item_no_entry.get()))
                element_list.append(str(self.description_entry.get('1.0', 'end-1c')))
                element_list.append(str(self.note_entry.get('1.0', 'end-1c')))
                element_list.append(float(self.price_entry.get()))
                element_list.append(float(self.line_total_entry.get()))
        except ValueError as e:
            print("ValueError: Error returning list: InvoiceLineItemWidget: get_line_elements_as_list", e)
            self.errorPrompt.create_error_window(e)
        except TypeError as e:
            print("TypeError: Error returning list: InvoiceLineItemWidget: get_line_elements_as_list", e)
            self.errorPrompt.create_error_window(e)
        except Error as e:
            print("Error returning list: InvoiceLineItemWidget: get_line_elements_as_list", e)
            self.errorPrompt.create_error_window(e)

        return element_list

    def get_line_total(self):
        line_tot = self.line_total_entry.get()
        if line_tot == '':
            line_tot = 0
        else:
            line_tot = round(float(line_tot), 2)
        return line_tot

    def get_line_id(self):
        return self.line_id

    def calculate_line_total(self):
        #calculate total
        qty = float(self.quantity_entry.get())
        price = float(self.price_entry.get())
        total = round((qty * price),2)
        self.line_total_entry.config(state='normal')
        self.line_total_entry.delete(0, tk.END)
        self.line_total_entry.insert(0, total)
        self.line_total_entry.config(state='disabled')

    def monitor_search_box(self, e):
        try:
            typed = self.price_entry.get()
            #print(typed)
            if typed == '':
                data = '0.00'
            else:
                data = 0
                self.calculate_line_total()
        except ValueError:
            print("Incorrect Value inside qty or price.")
            self.errorPrompt.create_error_window(e)
        except Error as e:
            print("Something went wrong")
            self.errorPrompt.create_error_window(e)

    def product_lookup(self, e):
        try:
            typed = self.item_no_entry.get()
            #print(typed)
            if typed == '':
                data = ''
                product_price = '0.00'
            else:
                description = ''
                product_price = 0.00
                for products in self.productObjList:
                    #print("INSIDELOOP:" + " " + str(products.getID()) + " " + products.getDescription())
                    if typed == str(products.getID()):
                        description = products.getDescription()
                        product_price = products.getUnitPrice()
                        #print("INSIDEIF", description, product_price)
                #data = self.product_dict.get(typed)
                #NOTE: Possible that maybe a lookup into the database is better for this rather than
                #populating a dictionary. Prices will also have to be populated in this call and that would
                #require two dictionaries or two db calls.
                #print(data)

                #populate description field
                self.description_entry.config(state='normal')
                self.description_entry.delete("1.0", tk.END)
                self.description_entry.insert("1.0", str(description))
                self.description_entry.config(state='disabled')

                #product_price = self.price_dict.get(typed)
                #populate the price field
                self.price_entry.delete(0, tk.END)
                self.price_entry.insert(0, str(product_price))

                #calculate total
                self.calculate_line_total()
        except ValueError as e:
            print("ValueError: Incorrect value inside item number field.", e)
            self.errorPrompt.create_error_window(e)
        except TypeError as e:
            print("TypeError: Incorrect value inside item number field.", e)
            self.errorPrompt.create_error_window(e)
        except KeyError as e:
            print("KeyError: Key does not exist in product dict.", e)
            self.errorPrompt.create_error_window(e)
        except Error as e:
            print("Uncaught Exception: Something went wrong with item number/description fields.", e)
            self.errorPrompt.create_error_window(e)

    def cache_product_data(self):
        self.coordinator = GPFISCoordinator()
        self.productObjList = self.coordinator.get_products()

        for obs in self.productObjList:
            print(obs.asList())


