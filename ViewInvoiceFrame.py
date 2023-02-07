import tkinter as tk
from tkinter import font

from ViewInvoiceSummaryWidget import ViewInvoiceSummaryWidget

class ViewInvoiceFrame():


    #Static Settings
    #Color theme
    bg_color = '#FFFFFF'
    label_color = '#4E6C50'
    data_color = '#AA8B56'
    header_color = '#F0EBCE'
    #Fonts
    title_font = 'Haettenschweiler'
    header_font = 'Haettenschweiler'
    label_font = 'Haettenschweiler'
    data_font = 'MS Sans Serif'
    #Controls the title of the frame.
    frame_title = "View Invoices Frame"

    def __init__(self, parent_frame):
        self.base_frame = parent_frame

    def setup_frame(self):
        self.invoice_view_frame = tk.Frame(self.base_frame, bg = self.bg_color)
        self.invoice_view_frame.pack(side='top', expand=1, fill='both')

    def create_invoice_view(self):
        placeholder_data_list = [[1234, "Times Distributing", 12345.67],[1234, "Times Distributing", 12345.67],[1234, "Times Distributing", 12345.67],[1234, "Times Distributing", 12345.67],[1234, "Times Distributing", 12345.67]]
        #View will automatically get the most recent 50 invoices. (maybe?)
        #If invoices beyond that are required user will have to use the search function
        #Search can only be done by date or customer and combo of paid/unpaid.
        # If search is done by customer then it will limit to most recent 50. 
        # Paid/Unpaid checkbox will be located here and will automatically update the db when state is changed.
        # | Invoice Number | Customer Name | Invoice Total | Paid/Unpaid [ ] | Button[Edit] |
        max_widgets = 5
        for i in range(max_widgets):
            visw = ViewInvoiceSummaryWidget(self.invoice_view_frame)
            visw.set_widget_values(placeholder_data_list[i][0],placeholder_data_list[i][1],placeholder_data_list[i][2])
            visw.setup_frame()

    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy()

    def build_frame(self):
        self.clear_display_frame()
        self.setup_frame()
        self.create_invoice_view()