import tkinter as tk
import random as rd
from tkinter import BOTH, LEFT, Menu

#Placeholder methods Delete these once all menu commands have been filled out.
def donothing():
    print("haha")
#-----------------------------------------------------

class GPF_OptionsMenu:

    def __init__(self, theRoot, add_customer_frame=None, view_customer_frame=None, add_product_frame=None, view_product_frame=None, add_invoice_frame=None, view_invoice_frame=None):
        #No frames can be None, if so something has gone wrong. Make sure to add a check for all frames to be set.

        self.menubar = Menu(theRoot)

        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New", command=donothing)
        self.filemenu.add_command(label="Open", command=donothing)
        self.filemenu.add_command(label="Save", command=donothing)
        self.filemenu.add_command(label="Save as...", command=donothing)
        self.filemenu.add_command(label="Close", command=donothing)

        self.filemenu.add_separator()

        self.filemenu.add_command(label="Exit", command=theRoot.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.customermenu = Menu(self.menubar, tearoff=0)
        self.customermenu.add_command(label="Add Customer", command=lambda: add_customer_frame.build_frame())
        self.customermenu.add_command(label="View Customers", command=lambda: view_customer_frame.build_frame())
        self.customermenu.add_command(label="Edit Customer", command=lambda: view_customer_frame.build_frame())
        #self.customermenu.add_separator()
        self.menubar.add_cascade(label="Customers", menu=self.customermenu)

        self.productmenu = Menu(self.menubar, tearoff=0)
        self.productmenu.add_command(label="Add Product", command=lambda: add_product_frame.build_frame())
        self.productmenu.add_command(label="View Products", command=lambda: view_product_frame.build_frame())
        self.productmenu.add_command(label="Edit Products", command=donothing)
        #self.productmenu.add_separator()
        self.menubar.add_cascade(label="Products", menu=self.productmenu)

        self.invoicemenu = Menu(self.menubar, tearoff=0)
        self.invoicemenu.add_command(label="New Invoice", command=lambda: add_invoice_frame.build_frame())
        self.invoicemenu.add_command(label="View Invoices", command=lambda: view_invoice_frame.build_frame())
        self.invoicemenu.add_command(label="Edit Invoices", command=donothing)
        #self.invoicemenu.add_separator()
        self.menubar.add_cascade(label="Invoices", menu=self.invoicemenu)

        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="Help Index", command=donothing)
        self.helpmenu.add_command(label="About...", command=donothing)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

    def getMenuBar(self):
        return self.menubar