import tkinter as tk
from tkinter import font
from tkcalendar import Calendar, DateEntry

from ViewInvoiceSummaryWidget import ViewInvoiceSummaryWidget
from InvoiceSearchWidget import InvoiceSearchWidget
from CustomerSearchWidget import CustomerSearchWidget
from Invoice import InvoiceObj

class ViewInvoiceFrame():
    #Static Settings
    #Color theme
    bg_color = '#FFFFFF'
    label_color = '#FFFFFF'
    data_color = '#FFFFFF'
    header_color = '#FFFFFF'
    #Fonts
    title_font = 'Haettenschweiler'
    header_font = 'Haettenschweiler'
    label_font = 'Haettenschweiler'
    data_font = 'MS Sans Serif'
    #Controls the title of the frame.
    frame_title = "View Invoices Frame"

    def __init__(self, parent_frame):
        self.base_frame = parent_frame
        self.invoice_object_list = []

    def setup_frame(self):
        self.invoice_view_frame = tk.Frame(self.base_frame, bg = self.bg_color, padx=20, pady=20)
        self.search_frame = tk.Frame(self.base_frame, bg = self.bg_color, pady=20, padx=20)
        self.invoice_view_frame.pack(side='right', expand=1, fill='x', anchor='n')
        self.unpaid_var = tk.BooleanVar()
        self.paid_var = tk.BooleanVar()

    def create_search_widget(self):
        self.isw = InvoiceSearchWidget(self.search_frame)
        self.isw.build_frame()

        self.search_btn = tk.Button(self.search_frame, text="Search...", width = 20, command=lambda: self.search_and_filter_by_customer())
        self.search_btn.pack(side='top')
        self.search_frame.pack(side='top')

    def cache_invoice_data(self):
        #Need to fetch all invoices based on values inside the search widget. Cannot happen until someone clicks search or 
        #a default routine is run to collect todays invoices and display.
        pass

    def create_invoice_view(self, customer_name=None):
        #I think the best way to handle this is to populate the list from a direct query to the db based on a search of the
        #customer name and dates as well as paid/unpaid. THEN build the frame using loop below.
        placeholder_data_list = [[1234, "Times Distributing", 12345.67],[1234, "Times Distributing", 12345.67],[1234, "Times Distributing", 12345.67],[1234, "Times Distributing", 12345.67],[1234, "Times Distributing", 12345.67]
                                ,[12345, "Times Distributing", 12345.67],[1254, "Times Distributing", 12345.67],[1234, "Times Distributing", 12345.67],[1234, "Times Distributing", 12345.67],[1234, "Times Distributing", 12345.67]]
        #View will automatically get the most recent 50 invoices. (maybe?)
        #If invoices beyond that are required user will have to use the search function
        #Search can only be done by date or customer and combo of paid/unpaid.
        # If search is done by customer then it will limit to most recent 50. 
        # Paid/Unpaid checkbox will be located here and will automatically update the db when state is changed.
        # | Invoice Number | Customer Name | Invoice Total | Paid/Unpaid [ ] | Button[Edit] |
        max_widgets = 5
        for i in range(max_widgets):
            #print("out",customer_name,placeholder_data_list[i][1])
            if customer_name in placeholder_data_list[i][1]:
                #print("in", customer_name,placeholder_data_list[i][1])
                visw = ViewInvoiceSummaryWidget(self.invoice_view_frame)
                visw.set_widget_values(self.invoice_object_list[i].get_inv_num(),self.invoice_object_list[i].get_buyer_id(),self.invoice_object_list[i].get_total(), self.invoice_object_list[i].get_status())
                visw.setup_frame()

    def search_and_filter_by_params(self):
        selected_cust = self.isw.get_customer()
        #returns as list [start date, end date]
        date_range = self.isw.get_date_selections()
        #returns as [paid, unpaid]
        paid_status = self.isw.get_paid_unpaid()

        self.cache_invoice_data(selected_cust, date_range, paid_status)

        self.fetch_invoice_results()
        self.clear_invoice_view()
        self.create_invoice_view(selected_cust)

    def fetch_invoice_results(self):
        
        for i in range(1,6):
            invoice_object = InvoiceObj(invoice_number = i, creation_date='2/13/23', delivery_date='2/13/23', discount_rate=0)
            invoice_object.addInvoiceItem(invoice_id = i, product_id= 77, case_quantity= '1 1/2, 2 1/2', quantity = 10, unit_price = 2.00, line_note='')
            invoice_object.addInvoiceItem(invoice_id = i, product_id= 77, case_quantity= '1 1/2, 2 1/2', quantity = 10, unit_price = 3.00, line_note='')
            invoice_object.addInvoiceItem(invoice_id = i, product_id= 77, case_quantity= '1 1/2, 2 1/2', quantity = 10, unit_price = 4.00, line_note='')
            invoice_object.addInvoiceItem(invoice_id = i, product_id= 77, case_quantity= '1 1/2, 2 1/2', quantity = 10, unit_price = 5.00, line_note='')
            invoice_object.calculate_invoice_subtotal()
            invoice_object.calculate_invoice_total()
            self.invoice_object_list.append(invoice_object)
            print(invoice_object.invoiceItemsAsList())

        print(self.invoice_object_list[0].get_total())

    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy()

    def clear_invoice_view(self):
        for children in self.invoice_view_frame.winfo_children():
            children.destroy()

    def build_frame(self):
        self.clear_display_frame()
        self.setup_frame()
        self.create_search_widget()
        self.create_invoice_view()