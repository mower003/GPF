import tkinter as tk
from InvoiceLineItemWidget import InvoiceLineItemWidget

class InvoiceLinesWidget():
    #Static Settings
    invoice_line_compositional_elements = ['Quantity', 'Cases', 'Item Num', 'Description', 'Note', 'Price', 'Total']
    #Color theme
    #bg_color = '#395144'
    bg_color = '#FFFFFF'
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
        self.lbl_list = []
        self.line_item_list = []

    def setup_frame(self):
        self.lines_frame = tk.Frame(self.base_frame, bg=self.bg_color, padx=45)
        self.lines_frame.grid_columnconfigure((0,1,2,3,4,5,6), weight=1, uniform='column')
        self.lines_frame.grid_rowconfigure((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15), weight=1, uniform='row')

    def create_column_headers(self):
        row = 0
        col = 0
        for element in self.invoice_line_compositional_elements:
            lbl = tk.Label(self.lines_frame, text= element,font=(self.data_font, 12, 'bold'), bg=self.header_color)
            #entry = tk.Entry(self.lines_frame, width=40, font=(self.data_font, 12))
            lbl.grid(row=row, column=col, sticky="E,W")
            #entry.grid(row = row, column=col+1, sticky="E,W")
            self.lbl_list.append(lbl)
            #self.entry_list.append(entry)
            col += 1
        self.lines_frame.pack(side="top", fill="both", expand=True)

    def create_lines(self, max_lines=20):

        line1 = InvoiceLineItemWidget(self.lines_frame)
        line1.place_line_item(1)
        self.line_item_list.append(line1)

        line2 = InvoiceLineItemWidget(self.lines_frame)
        line2.place_line_item(2)
        self.line_item_list.append(line2)

        line3 = InvoiceLineItemWidget(self.lines_frame)
        line3.place_line_item(3)
        self.line_item_list.append(line3)

        line4 = InvoiceLineItemWidget(self.lines_frame)
        line4.place_line_item(4)
        self.line_item_list.append(line4)

        line5 = InvoiceLineItemWidget(self.lines_frame)
        line5.place_line_item(5)
        self.line_item_list.append(line5)

        line6 = InvoiceLineItemWidget(self.lines_frame)
        line6.place_line_item(6)
        self.line_item_list.append(line6)

        line7 = InvoiceLineItemWidget(self.lines_frame)
        line7.place_line_item(7)
        self.line_item_list.append(line7)

        line8 = InvoiceLineItemWidget(self.lines_frame)
        line8.place_line_item(8)
        self.line_item_list.append(line8)

        line9 = InvoiceLineItemWidget(self.lines_frame)
        line9.place_line_item(9)
        self.line_item_list.append(line9)

        line10 = InvoiceLineItemWidget(self.lines_frame)
        line10.place_line_item(10)
        self.line_item_list.append(line10)

        line11 = InvoiceLineItemWidget(self.lines_frame)
        line11.place_line_item(11)
        self.line_item_list.append(line11)

        line12 = InvoiceLineItemWidget(self.lines_frame)
        line12.place_line_item(12)
        self.line_item_list.append(line12)

        line13 = InvoiceLineItemWidget(self.lines_frame)
        line13.place_line_item(13)
        self.line_item_list.append(line13)

        line14 = InvoiceLineItemWidget(self.lines_frame)
        line14.place_line_item(14)
        self.line_item_list.append(line14)

        line15 = InvoiceLineItemWidget(self.lines_frame)
        line15.place_line_item(15)
        self.line_item_list.append(line15)

        #line16 = InvoiceLineItemWidget(self.lines_frame)
        #line16.place_line_item(16)

        #line17 = InvoiceLineItemWidget(self.lines_frame)
        #line17.place_line_item(17)

        #line18 = InvoiceLineItemWidget(self.lines_frame)
        #line18.place_line_item(18)

        #line19 = InvoiceLineItemWidget(self.lines_frame)
        #line19.place_line_item(19)

        #line20 = InvoiceLineItemWidget(self.lines_frame)
        #line20.place_line_item(20)

    def get_all_line_items(self):
        line_items = []
        print("wholelist ", self.line_item_list)
        for lines in self.line_item_list:
            line = lines.get_line_elements_as_list()
            if line[0] == '' or line[0] == ' ':
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

    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy()

    def build_frame(self):
        self.setup_frame()
        self.create_column_headers()
        self.create_lines()
