import tkinter as tk

from GPFISCoordinator import GPFISCoordinator
from Entity import EntityObj
from Entity import EntityObjEnum


class EditCustomerFrame():

    #Static Settings
    customer_compositional_elements = ['Customer ID:', 'Name', 'Address Number', 'Street Name',  'City', 'State', 'Zip', 'Country', 'Active']
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
    frame_title = "Edit Entity Frame"

    def __init__(self, parent_frame, entity_list):
        self.base_frame = parent_frame
        self.coordinator = GPFISCoordinator()
        self.entity_list = entity_list
        self.build_frame()

    def set_up_frame(self):
        self.edit_entity_frame = tk.Toplevel(bd=2, bg=self.bg_color)
        self.btn = tk.Button(self.edit_entity_frame, text="Save", width=40, bg=self.data_color, command=lambda: self.save_entity_info_to_db())

    def save_entity_info_to_db(self):
        oEntity = EntityObj(entityList = self.getEntryElements())
        #print(oProduct.asListForDBUpdate())
        self.coordinator.update_entity(EntityObj = oEntity)

        
        self.edit_entity_frame.update()
        self.edit_entity_frame.destroy()

    def add_title_label(self):
        self.title = tk.Label(self.edit_entity_frame, text=self.frame_title, bg=self.label_color)
        self.title.config(font=(self.title_font,25))
        self.title.grid(row=0, column = 0, columnspan=3, ipady=5, pady=5, sticky="N,S,E,W")
        self.edit_entity_frame.grid_columnconfigure(0, weight=1)
        self.edit_entity_frame.grid_columnconfigure(1, weight=1)
        self.edit_entity_frame.grid_columnconfigure(2, weight=1)

    def create_entity_frame(self):
        self.entity_id_lbl = tk.Label(self.edit_entity_frame, text = "Customer ID:", font=(self.data_font, 12, 'bold'), bg=self.bg_color)
        self.entity_id_entry = tk.Entry(self.edit_entity_frame, width=40, font=(self.data_font, 12))
        self.entity_id_entry.insert(0, self.entity_list[EntityObjEnum.ENTITY_ID.value])
        self.entity_id_entry.config(state='disabled')
        self.entity_id_lbl.grid(row = 1, column = 0, sticky='W')
        self.entity_id_entry.grid(row = 1, column= 1, sticky='E,W')

        self.entity_name_lbl = tk.Label(self.edit_entity_frame, text = "Customer Name:", font=(self.data_font, 12, 'bold'), bg=self.bg_color)
        self.entity_name_entry = tk.Entry(self.edit_entity_frame, width=40, font=(self.data_font, 12))
        self.entity_name_entry.insert(0, self.entity_list[EntityObjEnum.ENTITY_NAME.value])
        self.entity_name_lbl.grid(row = 2, column = 0, sticky='W')
        self.entity_name_entry.grid(row = 2, column= 1, sticky='E,W')

        self.street_number_lbl = tk.Label(self.edit_entity_frame, text = "Address Number:", font=(self.data_font, 12, 'bold'), bg=self.bg_color)
        self.street_number_entry = tk.Entry(self.edit_entity_frame, width=40, font=(self.data_font, 12))
        self.street_number_entry.insert(0, self.entity_list[EntityObjEnum.STREET_NUMBER.value])
        self.street_number_lbl.grid(row = 3, column = 0, sticky='W')
        self.street_number_entry.grid(row = 3, column= 1, sticky='E,W')

        self.street_name_lbl = tk.Label(self.edit_entity_frame, text = "Street Name:", font=(self.data_font, 12, 'bold'), bg=self.bg_color)
        self.street_name_entry = tk.Entry(self.edit_entity_frame, width=40, font=(self.data_font, 12))
        self.street_name_entry.insert(0, self.entity_list[EntityObjEnum.STREET_NAME.value])
        self.street_name_lbl.grid(row = 4, column = 0, sticky='W')
        self.street_name_entry.grid(row = 4, column= 1, sticky='E,W')

        self.city_lbl = tk.Label(self.edit_entity_frame, text = "City:", font=(self.data_font, 12, 'bold'), bg=self.bg_color)
        self.city_entry = tk.Entry(self.edit_entity_frame, width=40, font=(self.data_font, 12))
        self.city_entry.insert(0, self.entity_list[EntityObjEnum.CITY.value])
        self.city_lbl.grid(row = 5, column = 0, sticky='W')
        self.city_entry.grid(row = 5, column= 1, sticky='E,W')

        self.state_lbl = tk.Label(self.edit_entity_frame, text = "State:", font=(self.data_font, 12, 'bold'), bg=self.bg_color)
        self.state_entry = tk.Entry(self.edit_entity_frame, width=40, font=(self.data_font, 12))
        self.state_entry.insert(0, self.entity_list[EntityObjEnum.STATE.value])
        self.state_lbl.grid(row = 6, column = 0, sticky='W')
        self.state_entry.grid(row = 6, column= 1, sticky='E,W')

        self.zip_lbl = tk.Label(self.edit_entity_frame, text = "Zip:", font=(self.data_font, 12, 'bold'), bg=self.bg_color)
        self.zip_entry = tk.Entry(self.edit_entity_frame, width=40, font=(self.data_font, 12))
        self.zip_entry.insert(0, self.entity_list[EntityObjEnum.ZIP.value])
        self.zip_lbl.grid(row = 7, column = 0, sticky='W')
        self.zip_entry.grid(row = 7, column= 1, sticky='E,W')

        self.country_lbl = tk.Label(self.edit_entity_frame, text = "Country:", font=(self.data_font, 12, 'bold'), bg=self.bg_color)
        self.country_entry = tk.Entry(self.edit_entity_frame, width=40, font=(self.data_font, 12))
        self.country_entry.insert(0, self.entity_list[EntityObjEnum.COUNTRY.value])
        self.country_lbl.grid(row = 8, column = 0, sticky='W')
        self.country_entry.grid(row = 8, column= 1, sticky='E,W')



        self.btn.grid(row = 9, column = 0, columnspan=3, ipadx=10, padx=5, pady=40)

    def build_frame(self):
        self.set_up_frame()
        self.add_title_label()
        self.create_entity_frame()
        #self.populate_form()

    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy()

    def getEntryElements(self):
        entity_list = []
        entity_list.append(self.entity_id_entry.get().strip())
        entity_list.append(self.entity_name_entry.get().strip())
        entity_list.append(self.street_number_entry.get().strip())
        entity_list.append(self.street_name_entry.get().strip())
        entity_list.append(self.city_entry.get().strip())
        entity_list.append(self.state_entry.get().strip())
        entity_list.append(self.zip_entry.get().strip())
        entity_list.append(self.country_entry.get().strip())
        entity_list.append(1)

        return entity_list
