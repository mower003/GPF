import tkinter as tk
from GPFISCoordinator import GPFISCoordinator
from EntityLineItemWidget import EntityLineItemWidget

class ViewCustomerFrame():
    #Static Settings
    #Controls the number and name of form elements
    customer_compositional_elements = ['ID', 'Name', 'Street No.', 'Street Name', 'City' ,'State' , 'Zip', 'Country', 'Active', '']
    #Color theme
    #bg_color = '#395144'
    bg_color = '#cccccc'
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
    frame_title = "Customer List"

    def __init__(self, parent_frame, canvas, root):
        self.base_frame = parent_frame
        self.canvas = canvas
        self.root = root
        self.coordinator = GPFISCoordinator()
        self.entity_list = []
        self.entity_lines_list = []

    def set_up_frame(self):
        self.title_frame = tk.Frame(self.base_frame, bd=2, bg= self.bg_color)
        self.entity_lines_frame = tk.Frame(self.base_frame, bg = self.bg_color, padx=10)
        self.entity_lines_frame.grid_columnconfigure(0, weight=1, uniform='column')
        self.entity_lines_frame.grid_columnconfigure(1, weight=3, uniform='column')
        self.entity_lines_frame.grid_columnconfigure(2, weight=2, uniform='column')
        self.entity_lines_frame.grid_columnconfigure(3, weight=3, uniform='column')
        self.entity_lines_frame.grid_columnconfigure(4, weight=3, uniform='column')
        self.entity_lines_frame.grid_columnconfigure(5, weight=1, uniform='column')
        self.entity_lines_frame.grid_columnconfigure(6, weight=1, uniform='column')
        self.entity_lines_frame.grid_columnconfigure(7, weight=1, uniform='column')
        self.entity_lines_frame.grid_columnconfigure(8, weight=1, uniform='column')
        self.entity_lines_frame.grid_columnconfigure(9, weight=1, uniform='column')
        
        #self.entity_lines_frame.grid_rowconfigure((0), weight=1)


    def create_entity_lines(self):
        row = 1
        for entities in self.entity_list:
            #print(entities.asList())
            eo = EntityLineItemWidget(self.entity_lines_frame, self, entityObj = entities)
            eo.place_entity_lines(row)
            self.entity_lines_list.append(eo)
            #self.entity_lines_frame.grid_rowconfigure((row), weight=1)
            #print("from create pentity lines", eo.get_product_line_info())
            row += 1
        self.update_scroll_region()
     
    def create_view_form(self, form_rows):
        row = 0
        col = 0
        for headers in self.customer_compositional_elements:
            #print(headers)
            lbl = tk.Label(self.entity_lines_frame, text = headers, font=(self.header_font,20), bg=self.bg_color)
            lbl.grid(row = row, column = col, sticky = "W,E")
            col += 1
        self.create_entity_lines()

        self.title_frame.pack()
        self.entity_lines_frame.pack()

    def add_title_label(self):
        self.title = tk.Label(self.title_frame, text=self.frame_title)
        self.title.config(font=(self.title_font,38),bg=self.bg_color)
        self.title.pack()

    def build_frame(self):

        self.clear_display_frame()
        self.cache_entity_data()
        self.set_up_frame()
        self.add_title_label()

        entity_rows = []
        #print("entity list: ",self.entity_list)
        for entities in self.entity_list:
            entity_rows.append(entities.asList())

        #print(entity_rows)
        self.create_view_form(entity_rows)

    def update_scroll_region(self):
        #Canvas holding scroll bar needs to be resized to fit line items.
        self.entity_lines_frame.update()
        self.base_frame.update()

        header_height = self.title_frame.winfo_reqheight()
        header_width = self.title_frame.winfo_reqwidth()
        lines_height = self.entity_lines_frame.winfo_reqheight()
        lines_width = self.entity_lines_frame.winfo_reqwidth()

        total_height = header_height + lines_height
        total_width = header_width + lines_width
        screen_width = self.root.winfo_screenwidth()

        #print("h         " + str(header_height) + "l        " + str(lines_height) + " w      " + str(lines_width))
        self.canvas.config(scrollregion=(0,0,screen_width, total_height))


    def cache_entity_data(self):
        self.entity_list = self.coordinator.get_entities()
        #print(self.entity_list)

    def clear_display_frame(self):
        for children in self.base_frame.winfo_children():
            children.destroy() 
