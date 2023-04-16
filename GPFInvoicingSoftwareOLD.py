import tkinter as tk
from datetime import date
from GPFDatabase import GPFDatabase as gpfd
from sqlite3 import Error
from GPFISUIBuilder import AddForm
from GPFISUIBuilder import ViewForm
from GPFISUIBuilder import ErrorPopUpWindow
from GPFISUIBuilder import DeleteForm
from GPFISUIBuilder import EditForm
from GPFISUIBuilder import AddInvoice
from GPFISUIBuilder import LineItem
from GPFISUIBuilder import InvoiceView

"""
 QUERIES 

Query to select range of dates
    SELECT * FROM invoices WHERE date BETWEEN '2021-02-03' AND '2021-02-05';
Query to select invoices and associated lineItems where the invoice numbers match
    SELECT invoices.invoice_num, discount, quantity, cases, vegetable_code, description, price_per_qty 
        FROM invoices INNER JOIN lineItems ON lineItems.invoice_num = invoices.invoice_num;
"""

gpf_database_connection = gpfd()
gpf_database_connection.create_connection()
#Global variables that determine if a sub-menu is open or closed.
cust_submenu_activated = True
prod_submenu_activated = True
inv_submenu_activated = True
rprts_submenu_activated = True

#Callback functions that fire upon clicking
#the corresponding buttons from their 'view' screens.
def on_cust_delete_btn_click(data):
    def callback():
        return delete_cust_from_db(data[0])
    return callback

def on_prod_delete_btn_click(data):
    def callback():
        return delete_prod_from_db(data[0])
    return callback

def on_cust_edit_btn_click(data):
    def callback():
        return edit_cust(data)
    return callback

def on_prod_edit_btn_click(data):
    def callback():
        return edit_prod(data)
    return callback

#Sets the customer description box inside the 'Invoice -> Create an Invoice' menu.
def set_desc_box(ind, prod_dict, inv_ui):
    inv_ui.desc_box_list[ind].insert(0,(prod_dict.get(inv_ui.item_num_stringvars[ind].get())))

#Manages the creation of the customer view UI elements and populates the UI
#with the customers from the database.
def view_customer_list():
    #Clear the displayFrame
    clear_display_frame()
    #Headers to put into displayFrame as columns
    customerHeaders = ['ID','Customer Name','Address','City','State','Zip']
    #customerRows = [(11, 'Marukai', '984 South Left Street Drive', 'Kearny', 'CA', '92001'), (12, 'Tokyo Central', '999 South St', 'Carlsbad', 'CA', '92024')]
    #Try to get customers from database, if failure create popup window with error
    try:
        customerRows = gpf_database_connection.get_customers()
    except Error as e:
        ErrorPopUpWindow().create_error_window(e)
        print(e)
    #Create customer ViewForm class
    cust_view = ViewForm(displayFrame)
    cust_view.add_title_label("Customer List")
    #Pass into column headers and data from customer database query
    cust_view.create_view_form(customerHeaders, customerRows)
    index = 0
    #For every customer there is a button to edit or delete. This attaches a callback
    #to each of those buttons and passes in the row number so the callback has the correct 
    #customer data. Edit and Delete buttons are appended to separate lists inside the ViewForm class.
    for btn in cust_view.edit_btn_list:
        btn.configure(command = on_cust_edit_btn_click(customerRows[index]))
        index += 1
    index = 0
    for btn in cust_view.delete_btn_list:
        btn.configure(command = on_cust_delete_btn_click(customerRows[index]))
        index += 1

#Creates the view using the GPFISUIBuilder class and populates it with
#products from the database.
def view_products_list():
    #Clears the display side frame.
    clear_display_frame()

    #These are required to build the columns for the product view.
    product_headers = ['ID', 'Product Name', 'Product Description', 'Product Price']

    #Try to fetch product rows from database. If there is an error
    #create a pop-up window with error message.
    try:
        product_rows = gpf_database_connection.get_products()
    except Error as e:
        ErrorPopUpWindow().create_error_window(e)
        print(e)
    
    #Creates an instance of the ViewForm class and passes the displayFrame
    #to it. Adds a title, and passes the product_header list and rows from the 
    #database.
    prod_view = ViewForm(displayFrame)
    prod_view.add_title_label("Product List")
    prod_view.create_view_form(product_headers, product_rows)

    #For every btn in the edit_btn and delete_btn list, configure it to call the specific method
    #and pass in the product information for the database from that row.
    index = 0
    for btn in prod_view.edit_btn_list:
        btn.configure(command = on_prod_edit_btn_click(product_rows[index]))
        index += 1
    index = 0
    for btn in prod_view.delete_btn_list:
        btn.configure(command = on_prod_delete_btn_click(product_rows[index]))
        index += 1

#Creates an edit window that allows the user to edit customer data.
def edit_cust(data):
    cust_form_list = ['Customer ID: ', 'Customer Name: ', 'Street Address: ', 'City: ', 'State: ', 'Zip Code: ']
    edit_ui = EditForm("Edit Customer")
    edit_ui.build_edit_window_UI(cust_form_list, data)
    edit_ui.entry_list[0].configure(state = 'disabled')
    edit_ui.btn.configure(command = lambda arg = edit_ui : post_cust_edit_to_db(edit_ui))

#Method that is passed to edit_ui button. Tries to post fields grabbed from that window
#into the database, deletes pop-up window, refreshes the display_frame with new database.
def post_cust_edit_to_db(edit_ui):
    customer = edit_ui.get_entry_elements()
    print(customer)
    try:
        gpf_database_connection.edit_customer(customer)
    except Error as e:
        ErrorPopUpWindow().create_error_window(e)
    finally:
        edit_ui.remove_window()
        clear_display_frame()
        view_customer_list()
    
def edit_prod(data):
    prod_form_list = ['Product ID: ','Product Name: ','Description: ', 'Product Price: ']
    edit_ui = EditForm("Edit Product")
    edit_ui.build_edit_window_UI(prod_form_list, data)
    edit_ui.entry_list[0].configure(state = 'disabled')
    edit_ui.btn.configure(command = lambda arg = edit_ui : post_product_edit_to_db(edit_ui))

def post_product_edit_to_db(edit_ui):
    product = edit_ui.get_entry_elements()
    print(product)
    try:
        gpf_database_connection.edit_product(product)
    except Error as e:
        ErrorPopUpWindow().create_error_window(e)
    finally:
        edit_ui.remove_window()
        clear_display_frame()
        view_products_list()

def delete_cust_from_db(cust_id):
    customer_to_delete = []
    customer_to_delete.append(cust_id)
    try:
        gpf_database_connection.delete_customer(customer_to_delete)
    except Error as e:
        ErrorPopUpWindow().create_error_window(e)
    finally:
        clear_display_frame()
        view_customer_list()

def delete_prod_from_db(prod_id):
    product_to_delete = []
    product_to_delete.append(prod_id)
    try:
        gpf_database_connection.delete_product(product_to_delete)
    except Error as e:
        ErrorPopUpWindow().create_error_window(e)
    finally:
        clear_display_frame()
        view_products_list()
    
def post_customer_to_db(customer_ui):
    customer = customer_ui.get_entry_elements()
    try:
        gpf_database_connection.insert_customer(customer)
    except Error as e:
        errorWindow = tk.Toplevel()
        errorWindow.title("Error")
        tempError = tk.Label(errorWindow, text=e)
        tempError.pack()
        b = tk.Button(errorWindow, text="Close", command=errorWindow.destroy)
        b.pack()

def post_product_to_db(product_ui):
    product = product_ui.get_entry_elements()
    try:
        gpf_database_connection.insert_product(product)
    except Error as e:
        errorWindow = tk.Toplevel()
        errorWindow.title("Error")
        tempError = tk.Label(errorWindow, text=e)
        tempError.pack()
        b = tk.Button(errorWindow, text="Close", command=errorWindow.destroy)
        b.pack()

def clear_display_frame():
    for children in displayFrame.winfo_children():
        children.destroy()

def add_product():
    clear_display_frame()
    prod_form_list = ['Product ID: ','Product Name: ', 'Product Description: ', 'Product Price: ']
    product_ui = AddForm(displayFrame)
    product_ui.add_title_label("Add A Product")
    product_ui.create_add_form(prod_form_list)
    product_ui.btn.configure(command = lambda arg = product_ui : post_product_to_db(arg))

def add_cust():
    clear_display_frame()
    cust_form_list = ['Customer ID: ', 'Customer Name: ', 'Street Address: ', 'City: ', 'State: ', 'Zip Code: ']
    customer_ui = AddForm(displayFrame)
    customer_ui.add_title_label("Add a Customer")
    customer_ui.create_add_form(cust_form_list)
    customer_ui.btn.configure(command= lambda arg = customer_ui : post_customer_to_db(arg))

def dictionify_products(products):
    products_dictionary = {}

    for prod in products:
        products_dictionary[prod[0]] = str(prod[1]) + " " + str(prod[2])

    print(products_dictionary)
    return products_dictionary

def dictionify_customers(customers):
    customers_dictionary = {}

    for cust in customers:
        cust_id = str(cust[0])
        cust_name = cust[1]
        cust_key = cust_id + " - " + cust_name
        customers_dictionary[cust_key] = cust[2] + " " + cust[3] + " " + cust[4] + " " + cust[5]
    return customers_dictionary 


#!!!!!!!!!!!THIS NEEDS TO BE REDONE. INVOICE CREATION/EDIT/VIEW SHOULD BE REVISED
def save_inv_to_db(invoice_ui):
    cust_id = invoice_ui.customer_info_vars[0].split("-")
    cust_id = cust_id[0].strip()
    inv_number = int(invoice_ui.inv_number.get())
    discount = invoice_ui.discount_var.get()
    thedate = date.today()
    today = thedate.strftime("%Y-%m-%d")
    inv = [discount, today, cust_id]
    lines = invoice_ui.get_lineitems()
    i = 1
    print(inv)

    try:
        gpf_database_connection.insert_invoice(inv)
        for line in lines:
            line.insert(0,str(inv_number) + "." + str(i))
            line.insert(len(line),inv_number)
            gpf_database_connection.insert_line_item(line)
            i += 1
            print("saved to database", line)
    except Error as e:
        ErrorPopUpWindow().create_error_window(e)
    finally:
        add_inv()
#!!!!!!!!!!!THIS NEEDS TO BE REDONE. INVOICE CREATION/EDIT/VIEW SHOULD BE REVISED
def add_inv():
    clear_display_frame()
    #cust_name_list = ['NULL']
    inv_form_headers = ['Quantity', 'Cases', 'Item Number','Description', 'Price', 'Total']
    inv_num = -1
    invoice_ui = AddInvoice(displayFrame)
    invoice_ui.add_title_label("Create an Invoice")
    try:
        cust_list = gpf_database_connection.get_customers()
        cust_dict = dictionify_customers(cust_list)
        product_list = gpf_database_connection.get_products()
        prod_dict = dictionify_products(product_list)
        inv_num = gpf_database_connection.get_next_inv_num()

        if inv_num[0] == None:
            inv_num = 1
        else:
            inv_num = int(inv_num[0]) + 1
    except Error as e:
        ErrorPopUpWindow().create_error_window(e)
    invoice_ui.inv_number.set(inv_num)
    invoice_ui.populate_dropdown(cust_dict.keys(), cust_dict)
    invoice_ui.create_invoice_add_form(inv_form_headers, 5, prod_dict)
    invoice_ui.btn.configure(command = lambda arg1 = invoice_ui : save_inv_to_db(arg1))
#!!!!!!!!!!!THIS NEEDS TO BE REDONE. INVOICE CREATION/EDIT/VIEW SHOULD BE REVISED
def nxt_btn_fnc(invoice_view_ui):
    cur_index = invoice_view_ui.invoice_numbers_list.index(int(invoice_view_ui.current_inv_num.get()))

    if cur_index == (len(invoice_view_ui.invoice_numbers_list)-1):
        cur_index = 0
    else:
        cur_index += 1
    invoice_view_ui.current_inv_num.set(str(invoice_view_ui.invoice_numbers_list[cur_index]))
    inv_data, line_items = fetch_invoice_data(int(invoice_view_ui.current_inv_num.get()))
    invoice_view_ui.build_invoice_display_frame(inv_data, line_items)
#!!!!!!!!!!!THIS NEEDS TO BE REDONE. INVOICE CREATION/EDIT/VIEW SHOULD BE REVISED
def bck_btn_fnc(invoice_view_ui):
    cur_index = invoice_view_ui.invoice_numbers_list.index(int(invoice_view_ui.current_inv_num.get()))

    if cur_index == 0:
        cur_index = len(invoice_view_ui.invoice_numbers_list)-1
    else:
        cur_index -= 1
    invoice_view_ui.current_inv_num.set(str(invoice_view_ui.invoice_numbers_list[cur_index]))
    inv_data, line_items = fetch_invoice_data(int(invoice_view_ui.current_inv_num.get()))
    invoice_view_ui.build_invoice_display_frame(inv_data, line_items)
#!!!!!!!!!!!THIS NEEDS TO BE REDONE. INVOICE CREATION/EDIT/VIEW SHOULD BE REVISED
def fetch_invoice_data(invoice_number):
    inv_query = [invoice_number]
    try:
        invoice = gpf_database_connection.get_invoice_by_invoicenum(inv_query)
        line_items = gpf_database_connection.get_line_items_by_invid(inv_query)
        print(invoice)
        return invoice, line_items
    except Error as e:
        ErrorPopUpWindow().create_error_window(e)
#!!!!!!!!!!!THIS NEEDS TO BE REDONE. INVOICE CREATION/EDIT/VIEW SHOULD BE REVISED
def view_invoices():
    clear_display_frame()
    try:
        #fetch all invoice numbers
        #pass them to the viewUI
        invoice_list = gpf_database_connection.get_invoice_list()
        invoice_view_ui = InvoiceView(displayFrame)
        invoice_view_ui.add_title_label("Invoice View")
        invoice_view_ui.set_inv_nums(invoice_list)
        invoice_view_ui.build_nav_frame()
        inv_data, line_items = fetch_invoice_data(invoice_list[-1])
        invoice_view_ui.build_invoice_display_frame(inv_data, line_items)
        invoice_view_ui.previous_invoice_btn.configure(command= lambda arg = invoice_view_ui : bck_btn_fnc(arg))
        invoice_view_ui.next_invoice_btn.configure(command= lambda arg = invoice_view_ui : nxt_btn_fnc(arg))
    except Error as e:
        ErrorPopUpWindow().create_error_window(e)

#Handles displaying and hiding Customer sub-buttons
def options_cust_frame(customer_frame):
    global cust_submenu_activated
    if(cust_submenu_activated):
        cust_view_btn.pack(side="top", padx=4, pady=4, ipadx=62)
        cust_add_btn.pack(side="top", padx=4, pady=4, ipadx=69)
        cust_submenu_activated = not cust_submenu_activated  
    else:
        cust_view_btn.pack_forget()
        cust_add_btn.pack_forget()
        cust_submenu_activated = not cust_submenu_activated

#Handles displaying and hiding Products sub-buttons
def options_prod_frame(products_frame):
    global prod_submenu_activated
    if(prod_submenu_activated):
        prod_view_btn.pack(side="top", padx=4, pady=4, ipadx=62)
        prod_add_btn.pack(side="top", padx=4, pady=4, ipadx=69)
        prod_submenu_activated = not prod_submenu_activated  
    else:
        prod_view_btn.pack_forget()
        prod_add_btn.pack_forget()
        prod_submenu_activated = not prod_submenu_activated

#Handles displaying and hiding Invoices sub-buttons
def options_inv_frame(invoices_frame):
    global inv_submenu_activated
    if(inv_submenu_activated):
        inv_view_btn.pack(side="top", padx=4, pady=4, ipadx=62)
        inv_add_btn.pack(side="top", padx=4, pady=4, ipadx=69)
        inv_edit_btn.pack(side="top", padx=4, pady=4, ipadx=68)
        inv_submenu_activated = not inv_submenu_activated  
    else:
        inv_view_btn.pack_forget()
        inv_add_btn.pack_forget()
        inv_edit_btn.pack_forget()
        inv_submenu_activated = not inv_submenu_activated

#Handles displaying and hiding Reports sub-buttons
def options_rprts_frame(reports_frame):
    global rprts_submenu_activated
    if(rprts_submenu_activated):
        rprts_by_cust_btn.pack(side="top", padx=4, pady=4, ipadx=60)
        rprts_by_prod_btn.pack(side="top", padx=4, pady=4, ipadx=65)
        rprts_by_inv_btn.pack(side="top", padx=4, pady=4, ipadx=67)
        rprts_submenu_activated = not rprts_submenu_activated  
    else:
        rprts_by_cust_btn.pack_forget()
        rprts_by_prod_btn.pack_forget()
        rprts_by_inv_btn.pack_forget()
        rprts_submenu_activated = not rprts_submenu_activated 



#Displays the left side panel of options. This panel is always visible and 
#allows the user to navigate between the different windows in the program.
#Current Windows: 
# Customer: Add, View, Edit, Delete
# Products: Add, View Edit, Delete
# Invoices: Create, View, Edit
# Reports: By Customer, By Product, By Invoice
def options_frame():
    #customer_frame = tk.Frame(optionsFrame, bg='grey', bd=5)
    customer_frame.pack(side="top", fill="x")

    #products_frame = tk.Frame(optionsFrame, bg='grey', bd=5)
    products_frame.pack(side="top", fill="x")

    #invoices_frame = tk.Frame(optionsFrame, bg='grey', bd=5)
    invoices_frame.pack(side="top", fill="x")

    #reports_frame = tk.Frame(optionsFrame, bg='grey', bd=5)
    reports_frame.pack(side="top", fill="x")

    #Creating base buttons for the options frame
    #and attaching method for showing sub-buttons
    customer_btn = tk.Button(customer_frame, text="Customers", command= lambda arg1= customer_frame : options_cust_frame(arg1))
    products_btn = tk.Button(products_frame, text="Products", command= lambda arg1= products_frame : options_prod_frame(arg1))
    invoices_btn = tk.Button(invoices_frame, text="Invoices", command= lambda arg1= invoices_frame : options_inv_frame(arg1))
    reports_btn = tk.Button(reports_frame, text="Reports", command= lambda arg1= reports_frame : options_rprts_frame(arg1))

    customer_btn.pack(side="top", padx=4, pady=4, fill="x", ipadx=100)
    products_btn.pack(side="top", padx=4, pady=4, fill="x")
    invoices_btn.pack(side="top", padx=4, pady=4, fill="x")
    reports_btn.pack(side="top", padx=4, pady=4, fill="x")

    


root = tk.Tk()
root.geometry("1000x800")

root.title("GPF Invoicing Software")

#Creating frames for the left-side GUI Options 
optionsFrame = tk.Frame(root, borderwidth=2, relief="sunken", bg = 'grey')
customer_frame = tk.Frame(optionsFrame, bg='grey', bd=5)
products_frame = tk.Frame(optionsFrame, bg='grey', bd=5)
invoices_frame = tk.Frame(optionsFrame, bg='grey', bd=5)
reports_frame = tk.Frame(optionsFrame, bg='grey', bd=5)

optionsFrame.pack(side="left", fill="both")
options_frame()

#Creating sub-buttons for customer
cust_view_btn = tk.Button(customer_frame, text="View Customer List", command = view_customer_list)
cust_add_btn = tk.Button(customer_frame, text="Add a Customer", command=add_cust)

#Creating sub-buttons for products
prod_view_btn = tk.Button(products_frame, text="View Product List", command = view_products_list)
prod_add_btn = tk.Button(products_frame, text="Add a Product", command=add_product)

#Creating sub-buttons for invoices
inv_view_btn = tk.Button(invoices_frame, text="View Invoice List", command = view_invoices)
inv_add_btn = tk.Button(invoices_frame, text="Create Invoice", command = add_inv)
inv_edit_btn = tk.Button(invoices_frame, text="Edit an Invoice")

#Creating sub-buttons for reports
rprts_by_cust_btn = tk.Button(reports_frame, text="View Customer Report")
rprts_by_prod_btn = tk.Button(reports_frame, text="View Product Report")
rprts_by_inv_btn = tk.Button(reports_frame, text="View Invoice Report")

displayFrame = tk.Frame(root, bd = 2, bg = 'grey')
displayFrame.pack(side = "left", fill="both", expand=True)



"""
leftFrame = tk.Frame(root, height = 300, width = 200, bg = 'green')
leftFrame.grid(column = 0, row = 0, padx=40)

rightFrame = tk.Frame(root,height = 200, width=200, bg = 'blue')
rightFrame.grid(column=1, row = 0)

invoiceBackSelectButton = tk.Button(leftFrame, padx = 5, pady= 5, text="<", width=5)
invoiceForwardSelectButton = tk.Button(leftFrame, padx = 5, pady = 5, text=">", width=5)
invoiceNumberLabel = tk.Label(leftFrame, padx = 10, pady= 5, text="  Invoice #: #####  ")

invoiceBackSelectButton.grid(column = 0, row=0, ipady = 10, ipadx = 5)
invoiceNumberLabel.grid(column = 1, row=0)
invoiceForwardSelectButton.grid(column = 2, row = 0)

rightFrameTitle = tk.Label(rightFrame, width = 10, height= 5, text= "Invoices")
rightFrameTitle.grid(column=0, row = 0, ipadx = 5, ipady = 5)
"""
#root.mainloop()