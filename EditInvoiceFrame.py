import tkinter as tk
from sqlite3 import Error


from CustomerSearchWidget import CustomerSearchWidget
from DateAndInvoiceNumberWidget import DateAndInvoiceNumberWidget
from InvoiceLinesWidget import InvoiceLinesWidget
from Invoice import InvoiceObj
from GPFISCoordinator import GPFISCoordinator
from ErrorPopUpWindow import ErrorPopUpWindow

class EditInvoiceFrame():
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
    frame_title = "Edit invoice"

    def __init__(self, parent_frame, invObject):
        self.base_frame = tk.Toplevel()
        self.oInvoice = invObject
        self.coordinator = GPFISCoordinator()
        self.errorPrompt = ErrorPopUpWindow(parent_frame)
        self.setup_frame()

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

        self.subtotal_display = tk.Entry(self.footer_frame)
        self.total_display = tk.Entry(self.footer_frame)
        self.discount_display = tk.Entry(self.footer_frame)
        self.discount_display.bind("<KeyRelease>", self.update_totals)

        self.discount_display.insert(0, self.oInvoice.get_discount_rate())
        self.subtotal_display.insert(0, self.oInvoice.get_subtotal())
        self.total_display.insert(0, self.oInvoice.get_total())

        self.subtotal_display.config(state='readonly')
        self.total_display.config(state='readonly')

        self.invoice_lines_frame.pack(side='top', fill='both')

        #Build the customer search and populate functionality
        self.cust_widg_frame.build_frame()
        self.cust_widg_frame.set_customer(self.oInvoice.get_buyer_name())

        #Build the invoice number and date functionality
        self.date_and_invoice_widg.build_frame()
        self.date_and_invoice_widg.set_invoice_number(self.oInvoice.get_inv_num())

        #Build the invoice lines frame
        self.inv_lines_widget.build_frame()
        self.inv_lines_widget.populate_lines(self.oInvoice)

        self.discount_lbl.grid(column=2, row=0, sticky='E')
        self.discount_display.grid(column=3, row=0, sticky='E')

        self.subtotal_lbl.grid(column=2, row=1, sticky='E')
        self.subtotal_display.grid(column=3, row=1, sticky='E')

        self.total_lbl.grid(column=2, row=2, sticky='E')
        self.total_display.grid(column=3, row=2, sticky='E')

        self.save_btn.grid(column=0, row=0,columnspan=2, sticky='W', padx=20)

        self.footer_frame.pack(side='top', fill='both')

    def update_totals(self, e):
        try:
            typed = self.discount_display.get()
            print("from upd totals", typed)
            if typed == '':
                data = "0.00"
            else:
                subtotal = self.inv_lines_widget.get_all_line_totals()
                print(subtotal)
                total = float(subtotal) - float(typed)

                #readonly entry boxes have to bet set to normal before you can update
                self.subtotal_display.configure(state='normal')
                self.total_display.configure(state='normal')

                self.subtotal_display.delete(0, tk.END)
                self.total_display.delete(0, tk.END)
                subtotal = round(subtotal,2)
                self.subtotal_display.insert(0, str(round(subtotal,2)))
                self.total_display.insert(0, str(round(total,2)))

                self.subtotal_display.configure(state='readonly')
                self.total_display.configure(state='readonly')
        except ValueError as e:
            print("Incorrect value used inside discount box.", e)
            self.errorPrompt.create_error_window(e)
        except Error as e:
            print("Something has gone wrong calculating totals.", e)
            self.errorPrompt.create_error_window(e)

    def save_invoice(self):
        try:
            current_inv_num = self.date_and_invoice_widg.get_invoice_number()
            current_customer = self.cust_widg_frame.get_selected_customer()
            inv_date = self.date_and_invoice_widg.get_invoice_date()
            del_date = self.date_and_invoice_widg.get_delivery_date()
            #date_list = self.date_and_invoice_widg.get_dates()
            inv_note = ''
            issuer_id = int(37)
            customer_id = self.coordinator.get_entity_id_by_name(current_customer, exactMatch=True)
            inv_status = 0
            inv_discount = round(float(self.discount_display.get()),2)
            tax_amount = 0
            subtotal = round(float(self.subtotal_display.get()),2)
            total = round(float(self.total_display.get()),2)
            credit_inv_num = 0
            line_items = self.inv_lines_widget.get_all_line_items()
            #line_items.insert(0, current_inv_num)

            the_invoice = InvoiceObj(int(current_inv_num), creation_date=inv_date, delivery_date=del_date, 
            note=inv_note, issuer_id=issuer_id, buyer_id=customer_id, status=inv_status, discount_rate=inv_discount, 
            tax_amount=tax_amount, subtotal=subtotal, total=total, credit_inv_num=credit_inv_num)

            for lines in line_items:
                lines.insert(1, current_inv_num)
                print(lines)
                the_invoice.addInvoiceItem(invItemAsList=lines)

            #print("From AddInvoiceFrame:save_invoice() InvoiceObj",the_invoice.asListForDBInsertion())
            #print("From AddInvoiceFrame:save_invoice() InvoiceItemObj", the_invoice.toList())

            self.coordinator.update_invoice(InvoiceObj=the_invoice)
        except Error as e:
            print("Error occurred during invoice insertion.", e)
            self.errorPrompt.create_error_window(e)
        finally:
            self.clear_display_frame()
            self.close_window()

    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy()

    def close_window(self):
        self.base_frame.update()
        self.base_frame.destroy()

    def build_frame(self):
        self.clear_display_frame()
        self.setup_frame()
        #self.create_customer_widget()
