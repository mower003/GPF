import tkinter as tk

class ErrorPopUpWindow():

    def __init__(self):
        self.errorWindow = tk.Toplevel()
        self.errorWindow.title("Error")

    def create_error_window(self, e):
        self.tempError = tk.Label(self.errorWindow, text=e)
        self.tempError.pack()
        self.b = tk.Button(self.errorWindow, text="Close", command=self.errorWindow.destroy)
        self.b.pack()

class EditForm():
    def __init__(self, title):
        self.editWindow = tk.Toplevel()
        self.editWindow.geometry("400x200")
        self.editWindow.title(title)
        self.lbl_list = []
        self.entry_list = []
        self.btn = tk.Button(self.editWindow, text="Save", width=10)

    def build_edit_window_UI(self,form_elements,data):
        print(data)
        row = 0
        col = 0
        for element in form_elements:
            lbl = tk.Label(self.editWindow, text= element)
            entry = tk.Entry(self.editWindow, width=30)
            entry.insert(0,str(data[row]))
            lbl.grid(row=row, column=col, sticky="W")
            entry.grid(row = row, column=col+1, sticky="E,W", padx=5)
            self.lbl_list.append(lbl)
            self.entry_list.append(entry)
            row += 1
        self.btn.grid(row=row+1, column = 1, ipadx=10, padx=5, pady=40)

    def get_entry_elements(self):
        entry_elements = []
        for element in self.entry_list:
            entry_elements.append(element.get())
        if entry_elements[0].isnumeric():
            entry_elements[0] = int(entry_elements[0])
        entry_elements.append(entry_elements.pop(0))
        entry_elements = tuple(entry_elements)
        print(entry_elements)
        return entry_elements

    def remove_window(self):
        self.editWindow.destroy()


class AddForm():
    def __init__(self, parent_frame):
        self.lbl_list = []
        self.entry_list = []
        self.my_frame = tk.Frame(parent_frame, bd=2, bg='grey')
        self.btn = tk.Button(self.my_frame, text="Save", width=40)
        self.my_frame.pack(side="top", pady=2, padx=2, fill="both", expand=True)

    def add_title_label(self, title_name):
        self.title = tk.Label(self.my_frame, text=title_name)
        self.title.config(font=("",25))
        self.title.grid(row=0, column = 0, columnspan=3, ipady=5, pady=5, sticky="E,W")
        self.my_frame.grid_columnconfigure(0, weight=1)
        self.my_frame.grid_columnconfigure(1, weight=1)
        self.my_frame.grid_columnconfigure(2, weight=1)

    def get_entry_elements(self):
        entry_elements = []
        for element in self.entry_list:
            entry_elements.append(element.get())
        if entry_elements[0].isnumeric():
            entry_elements[0] = int(entry_elements[0]) 
        entry_elements = tuple(entry_elements)
        print(entry_elements)
        return entry_elements

    def create_add_form(self,form_elements):
        row = 1
        col = 0
        for element in form_elements:
            lbl = tk.Label(self.my_frame, text= element)
            entry = tk.Entry(self.my_frame, width=70)
            lbl.grid(row=row, column=col, sticky="W")
            entry.grid(row = row, column=col+1, sticky="E,W")
            self.lbl_list.append(lbl)
            self.entry_list.append(entry)
            row += 1
        self.btn.grid(row=row+1, column = 0, columnspan= 3, ipadx=10, padx=5, pady=40)

class ViewForm():

    def __init__(self, parent_frame):
        self.lbl_list = []
        self.delete_btn_list = []
        self.edit_btn_list = []
        self.my_frame = tk.Frame(parent_frame, bd=2, bg='grey')
        self.my_frame.pack(side="top", pady=2, padx=2, fill="both", expand=True)
        
    def create_view_form(self, form_headers, form_rows):
        row = 1
        col = 0
        for headers in form_headers:
            lbl = tk.Label(self.my_frame, text = headers, font=('',15, 'bold'))
            lbl.grid(row = row, column = col, sticky = "W,E")
            self.my_frame.grid_columnconfigure(col, weight=1)
            col += 1
        
        row = 2
        col = 0
        index = 0
        for element in form_rows:
            for item in element:
                lbl = tk.Label(self.my_frame, text = item, borderwidth=2, relief="solid", font=('', 12))
                lbl.grid(row = row, column = col, sticky = "W,E")
                self.lbl_list.append(lbl)
                col += 1
            edit_btn = tk.Button(self.my_frame, text="Edit", padx=5)
            delete_btn = tk.Button(self.my_frame, text="Delete", padx=5)
            edit_btn.grid(row=row, column=col+1)
            #delete_btn.grid(row=row, column=col+2)
            self.edit_btn_list.append(edit_btn)
            self.delete_btn_list.append(delete_btn)
            row += 1
            col = 0
            index += 1

    def add_title_label(self, title_name):
        self.title = tk.Label(self.my_frame, text=title_name)
        self.title.config(font=("",25))
        self.title.grid(row=0, column = 0, columnspan=6, ipady=5, pady=5, sticky="E,W")

class DeleteForm():

    def __init__(self, parent_frame):
        self.lbl_list = []
        self.entry_list = []
        self.my_frame = tk.Frame(parent_frame, bd=2, bg='grey')
        self.btn = tk.Button(self.my_frame, text="Delete", width=40)
        self.my_frame.pack(side="top", pady=2, padx=2, fill="both", expand=True)

    def add_title_label(self, title_name):
        self.title = tk.Label(self.my_frame, text=title_name)
        self.title.config(font=("",25))
        self.title.grid(row=0, column = 0, columnspan=2, ipady=5, pady=5, sticky="E,W")
        self.my_frame.grid_columnconfigure(0, weight=1)
        self.my_frame.grid_columnconfigure(1, weight=3)

    def get_entry_elements(self):
        entry_elements = []
        customer_id_to_delete = self.entry_list[0].get()
        if customer_id_to_delete.isnumeric():
            entry_elements.append(int(customer_id_to_delete))

        return entry_elements

    def create_delete_form(self, form_elements):
        row = 1
        col = 0
        for element in form_elements:
            lbl = tk.Label(self.my_frame, text= element)
            entry = tk.Entry(self.my_frame)
            lbl.grid(row=row, column=col, sticky="nsew", padx=5)
            entry.grid(row = row, column=col+1, sticky="nsew", padx=5)
            self.lbl_list.append(lbl)
            self.entry_list.append(entry)
            row += 1
        self.btn.grid(row=row+1, column = 0, columnspan= 2, ipadx=10, padx=5, pady=40)

class AddInvoice():

    def __init__(self, parent_frame):
        self.customer = tk.StringVar()
        self.subtotal = 0.00
        self.subtotal_var = tk.StringVar()
        self.discount_var = tk.StringVar()
        self.inv_number = tk.StringVar()
        self.customer_info_vars = []
        self.lineItems = []
       
        self.customer.set("Choose a Customer")

        self.my_frame = tk.Frame(parent_frame)
        self.title_frame = tk.Frame(self.my_frame, bg='grey')
        self.header_frame = tk.Frame(self.my_frame)
        self.form_frame = tk.Frame(self.my_frame)
        self.line_items_frame = tk.Frame(self.my_frame)
        self.total_frame = tk.Frame(self.my_frame)

        self.inv_num = tk.Label(self.header_frame, textvariable = self.inv_number, font=("",14))

        self.my_frame.pack(side='top', fill='both')
        self.title_frame.pack(side='top', fill = 'x')
        self.header_frame.pack(side='top', fill= 'x')
        self.form_frame.pack(side='top',fill='x')
        self.line_items_frame.pack(side='top', fill='x')
        self.total_frame.pack(side='top', fill='x')
        self.btn = tk.Button(self.total_frame, text="Save & Print", width=40)
        self.add_lineitem_btn = tk.Button(self.total_frame, text="Add a Line", width=20)

    def add_title_label(self, title_name):
        self.title = tk.Label(self.title_frame, text=title_name)
        self.title.config(font=("",25))
        self.title.pack(side='top', fill='x')

    def populate_dropdown(self, customer_list, cust_dict):
        print(customer_list)
        cust_address_var = tk.StringVar(self.header_frame)
        cust_options = tk.StringVar(self.header_frame)
        cust_options.set("Select a Customer")
        cust_address_var.set("None")
        customer_dropdown = tk.OptionMenu(self.header_frame, cust_options, *customer_list)
        customer_dropdown.grid(row = 0, column = 0, columnspan=2, pady=10)

        customer_address_lbl = tk.Label(self.header_frame, textvariable = cust_address_var, font=("",14))
        customer_address_lbl.grid(row = 0, column = 2, columnspan=2, pady=10, padx=10)

        def set_cust_lbl(*args):
            cust_address_var.set(cust_dict[cust_options.get()])
            self.customer_info_vars.insert(0, cust_options.get())
        cust_options.trace('w',set_cust_lbl)

    def create_invoice_add_form(self, form_headers, lineItemRows, product_dict):
        row = 0
        col = 0
        invoice_label = tk.Label(self.header_frame, text="Invoice Number: ", font=("",14))
        invoice_label.grid(row = 0, column = 5, pady=2, padx=2, sticky="w")
        self.inv_num.grid(row=0, column=6, pady=2, padx=2, sticky="W")

        for headers in form_headers:
            lbl = tk.Label(self.form_frame, text = headers, font=('',15, 'bold'))
            lbl.grid(row = row, column = col, sticky = "NSW")
            self.form_frame.grid_columnconfigure(col, weight=1)
            col += 1
        row = 4
        for i in range(0,lineItemRows+1):
            #self.create_line_item(product_dict.keys(), row, product_dict)
            li = LineItem(self.line_items_frame, product_dict)
            li.price.trace_add('write',self.calculate_subtotal)
            self.lineItems.append(li)
            row += i

        self.discount_var.set("0.00")
        total_var = tk.StringVar()

        inv_subtotal_lbl = tk.Label(self.total_frame, text="Subtotal ")
        inv_subtotal_entry = tk.Entry(self.total_frame, textvariable=self.subtotal_var, state="disabled")

        discount_lbl = tk.Label(self.total_frame, text="Discount ")
        discount_entry = tk.Entry(self.total_frame, textvariable=self.discount_var)

        inv_total_lbl = tk.Label(self.total_frame, text="Total ")
        inv_total_entry = tk.Entry(self.total_frame, textvariable=total_var, state="disabled")

        def total_callback(*args):
            try:
                inv_total = round(float(self.subtotal_var.get().replace("$",'').replace(',','')) - float(self.discount_var.get()), 2)
                total_var.set('$ {:,.2f}'.format(inv_total))
            except tk.TclError as e:
                print(e)
            except ValueError as e:
                print(e)
        self.subtotal_var.trace_add('write', self.calculate_subtotal)
        self.discount_var.trace('w', total_callback)

        filler_label = tk.Label(self.total_frame)
        self.total_frame.columnconfigure(0,weight=1)
        filler_label.grid(row = 0, column = 0, columnspan=7, rowspan=3, sticky='nsew')
        inv_subtotal_lbl.grid(row = 0, column = 8)
        discount_lbl.grid(row = 1, column = 8, sticky='e')
        inv_total_lbl.grid(row = 2, column = 8)

        inv_subtotal_entry.grid(row = 0, column = 9)
        discount_entry.grid(row = 1, column = 9)
        inv_total_entry.grid(row = 2, column = 9)

        self.btn.grid(row=row+4, column = 2, columnspan= 4, ipadx=10, padx=5, pady=40)
        self.add_lineitem_btn.grid(row=row+4, column = 0, columnspan= 2, padx = 10, pady=40)
        self.add_lineitem_btn.configure(command = lambda arg = product_dict : self.add_line(arg))

    def calculate_subtotal(self,*args):
        try:
            total = 0
            for lines in self.lineItems:
                print(lines.get_line_values())
                total += lines.get_line_total()
            self.subtotal_var.set(str(total))
        except tk.TclError as e:
            print(e)
        except ValueError as e:
            print(e)
    
    def add_line(self, product_dict):
        li = LineItem(self.line_items_frame, product_dict)
        self.lineItems.append(li)

    def get_lineitems(self):
        line_items = []
        for lines in self.lineItems:
            line = lines.get_line_values()
            if line[0] != 0:
                line_items.append(line)
        return line_items



class LineItem():

    def __init__(self, parent_frame, product_dict):
        self.line_item_frame = tk.Frame(parent_frame)
        self.line_item_frame.pack(side='top', fill='both', expand = True)
        for i in range(0,6):
            self.line_item_frame.columnconfigure(i,weight=1)
        self.product_dictionary = product_dict

        self.quantity = tk.IntVar(self.line_item_frame)
        #self.cases = tk.StringVar(self.line_item_frame)
        self.item_num_var = tk.IntVar(self.line_item_frame)
        self.product_description_var = tk.StringVar(self.line_item_frame)
        self.price = tk.DoubleVar(self.line_item_frame)
        self.total = tk.DoubleVar(self.line_item_frame)

        self.quantity_entry = tk.Entry(self.line_item_frame, textvariable= self.quantity)
        self.cases_entry = tk.Entry(self.line_item_frame)
        self.item_num_dd = tk.OptionMenu(self.line_item_frame, self.item_num_var, *product_dict.keys())
        self.item_num_dd.configure(width = 15)
        self.product_description = tk.Label(self.line_item_frame, textvariable=self.product_description_var, padx=1, height=2, width = 20, wraplength=150, bd=1, relief='sunken')
        self.price_entry = tk.Entry(self.line_item_frame, textvariable = self.price)
        self.total_entry = tk.Entry(self.line_item_frame, state="disabled", textvariable = self.total)

        self.quantity_entry.grid(row = 0, column = 0, sticky="new", padx=1, pady=1)
        self.cases_entry.grid(row = 0, column = 1, sticky="new", padx=1, pady=1)
        self.item_num_dd.grid(row = 0, column = 2, sticky="new", padx=1)
        self.product_description.grid(row = 0, column = 3, sticky="new", padx=1, pady=1, ipady=1, ipadx=1)
        self.price_entry.grid(row = 0, column = 4, sticky="new", padx=1, pady=1)
        self.total_entry.grid(row = 0, column = 5, sticky="new", padx=1, pady=1)

        self.price.trace_add('write',self.calculate_line_total)
        self.item_num_var.trace_add('write', self.show_desc)

    def get_line_values(self):
        line_list = [self.quantity.get(),self.cases_entry.get(),self.item_num_var.get(),self.product_description_var.get(),self.price.get()]
        return line_list

    def get_line_total(self):
        return self.total.get()

    def calculate_line_total(self,*args):
        try:
            #price = self.price.get()
            #qty = self.quantity.get())
            tot = round((self.price.get() * self.quantity.get()), 2)
            #total_string = '$ {:,.2f}'.format(tot) 
            self.total.set(tot)
        except tk.TclError as e:
            print(e)
        except ValueError as e:
            print(e)

    def show_desc(self,*args):
            self.product_description_var.set(self.product_dictionary.get(self.item_num_var.get()))

class InvoiceView():

    def __init__(self, parent_frame):
        self.current_inv_num = tk.StringVar()
        self.invoice_numbers_list = []
        self.my_frame = tk.Frame(parent_frame)
        self.title_frame = tk.Frame(self.my_frame)
        self.invoice_navigation_frame = tk.Frame(self.my_frame, bg='grey')
        self.invoice_display_frame = tk.Frame(self.my_frame)

        self.my_frame.pack(side='top', fill='both', expand=True)
        self.title_frame.pack(side='top', fill='x')
        self.invoice_navigation_frame.pack(side='top', fill='x')
        self.invoice_display_frame.pack(side='top', fill='both')

        self.previous_invoice_btn = tk.Button(self.invoice_navigation_frame, text="Back", width=15)
        self.next_invoice_btn = tk.Button(self.invoice_navigation_frame, text="Next", width=15)

    def add_title_label(self, title_name):
        for children in self.title_frame.winfo_children():
            children.destroy()
        title_lbl = tk.Label(self.title_frame, text=title_name, font=("",25))
        title_lbl.pack(side='top', fill='x')

    def set_inv_nums(self, inv_nums):
        self.invoice_numbers_list = inv_nums
    
    """
    def nxt_btn_fnc(self):
        cur_index = self.invoice_numbers_list.index(int(self.current_inv_num.get()))

        if cur_index == (len(self.invoice_numbers_list)-1):
            cur_index = 0
        else:
            cur_index += 1
        self.current_inv_num.set(str(self.invoice_numbers_list[cur_index]))

    def bck_btn_fnc(self):
        cur_index = self.invoice_numbers_list.index(int(self.current_inv_num.get()))

        if cur_index == 0:
            cur_index = len(self.invoice_numbers_list)-1
        else:
            cur_index -= 1
        self.current_inv_num.set(str(self.invoice_numbers_list[cur_index]))
    """
    def build_nav_frame(self):
        self.current_inv_num.set(str(self.invoice_numbers_list[-1]))

        self.invoice_navigation_frame.columnconfigure(0, weight=1)
        self.invoice_navigation_frame.columnconfigure(1, weight=1)
        self.invoice_navigation_frame.columnconfigure(2, weight=1)
        self.invoice_navigation_frame.columnconfigure(3, weight=1)

        invoice_text_label = tk.Label(self.invoice_navigation_frame, text="Invoice: ", font=("", 14), bg='grey')
        current_invoice_number_label = tk.Label(self.invoice_navigation_frame, textvariable=self.current_inv_num, font=("",14), bg='grey')

        self.previous_invoice_btn.grid(row = 0, column = 0, sticky='e', pady=5)
        invoice_text_label.grid(row = 0, column = 1, pady=5)
        current_invoice_number_label.grid(row = 0, column=2, pady=5)
        self.next_invoice_btn.grid(row = 0, column=3, sticky='w', pady=5)

    def build_invoice_display_frame(self, invoice_data, line_items):
        for children in self.invoice_display_frame.winfo_children():
            children.destroy()
        #line_string = ""
        line_totals = []
        row = 1
        address_string = str(invoice_data[0][4]) + "\n" + str(invoice_data[0][5]) + ", " +str(invoice_data[0][6]) + ", " +str(invoice_data[0][7]) + ", " +str(invoice_data[0][8])
        self.add_title_label(address_string)
        headers = ['Quantity', 'Cases','Product ID', 'Description', 'Price', 'Total']
        col = 0
        for items in headers:
            lbl = tk.Label(self.invoice_display_frame, text = items, font=("",12))
            lbl.grid(row = 0, column = col)
            self.invoice_display_frame.columnconfigure(col, weight=1)
            col += 1
        for lines in line_items:
            print(lines[1],lines[5])
            #calculate line item total and append to list to use in calculating subtotal
            line_total = lines[1] * lines[5]
            line_totals.append(line_total)
            #create labels for each line item to display them
            qty_lbl = tk.Label(self.invoice_display_frame, text = lines[1])
            cases_lbl = tk.Label(self.invoice_display_frame, text = lines[2])
            prodid_lbl = tk.Label(self.invoice_display_frame, text = lines[3])
            desc_lbl = tk.Label(self.invoice_display_frame, text = lines[4])
            price_lbl = tk.Label(self.invoice_display_frame, text = lines[5])
            linetotal_lbl = tk.Label(self.invoice_display_frame, text = '{:,.2f}'.format(line_total))
            #place them on the UI
            qty_lbl.grid(row = row, column = 0)
            cases_lbl.grid(row = row, column = 1)
            prodid_lbl.grid(row = row, column = 2)
            desc_lbl.grid(row = row, column = 3)
            price_lbl.grid(row = row, column = 4)
            linetotal_lbl.grid(row = row, column = 5)
            #line_string += str(lines[1]) + " " + str(lines[2]) + " " + str(lines[3]) + " " + str(lines[4]) + " " + str(lines[5]) + " " + '{:,.2f}'.format(line_total) 
            #lines_lbl = tk.Label(self.invoice_display_frame, text = line_string, font=("", 12))
            #lines_lbl.grid(row = row, column = 0, columnspan=3, sticky='w', pady=3, padx=2)
            #line_string = ""
            row += 1

        """
        customer_text_lbl = tk.Label(self.invoice_display_frame, text="Customer: ")
        customer_name_lbl = tk.Label(self.invoice_display_frame, text=invoice_data[0][4])
        customer_address_text_lbl = tk.Label(self.invoice_display_frame, text="Address: ")
        customer_address = tk.Label(self.invoice_display_frame, text=address_string)
        """
        date_text_lbl = tk.Label(self.invoice_display_frame, text= "Date: ")
        date = tk.Label(self.invoice_display_frame, text = invoice_data[0][2])

        #calculate subtotal using list of line totals.
        subtotal_amnt = 0.0
        for element in line_totals:
            subtotal_amnt += element

        subtotal_string = '$ {:,.2f}'.format(subtotal_amnt) 
        subtotal = tk.Label(self.invoice_display_frame, text = "Subtotal: " + subtotal_string, font=("",14))

        #calculate total using provided discount from database and calculated subtotal.
        total_amnt = subtotal_amnt - invoice_data[0][3]
        total_string = '$ {:,.2f}'.format(total_amnt) 
        discount_string = '$ {:,.2f}'.format(invoice_data[0][3])
        
        #create the labels and place them onto UI
        total_lbl = tk.Label(self.invoice_display_frame, text = "Total: " + total_string, font=("", 14))
        discount_lbl = tk.Label(self.invoice_display_frame, text = "Discount: " + discount_string, font = ("", 14))
        row +=1
        subtotal.grid(row = row, column = 5, sticky='e', pady = 3, padx = 2)
        row +=1
        discount_lbl.grid(row = row, column = 5,  sticky='e', pady=3, padx=2)
        row +=1
        total_lbl.grid(row = row, column = 5,  sticky='e', pady=3, padx = 2)
        row +=1

        """
        customer_text_lbl.grid(row = 0, column = 0)
        customer_name_lbl.grid(row = 0, column = 1)

        customer_address_text_lbl.grid(row = 0, column = 2)
        customer_address.grid(row = 0, column = 3)
        """
        #Create a place to display the date of the invoice.
        date_text_lbl.grid(row = 0, column = 6)
        date.grid(row = 0, column = 7)

        edit_button = tk.Button(self.invoice_display_frame, text="Edit Invoice", command=print("clicked"))
        edit_button.grid(row = row, column = 3, columnspan = 2)

"""
class EditInvoice():
    def __init__(self, invoice_data):
        self.edit_inv_frame = tk.Toplevel()
        self.edit_inv_frame.geometry("800x800")
        self.edit_inv_frame.title("Edit Invoice")

        self.customer_name_label = tk.Label(self.edit_inv_frame, text="Customer Name")
        self.customer_address_label = tk.Label(self.edit_inv_frame, text="Customer Address")
        self.invoice_number = tk.Label(self.edit_inv_frame, text="Invoice Number")
        self.
"""






        