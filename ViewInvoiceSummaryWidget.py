import tkinter as tk
from GPFISCoordinator import GPFISCoordinator
from EditInvoiceFrame import EditInvoiceFrame
from GPFISPrintFunctions import GPFIS2HTML

class ViewInvoiceSummaryWidget():
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
    frame_title = "View Invoice Summary Widget"

    def __init__(self, parent_frame):
        self.base_frame = parent_frame
        self.coordinator = GPFISCoordinator()
        self.invoice_summary_frame = tk.Frame(self.base_frame, bg=self.bg_color, padx=10)
        self.invoice_summary_frame.pack(side='top', fill='x', expand=1)

        self.invoice_summary_frame.grid_columnconfigure((2,3,4), weight=2, uniform='column')
        self.invoice_summary_frame.grid_columnconfigure((0,1,5,6,7), weight=1, uniform='column')
        self.paid_status_var = tk.BooleanVar()

        self.inv_num_lbl = tk.Label(self.invoice_summary_frame, text="Null", bg=self.data_color, font=(self.data_font, 12), borderwidth=1, relief='solid', anchor='w')
        self.delivery_date_lbl = tk.Label(self.invoice_summary_frame, text="Null", bg=self.data_color, font=(self.data_font, 12), borderwidth=1, relief='solid', anchor='w')
        self.buyer_name_lbl = tk.Label(self.invoice_summary_frame, text="Null", bg=self.data_color, font=(self.data_font, 12), borderwidth=1, relief='solid', anchor='w')
        self.shipto_name_lbl = tk.Label(self.invoice_summary_frame, text="Null", bg=self.data_color, font=(self.data_font, 12), borderwidth=1, relief='solid', anchor='w')
        self.invoice_total = tk.Label(self.invoice_summary_frame, text="Null", bg=self.data_color, font=(self.data_font, 12), borderwidth=1, relief='solid', anchor='w')
        self.paid_checkbox = tk.Checkbutton(self.invoice_summary_frame, text="Paid", variable=self.paid_status_var, command=lambda: self.update_paid_status(), borderwidth=1, relief='solid', activebackground='#D3D3D3')
        self.edit_invoice_btn = tk.Button(self.invoice_summary_frame, text="Edit", bg=self.data_color, command=lambda: self.edit_invoice_window(), borderwidth=1, relief='raised', activebackground='#D3D3D3')
        self.preview_invoice_btn = tk.Button(self.invoice_summary_frame, text="Print Preview", bg=self.data_color, command=lambda: self.print_preview(), borderwidth=1, relief='raised', activebackground='#D3D3D3')

    def setup_frame(self):
        self.inv_num_lbl.grid(column=0, row=0, sticky='E,W')
        self.delivery_date_lbl.grid(column=1, row=0, sticky='E,W')
        self.buyer_name_lbl.grid(column=2, row=0, sticky='E,W')
        self.shipto_name_lbl.grid(column=3, row=0, sticky='E,W')
        self.invoice_total.grid(column=4, row=0, sticky='E,W')
        self.paid_checkbox.grid(column=5, row=0, sticky='E,W', padx=2)
        self.edit_invoice_btn.grid(column=6, row=0, sticky='E,W', padx=2)
        self.preview_invoice_btn.grid(column=7, row=0, sticky='E,W', padx=2)

    def set_widget_values(self, inv_num, delivery_date, customer_name, shipto_name, invoice_total, paid_status=0):
        self.inv_num_lbl.config(text="Invoice #: " + str(inv_num))
        self.delivery_date_lbl.config(text=str(delivery_date))
        self.buyer_name_lbl.config(text=str(customer_name))
        self.shipto_name_lbl.config(text=str(shipto_name))
        self.invoice_total.config(text="Invoice Total: " + str(invoice_total))
        self.paid_status_var.set(paid_status)
        
    def update_paid_status(self):
        self.coordinator.update_paid_status(self.get_invoice_number(), self.get_paid_status())
        #print("Paid status changed to: ", self.paid_status_var.get())

    def edit_invoice_window(self):
        inv_num = self.get_invoice_number()
        oInvoice = self.coordinator.fetch_invoice_for_edit(inv_num)
        print(oInvoice)
        eif = EditInvoiceFrame(self.base_frame, oInvoice)

    def print_preview(self):
        inv_num = self.get_invoice_number()
        print_preview = GPFIS2HTML(inv_num)
        print_preview.build_HTML_invoice()

    def get_invoice_number(self):
        inv_num = str(self.inv_num_lbl.cget("text"))
        return inv_num.replace('Invoice #: ', '')
    
    def get_delivery_date(self):
        return self.delivery_date_lbl.cget("text")

    def get_customer_name(self):
        return self.buyer_name_lbl.cget("text")
    
    def get_shipto_name(self):
        return self.shipto_name_lbl.cget("text")

    def get_paid_status(self):
        return self.paid_status_var.get()

    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy()