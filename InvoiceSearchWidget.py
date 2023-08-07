import tkinter as tk
from tkcalendar import Calendar, DateEntry
from datetime import datetime, timedelta

class InvoiceSearchWidget():
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
    frame_title = "Invoice Search Frame"

    def __init__(self, parent_frame):
        self.base_frame = parent_frame
        self.unpaid_var = tk.BooleanVar()
        self.paid_var = tk.BooleanVar()

    def setup_frames(self):
        self.customer_search_frame = tk.Frame(self.base_frame, bg=self.bg_color, padx=5, pady=5)
        self.invoice_date_frame = tk.Frame(self.base_frame, bg=self.bg_color, padx=5, pady=5)
        self.paid_status_frame = tk.Frame(self.base_frame, bg=self.bg_color, padx=5, pady=5)

        self.customer_search_box = tk.Entry(self.customer_search_frame, foreground='grey', width=30)
        self.customer_search_box.bind("<Button-1>", self.clear_customer_search_default)
        self.customer_search_box.insert(tk.END, "Search by Customer Name...")

        self.date_selection_start_lbl = tk.Label(self.invoice_date_frame, text="Date Begin: ")
        self.date_selection_end_lbl = tk.Label(self.invoice_date_frame, text="Date End: ")
        self.date_selection_start = DateEntry(self.invoice_date_frame, width=30, background='darkblue', foreground='white', borderwidth=2)
        self.date_selection_end = DateEntry(self.invoice_date_frame, width=30, background='darkblue', foreground='white', borderwidth=2)

        self.unpaid_lbl = tk.Label(self.paid_status_frame, text="Check to filter by unpaid: ")
        self.unpaid_checkbox = tk.Checkbutton(self.paid_status_frame,text="Unpaid", variable=self.unpaid_var)
        self.paid_checkbox = tk.Checkbutton(self.paid_status_frame,text="Paid", variable=self.paid_var)

        self.customer_search_box.grid(row=0, column=0, sticky='e,w')

        self.date_selection_start_lbl.grid(row=0, column=0, sticky='e,w')
        self.date_selection_start.grid(row=1, column = 0, sticky='e,w')

        self.date_selection_end_lbl.grid(row=2, column=0, sticky='e,w')
        self.date_selection_end.grid(row=3, column=0, sticky='e,w')

        self.unpaid_lbl.grid(row = 0, column=0, columnspan=2, sticky='e,w')
        self.paid_checkbox.grid(row = 1, column = 0, sticky='e,w')
        self.unpaid_checkbox.grid(row = 1, column = 1, sticky='e,w')

        self.customer_search_frame.pack(side='top')
        self.invoice_date_frame.pack(side='top', expand=1)
        self.paid_status_frame.pack(side='top')

    def clear_customer_search_default(self, e):
        self.customer_search_box.delete(0, tk.END)
        self.customer_search_box.config(foreground='black')

    def get_customer(self):
        if self.customer_search_box.get() == 'Search by Customer Name...':
            customer = None
        elif self.customer_search_box.get() == '':
            customer = None
        else:
            customer = self.customer_search_box.get()

        #print("returning customer search box " + customer)
        return customer

    def get_date_selections(self):

        date_list = []

        ddate = datetime.strptime(str(self.date_selection_start.get_date()), '%Y-%m-%d')
        date = ddate.strftime('%m-%d-%Y')
        date_list.append(date)

        ddate = datetime.strptime(str(self.date_selection_end.get_date()), '%Y-%m-%d')
        date = ddate.strftime('%m-%d-%Y')
        date_list.append(date)

        return date_list

    def get_paid_unpaid(self):

        invoice_status_list = []

        invoice_status_list.append(self.paid_var.get())
        invoice_status_list.append(self.unpaid_var.get())

        return invoice_status_list


    def build_frame(self):
        self.clear_display_frame()
        self.setup_frames()

    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy()