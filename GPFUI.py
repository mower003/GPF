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
from tkinter import BOTH, LEFT, Menu

class GPFUI():
    def start():

        root = tk.Tk()

        root.title('Green Paradise Farms')
        root.iconbitmap('GPFISHTMLObjects\Invoices\imgs\gpf_logo.ico')

        window_width = 700
        window_height = 500

        # get the screen dimension
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        #Window controls
        #Fullscreen no top toolbar
        #root.attributes('-fullscreen', True)
        #Full screen with right top toolbar
        #root.geometry("%dx%d" % (screen_width, screen_height))
        #Use window geometery and center
        root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        #baseFrame = tk.Frame(root, bd = 5, bg = 'grey')
        #baseFrame.pack(fill=BOTH, expand=1)

        #scrollbar set up
        baseFrame = tk.Frame(root,bg = '#FFFFFF')
        baseFrame.pack(fill=BOTH, expand=1)

        baseCanvas = tk.Canvas(baseFrame, bg="#FFFFFF")
        baseCanvas.pack(side='left', fill=BOTH, expand=1)

        v_scroll = tk.Scrollbar(baseFrame, orient='vertical', command=baseCanvas.yview)
        v_scroll.pack(side='right', fill='y')

        baseFrame_2 = tk.Frame(baseCanvas, bg="#FFFFFF", highlightbackground='green', highlightthickness=2)

        #Instantiate class objects for each menu option
        #Each object builds and controls UI widgets
        order_board_frame = OrderBoardFrame(baseFrame_2)
        add_customer_frame = AddCustomerFrame(baseFrame_2)
        view_customer_frame = ViewCustomerFrame(baseFrame_2)
        add_product_frame = AddProductFrame(baseFrame_2)
        view_product_frame = ViewProductFrame(baseFrame_2)
        add_invoice_frame = AddInvoiceFrame(baseFrame_2, baseCanvas)
        view_invoice_frame = ViewInvoiceFrame(baseFrame_2)
        statement_frame = Statements(baseFrame_2, baseCanvas)

        baseCanvas.configure(yscrollcommand=v_scroll.set)
        baseCanvas.bind("<Configure>", lambda e: baseCanvas.configure(scrollregion= baseCanvas.bbox("all")))

        baseCanvas.create_window((0,0), window=baseFrame_2, anchor='nw', tags="baseFrame_2")
        baseCanvas.itemconfig("baseFrame_2", height=screen_height, width=screen_width)

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

        baseMenu = OptionsMenu.GPF_OptionsMenu(root, 
                                            add_customer_frame = add_customer_frame, 
                                            view_customer_frame= view_customer_frame, 
                                            add_product_frame= add_product_frame, 
                                            view_product_frame= view_product_frame, 
                                            add_invoice_frame= add_invoice_frame, 
                                            view_invoice_frame= view_invoice_frame,
                                            order_board_frame= order_board_frame,
                                            statement_frame= statement_frame)
        root.config(menu=baseMenu.getMenuBar())

        root.mainloop()

