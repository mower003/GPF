import tkinter as tk
from GPFISCoordinator import GPFISCoordinator

class CustomerSearchWidget(tk.Frame):

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
        self.entityNameList = []
        self.customer_search_lbl_var = tk.StringVar(master = self.base_frame, value="Customer Search...")
        self.current_customer = ""
        self.customer_info = ""
        self.selected_entity_obj = None

    def setup_frame(self):
        self.customer_frame = tk.Frame(self.base_frame, bg=self.bg_color, padx=20, pady=20)
        self.customer_listbox = tk.Listbox(self.customer_frame, height=3, width=40, font=(self.data_font, 13))
        self.customer_display_label = tk.Label(self.customer_frame, text="\n", width=40, font=(self.data_font, 15))

    def create_customer_widget(self):
        self.customer_search_lbl = tk.Label(self.customer_frame, text=self.customer_search_lbl_var.get(), font=(self.data_font, 12, 'bold'), bg=self.bg_color)
        self.customer_search_lbl.pack(side="top", anchor='nw')

        self.customer_search_entrybox = tk.Entry(self.customer_frame, width=40)
        self.customer_search_entrybox.pack(side="top", anchor='nw')
        self.customer_search_entrybox.bind("<KeyRelease>",self.monitor_search_box)

        #self.customer_listbox = tk.Listbox(self.customer_frame, height=3, width=40)
        self.customer_listbox.pack(side="top", anchor='nw', pady=5)
        self.customer_listbox.bind("<<ListboxSelect>>", self.populate_customer_label)

        #self.customer_display_label = tk.Label(self.customer_frame, text="")
        self.customer_display_label.pack(side="top", anchor='nw', expand=True)

        self.customer_frame.grid()

        self.update_customer_listbox()

    def set_grid_position(self, row, col):
        self.customer_frame.grid(row=row, column=col)

    def set_invoice_object(self, InvObj):
        self.oInvoice = InvObj

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
                self.selected_entity_obj = entities
                if self.customer_search_lbl_var.get() == 'Bill To:':
                    self.oInvoice.set_buyer(entities)
                if self.customer_search_lbl_var.get() == 'Ship To:':
                    self.oInvoice.set_shipto(entities)
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

    def set_entity_list(self, entityList):
        self.entityList = entityList
        self.populate_entity_name_list()
            
    def populate_entity_name_list(self):
        for entities in self.entityList:
            self.entityNameList.append(entities.getName())

    def get_selected_customer(self):
        return self.current_customer
    
    def get_selected_entity_obj(self):
        return self.selected_entity_obj
    
    def set_customer(self, entityObj):
        self.customer_listbox.delete(0, tk.END)
        self.customer_listbox.insert(tk.END, entityObj.getName())
        self.customer_listbox.activate(0)
        self.current_customer = entityObj.getName()
        self.selected_entity_obj = entityObj
        self.populate_customer_label(e=None)

    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy()

    def set_top_label(self, label_description):
        self.customer_search_lbl_var.set(label_description)

    def set_searchbox_and_label(self, entityObj):
        self.customer_search_entrybox.insert(0, entityObj.getName())
        self.customer_display_label.configure(text=entityObj.getAsCustomerWidgetDisplay())

    def build_frame(self):
        self.setup_frame()
        self.create_customer_widget()