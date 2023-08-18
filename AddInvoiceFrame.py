import tkinter as tk
from sqlite3 import Error

from CustomerSearchWidget import CustomerSearchWidget
from DateAndInvoiceNumberWidget import DateAndInvoiceNumberWidget
from InvoiceLinesWidget import InvoiceLinesWidget
from InvoiceInfoWidget import InvoiceInfoWidget
from Invoice import InvoiceObj
from Entity import EntityObj
from GPFISCoordinator import GPFISCoordinator
from ErrorPopUpWindow import ErrorPopUpWindow

class AddInvoiceFrame():

    #Static Settings
    #Controls the number and name of form elements
    invoice_compositional_elements = ['invoice Number: ', 'Name: ', 'Description: ', 'Price: ', 'Note: ', 'Case Style: ']
    #Color theme
    invoice_bg_color = '#cccccc'
    invoice_label_color = '#cccccc'
    invoice_data_color = '#AA8B56'
    invoice_header_color = '#F0EBCE'
    #Fonts
    invoice_title_font = 'Haettenschweiler'
    invoice_header_font = 'Haettenschweiler'
    invoice_label_font = 'Haettenschweiler'
    invoice_data_font = 'MS Sans Serif'
    #Controls the title of the frame.
    frame_title = "Add invoice"

    def __init__(self, parent_frame, canvas):
        self.base_frame = parent_frame
        self.canvas = canvas
        self.coordinator = GPFISCoordinator()
        self.errorPrompt = ErrorPopUpWindow(parent_frame)
        self.entityList = self.cache_entity_data()
        self.oInvoice = InvoiceObj()

    def setup_frame(self):
        subtotvar = tk.DoubleVar(0.00)
        totvar = tk.DoubleVar(0.00)
        discvar = tk.DoubleVar(0.00)

        self.invoice_header_frame = tk.Frame(self.base_frame, bg=self.invoice_bg_color, padx=5, pady=5)

        self.billto_frame = CustomerSearchWidget(self.invoice_header_frame)
        self.billto_frame.set_top_label("Bill To:")
        self.billto_frame.set_entity_list(self.entityList)
        self.billto_frame.set_invoice_object(self.oInvoice)

        self.shipto_frame = CustomerSearchWidget(self.invoice_header_frame)
        self.shipto_frame.set_top_label("Ship To:")
        self.shipto_frame.set_entity_list(self.entityList)
        self.shipto_frame.set_invoice_object(self.oInvoice)
    
        self.date_and_invoice_widg = DateAndInvoiceNumberWidget(self.invoice_header_frame)
        self.date_and_invoice_widg.set_invoice_object(self.oInvoice)

        self.invoice_header_frame.pack(side='top', fill='both')

        self.invoice_info_frame = InvoiceInfoWidget(self.base_frame)
        self.invoice_info_frame.build_frame()
        self.invoice_info_frame.info_frame.pack(side='top', fill='both')
        self.invoice_info_frame.payment_terms.bind("<<ComboboxSelected>>", self.payment_terms_event)
        applied_credit = self.invoice_info_frame.get_applied_credit_var()

        self.invoice_lines_frame = tk.Frame(self.base_frame, bg=self.invoice_bg_color, padx=5, pady=5)

        self.inv_lines_widget = InvoiceLinesWidget(self.invoice_lines_frame)
        self.inv_lines_widget.set_invoice_object(self.oInvoice)
        self.inv_lines_widget.set_footer_vars(subtotvar, totvar, discvar)
        self.inv_lines_widget.set_applied_credit_var(applied_credit)

        self.footer_frame = tk.Frame(self.invoice_lines_frame, bg=self.invoice_bg_color, padx=5, pady=5)
        self.subtotal_lbl = tk.Label(self.footer_frame, bg=self.invoice_bg_color, text="Subtotal: ")
        self.total_lbl = tk.Label(self.footer_frame, bg=self.invoice_bg_color,text="Total: ")
        self.discount_lbl = tk.Label(self.footer_frame, bg=self.invoice_bg_color,text="Discount: ")
        self.save_btn = tk.Button(self.footer_frame, text="Save", padx=5, width=15, command=lambda: self.save_invoice())


        self.subtotal_display = tk.Entry(self.footer_frame, state='readonly', textvariable=subtotvar)
        self.total_display = tk.Entry(self.footer_frame, state='readonly', textvariable=totvar)
        self.discount_display = tk.Entry(self.footer_frame, textvariable=discvar)
        self.discount_display.bind("<KeyRelease>", self.update_totals)

        self.invoice_lines_frame.pack(side='top', fill='both')

        self.billto_frame.build_frame()
        self.shipto_frame.build_frame()

        self.billto_frame.set_grid_position(row=0, col=0)
        self.shipto_frame.set_grid_position(row=0, col=1)

        #Build the invoice number and date functionality
        self.date_and_invoice_widg.build_frame()
        #Get new Invoice Number
        self.date_and_invoice_widg.set_invoice_number(self.coordinator.get_next_invoice())

        self.invoice_info_frame.set_due_date(self.date_and_invoice_widg.get_due_date())

        #Build the invoice lines frame
        self.inv_lines_widget.build_frame()

        self.discount_lbl.grid(column=2, row=0, sticky='E')
        self.discount_display.grid(column=3, row=0, sticky='E')

        self.subtotal_lbl.grid(column=2, row=1, sticky='E')
        self.subtotal_display.grid(column=3, row=1, sticky='E')

        self.total_lbl.grid(column=2, row=2, sticky='E')
        self.total_display.grid(column=3, row=2, sticky='E')

        self.save_btn.grid(column=0, row=0,columnspan=2, sticky='W', padx=20)

        self.footer_frame.pack(side='top', fill='both', expand=True)

        #Canvas holding scroll bar needs to be resized to fit line items.
        screen_width = self.base_frame.winfo_screenwidth()
        screen_height = self.base_frame.winfo_screenheight()

        header_height = self.invoice_header_frame.winfo_height()
        info_height = self.invoice_info_frame.info_frame.winfo_height()
        lines_height = self.base_frame.winfo_height()
        footer_height = self.footer_frame.winfo_height()
        total_height = screen_height + header_height + info_height + lines_height + footer_height

        self.canvas.itemconfig("baseFrame_2", height=total_height, width=screen_width)

        #self.invoice_lines_frame.pack(side='top', fill='both')

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
            oInvoice = InvoiceObj()
            oInvoice.set_inv_num(self.date_and_invoice_widg.get_invoice_number())
            #Set billto details
            oInvoice.set_buyer(self.billto_frame.get_selected_entity_obj())

            #Set shipto details
            if self.shipto_frame.get_selected_entity_obj() is None:
                oInvoice.set_shipto(self.billto_frame.get_selected_entity_obj())
            else:
                oInvoice.set_shipto(self.shipto_frame.get_selected_entity_obj())

            print(self.date_and_invoice_widg.get_invoice_date())
            print(self.date_and_invoice_widg.get_delivery_date())
            oInvoice.set_invoice_date(self.date_and_invoice_widg.get_invoice_date())
            oInvoice.set_ship_date(self.date_and_invoice_widg.get_delivery_date())

            #Set the ansillary details
            oInvoice.set_payment_terms(self.invoice_info_frame.get_payment_terms())
            oInvoice.set_due_date(self.invoice_info_frame.get_due_date())
            oInvoice.set_po_number(self.invoice_info_frame.get_customer_po())
            oInvoice.set_applied_credit_amount(self.invoice_info_frame.get_applied_credit_amount())
            oInvoice.set_credit_invoice_number(self.invoice_info_frame.get_credit_invoice_num())
            oInvoice.set_note(self.invoice_info_frame.get_note())

            print(self.invoice_info_frame.get_payment_terms())
            print(self.invoice_info_frame.get_customer_po())


            oIssuer = EntityObj(37, 'Green Paradise Farms', '2555', 'Guajome Lake Road', 'Vista', 'CA', '92084', 'USA', 1)
            oInvoice.set_issuer(oIssuer)

            oInvoice.set_status(0)

            oInvoice.set_discount_amount(self.discount_display.get())
            oInvoice.set_subtotal(self.subtotal_display.get())
            oInvoice.set_total(self.total_display.get())

            oInvoice.set_sales_tax(0)

            line_items = self.inv_lines_widget.get_all_line_items()
            #line_items.insert(0, current_inv_num)

            for lines in line_items:
                lines.insert(1, oInvoice.get_inv_num())
                print(lines)
                oInvoice.addInvoiceItem(invItemAsList=lines)

            print("From AddInvoiceFrame:save_invoice() InvoiceObj",oInvoice.asListForDBInsertion())
            print("From AddInvoiceFrame:save_invoice() InvoiceItemObj", oInvoice.toList())

            self.coordinator.add_invoice(InvoiceObj=oInvoice)
            self.coordinator.insert_invoice_items(InvoiceObj=oInvoice)
        except Error as e:
            print("Error occurred during invoice insertion.", e)
            self.errorPrompt.create_error_window(e)
        finally:
            self.clear_display_frame()

    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy()

    def payment_terms_event(self, e):
        selected = self.invoice_info_frame.get_payment_terms()
        num = selected.split(' ')
        num = num[1]    
        self.invoice_info_frame.calculate_due_date(self.date_and_invoice_widg.get_delivery_date(), num)

    def cache_entity_data(self):
        data = self.coordinator.get_entities_simple()
        return data

    def build_frame(self):
        self.clear_display_frame()
        self.setup_frame()
        #self.create_customer_widget()