import tkinter as tk

class InvoiceLineItemWidget():

    product_dict = {"77":"Tokyo Negi", "78": "Kabu (Packed in bags)", "1": "Cucumber (Kyuuri)(Loose 50 lb box)"}
    price_dict = {"77":2.53, "78": 2.03, "1": 1.85}

    def __init__(self, parent_frame):
        self.base_frame = parent_frame

        self.quantity_entry = tk.Entry(self.base_frame, width=7, background='#E5E4E2')
        self.cases_entry = tk.Entry(self.base_frame, width=10, background='#E5E4E2')
        self.item_no_entry = tk.Entry(self.base_frame, width=5, background='#E5E4E2')
        self.description_entry = tk.Text(self.base_frame, width=20, height=2, background='#E5E4E2', wrap= tk.WORD)
        self.note_entry = tk.Text(self.base_frame, width=20, height=2, background='#E5E4E2', wrap= tk.WORD)
        self.price_entry = tk.Entry(self.base_frame, width=10, background='#E5E4E2')
        self.line_total_entry = tk.Entry(self.base_frame, width=10, background='#E5E4E2')

        self.description_entry.config(state='disabled')

        self.price_entry.bind("<KeyRelease>", self.monitor_search_box)
        self.quantity_entry.bind("<KeyRelease>", self.monitor_search_box)
        self.item_no_entry.bind("<KeyRelease>", self.product_lookup)

    def place_line_item(self, theRow):
        self.quantity_entry.grid(row=theRow, column=0, sticky='N,E,W', pady=2, ipady=8)
        self.cases_entry.grid(row=theRow, column=1, sticky='N,E,W',pady=2, ipady=8)
        self.item_no_entry.grid(row=theRow, column=2, sticky='N,E,W', ipady=8, pady=2)
        self.description_entry.grid(row=theRow, column=3, sticky='N,E,W', pady=2)
        self.note_entry.grid(row=theRow, column=4, sticky='N,E,W', pady=2)
        self.price_entry.grid(row=theRow, column=5, sticky='N,E,W', ipady=8, pady=2)
        self.line_total_entry.grid(row=theRow, column=6, sticky='N,E,W', ipady=8, pady=2)

    def get_line_elements_as_list(self):
        element_list = []
        element_list.append(self.quantity_entry.get())
        element_list.append(self.cases_entry.get())
        element_list.append(self.item_no_entry.get())
        element_list.append(self.description_entry.get('1.0', 'end-1c'))
        element_list.append(self.note_entry.get('1.0', 'end-1c'))
        element_list.append(self.price_entry.get())
        element_list.append(self.line_total_entry.get())

        return element_list

    def get_line_total(self):
        line_tot = self.line_total_entry.get()
        if line_tot == '':
            line_tot = 0
        else:
            line_tot = round(float(line_tot), 2)
        return line_tot

    def monitor_search_box(self, e):
        try:
            typed = self.price_entry.get()
            #print(typed)
            if typed == '':
                data = '0.00'
            else:
                data = 0
                qty = float(self.quantity_entry.get())
                price = float(self.price_entry.get())
                data = round((qty * price),2)
                self.line_total_entry.delete(0, tk.END)
                self.line_total_entry.insert(0, data)
        except ValueError:
            print("Incorrect Value inside qty or price.")
        except:
            print("Something went wrong")

    def product_lookup(self, e):
        try:
            typed = self.item_no_entry.get()
            #print(typed)
            if typed == '':
                data = ''
                product_price = '0.00'
            else:
                data = self.product_dict.get(typed)
                #NOTE: Possible that maybe a lookup into the database is better for this rather than
                #populating a dictionary. Prices will also have to be populated in this call and that would
                #require two dictionaries or two db calls.
                #print(data)

                #populate description field
                self.description_entry.config(state='normal')
                self.description_entry.delete("1.0", tk.END)
                self.description_entry.insert("1.0", str(data))
                self.description_entry.config(state='disabled')

                product_price = self.price_dict.get(typed)
                #populate the price field
                self.price_entry.delete(0, tk.END)
                self.price_entry.insert(0, str(product_price))
        except ValueError:
            print("Incorrect value inside item number field.")
        except KeyError:
            print("Key does not exist in product dict.")
        except:
            print("Something went wrong with item number/description fields.", e)


