import tkinter as tk
from InvoiceLineItemWidget import InvoiceLineItemWidget
from InvoiceItem import InvoiceItemObj
from GPFISCoordinator import GPFISCoordinator

class InvoiceLinesWidget():
    #Static Settings
    invoice_line_compositional_elements = ['Quantity', 'Cases', 'Item Num', 'Description', 'Note', 'Price', 'Total']
    #Color theme
    #bg_color = '#395144'
    bg_color = '#cccccc'
    #bg_color = '#E5E4E2'
    label_color = '#4E6C50'
    data_color = '#AA8B56'
    header_color = '#F0EBCE'
    #Fonts
    title_font = 'Haettenschweiler'
    header_font = 'Haettenschweiler'
    label_font = 'MS Sans Serif'
    data_font = 'MS Sans Serif'
    #Controls the title of the frame.
    frame_title = "Invoice Lines Widget"

    def __init__(self, parent_frame):
        self.base_frame = parent_frame
        self.productObjList = []
        self.line_item_list = []
        self.coordinator = GPFISCoordinator()
        self.cache_product_data()

    def setup_frame(self):
        self.lines_frame = tk.Frame(self.base_frame, bg=self.bg_color, padx=45)
        self.lines_frame.grid_columnconfigure((0,1,2,3,4,5,6), weight=1, uniform='column')
        self.lines_frame.grid_rowconfigure((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15), weight=1, uniform='row')

    def get_frame_height(self):
        return self.lines_frame.winfo_height()

    def create_column_headers(self):
        row = 0
        col = 0
        for element in self.invoice_line_compositional_elements:
            lbl = tk.Label(self.lines_frame, text= element,font=(self.data_font, 12, 'bold'), bg=self.header_color)
            lbl.grid(row=row, column=col, sticky="E,W")
            col += 1
        self.lines_frame.pack(side="top", fill="both", expand=True)

    def cache_product_data(self):
        self.productObjList = self.coordinator.get_products()

        #print("####From InvoiceLinesWidget####")
        #print("#####Caching Product Data#####")
        #for obs in self.productObjList:
        #    print(obs.asList())

    def create_lines(self, max_lines=20):

        for i in range(1, max_lines+1):
            line = InvoiceLineItemWidget(self.lines_frame)
            line.place_line_item(i)
            line.set_invoice_object(self.oInvoice)
            line.set_footer_vars(self.subtotvar, self.totvar, self.discvar)
            self.line_item_list.append(line)

        for lines in self.line_item_list:
            lines.setProductData(self.productObjList)

        for lines in self.line_item_list:
            peb = lines.get_price_entry_box()
            qeb = lines.get_quantity_entry_box()
            preb = lines.get_product_entry_box()
            #print(type(peb))
            peb.bind("<FocusOut>", self.recalculation_wrapper)
            qeb.bind("<FocusOut>", self.recalculation_wrapper)
            preb.bind("<FocusOut>", self.recalculation_wrapper)

    def populate_lines(self, invObj):
        invoice_item_list = invObj.getInvoiceItemList()
        index = 0
        for lines in invoice_item_list:
            self.line_item_list[index].set_line_item_attributes(lines.asUpdateList())
            index += 1

    def set_footer_vars(self, subvar, totvar, discvar):
        self.subtotvar = subvar
        self.totvar = totvar
        self.discvar = discvar

    def set_applied_credit_var(self, app_cred):
        self.applied_credit_var = app_cred

    def set_invoice_object(self, invObject):
        self.oInvoice = invObject

    def get_all_line_items(self):
        line_items = []
        print("wholelist ", self.line_item_list)
        for lines in self.line_item_list:
            line = lines.get_line_elements_as_list()
            print("A LINE ITEM", line)
            #Check for lines that have not had data added to them.
            if (line is None) or (line[0] == '') or (line[0] == ' '):
                continue
            else:
                print("from getalllineitems ",line)
                line_items.append(line)
        return line_items

    def get_all_line_totals(self):
        inv_subtotal = 0
        for lines in self.line_item_list:
            if lines.get_line_total() == '':
                continue
            else:
                inv_subtotal += round(float(lines.get_line_total()), 2)
        return inv_subtotal

    def recalculation_wrapper(self, event=None):
        self.update_line_totals()
        self.update_subtotal()
        self.update_total()
        self.update_applied_credit_var()

    def update_line_totals(self, ):
        for lines in self.line_item_list:
            lines.recalculate_line_total()

    def update_subtotal(self):
        inv_subtotal = 0
        for lines in self.line_item_list:
            if lines.get_line_total() == '':
                continue
            else:
                inv_subtotal += round(float(lines.get_line_total()), 2)

        self.subtotvar.set(inv_subtotal)

    def update_applied_credit_var(self):
        applied_credit = 0
        for lines in self.line_item_list:
            if '-' in str(lines.get_line_total()):
                applied_credit += round(float(lines.get_line_total()), 2)

        self.applied_credit_var.set(applied_credit)


    def update_total(self):
        self.totvar.set(self.subtotvar.get() - self.discvar.get())

    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy()

    def build_frame(self):
        self.setup_frame()
        self.create_column_headers()
        self.create_lines()
