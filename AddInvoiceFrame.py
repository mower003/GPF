import tkinter as tk
from CustomerSearchWidget import CustomerSearchWidget
from DateAndInvoiceNumberWidget import DateAndInvoiceNumberWidget
from InvoiceLinesWidget import InvoiceLinesWidget

class AddInvoiceFrame():

    #Static Settings
    #Controls the number and name of form elements
    invoice_compositional_elements = ['invoice Number: ', 'Name: ', 'Description: ', 'Price: ', 'Note: ', 'Case Style: ']
    #Color theme
    invoice_bg_color = '#FFFFFF'
    invoice_label_color = '#4E6C50'
    invoice_data_color = '#AA8B56'
    invoice_header_color = '#F0EBCE'
    #Fonts
    invoice_title_font = 'Haettenschweiler'
    invoice_header_font = 'Haettenschweiler'
    invoice_label_font = 'Haettenschweiler'
    invoice_data_font = 'MS Sans Serif'
    #Controls the title of the frame.
    frame_title = "Add invoice"

    def __init__(self, parent_frame):
        self.base_frame = parent_frame

    def setup_frame(self):
        self.invoice_header_frame = tk.Frame(self.base_frame, bg=self.invoice_bg_color, padx=5, pady=5)
        self.cust_widg_frame = CustomerSearchWidget(self.invoice_header_frame)
        self.date_and_invoice_widg = DateAndInvoiceNumberWidget(self.invoice_header_frame)
        self.invoice_header_frame.pack(side='top', fill='both')

        self.invoice_lines_frame = tk.Frame(self.base_frame, bg=self.invoice_bg_color, padx=5, pady=5)

        self.inv_lines_widget = InvoiceLinesWidget(self.invoice_lines_frame)

        self.footer_frame = tk.Frame(self.invoice_lines_frame, bg=self.invoice_bg_color, padx=5, pady=5)
        self.subtotal_lbl = tk.Label(self.footer_frame, text="Subtotal: ")
        self.total_lbl = tk.Label(self.footer_frame, text="Total: ")
        self.discount_lbl = tk.Label(self.footer_frame, text="Discount: ")
        self.save_btn = tk.Button(self.footer_frame, text="Save", padx=5, width=15, command=lambda: self.save_invoice())

        self.subtotal_display = tk.Entry(self.footer_frame, state='readonly')
        self.total_display = tk.Entry(self.footer_frame, state='readonly')
        self.discount_display = tk.Entry(self.footer_frame)
        self.discount_display.bind("<KeyRelease>", self.update_totals)

        self.invoice_lines_frame.pack(side='top', fill='both')

        #Build the customer search and populate functionality
        self.cust_widg_frame.build_frame()

        #Build the invoice number and date functionality
        self.date_and_invoice_widg.build_frame()

        #Build the invoice lines frame
        self.inv_lines_widget.build_frame()

        self.discount_lbl.grid(column=2, row=0, sticky='E')
        self.discount_display.grid(column=3, row=0, sticky='E')

        self.subtotal_lbl.grid(column=2, row=1, sticky='E')
        self.subtotal_display.grid(column=3, row=1, sticky='E')

        self.total_lbl.grid(column=2, row=2, sticky='E')
        self.total_display.grid(column=3, row=2, sticky='E')

        self.save_btn.grid(column=0, row=0,columnspan=2, sticky='W', padx=20)

        self.footer_frame.pack(side='top', fill='both')

        #self.invoice_lines_frame.pack(side='top', fill='both')

    def update_totals(self, e):
        try:

            typed = self.discount_display.get()
            print("from upd totals", typed)
            if typed == '':
                data = "0.00"
            else:
                subtotal = self.inv_lines_widget.get_all_line_totals()
                total = float(subtotal) - float(typed)

                #readonly entry boxes have to bet set to normal before you can update
                self.subtotal_display.configure(state='normal')
                self.total_display.configure(state='normal')

                self.subtotal_display.delete(0, tk.END)
                self.total_display.delete(0, tk.END)

                self.subtotal_display.insert(0, str(round(subtotal),2))
                self.total_display.insert(0, str(round(total),2))

                self.subtotal_display.configure(state='readonly')
                self.total_display.configure(state='readonly')
        except ValueError:
            print("Incorrect value used inside discount box.")
        except:
            print("Something has gone wrong calculating totals.")

    def save_invoice(self):
        current_customer = self.cust_widg_frame.get_selected_customer()
        date_list = self.date_and_invoice_widg.get_dates()
        current_inv_num = self.date_and_invoice_widg.get_invoice_number()
        line_items = self.inv_lines_widget.get_all_line_items()

        print("Invoice Number: ", current_inv_num)
        print("Customer: " + current_customer)
        print("Invoice Date: ", date_list[0])
        print("Delivery Date: ", date_list[1])
        print("Line Items: "+ "\n")
        print(line_items)

    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy()

    def build_frame(self):
        self.clear_display_frame()
        self.setup_frame()
        #self.create_customer_widget()