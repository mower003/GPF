import tkinter as tk

class ViewCustomerFrame():

    #Static Settings
    #Controls the number and name of form elements
    customer_compositional_elements = ['Customer Number ', 'Name ', 'Address ', 'City ', 'State ', 'Zip ']
    #Color theme
    customer_bg_color = '#395144'
    customer_label_color = '#4E6C50'
    customer_data_color = '#AA8B56'
    customer_header_color = '#F0EBCE'
    #Fonts
    customer_title_font = 'Haettenschweiler'
    customer_header_font = 'Haettenschweiler'
    customer_label_font = 'Haettenschweiler'
    customer_data_font = 'MS Sans Serif'
    #Controls the title of the frame.
    frame_title = "Green Paradise Farms - Customer List"

    def __init__(self, parent_frame):
        self.base_frame = parent_frame
        self.lbl_list = []
        self.delete_btn_list = []
        self.view_btn_list = []
        #self.my_frame = tk.Frame(parent_frame, bd=2, bg='grey')
        #self.my_frame.pack(side="top", fill="both", expand=True)

    def set_up_frame(self):
        self.my_frame = tk.Frame(self.base_frame, bd=2, bg=self.customer_bg_color)
        
    def create_view_form(self, form_rows):
        row = 1
        col = 0
        for headers in self.customer_compositional_elements:
            lbl = tk.Label(self.my_frame, text = headers, font=(self.customer_header_font,20), bg=self.customer_header_color)
            lbl.grid(row = row, column = col, sticky = "W,E")
            self.my_frame.grid_columnconfigure(col, weight=1)
            col += 1
        
        row = 2
        col = 0
        index = 0
        for element in form_rows:
            for item in element:
                lbl = tk.Label(self.my_frame, text = item, borderwidth=2, relief="solid", font=(self.customer_data_font, 12), bg=self.customer_data_color)
                lbl.grid(row = row, column = col, sticky = "W,E")
                self.lbl_list.append(lbl)
                col += 1
            view_btn = tk.Button(self.my_frame, text="Edit", padx=5, bg=self.customer_data_color)
            delete_btn = tk.Button(self.my_frame, text="Delete", padx=5)
            view_btn.grid(row=row, column=col+1)
            #delete_btn.grid(row=row, column=col+2)
            self.view_btn_list.append(view_btn)
            self.delete_btn_list.append(delete_btn)
            row += 1
            col = 0
            index += 1
        
        self.my_frame.pack(side="top", fill="both", expand=True)

    def add_title_label(self):
        self.title = tk.Label(self.my_frame, text=self.frame_title)
        self.title.config(font=(self.customer_title_font,38),bg=self.customer_label_color)
        self.title.grid(row=0, column = 0, columnspan=len(self.customer_compositional_elements)+2, ipady=5, pady=5, sticky="E,W")

    def build_frame(self):
        self.clear_display_frame()
        self.set_up_frame()
        self.add_title_label()
        #A call to a class that fetches customer data should be put here
        #the returned result should be passed into create_view_form as a list of tuples IIRC
        form_rows = [(77, ' Times', '89 w', 'LA', 'CA', 92009)]
        self.create_view_form(form_rows)

    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy()
