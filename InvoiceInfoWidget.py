import tkinter as tk

class InvoiceInfoWidget():
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
    frame_title = "Invoice Info Widget"

    def __init__(self, parent_frame):
        self.base_frame = parent_frame
        self.info_frame = tk.Frame(self.base_frame, padx=15, pady=10, bg=self.bg_color, highlightbackground='black', highlightthickness=2)

    def create_ui_elements(self):
        self.ship_date_lbl = tk.Label(self.info_frame, text="Ship Date", bg=self.label_color, font=(self.label_font, 12, 'bold'))
        self.payment_terms_lbl = tk.Label(self.info_frame, text="Payment Terms", bg=self.label_color, font=(self.label_font, 12, 'bold'))
        self.due_date_lbl = tk.Label(self.info_frame, text="Due Date", bg=self.label_color, font=(self.label_font, 12, 'bold'))
        self.customer_po_lbl = tk.Label(self.info_frame, text="Customer PO", bg=self.label_color, font=(self.label_font, 12, 'bold'))
        self.applied_credit_amount_lbl = tk.Label(self.info_frame, text="Credit Total", bg=self.label_color, font=(self.label_font, 12, 'bold'))
        self.credit_invoice_num_lbl = tk.Label(self.info_frame, text="Credit Invoice Number", bg=self.label_color, font=(self.label_font, 12, 'bold'))
        self.note_lbl = tk.Label(self.info_frame, text="Notes", bg=self.label_color, font=(self.label_font, 12, 'bold'))

        self.ship_date = tk.Entry(self.info_frame, bg=self.data_color, font=(self.data_font, 12, 'bold'))
        self.due_date = tk.Entry(self.info_frame, bg=self.data_color, font=(self.data_font, 12, 'bold'))
        self.payment_terms = tk.Entry(self.info_frame, bg=self.data_color, font=(self.data_font, 12, 'bold'))
        self.customer_po = tk.Entry(self.info_frame, bg=self.data_color, font=(self.data_font, 12, 'bold'))
        self.applied_credit_amount = tk.Entry(self.info_frame, bg=self.data_color, font=(self.data_font, 12, 'bold'))
        self.credit_invoice_num = tk.Entry(self.info_frame, bg=self.data_color, font=(self.data_font, 12, 'bold'))
        self.note = tk.Entry(self.info_frame, bg=self.data_color, font=(self.data_font, 12, 'bold'))

    def place_ui_elements(self):
        self.ship_date_lbl.grid(row = 0, column = 0, sticky='we')
        self.payment_terms_lbl.grid(row = 0, column = 1, sticky='we')
        self.due_date_lbl.grid(row = 0, column = 2, sticky='we')

        self.customer_po_lbl.grid(row = 2, column = 0, sticky='we')
        self.applied_credit_amount_lbl.grid(row = 2, column = 1, sticky='we')
        self.credit_invoice_num_lbl.grid(row = 2, column = 2, sticky='we')
        self.note_lbl.grid(row = 2, column = 3, sticky='we')

        self.ship_date.grid(row = 1, column = 0, sticky='we')
        self.due_date.grid(row = 1, column = 1, sticky='we')
        self.payment_terms.grid(row = 1, column = 2, sticky='we')

        self.customer_po.grid(row = 3, column = 0, sticky='we')
        self.applied_credit_amount.grid(row = 3, column = 1, sticky='we')
        self.credit_invoice_num.grid(row = 3, column = 2, sticky='we')
        self.note.grid(row = 3, column = 3, sticky='we')

    def configure_elements(self):
        self.info_frame.grid_columnconfigure((0,1,2,3), weight=1, uniform='column')

    def build_frame(self):
        self.create_ui_elements()
        self.configure_elements()
        self.place_ui_elements()

    def clear_display_frame(self):
        for children in self.info_frame.winfo_children():
            children.destroy()


    

    
