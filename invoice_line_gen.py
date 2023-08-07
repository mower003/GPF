



for i in range(35, 53):
    print("INSERT INTO invoice_item (id, invoice_id, product_id, case_quantity, quantity, unit_price, tax_rate, tax_amount) VALUES (1, %s, 1, 10, 6172.83, 1.0, 0.0, 0.0);" % i)
    print("INSERT INTO invoice_item (id, invoice_id, product_id, case_quantity, quantity, unit_price, tax_rate, tax_amount) VALUES (2, %s, 1, 10, 6172.84, 1.0, 0.0, 0.0);" % i)
