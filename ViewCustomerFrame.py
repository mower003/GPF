import tkinter as tk
from GPFISCoordinator import GPFISCoordinator
from EntityLineItemWidget import EntityLineItemWidget

class ViewCustomerFrame():
    print("I AM THE NEW CUSTOMER FRAME")
    #Static Settings
    #Controls the number and name of form elements
    customer_compositional_elements = ['Customer ID ', 'Name ', 'Street Number ', 'Street Name ', 'City ' ,'State' , 'Country ', 'Active ', '']
    print(customer_compositional_elements)
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
    frame_title = "Entity List"

    def __init__(self, parent_frame):
        print("INIT HAS BEEN CALLED vcf")
        self.base_frame = parent_frame
        self.coordinator = GPFISCoordinator()
        self.entity_list = []
        self.entity_lines_list = []

    def set_up_frame(self):
        print("SETTING UP THE FRAME")
        self.title_frame = tk.Frame(self.base_frame, bd=2, bg= self.bg_color)
        self.entity_lines_frame = tk.Frame(self.base_frame, bg = self.bg_color, padx=10)
        self.entity_lines_frame.grid_columnconfigure((0), weight=2, uniform='column')
        self.entity_lines_frame.grid_columnconfigure((1), weight=1, uniform='column')
        self.entity_lines_frame.grid_columnconfigure((2), weight=1, uniform='column')
        self.entity_lines_frame.grid_columnconfigure((3), weight=1, uniform='column')
        self.entity_lines_frame.grid_columnconfigure((4), weight=1, uniform='column')
        self.entity_lines_frame.grid_columnconfigure((5), weight=1, uniform='column')
        self.entity_lines_frame.grid_columnconfigure((6), weight=3, uniform='column')
        self.entity_lines_frame.grid_columnconfigure((7), weight=3, uniform='column')
        self.entity_lines_frame.grid_columnconfigure((8), weight=3, uniform='column')
        
        #self.entity_lines_frame.grid_rowconfigure((0), weight=1)


    def create_entity_lines(self):
        row = 1
        for entities in self.entity_list:
            print(entities.asList())
            eo = EntityLineItemWidget(self.entity_lines_frame, entityObj = entities)
            eo.place_entity_lines(row)
            self.entity_lines_list.append(eo)
            #self.entity_lines_frame.grid_rowconfigure((row), weight=1)
            #print("from create pentity lines", eo.get_product_line_info())
            row += 1
     
    def create_view_form(self, form_rows):
        row = 0
        col = 0
        for headers in self.customer_compositional_elements:
            print(headers)
            lbl = tk.Label(self.entity_lines_frame, text = headers, font=(self.header_font,20), bg=self.header_color)
            lbl.grid(row = row, column = col, sticky = "W,E")
            col += 1
        self.create_entity_lines()
        
        self.title_frame.pack(side='top', fill='x')
        self.entity_lines_frame.pack(side='top', fill='both', expand=True)

    def add_title_label(self):
        self.title = tk.Label(self.title_frame, text=self.frame_title)
        self.title.config(font=(self.title_font,38),bg=self.bg_color)
        self.title.pack(side='top', fill='x')

    def build_frame(self):
        print("BUILD FRAME HAS BEEN CALLED VCF")
        self.clear_display_frame()
        self.cache_entity_data()
        self.set_up_frame()
        self.add_title_label()

        entity_rows = []
        print("entity list: ",self.entity_list)
        for entities in self.entity_list:
            entity_rows.append(entities.asList())

        print(entity_rows)
        self.create_view_form(entity_rows)

    def cache_entity_data(self):
        self.entity_list = self.coordinator.get_entities()
        print(self.entity_list)

    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy() 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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
