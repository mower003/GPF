import tkinter as tk

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
        self.invoice_summary_frame = tk.Frame(self.base_frame, bg=self.bg_color)
        self.invoice_summary_frame.pack(side='top', fill='x', expand=1)

        self.invoice_summary_frame.grid_columnconfigure((0,1,2,3,4), weight=1, uniform='column')
        self.paid_status_var = tk.BooleanVar()

        self.inv_num_lbl = tk.Label(self.invoice_summary_frame, text="Null", bg=self.data_color, font=(self.data_font, 12), borderwidth=1, relief='solid')
        self.customer_name_lbl = tk.Label(self.invoice_summary_frame, text="Null", bg=self.data_color, font=(self.data_font, 12), borderwidth=1, relief='solid')
        self.invoice_total = tk.Label(self.invoice_summary_frame, text="Null", bg=self.data_color, font=(self.data_font, 12), borderwidth=1, relief='solid')
        self.paid_checkbox = tk.Checkbutton(self.invoice_summary_frame, text="Paid", variable=self.paid_status_var, command=lambda: self.update_paid_status(), borderwidth=1, relief='solid')
        self.edit_invoice_btn = tk.Button(self.invoice_summary_frame, text="Edit", bg=self.data_color, command=lambda: self.edit_invoice_window(), borderwidth=1, relief='solid')

    def setup_frame(self):
        self.inv_num_lbl.grid(column=0, row=0, sticky='E,W')
        self.customer_name_lbl.grid(column=1, row=0, sticky='E,W')
        self.invoice_total.grid(column=2, row=0, sticky='E,W')
        self.paid_checkbox.grid(column=3, row=0, sticky='E,W')
        self.edit_invoice_btn.grid(column=4, row=0, sticky='E,W')

    def set_widget_values(self, inv_num, customer_name, invoice_total, paid_status=0):
        self.inv_num_lbl.config(text=inv_num)
        self.customer_name_lbl.config(text=customer_name)
        self.invoice_total.config(text=invoice_total)
        self.paid_status_var.set(paid_status)
        
    def update_paid_status(self):
        print("Paid status changed to: ", self.paid_status_var.get())

    def edit_invoice_window(self):
        top = tk.Toplevel(self.base_frame)
        print(self.get_invoice_number())
        print("Spawn a toplevel window here")
        top.mainloop()

    def get_invoice_number(self):
        return self.inv_num_lbl.cget("text")

    def get_customer_name(self):
        return self.customer_name_lbl.cget("text")

    def get_paid_status(self):
        return self.paid_status_var.get()

    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy()