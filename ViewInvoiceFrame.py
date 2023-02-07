import tkinter as tk
from tkinter import font

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

    def create_invoice_view(self):
        #View will automatically get the most recent 100 invoices.
        #If invoices beyond that are required user will have to use the search function
        #Search can only be done by date or customer.
        # If search is done by customer then it will limit to most recent 100. 
        # Paid/Unpaid checkbox will be located here and will automatically update the db when state is changed.
        #
        pass

    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy()

    def build_frame(self):
        self.clear_display_frame()
        self.setup_frame()
        #self.create_customer_widget()