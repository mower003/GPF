import tkinter as tk
from GPFISCoordinator import GPFISCoordinator

class CustomerSearchWidget():

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
    frame_title = "Customer Search Widget"

    def __init__(self, parent_frame):
        self.base_frame = parent_frame
        self.current_customer = ""
        self.customer_dict = {"Times Distributing":"989 W Broadway, Los Angeles CA, 92001",
                        "Nagatoshi Distributing":"990 W Broadyway, Los Angeles CA, 92001",
                        "DM Distributing":"990 W Broadyway, Los Angeles CA, 92001",
                        "Saiya Distributing":"990 W Broadyway, Los Angeles CA, 92001",
                        "Yamataka Distributing":"990 W Broadyway, Los Angeles CA, 92001"}
        self.customer_info = list(self.customer_dict.keys())

    def setup_frame(self):
        self.customer_frame = tk.Frame(self.base_frame, bg=self.bg_color, padx=20, pady=20)
        self.customer_listbox = tk.Listbox(self.customer_frame, height=3, width=40, font=(self.data_font, 13))
        self.customer_display_label = tk.Label(self.customer_frame, text="", width=34, font=(self.data_font, 15))

    def create_customer_widget(self):
        self.customer_search_lbl = tk.Label(self.customer_frame, text="Customer Search...", font=(self.data_font, 12, 'bold'), bg=self.bg_color)
        self.customer_search_lbl.pack(side="top", anchor='nw')

        self.customer_search_entrybox = tk.Entry(self.customer_frame, width=40)
        self.customer_search_entrybox.pack(side="top", anchor='nw')
        self.customer_search_entrybox.bind("<KeyRelease>",self.monitor_search_box)

        #self.customer_listbox = tk.Listbox(self.customer_frame, height=3, width=40)
        self.customer_listbox.pack(side="top", anchor='nw', pady=5)
        self.customer_listbox.bind("<<ListboxSelect>>", self.populate_customer_label)

        #self.customer_display_label = tk.Label(self.customer_frame, text="")
        self.customer_display_label.pack(side="top", anchor='nw')

        self.customer_frame.pack(side='left', anchor='nw')

        self.update_customer_listbox(self.customer_info)

    def monitor_search_box(self, e):
        typed = self.customer_search_entrybox.get()
        #print(typed)
        if typed == '':
            data = self.customer_info
        else:
            data = []
            for customer in self.customer_info:
                #print("TL: "+ typed.lower() + "CL: "+ customer.lower())
                if typed.lower() in customer.lower():
                    data.append(customer)

        self.update_customer_listbox(data)

    def populate_customer_label(self, e):
        self.customer_display_label.config(text=" ")

        print(str(self.customer_listbox.get(tk.ACTIVE)), e)
        selected_listbox_customer = str(self.customer_listbox.get(tk.ACTIVE))
        self.current_customer = selected_listbox_customer
        full_customer_info = selected_listbox_customer + "\n" + self.customer_dict.get(selected_listbox_customer)
        
        self.customer_display_label.config(text=full_customer_info)

    def update_customer_listbox(self, data):
        self.customer_listbox.delete(0, tk.END)

        for key in data:
            self.customer_listbox.insert(tk.END, key)

    def cache_basic_customer_information(self):
        self.customer_info = GPFISCoordinator.get_entity_basic()
        self.customer_info = {"Times Distributing":"989 W Broadway, Los Angeles CA, 92001",
                              "Nagtoshi Distributing":"990 W Broadyway, Los Angeles CA, 92001"}

    def get_selected_customer(self):
        return self.current_customer

    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy()

    def build_frame(self):
        self.setup_frame()
        self.create_customer_widget()