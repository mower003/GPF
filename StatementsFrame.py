import tkinter as tk

from tkinter import ttk
from GPFISCoordinator import GPFISCoordinator
from GPFISPrintFunctions import GPFISStatment2HTML
from StatementInvoiceSummaryWidget import StatementInvoiceSummaryWidget

from tkcalendar import DateEntry
from datetime import datetime

class Statements(tk.Frame):
    #Static Settings
    #Color theme
    bg_color = '#FFFFFF'
    label_color = '#F0EBCE'
    data_color = '#FFFFFF'
    header_color = '#F0EBCE'
    #Fonts
    title_font = 'MS Sans Serif'
    header_font = 'MS Sans Serif'
    label_font = 'MS Sans Serif'
    data_font = 'MS Sans Serif'
    #Controls the title of the frame.
    frame_title = "Statements"

    def __init__(self, parent_frame, canvas):
        self.base_frame = parent_frame
        self.canvas = canvas
        self.coordinator = GPFISCoordinator()

    def fetch_customer_objects(self):
        return self.coordinator.get_entities()
    
    def rebuild_frame(self):
        self.clear_display_frame()
        self.build_frame()

    def fetch_statement(self):
        self.oustanding_balance = 0
        self.grand_total = 0
        start_date, end_date = self.get_formatted_dates()
        print(start_date, end_date)
        customer_id = self.get_selected_customer_id()

        self.invoice_list = self.coordinator.get_invoices_for_statement_search(customer_id, [start_date, end_date])
        print(self.invoice_list)

        hsisw = StatementInvoiceSummaryWidget(self.statements_frame)
        hsisw.create_as_header()
        hsisw.setup_frame()

        for invObj in self.invoice_list:
            sisw = StatementInvoiceSummaryWidget(self.statements_frame)
            sisw.create_ui_elements()
            sisw.set_widget_values(invObj.get_inv_num(), invObj.get_buyer_name(), 
                                   invObj.get_ship_to_name(), invObj.get_invoice_date(), 
                                   invObj.get_delivery_date(), invObj.get_status(), invObj.get_total())
            sisw.setup_frame()

            if invObj.get_status() == 0:
                self.oustanding_balance += round(float(invObj.get_total()),2)
                self.grand_total += round(float(invObj.get_total()),2)
            if invObj.get_status() == 1:
                self.grand_total += round(float(invObj.get_total()),2)

        fsisw = StatementInvoiceSummaryWidget(self.statements_frame)
        fsisw.create_as_footer(self.oustanding_balance, self.grand_total)

        self.update_canvas_size()
    
    def create_customer_name_list(self):
        for customer in self.oCustomer_list:
            item = "[" + str(customer.getID()) + "] " + customer.getName()
            print(item)
            self.customer_name_list.append(item)

    def get_formatted_dates(self):
        sdate = datetime.strptime(str(self.date_selection_start.get_date()), '%Y-%m-%d')
        start_date = sdate.strftime('%m-%d-%Y')

        edate = datetime.strptime(str(self.date_selection_end.get_date()), '%Y-%m-%d')
        end_date = edate.strftime('%m-%d-%Y')
        return start_date, end_date
    
    def get_selected_customer_id(self):
        selected_customer = self.customer_selection_box.get()
        #print(selected_customer)
        selected_customer = selected_customer.split(" ")
    
        customer_id = selected_customer[0].replace("[", "")
        customer_id = customer_id.replace("]","")
        print(customer_id)

        return customer_id
        #for customer in self.oCustomer_list:
            #if customer.getID() == customer_id:
                #oSelectedCustomer = customer

        #return oSelectedCustomer

    def get_selected_customer_name(self):
        selected_customer = self.customer_selection_box.get()
        #print(selected_customer)
        selected_customer = selected_customer.split(" ")
    
        customer_name = " ".join(selected_customer[1:])
        print(customer_name)

        return customer_name

    def setup_frame(self):
        self.statements_frame = tk.Frame(self.base_frame, bg=self.bg_color)
        self.oCustomer_list = self.fetch_customer_objects()
        self.customer_name_list = []
        self.create_customer_name_list()
        self.customer_selection_box = ttk.Combobox(self.statements_frame, values = self.customer_name_list, state='readonly',width= 30 ,font=(self.data_font, 12, 'bold'), justify='center')

        self.date_selection_start_lbl = tk.Label(self.statements_frame, text="Date Begin: ")
        self.date_selection_end_lbl = tk.Label(self.statements_frame, text="Date End: ")
        self.date_selection_start = DateEntry(self.statements_frame, width=30, background='darkblue', foreground='white', borderwidth=2, date_pattern='mm-dd-y')
        self.date_selection_end = DateEntry(self.statements_frame, width=30, background='darkblue', foreground='white', borderwidth=2, date_pattern='mm-dd-y')

        self.customer_selection_box.pack(side='top', anchor='nw', padx = 20, pady= 20)

        self.date_selection_start_lbl.pack(side='top', anchor='nw', padx = 20)
        self.date_selection_start.pack(side='top', anchor='nw', padx = 20)
        self.date_selection_end_lbl.pack(side='top', anchor='nw', padx = 20)
        self.date_selection_end.pack(side='top', anchor='nw', padx = 20)

        self.search_button = tk.Button(self.statements_frame, text="Search", command= lambda: self.fetch_statement())
        self.search_button.pack(side='left', anchor='nw', padx=20, pady=5)

        self.print_button = tk.Button(self.statements_frame, text="Print", command= lambda: self.print_statement())
        self.print_button.pack(side='left', anchor='nw', padx=20, pady=5)

        self.clear_frame_button = tk.Button(self.statements_frame, text="Clear", command= lambda: self.rebuild_frame())
        self.clear_frame_button.pack(side='left', anchor='nw', padx=20, pady=5)

        self.statements_frame.pack(side='top', expand=True, fill='x', anchor= 'nw')  

        self.update_canvas_size()

    def print_statement(self):
        customer_name = self.get_selected_customer_name()
        begin_date, end_date = self.get_formatted_dates()
        print("BEFORE PRINT")
        print(customer_name)
        print(begin_date, end_date)
        printer = GPFISStatment2HTML(self.invoice_list, customer_name, begin_date, end_date, self.oustanding_balance, self.grand_total)
        printer.build_HTML_statement()
    
    def update_canvas_size(self):
        #Canvas holding scroll bar needs to be resized to fit line items.
        screen_width = self.base_frame.winfo_screenwidth()
        screen_height = self.base_frame.winfo_screenheight()

        statement_width = self.statements_frame.winfo_screenwidth()
        statement_height = self.statements_frame.winfo_screenheight()
        print("STATEMENTWIDTH: ", statement_width)
        print("STATEMENTHEIGHT: ", statement_height)
        total_height = screen_height 

        self.canvas.itemconfig("baseFrame_2", height=total_height, width=screen_width) 

    def build_frame(self):
        self.clear_display_frame()
        self.setup_frame()

    def clear_statements_frame(self):
        for children in self.statements_frame.winfo_children():
            children.destroy()

    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy()