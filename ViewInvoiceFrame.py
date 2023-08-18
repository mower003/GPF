import tkinter as tk
from tkinter import font
from tkcalendar import Calendar, DateEntry

from datetime import date

from ViewInvoiceSummaryWidget import ViewInvoiceSummaryWidget
from InvoiceSearchWidget import InvoiceSearchWidget
from CustomerSearchWidget import CustomerSearchWidget
from GPFISCoordinator import GPFISCoordinator
from Invoice import InvoiceObj

class ViewInvoiceFrame():
    #Static Settings
    #Color theme
    bg_color = '#cccccc'
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

    def __init__(self, parent_frame, canvas, root):
        self.base_frame = parent_frame
        self.canvas = canvas
        self.root = root
        self.coordinator = GPFISCoordinator()
        self.invoice_object_list = []

    def setup_frame(self):
        self.invoice_view_frame = tk.Frame(self.base_frame, bg = self.bg_color, pady=20)
        self.search_frame = tk.Frame(self.base_frame, bg = self.bg_color, pady=5)
        #self.invoice_view_frame.pack(side='right', expand=1, anchor='n')
        self.invoice_view_frame.grid(row = 0, column=1)

    def create_search_widget(self):
        self.isw = InvoiceSearchWidget(self.search_frame)
        self.isw.build_frame()

        self.search_btn = tk.Button(self.search_frame, text="Search...", width = 20, command=lambda: self.search_and_filter_by_customer())
        self.search_btn.pack(side='top')
        #self.search_frame.pack(side='top', anchor='nw')
        self.search_frame.grid(row=0, column=0, sticky='nw')

    def create_invoice_view(self, customer_name=None):
        tdy = date.today()

        if customer_name is None:
            self.fetch_recent_invoice_data(tdy)

            for invObj in self.invoice_object_list:
                visw = ViewInvoiceSummaryWidget(self.invoice_view_frame)
                visw.set_widget_values(invObj.get_inv_num(), invObj.get_delivery_date(), invObj.get_buyer_name(), invObj.get_ship_to_name(), invObj.get_total(), invObj.get_status())
                visw.setup_frame()
        else:
            for invObj in self.invoice_object_list:
                visw = ViewInvoiceSummaryWidget(self.invoice_view_frame)
                visw.set_widget_values(invObj.get_inv_num(), invObj.get_delivery_date(), invObj.get_buyer_name(), invObj.get_ship_to_name(), invObj.get_total(), invObj.get_status())
                visw.setup_frame()
        self.update_scroll_region()
        #View will automatically get the most recent 50 invoices. (maybe?)
        #If invoices beyond that are required user will have to use the search function
        #Search can only be done by date or customer and combo of paid/unpaid.
        # If search is done by customer then it will limit to most recent 50. 
        # Paid/Unpaid checkbox will be located here and will automatically update the db when state is changed.
        # | Invoice Number | Customer Name | Invoice Total | Paid/Unpaid [ ] | Button[Edit] |

    def search_and_filter_by_customer(self):
        selected_cust = self.isw.get_customer()
        #returns as list [start date, end date]
        date_range = self.isw.get_date_selections()
        #returns as [paid, unpaid]
        paid_status = self.isw.get_paid_unpaid()
        print(selected_cust + " " + str(date_range) + " " + str(paid_status))

        #self.cache_invoice_data(selected_cust, date_range, paid_status)

        self.fetch_invoice_results(selected_cust, date_range, paid_status)
        self.clear_invoice_view()
        self.create_invoice_view(selected_cust)

    def fetch_recent_invoice_data(self, todaysDate):
        self.invoice_object_list.clear()
        self.invoice_object_list = self.coordinator.get_recent_invoices(todaysDate)

    def fetch_invoice_results(self, selected_cust, date_range, paid_status):
        self.invoice_object_list.clear()
        self.invoice_object_list = self.coordinator.get_invoices_using_search_params(selected_cust, date_range, paid_status)
        print("INVOIVE OBJECT LIST")
        print(self.invoice_object_list)
        #print(customerInvList)

    def update_scroll_region(self):
        #Canvas holding scroll bar needs to be resized to fit line items.
        self.invoice_view_frame.update()
        self.base_frame.update()

        frame_height = self.invoice_view_frame.winfo_reqheight()
        frame_width = self.invoice_view_frame.winfo_reqwidth()

        total_height = frame_height
        total_width = frame_width
        screen_width = self.root.winfo_screenwidth()

        print("h         " + str(frame_height))

        #self.canvas.itemconfig("baseFrame_2", height=total_height, width=screen_width)
        #self.canvas.update_idletasks()
        #self.wrapper_frame.update()
        #self.entity_lines_frame.update_idletasks()
        #self.base_frame.update_idletasks()
        #bbox = self.base_frame.bbox("all")
        #bboxa = self.entity_lines_frame.bbox("all")

        #print("bbox   " + str(bbox) + "   bboxa     " + str(bboxa))
        #bbox is bound by topmost coords (0,0) and bottom rightmost coords (frame width, frame height)
        self.canvas.config(scrollregion=(0,0,screen_width, total_height))
        #self.canvas.config(scrollregion=(self.entity_lines_frame.bbox("all")))

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