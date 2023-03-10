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
        self.entityList = []
        self.current_customer = ""
        self.customer_info = ""
        self.cache_basic_customer_information()

    def setup_frame(self):
        self.customer_frame = tk.Frame(self.base_frame, bg=self.bg_color, padx=20, pady=20)
        self.customer_listbox = tk.Listbox(self.customer_frame, height=3, width=40, font=(self.data_font, 13))
        self.customer_display_label = tk.Label(self.customer_frame, text="", width=40, font=(self.data_font, 15))

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
        self.customer_display_label.pack(side="top", anchor='nw', expand=True)

        self.customer_frame.pack(side='left', anchor='nw')

        self.update_customer_listbox()

    def monitor_search_box(self, e):
        typed = self.customer_search_entrybox.get()
        #print(typed)
        if typed == '':
            data = self.entityNameList
        else:
            data = []
            for entity in self.entityNameList:
                #print("TL: "+ typed.lower() + "CL: "+ customer.lower())
                if typed.lower() in entity.lower():
                    data.append(entity)

        self.update_customer_listbox(data)

    def populate_customer_label(self, e):
        self.customer_display_label.config(text=" ")

        #print(str(self.customer_listbox.get(tk.ACTIVE)), e)
        selected_listbox_customer = str(self.customer_listbox.get(tk.ACTIVE))
        self.current_customer = selected_listbox_customer
        for entities in self.entityList:
            #print(entities)
            if self.current_customer == entities.getName():
                full_customer_info = entities.getAsCustomerWidgetDisplay()
                #print(full_customer_info)
        #full_customer_info = selected_listbox_customer + "\n" + self.customer_dict.get(selected_listbox_customer)
        
        self.customer_display_label.config(text=full_customer_info)

    def update_customer_listbox(self, data=None):
        self.customer_listbox.delete(0, tk.END)

        if data is None:
            for entity in self.entityList:
                self.customer_listbox.insert(tk.END, entity.getName())
        else:
            for entity in data:
                self.customer_listbox.insert(tk.END, entity)

        #for key in data:
        #    self.customer_listbox.insert(tk.END, key)

    def cache_basic_customer_information(self):
        coordinator = GPFISCoordinator()
        self.entityList = coordinator.get_entities_simple()
        self.entityNameList = []
        for entities in self.entityList:
            #print(entities.toList())
            self.entityNameList.append(entities.getName())
            

    def get_selected_customer(self):
        return self.current_customer

    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy()

    def build_frame(self):
        self.setup_frame()
        self.create_customer_widget()