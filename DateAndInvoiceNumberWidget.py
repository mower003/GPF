import tkinter as tk
from tkcalendar import Calendar, DateEntry
from datetime import datetime, timedelta

class DateAndInvoiceNumberWidget():

    #Static Settings
    #Color theme
    bg_color = '#FFFFFF'
    label_color = '#FFFFFF'
    data_color = '#FFFFFF'
    header_color = '#FFFFFF'
    #Fonts
    title_font = 'Haettenschweiler'
    header_font = 'Haettenschweiler'
    label_font = 'MS Sans Serif'
    data_font = 'MS Sans Serif'
    #Controls the title of the frame.
    frame_title = "Data and Invoice Number Widget"

    def __init__(self, parent_frame):
        self.base_frame = parent_frame

    def setup_frame(self):
        self.invoice_data_frame = tk.Frame(self.base_frame, bg=self.bg_color, padx=5, pady=20)

    def create_ui_elements(self):
        self.invoice_desc_label = tk.Label(self.invoice_data_frame, text="Invoice Number: ", bg=self.label_color, font=(self.label_font,16))
        self.invoice_num_label = tk.Label(self.invoice_data_frame, text='100105', bg=self.label_color, font=(self.label_font, 16))

        self.delivery_date_label = tk.Label(self.invoice_data_frame, text="Delivery Date: ", bg=self.label_color, font=(self.label_font, 16))
        self.delivery_date_selection = DateEntry(self.invoice_data_frame, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='mm-dd-y')

        self.invoice_date_label = tk.Label(self.invoice_data_frame, text="Invoice Date: ", bg=self.label_color, font=(self.label_font, 16))
        self.invoice_date_selection = DateEntry(self.invoice_data_frame, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='mm-dd-y')

        self.invoice_desc_label.grid(column=0, row=0)
        self.invoice_num_label.grid(column=1, row=0)

        self.delivery_date_label.grid(column=0, row=1)
        self.delivery_date_selection.grid(column=1,row=1)

        self.invoice_date_label.grid(column=0, row=2)
        self.invoice_date_selection.grid(column=1, row=2)

        #self.invoice_data_frame.pack(side='right', padx=200)
        self.invoice_data_frame.grid(row=0, column=3)

    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy()

    def get_dates(self):
        date_list = []
        date_list.append(self.invoice_date_selection.get_date())
        date_list.append(self.delivery_date_selection.get_date())
        print(date_list)
        return date_list

    def get_invoice_date(self):
        ddate = datetime.strptime(str(self.invoice_date_selection.get_date()), '%Y-%m-%d')
        date = ddate.strftime('%m-%d-%Y')
        return str(date)

    def get_delivery_date(self):
        ddate = datetime.strptime(str(self.delivery_date_selection.get_date()), '%Y-%m-%d')
        date = ddate.strftime('%m-%d-%Y')
        return str(date)

    def get_due_date(self):
        ddate = datetime.strptime(str(self.delivery_date_selection.get_date()), '%Y-%m-%d') + timedelta(days=21)
        due_date = ddate.strftime('%m-%d-%Y')
        return str(due_date)

    def get_invoice_number(self):
        return self.invoice_num_label.cget("text")

    def set_invoice_number(self, inv_num):
        self.invoice_num_label.config(text=str(inv_num))
        self.oInvoice.set_inv_num(inv_num)

    def set_invoice_object(self, invObject):
        self.oInvoice = invObject

    def set_invoice_date(self, date):
        self.invoice_date_selection.set_date(datetime.strptime(date, "%m-%d-%Y"))

    def set_delivery_date(self, date):
        self.delivery_date_selection.set_date(datetime.strptime(date, "%m-%d-%Y"))

    def build_frame(self):
        self.setup_frame()
        self.create_ui_elements()