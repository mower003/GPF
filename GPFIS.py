from GPFDatabase import GPFDatabase as gpfd
gp = gpfd()

def main_menu():
    print("                     ")
    print("                     ")
    print(" 1) Customer ")
    print("                     ")
    print(" 2) Vegetable ")
    print("                     ")
    print(" 3) Invoicing ")
    print("                     ")
    print("                     ")

    valid = False
    while(valid == False):
        select = int(input(" "))
        if(select == 1):
            valid = True
            customer_menu()
        elif(select == 2):
            valid = True
            vegetable_menu()
        elif(select == 3):
            valid = True
            invoice_menu()

def view_customers():
    customers = gp.get_customers()
    i = 1
    for cust in customers:
        print("------------------------------------------------------")
        print(str(i) +") " + "Customer ID: " + str(cust[0]) + " Customer Name: " + cust[1]+" Customer Address: " + cust[2] + ", "+cust[3] + ", "+cust[4]+", "+cust[5])
        print("------------------------------------------------------")
        i += 1

def do_nothing():
    print("do nothing")

def customer_menu():
    print("                     ")
    print("                     ")
    print(" 1) Add a new Customer")
    print("                     ")
    print(" 2) Edit Customer Information")
    print("                     ")
    print(" 3) View Customers")
    print("                     ")
    print(" 4) Delete a Customer")
    print("                     ")

    select = int(input(" "))
    if(select == 1):
        #customer menu
        add_customer()
    elif(select == 2):
        #edit customer
        edit_customer()
    elif(select == 3):
        #invoicing menu
        view_customers()
    elif(select == 4):
        #delete
        do_nothing()
    else:
        select = int(input(" "))

def vegetable_menu():
    print("                     ")
    print("                     ")
    print(" 1) Add a new Vegetable")
    print("                     ")
    print(" 2) Edit Vegetable Information")
    print("                     ")
    print(" 3) View Vegetables")
    print("                     ")
    print(" 4) Delete a Vegetable")
    print("                     ")

    select = int(input(" "))
    if(select == 1):
        #customer menu
        do_nothing()
    elif(select == 2):
        #vegetable menu
        do_nothing()
    elif(select == 3):
        #invoicing menu
        do_nothing()
    elif(select == 4):
        #delete
        do_nothing()
    else:
        select = int(input(" "))

def invoice_menu():
    print("                     ")
    print("                     ")
    print(" 1) Create an Invoice")
    print("                     ")
    print(" 2) Edit an Invoice")
    print("                     ")
    print(" 3) View Invoices")
    print("                     ")

    select = int(input(" "))
    if(select == 1):
        #customer menu
        do_nothing()
    elif(select == 2):
        #vegetable menu
        do_nothing()
    elif(select == 3):
        #invoicing menu
        view_invoices()
        do_nothing()
    else:
        select = int(input(" "))

def view_invoices():
    invoice_nums = gp.get_invoice_list()
    print (invoice_nums)
    names = gp.get_invoice_columns()
    print(names)
    #print(invoices)
    for nums in invoice_nums:
        #print(inv)
        invoices = gp.get_invoice_by_invoicenum([nums])
        #print(invoices)
        invoice = invoices[0]
        
        print("Invoice Number: ", invoice[0])
        print("Customer ID: ", invoice[1])
        print("Order Date: ", invoice[2])
        print("Invoice Date: ", invoice[3])
        print("Comment: ", invoice[4])
        print("Discount: ", invoice[5])
        print("Customer Name: ", invoice[6])
        print("Customer Address: ", invoice[7])
        print("Customer State: ", invoice[8])
        print("Customer City: ", invoice[9])
        print("Customer Zip: ", invoice[10])
        print()
        
        line_items = gp.get_line_items_by_invid([invoice[0]])
        for lines in line_items:
            #print(lines)
            line_total = float(int(lines[1]) * float(lines[5]))
            print("Line Number: ",lines[0])
            print("Quantity: ", lines[1])
            print("Cases: ",lines[2])
            print("Product ID: ",lines[3])
            print("Description: ",lines[4])
            print("Price: ",lines[5])
            print("Line Total: ",line_total)
            print("Associated to Invoice Number: ",lines[6])
            print()

    #print (invoices)

def add_customer():
        print("Add a customer: ")
        
        customer_id = int(input("Enter customer ID: "))
        customer_name = input("Enter customer name: ")
        customer_address = input("Enter customer street address: ")
        customer_state = input("Enter customer state: ")
        customer_city = input("Enter customer city: ")
        customer_zip = input("Enter customer zipcode: ")

        new_customer = (customer_id, customer_name, customer_address, customer_city, customer_state, customer_zip)

        try:
            gp.insert_customer(new_customer)
            gp.close_connection()
        except Error as e:
            print(e)

def edit_print_cust_info(cust):
    print("1) ID: " + str(cust[0]))
    print("2) Name: " + cust[1])
    print("3) Address: " + cust[2])
    print("4) City: " + cust[3])
    print("5) State: " + cust[4])
    print("6) Zip: " + cust[5])

def edit_customer():
    view_customers()
    customers = gp.get_customers()
    select = int(input("Enter Customer ID to edit: "))

    for cust in customers:
        if select in cust:
            print("1) ID: " + str(cust[0]))
            print("2) Name: " + cust[1])
            print("3) Address: " + cust[2])
            print("4) City: " + cust[3])
            print("5) State: " + cust[4])
            print("6) Zip: " + cust[5])
            while(True):
                edit_field = int(input("Select a field to edit or 'C' to confirm: "))
                if edit_field == 1:
                    cust[0] = int(input("Enter new ID: "))
                if edit_field == 2:
                    cust[1] = input("Enter new name: ")
                if edit_field == 3:
                    cust[2] = input("Enter new street address")
                if edit_field == 4:
                    cust[3] = input("Enter new City: ")
                if edit_field == 5:
                    cust[4] = input("Enter new State")
                if edit_field == 6:
                    cust[5] = input("Enter new ZIP: ")
                if edit_field == 'C':
                    break
                edit_print_cust_info()



def add_vegetable():
    print("Add a vegetable: ")

    vegetable_id = int(input("Enter a vegetable ID #: "))
    vegetable_name = input("Enter the vegetable name: ")
    vegetable_desc = input("Enter the vegetables description and packaging information: ")

    new_vegetable = (vegetable_id, vegetable_name, vegetable_desc)

    try:
            gp.insert_vegetable(new_vegetable)
            gp.close_connection()
    except Error as e:
            print(e)

def create_invoice():
    choice = input("Create a new invoice? <Y/N>")

    if choice == 'Y':
        #make invoice
        do_nothing()
    elif choice == 'N':
        #go back
        do_nothing()
    else:
        print("Incorrect value, please enter 'Y' OR 'N'")
        choice = input("Create a new invoice? <Y/N>")

def main():
    gp.create_connection()
    #add_customer()
    main_menu()


if __name__ == '__main__':
    main()