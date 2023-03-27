import tkinter as tk
from GPFISCoordinator import GPFISCoordinator
from EditCustomerFrame import EditCustomerFrame
from Entity import EntityObj
from Entity import EntityObjEnum

class EntityLineItemWidget():

    #Static Settings
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
    frame_title = "Entity Line Item Widget"

    def __init__(self, parent_frame, entity_id = -999, entity_name = None, st_name = None, st_number = None, city = None, state = None, zip = None, country = 'USA', is_active = None, * , entityObj = None):
        self.base_frame = parent_frame
        self.oEntity = entityObj
        self.coordinator = GPFISCoordinator()
        self.create_ui_elements()

        if entityObj is None:
            self.entity_id.insert("1.0", entity_id)
            self.entity_name.insert("1.0", entity_name)
            self.st_name.insert("1.0", st_name)
            self.st_number.insert("1.0", st_number)
            self.city.insert("1.0", city)
            self.state.insert("1.0", state)
            self.zip.insert("1.0", zip)
            self.country.insert("1.0", country)
            self.is_active.insert("1.0", is_active)
        else:
            self.populate_ui_elements_from_object(entityObj=entityObj)

        self.disable_text_boxes()

    def spawn_edit_window(self, entityObj=None):
        if entityObj is None:
            self.ec = EditCustomerFrame(self.base_frame, self.get_entity_as_list())
        else:
            self.ec = EditCustomerFrame(self.base_frame, entityObj.asList())
            self.clear_display_frame()

    def place_entity_lines(self, row_number):
        self.entity_id.grid(row=row_number, column=EntityObjEnum.ENTITY_ID.value, sticky='N,E,W', pady=2)
        self.entity_name.grid(row=row_number, column=EntityObjEnum.ENTITY_NAME.value, sticky='N,E,W', pady=2)
        self.st_name.grid(row=row_number, column=EntityObjEnum.STREET_NAME.value, sticky='N,E,W', pady=2)
        self.st_number.grid(row=row_number, column=EntityObjEnum.STREET_NUMBER.value, sticky='N,E,W', pady=2)
        self.city.grid(row=row_number, column=EntityObjEnum.CITY.value, sticky='N,E,W', pady=2)
        self.state.grid(row=row_number, column=EntityObjEnum.STATE.value, sticky='N,E,W', pady=2)
        self.zip.grid(row=row_number, column=EntityObjEnum.ZIP.value, sticky='N,E,W', pady=2)
        self.country.grid(row=row_number, column=EntityObjEnum.COUNTRY.value, sticky='N,E,W', pady=2)
        self.is_active.grid(row=row_number, column=EntityObjEnum.IS_ACTIVE.value, sticky='N,E,W', pady=2)
        self.edit_button.grid(row=row_number, column=9, sticky='N,E,W')


    def disable_text_boxes(self):
        self.entity_id.config(state='disabled')
        self.entity_name.config(state='disabled')
        self.st_name.config(state='disabled')
        self.st_number.config(state='disabled')
        self.city.config(state='disabled')
        self.state.config(state='disabled')
        self.zip.config(state='disabled')
        self.country.config(state='disabled')
        self.is_active.config(state='disabled')

    def enable_text_boxes(self):
        self.entity_id.config(state='active')
        self.entity_name.config(state='active')
        self.st_name.config(state='active')
        self.st_number.config(state='active')
        self.city.config(state='active')
        self.state.config(state='active')
        self.zip.config(state='active')
        self.country.config(state='active')
        self.is_active.config(state='active')

    def create_ui_elements(self):
        self.entity_id = tk.Text(self.base_frame, bg=self.bg_color, font=(self.label_font, 12), width=20, height=2, wrap=tk.WORD)
        self.entity_name = tk.Text(self.base_frame, bg=self.bg_color, font=(self.label_font, 12), width=20, height=2, wrap=tk.WORD)
        self.st_name = tk.Text(self.base_frame, bg=self.bg_color, font=(self.label_font, 12), width=20, height=2, wrap=tk.WORD)
        self.st_number = tk.Text(self.base_frame, bg=self.bg_color, font=(self.label_font, 12), width=20, height=2, wrap=tk.WORD)
        self.city = tk.Text(self.base_frame, bg=self.bg_color, font=(self.label_font, 12), width=20, height=2, wrap=tk.WORD)
        self.state = tk.Text(self.base_frame, bg=self.bg_color, font=(self.label_font, 12), width=20, height=2, wrap=tk.WORD)
        self.zip = tk.Text(self.base_frame, bg=self.bg_color, font=(self.label_font, 12), width=20, height=2, wrap=tk.WORD)
        self.country = tk.Text(self.base_frame, bg=self.bg_color, font=(self.label_font, 12), width=20, height=2, wrap=tk.WORD)
        self.is_active = tk.Text(self.base_frame, bg=self.bg_color, font=(self.label_font, 12), width=20, height=2, wrap=tk.WORD)
        self.edit_button = tk.Button(self.base_frame, text="Edit", command=lambda: self.spawn_edit_window(self.oEntity))

    def populate_ui_elements_from_object(self, entityObj):
        self.entity_id.insert("1.0", entityObj.getID())
        self.entity_name.insert("1.0", entityObj.getName())
        self.st_name.insert("1.0", entityObj.getStreetName())
        self.st_number.insert("1.0", entityObj.getStreetNumber())
        self.city.insert("1.0", entityObj.getCity())
        self.state.insert("1.0", entityObj.getState())
        self.zip.insert("1.0", entityObj.getZip())
        self.country.insert("1.0", entityObj.getCountry())
        self.is_active.insert("1.0", entityObj.getIsActive())

    def get_entity_as_list(self):
        list = []
        list.append(str(self.entity_id.get("1.0", tk.END)))
        list.append(str(self.entity_name.get("1.0", tk.END)))
        list.append(str(self.st_name.get("1.0", tk.END)))
        list.append(str(self.st_number.get("1.0", tk.END)))
        list.append(str(self.city.get("1.0", tk.END)))
        list.append(str(self.state.get("1.0", tk.END)))
        list.append(str(self.zip.get("1.0", tk.END)))
        list.append(str(self.country.get("1.0", tk.END)))
        list.append(str(self.is_active.get("1.0", tk.END)))
        return list

    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy()


