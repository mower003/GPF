import tkinter as tk
import random as rd
from GPFISCoordinator import GPFISCoordinator
from Entity import EntityObj
from Entity import EntityObjEnum

class AddCustomerFrame():

    #Static Settings
    #Controls the number and name of form elements
    customer_compositional_elements = ['Customer ID:', 'Name', 'Address Number', 'Street Name',  'City', 'State', 'Zip', 'Country', 'Active']
    #Color theme
    bg_color = '#FFFFFF'
    label_color = '#FFFFFF'
    data_color = '#AA8B56'
    header_color = '#F0EBCE'
    #Fonts
    title_font = 'Haettenschweiler'
    header_font = 'Haettenschweiler'
    label_font = 'Haettenschweiler'
    data_font = 'MS Sans Serif'
    #Controls the title of the frame.
    frame_title = "Add Customer"

    def __init__(self, parent_frame):
        self.base_frame = parent_frame
        self.coordinator = GPFISCoordinator()

    def set_up_frame(self):
        self.entity_frame = tk.Frame(self.base_frame, bd=2, bg=self.bg_color)
        self.btn = tk.Button(self.entity_frame, text="Save", width=40, bg=self.data_color)
        self.btn.configure(command=self.save_entity_info_to_db)

    def save_entity_info_to_db(self):
        print(self.get_entry_elements_as_list())

        oEntity = EntityObj(entityList = self.get_entry_elements_as_list())
        self.coordinator.insert_entity(EntityObj=oEntity)

        self.clear_product_data()

    def add_title_label(self):
        self.title = tk.Label(self.entity_frame, text=self.frame_title, bg=self.label_color)
        self.title.config(font=(self.title_font,25))
        self.title.grid(row=0, column = 0, columnspan=3, ipady=5, pady=5, sticky="N,S,E,W")
        #self.entity_frame.grid_columnconfigure(0, weight=1)
        #self.entity_frame.grid_columnconfigure(1, weight=2)
        #self.entity_frame.grid_columnconfigure(2, weight=1)

    def create_entity_frame(self):
        self.entity_id_lbl = tk.Label(self.entity_frame, text = "Customer ID:", font=(self.data_font, 12, 'bold'), bg=self.bg_color)
        self.entity_id_entry = tk.Entry(self.entity_frame, width=40, font=(self.data_font, 12))
        self.entity_id_lbl.grid(row = 1, column = 0, sticky='W')
        self.entity_id_entry.grid(row = 1, column= 1, sticky='E,W')

        self.entity_name_lbl = tk.Label(self.entity_frame, text = "Customer Name:", font=(self.data_font, 12, 'bold'), bg=self.bg_color)
        self.entity_name_entry = tk.Entry(self.entity_frame, width=40, font=(self.data_font, 12))
        self.entity_name_lbl.grid(row = 2, column = 0, sticky='W')
        self.entity_name_entry.grid(row = 2, column= 1, sticky='E,W')

        self.street_number_lbl = tk.Label(self.entity_frame, text = "Address Number:", font=(self.data_font, 12, 'bold'), bg=self.bg_color)
        self.street_number_entry = tk.Entry(self.entity_frame, width=40, font=(self.data_font, 12))
        self.street_number_lbl.grid(row = 3, column = 0, sticky='W')
        self.street_number_entry.grid(row = 3, column= 1, sticky='E,W')

        self.street_name_lbl = tk.Label(self.entity_frame, text = "Street Name:", font=(self.data_font, 12, 'bold'), bg=self.bg_color)
        self.street_name_entry = tk.Entry(self.entity_frame, width=40, font=(self.data_font, 12))
        self.street_name_lbl.grid(row = 4, column = 0, sticky='W')
        self.street_name_entry.grid(row = 4, column= 1, sticky='E,W')

        self.city_lbl = tk.Label(self.entity_frame, text = "City:", font=(self.data_font, 12, 'bold'), bg=self.bg_color)
        self.city_entry = tk.Entry(self.entity_frame, width=40, font=(self.data_font, 12))
        self.city_lbl.grid(row = 5, column = 0, sticky='W')
        self.city_entry.grid(row = 5, column= 1, sticky='E,W')

        self.state_lbl = tk.Label(self.entity_frame, text = "State:", font=(self.data_font, 12, 'bold'), bg=self.bg_color)
        self.state_entry = tk.Entry(self.entity_frame, width=40, font=(self.data_font, 12))
        self.state_lbl.grid(row = 6, column = 0, sticky='W')
        self.state_entry.grid(row = 6, column= 1, sticky='E,W')

        self.zip_lbl = tk.Label(self.entity_frame, text = "Zip:", font=(self.data_font, 12, 'bold'), bg=self.bg_color)
        self.zip_entry = tk.Entry(self.entity_frame, width=40, font=(self.data_font, 12))
        self.zip_lbl.grid(row = 7, column = 0, sticky='W')
        self.zip_entry.grid(row = 7, column= 1, sticky='E,W')

        self.country_lbl = tk.Label(self.entity_frame, text = "Country:", font=(self.data_font, 12, 'bold'), bg=self.bg_color)
        self.country_entry = tk.Entry(self.entity_frame, width=40, font=(self.data_font, 12))
        self.country_lbl.grid(row = 8, column = 0, sticky='W')
        self.country_entry.grid(row = 8, column= 1, sticky='E,W')

        self.btn.grid(row = 9, column = 0, columnspan=3, ipadx=10, padx=5, pady=40)

        self.entity_frame.pack(side='top', anchor='center')

    def build_frame(self):
        self.clear_display_frame()
        self.set_up_frame()
        self.add_title_label()
        self.create_entity_frame()

    def get_entry_elements_as_list(self):
        list = []
        list.insert(EntityObjEnum.ENTITY_ID.value, self.entity_id_entry.get().strip())
        list.insert(EntityObjEnum.ENTITY_NAME.value, self.entity_name_entry.get().strip())
        list.insert(EntityObjEnum.STREET_NUMBER.value, self.street_number_entry.get().strip())
        list.insert(EntityObjEnum.STREET_NAME.value, self.street_name_entry.get().strip())
        list.insert(EntityObjEnum.CITY.value, self.city_entry.get().strip())
        list.insert(EntityObjEnum.STATE.value, self.state_entry.get().strip())
        list.insert(EntityObjEnum.ZIP.value, self.zip_entry.get().strip())
        list.insert(EntityObjEnum.COUNTRY.value, self.country_entry.get().strip())
        list.insert(EntityObjEnum.IS_ACTIVE.value, 1)

        return list

    def clear_product_data(self):
        self.entity_id_entry.delete(0, tk.END)
        self.entity_name_entry.delete(0, tk.END)
        self.street_number_entry.delete(0, tk.END)
        self.street_name_entry.delete(0, tk.END)
        self.city_entry.delete(0, tk.END)
        self.state_entry.delete(0, tk.END)
        self.zip_entry.delete(0, tk.END)
        self.country_entry.delete(0, tk.END)

    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy()