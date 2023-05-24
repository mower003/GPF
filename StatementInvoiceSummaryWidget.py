import tkinter as tk
from GPFISCoordinator import GPFISCoordinator

class StatementInvoiceSummaryWidget():
    #Static Settings
    #Color theme
    bg_color = '#FFFFFF'
    label_color = '#FFFFFF'
    data_color = '#E5E4E2'
    header_color = '#FFFFFF'
    #Fonts
    title_font = 'Haettenschweiler'
    header_font = 'Haettenschweiler'
    label_font = 'Haettenschweiler'
    data_font = 'MS Sans Serif'
    #Controls the title of the frame.
    frame_title = "Statement Invoice Summary Widget"

    def __init__(self, parent_frame):
        self.base_frame = parent_frame
        self.coordinator = GPFISCoordinator()
        self.invoice_summary_frame = tk.Frame(self.base_frame, bg=self.bg_color, padx=10)
        self.invoice_summary_frame.pack(side='top', fill='x', expand=1)

        self.invoice_summary_frame.grid_columnconfigure((1,2,3), weight=2, uniform='column')
        self.invoice_summary_frame.grid_columnconfigure((0,4,5,6,7), weight=1, uniform='column')
        self.invoice_summary_frame.grid_rowconfigure(0,uniform='row')

    def create_ui_elements(self):
        self.inv_num_lbl = tk.Label(self.invoice_summary_frame, text="Null", bg=self.data_color, font=(self.data_font, 12), borderwidth=1, relief='solid', anchor='w')
        self.buyer_name_lbl = tk.Label(self.invoice_summary_frame, text="Null", bg=self.data_color, font=(self.data_font, 12), borderwidth=1, relief='solid', anchor='w')
        self.shipto_name_lbl = tk.Label(self.invoice_summary_frame, text="Null", bg=self.data_color, font=(self.data_font, 12), borderwidth=1, relief='solid', anchor='w')
        self.invoice_date = tk.Label(self.invoice_summary_frame, text="Null", bg=self.data_color, font=(self.data_font, 12), borderwidth=1, relief='solid', anchor='w')
        self.delivery_date = tk.Label(self.invoice_summary_frame, text="Null", bg=self.data_color, font=(self.data_font, 12), borderwidth=1, relief='solid', anchor='w')    
        self.invoice_total = tk.Label(self.invoice_summary_frame, text="Null", bg=self.data_color, font=(self.data_font, 12), borderwidth=1, relief='solid', anchor='w')
        self.paid_status = tk.Label(self.invoice_summary_frame, text="Null", bg=self.data_color, font=(self.data_font, 12), borderwidth=1, relief='solid', anchor='w')

    def create_as_header(self):
        self.inv_num_lbl = tk.Label(self.invoice_summary_frame, text="Invoice #", bg=self.header_color, font=(self.data_font, 12), borderwidth=1, relief='solid', anchor='w')
        self.buyer_name_lbl = tk.Label(self.invoice_summary_frame, text="Bill To", bg=self.header_color, font=(self.data_font, 12), borderwidth=1, relief='solid', anchor='w')
        self.shipto_name_lbl = tk.Label(self.invoice_summary_frame, text="Ship To", bg=self.header_color, font=(self.data_font, 12), borderwidth=1, relief='solid', anchor='w')
        self.invoice_date = tk.Label(self.invoice_summary_frame, text="Invoice Date", bg=self.header_color, font=(self.data_font, 12), borderwidth=1, relief='solid', anchor='w')
        self.delivery_date = tk.Label(self.invoice_summary_frame, text="Delivery Date", bg=self.header_color, font=(self.data_font, 12), borderwidth=1, relief='solid', anchor='w')    
        self.paid_status = tk.Label(self.invoice_summary_frame, text="Payment Status", bg=self.header_color, font=(self.data_font, 12), borderwidth=1, relief='solid', anchor='w')
        self.invoice_total = tk.Label(self.invoice_summary_frame, text="Total", bg=self.header_color, font=(self.data_font, 12), borderwidth=1, relief='solid', anchor='w')

    def create_as_footer(self, outstanding_balance, total):
        self.space1 = tk.Label(self.invoice_summary_frame, text="", bg=self.header_color, font=(self.data_font, 12), borderwidth=1, relief='solid', anchor='w')
        self.space2 = tk.Label(self.invoice_summary_frame, text="", bg=self.header_color, font=(self.data_font, 12), borderwidth=1, relief='solid', anchor='w')
        self.space3 = tk.Label(self.invoice_summary_frame, text="", bg=self.header_color, font=(self.data_font, 12), borderwidth=1, relief='solid', anchor='w')
        self.outstanding_balance_txt = tk.Label(self.invoice_summary_frame, text="Oustanding Balance", bg=self.header_color, font=(self.data_font, 12), borderwidth=1, relief='solid', anchor='w')
        self.oustanding_balance= tk.Label(self.invoice_summary_frame, text=str(outstanding_balance), bg=self.header_color, font=(self.data_font, 12), borderwidth=1, relief='solid', anchor='w')    
        self.total_txt = tk.Label(self.invoice_summary_frame, text="Total", bg=self.header_color, font=(self.data_font, 12), borderwidth=1, relief='solid', anchor='w')
        self.total = tk.Label(self.invoice_summary_frame, text=str(total), bg=self.header_color, font=(self.data_font, 12), borderwidth=1, relief='solid', anchor='w')

        self.space1.grid(column=0, row=0, sticky='E,W')
        self.space2.grid(column=1, row=0, sticky='E,W')
        self.space3.grid(column=2, row=0, sticky='E,W')
        self.outstanding_balance_txt.grid(column=3, row=0, sticky='E,W')
        self.oustanding_balance.grid(column=4, row=0, sticky='E,W')
        self.total_txt.grid(column=5, row=0, sticky='E,W')
        self.total.grid(column=6, row=0, sticky='E,W')

    def setup_frame(self):
        self.inv_num_lbl.grid(column=0, row=0, sticky='E,W')
        self.buyer_name_lbl.grid(column=1, row=0, sticky='E,W')
        self.shipto_name_lbl.grid(column=2, row=0, sticky='E,W')
        self.invoice_date.grid(column=3, row=0, sticky='E,W')
        self.delivery_date.grid(column=4, row=0, sticky='E,W')
        self.paid_status.grid(column=5, row=0, sticky='E,W')
        self.invoice_total.grid(column=6, row=0, sticky='E,W')

    def set_widget_values(self, inv_num, customer_name, shipto_name,invoice_date, delivery_date, paid_status, invoice_total):
        self.inv_num_lbl.config(text=str(inv_num))
        self.buyer_name_lbl.config(text=str(customer_name))
        self.shipto_name_lbl.config(text=str(shipto_name))
        self.invoice_date.config(text=str(invoice_date))
        self.delivery_date.config(text=str(delivery_date))
        self.paid_status.config(text=str(self.get_paid_as_str(paid_status)))
        self.invoice_total.config(text=str(invoice_total))

    def get_paid_as_str(self, paid_status):
        status = ""
        if paid_status == 0:
            status = "Unpaid"
        if paid_status == 1:
            status = "Paid"

        return status

    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy()