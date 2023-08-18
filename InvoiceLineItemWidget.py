import tkinter as tk
from sqlite3 import Error
import locale
from ErrorPopUpWindow import ErrorPopUpWindow
from GPFISCoordinator import GPFISCoordinator

class InvoiceLineItemWidget():

    def __init__(self, parent_frame):
        self.base_frame = parent_frame
        self.productObjList = []
        self.previous_line_total = 0
        self.errorPrompt = ErrorPopUpWindow(self.base_frame)
        self.line_id = -999
        self.quantity_entry = tk.Entry(self.base_frame, width=7, background='#E5E4E2')
        self.cases_entry = tk.Entry(self.base_frame, width=10, background='#E5E4E2')
        self.item_no_entry = tk.Entry(self.base_frame, width=5, background='#E5E4E2')
        self.description_entry = tk.Text(self.base_frame, width=20, height=1, background='#E5E4E2', wrap= tk.WORD)
        self.note_entry = tk.Entry(self.base_frame, width=20, background='#E5E4E2')
        self.price_entry = tk.Entry(self.base_frame, width=10, background='#E5E4E2')
        self.line_total_entry = tk.Entry(self.base_frame, width=10, background='#E5E4E2')

        self.description_entry.config(state='disabled')
        self.line_total_entry.config(state='disabled')

        self.price_entry.bind("<FocusOut>", self.monitor_quantity_and_price_box)
        self.quantity_entry.bind("<FocusOut>", self.monitor_quantity_and_price_box)
        self.item_no_entry.bind("<KeyRelease>", self.product_lookup)

    def place_line_item(self, theRow):
        self.line_id = theRow
        #, ipady=8 cnp from below attributes.
        self.quantity_entry.grid(row=theRow, column=0, sticky='N,E,W', pady=2)
        self.cases_entry.grid(row=theRow, column=1, sticky='N,E,W',pady=2)
        self.item_no_entry.grid(row=theRow, column=2, sticky='N,E,W', pady=2)
        self.description_entry.grid(row=theRow, column=3, sticky='N,E,W', pady=2)
        self.note_entry.grid(row=theRow, column=4, sticky='N,E,W', pady=2)
        self.price_entry.grid(row=theRow, column=5, sticky='N,E,W', pady=2)
        self.line_total_entry.grid(row=theRow, column=6, sticky='N,E,W', pady=2)

    def get_line_elements_as_list(self):
        try:
            element_list = []
            element_list.append(int(self.line_id))
            element_list.append(int(self.item_no_entry.get()))
            element_list.append(str(self.cases_entry.get()))
            element_list.append(int(self.quantity_entry.get()))
            element_list.append(float(self.price_entry.get()))
            element_list.append(str(self.note_entry.get()))
            element_list.append(str(self.description_entry.get('1.0', 'end-1c')))
            element_list.append(float(self.line_total_entry.get()))

            return element_list
        except ValueError as e:
            print("ValueError: Error returning list: InvoiceLineItemWidget: get_line_elements_as_list", e)
            #self.errorPrompt.create_error_window(e)
        except TypeError as e:
            print("TypeError: Error returning list: InvoiceLineItemWidget: get_line_elements_as_list", e)
            #self.errorPrompt.create_error_window(e)
        except Error as e:
            print("Error returning list: InvoiceLineItemWidget: get_line_elements_as_list", e)
            #self.errorPrompt.create_error_window(e)

    def get_line_total(self):
        line_tot = self.line_total_entry.get()
        if line_tot == '':
            line_tot = 0
        else:
            line_tot = round(float(line_tot),2)
        return line_tot
    
    def set_line_item_attributes(self, lineItem):
        #print("from inside setlineitemattr: ", lineItem)
        self.enable_line_item_attributes()
        self.line_id = lineItem[0]
        self.quantity_entry.insert(0, int(lineItem[1]))
        self.cases_entry.insert(0, str(lineItem[2]))
        self.item_no_entry.insert(0, int(lineItem[3]))
        self.description_entry.insert("1.0", str(lineItem[4]))
        self.note_entry.insert(0, str(lineItem[5]))
        self.price_entry.insert(0, locale.currency(float(lineItem[6]), False, False, False))
        self.line_total_entry.insert(0, round(float(lineItem[7]),2))
        self.disable_standard_item_attributes()

    def enable_line_item_attributes(self):
        self.description_entry.config(state='normal')
        self.quantity_entry.config(state='normal')
        self.cases_entry.config(state='normal')
        self.item_no_entry.config(state='normal')
        self.description_entry.config(state='normal')
        self.note_entry.config(state='normal')
        self.price_entry.config(state='normal')
        self.line_total_entry.config(state='normal')

    def disable_standard_item_attributes(self):
        self.description_entry.config(state='disabled')
        self.line_total_entry.config(state='disabled')

    def get_line_id(self):
        return self.line_id

    def calculate_line_total(self):
        #calculate total
        total = int(self.quantity_entry.get()) * float(self.price_entry.get())
        total = round(float(total),2)
        #print("(Invoice Line Item Widget) Line Total Calculation -> ", total)
        self.line_total_entry.config(state='normal')
        self.line_total_entry.delete(0, tk.END)
        self.line_total_entry.insert(0, total)
        self.line_total_entry.config(state='disabled')

    def set_invoice_object(self, invObject):
        self.oInvoice = invObject

    def get_price_entry_box(self):
        return self.price_entry
    
    def get_quantity_entry_box(self):
        return self.quantity_entry
    
    def get_product_entry_box(self):
        return self.item_no_entry
    
    def recalculate_line_total(self):
        try:
            qty = self.quantity_entry.get()
            price = self.price_entry.get()
            if qty == '' or price == '':
                qty = 0
                price = 0 
            else:
                self.calculate_line_total()
        except ValueError:
            print("Incorrect Value inside qty or price.",e)
            self.errorPrompt.create_error_window(e)
        except Error as e:
            print("Something went wrong")
            self.errorPrompt.create_error_window(e)

    def monitor_quantity_and_price_box(self, e):
        try:
            qty = self.quantity_entry.get()
            price = self.price_entry.get()
            #print("quantity", qty)
            #print("price", price)
            if qty == '' or price == '':
                qty = 0
                price = 0 
            else:
                self.calculate_line_total()
                #self.calculate_inv_totals()
        except ValueError:
            print("Incorrect Value inside qty or price.",e)
            self.errorPrompt.create_error_window(e)
        except Error as e:
            print("Something went wrong")
            self.errorPrompt.create_error_window(e)

    def clear_line(self):
        self.enable_line_item_attributes()
        self.quantity_entry.delete(0, tk.END)
        self.cases_entry.delete(0, tk.END)
        self.item_no_entry.delete(0, tk.END)
        self.description_entry.delete("1.0", tk.END)
        self.note_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.line_total_entry.delete(0, tk.END)
        self.disable_standard_item_attributes()

    def product_lookup(self, e):
        try:
            typed = self.item_no_entry.get()
            #print(typed)
            if typed == '':
                if self.quantity_entry.get() == '':
                    self.clear_line()
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
                #self.calculate_inv_totals()
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

    def setProductData(self, productList):
        self.productObjList = productList

    def set_footer_vars(self, subvar, totvar, discvar):
        self.subtotvar = subvar
        self.totvar = totvar
        self.discvar = discvar


