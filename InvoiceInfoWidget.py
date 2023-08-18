import tkinter as tk
from tkinter import ttk

from datetime import datetime, timedelta

class InvoiceInfoWidget():
    #Static Settings
    #Color theme
    bg_color = '#cccccc'
    label_color = '#F0EBCE'
    data_color = '#FFFFFF'
    header_color = '#F0EBCE'
    #Fonts
    title_font = 'MS Sans Serif'
    header_font = 'MS Sans Serif'
    label_font = 'MS Sans Serif'
    data_font = 'MS Sans Serif'
    #Controls the title of the frame.
    frame_title = "Invoice Info Widget"

    def __init__(self, parent_frame):
        self.base_frame = parent_frame
        self.payment_terms_list = ["NET 21 DAYS", "NET 30 DAYS", "NET 35 DAYS", "NET 42 DAYS"]
        self.due_date_var = tk.StringVar("")
        self.customer_po_var = tk.StringVar("")
        self.applied_credit_var = tk.DoubleVar(0.00)
        self.credit_invoice_num_var = tk.StringVar("")
        self.note_var = tk.StringVar("")
        self.info_frame = tk.Frame(self.base_frame, padx=15, pady=10, bg=self.bg_color)

    def create_ui_elements(self):
        self.payment_terms_lbl = tk.Label(self.info_frame, text="Payment Terms", bg=self.label_color, font=(self.label_font, 12, 'bold'))
        self.due_date_lbl = tk.Label(self.info_frame, text="Due Date", bg=self.label_color, font=(self.label_font, 12, 'bold'))
        self.customer_po_lbl = tk.Label(self.info_frame, text="Customer PO", bg=self.label_color, font=(self.label_font, 12, 'bold'))
        self.applied_credit_amount_lbl = tk.Label(self.info_frame, text="Credit Total", bg=self.label_color, font=(self.label_font, 12, 'bold'))
        self.credit_invoice_num_lbl = tk.Label(self.info_frame, text="Credit Invoice Number", bg=self.label_color, font=(self.label_font, 12, 'bold'))
        self.note_lbl = tk.Label(self.info_frame, text="Notes", bg=self.label_color, font=(self.label_font, 12, 'bold'))

        self.due_date = tk.Entry(self.info_frame, textvariable= self.due_date_var, bg=self.data_color, font=(self.data_font, 12, 'bold'), justify='center')
        self.payment_terms = ttk.Combobox(self.info_frame, values=self.payment_terms_list, state='readonly', font=(self.data_font, 12, 'bold'), justify='center')
        #self.payment_terms = tk.Entry(self.info_frame, textvariable=self.payment_terms_var, bg=self.data_color, font=(self.data_font, 12, 'bold'), justify='center')
        self.customer_po = tk.Entry(self.info_frame, textvariable=self.customer_po_var, bg=self.data_color, font=(self.data_font, 12, 'bold'), justify='center')
        self.applied_credit_amount = tk.Entry(self.info_frame, textvariable= self.applied_credit_var, bg=self.data_color, font=(self.data_font, 12, 'bold'), justify='center')
        self.credit_invoice_num = tk.Entry(self.info_frame, textvariable=self.credit_invoice_num_var, bg=self.data_color, font=(self.data_font, 12, 'bold'), justify='center')
        self.note = tk.Entry(self.info_frame, textvariable=self.note_var, bg=self.data_color, font=(self.data_font, 12, 'bold'), justify='center')

    def place_ui_elements(self):
        self.payment_terms_lbl.grid(row = 0, column = 0, sticky='we')
        self.due_date_lbl.grid(row = 0, column = 1, sticky='we')
        self.customer_po_lbl.grid(row = 0, column = 2, sticky='we')

        self.payment_terms.grid(row = 1, column = 0, sticky='we')
        self.due_date.grid(row = 1, column = 1, sticky='we')
        self.customer_po.grid(row = 1, column = 2, sticky='we')

        self.applied_credit_amount_lbl.grid(row = 2, column = 0, sticky='we')
        self.credit_invoice_num_lbl.grid(row = 2, column = 1, sticky='we')
        self.note_lbl.grid(row = 2, column = 2, sticky='we')

        self.applied_credit_amount.grid(row = 3, column = 0, sticky='we')
        self.credit_invoice_num.grid(row = 3, column = 1, sticky='we')
        self.note.grid(row = 3, column = 2, sticky='we')

    def configure_elements(self):
        self.info_frame.grid_columnconfigure((0,1,2), weight=1, uniform='column')

    def build_frame(self):
        self.create_ui_elements()
        self.configure_elements()
        self.place_ui_elements()

    def clear_display_frame(self):
        for children in self.info_frame.winfo_children():
            children.destroy()

    def calculate_due_date(self, date, num_days):
        ddate = datetime.strptime(str(date), '%m-%d-%Y') + timedelta(days=int(num_days))
        due_date = ddate.strftime('%m-%d-%Y')
        self.set_due_date(due_date=due_date)

    def get_applied_credit_amount(self):
        return str(self.applied_credit_amount.get())
    
    def get_applied_credit_var(self):
        return self.applied_credit_var

    def get_customer_po(self):
        return str(self.customer_po.get())
    
    def get_due_date(self):
        return str(self.due_date.get())
    
    def get_payment_terms(self):
        return str(self.payment_terms.get())
    
    def get_credit_invoice_num(self):
        return str(self.credit_invoice_num.get())
    
    def get_note(self):
        return str(self.note.get())
    
    def set_payment_terms(self, pymnt_trms):
        self.payment_terms.set(pymnt_trms)

    def set_due_date(self, due_date):
        self.due_date_var.set(due_date)

    def set_customer_po(self, po):
        self.customer_po_var.set(po)

    def set_applied_credit_amount(self, amnt):
        self.applied_credit_var.set(amnt)

    def set_credit_inv_number(self, num):
        self.credit_invoice_num_var.set(num)

    def set_inv_note(self, note):
        self.note_var.set(note)


    

    
