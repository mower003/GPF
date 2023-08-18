import tkinter as tk
import random as rd
import OptionsMenu
from AddCustomerFrame import AddCustomerFrame
from ViewCustomerFrame import ViewCustomerFrame
from AddProductFrame import AddProductFrame
from ViewProductFrame import ViewProductFrame
from AddInvoiceFrame import AddInvoiceFrame
from ViewInvoiceFrame import ViewInvoiceFrame
from OrderBoardFrame import OrderBoardFrame
from StatementsFrame import Statements
from ProductBreakdownFrame import ProductBreakdownFrame
from tkinter import BOTH, LEFT, Menu

class GPFUI():
    def __init__(self):
        self.root = tk.Tk()
        #self.baseFrame = tk.Frame(self.root,bg = '#FFFFFF')
        self.baseCanvas = tk.Canvas(self.root, bg='#FFFFFF')
        self.baseFrame_2 = tk.Frame(self.baseCanvas, bg='#FFFFFF')
        self.sbHorizontalScrollBar = tk.Scrollbar(self.root)
        self.sbVerticalScrollBar = tk.Scrollbar(self.root)

    def create_scrollable_container(self):
        self.baseCanvas.config(xscrollcommand=self.sbHorizontalScrollBar.set,yscrollcommand=self.sbVerticalScrollBar.set, highlightthickness=0)
        self.sbHorizontalScrollBar.config(orient=tk.HORIZONTAL, command=self.baseCanvas.xview)
        self.sbVerticalScrollBar.config(orient=tk.VERTICAL, command=self.baseCanvas.yview)

        self.sbHorizontalScrollBar.pack(fill=tk.X, side=tk.BOTTOM, expand=tk.FALSE)
        self.sbVerticalScrollBar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)

        self.baseCanvas.pack(fill=tk.BOTH, side=tk.LEFT, expand=tk.TRUE)
        self.baseCanvas.create_window(0, 0, window=self.baseFrame_2, anchor=tk.NW)

    def update_scrollable_region(self):
        self.baseCanvas.update_idletasks()
        self.baseCanvas.config(scrollregion=self.baseFrame_2.bbox())

    def start(self):

        #root = tk.Tk()

        self.root.title('Green Paradise Farms')
        self.root.iconbitmap('GPFISHTMLObjects\Invoices\imgs\gpf_logo.ico')

        window_width = 700
        window_height = 500

        # get the screen dimension
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        #print("SCREEN HEIGHT:      " + str(screen_height) + " SCREEN WIDTH:      " + str(screen_width))

        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        #Window controls
        #Fullscreen no top toolbar
        self.root.attributes('-fullscreen', True)
        self.root.update_idletasks()
        #Full screen with right top toolbar
        #root.geometry("%dx%d" % (screen_width, screen_height))
        #Use window geometery and center
        #self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        #baseFrame = tk.Frame(root, bd = 5, bg = 'grey')
        #baseFrame.pack(fill=BOTH, expand=1)

        #scrollbar set up
        #baseFrame = tk.Frame(self.root,bg = '#FFFFFF')
        #self.baseFrame.pack()
        self.baseFrame_2.pack()

        #baseCanvas = tk.Canvas(self.baseFrame, bg="#FFFFFF")
        #self.baseCanvas.pack(side='left', fill=BOTH, expand=1)

        #v_scroll = tk.Scrollbar(self.baseFrame, orient='vertical', command=self.baseCanvas.yview)
        #v_scroll.pack(side='right', fill='y')

        #baseFrame_2 = tk.Frame(self.baseCanvas, bg="#FFFFFF")

        #Instantiate class objects for each menu option
        #Each object builds and controls UI widgets
        order_board_frame = OrderBoardFrame(self.baseFrame_2)
        add_customer_frame = AddCustomerFrame(self.baseFrame_2)
        view_customer_frame = ViewCustomerFrame(self.baseFrame_2, self.baseCanvas, self.root)
        add_product_frame = AddProductFrame(self.baseFrame_2)
        view_product_frame = ViewProductFrame(self.baseFrame_2, self.baseCanvas, self.root)
        add_invoice_frame = AddInvoiceFrame(self.baseFrame_2, self.baseCanvas)
        view_invoice_frame = ViewInvoiceFrame(self.baseFrame_2, self.baseCanvas, self.root)
        statement_frame = Statements(self.baseFrame_2, self.baseCanvas, self.root)
        product_breakdown_frame = ProductBreakdownFrame(self.baseFrame_2, self.baseCanvas, self.root)

        self.baseFrame_2.configure(bg='#cccccc')
        self.baseCanvas.configure(bg='#cccccc')

        self.create_scrollable_container()
        self.update_scrollable_region()
        #baseCanvas.configure(yscrollcommand=v_scroll.set)
        #baseCanvas.bind("<Configure>", lambda e: baseCanvas.configure(scrollregion= baseCanvas.bbox("all")))

        #baseCanvas.create_window((0,0), window=baseFrame_2, anchor='nw', tags="baseFrame_2")
        #baseCanvas.itemconfig("baseFrame_2", height=screen_height, width=screen_width)

        #baseCanvas = tk.Canvas(baseFrame, scrollregion=(0,0, 1500, 1500))
        #vbar = tk.Scrollbar(baseFrame, orient='vertical')
        #vbar.pack(side='right', fill='y')
        #vbar.config(command=baseCanvas.yview)
        #baseCanvas.config(yscrollcommand=vbar.set)
        #baseCanvas.pack(side='left' ,fill='both', expand=True)

        #This class should make an object for all the frames like view customer, add customer, view product, add product etc..
        #each of those objects will have a reference to the base frame and be passed to the menu class.
        #the menu class will have references to those objects, be able to call their methods, and change frames based on the menu action selected.
        #Each of those objects may or may not have imported classes that deal with retrieving or sending data to the databse. Those classes
        #WILL NOT handle any of that themselves, beyond making a call asks for or sends data. Data that is sent or comes in should be in list or tuple form. 
        # (possible that it may be lists or tuples of appropriate objects e.g. Product, Customer classes)

        baseMenu = OptionsMenu.GPF_OptionsMenu(self.root, 
                                            add_customer_frame = add_customer_frame, 
                                            view_customer_frame= view_customer_frame, 
                                            add_product_frame= add_product_frame, 
                                            view_product_frame= view_product_frame, 
                                            add_invoice_frame= add_invoice_frame, 
                                            view_invoice_frame= view_invoice_frame,
                                            order_board_frame= order_board_frame,
                                            statement_frame= statement_frame,
                                            product_breakdown_frame = product_breakdown_frame)
        self.root.config(menu=baseMenu.getMenuBar())

        self.root.mainloop()
