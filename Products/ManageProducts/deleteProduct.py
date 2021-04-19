from Products.ManageProducts.addProduct import *


db = Database('Database/Database.db')


def remove_product(productMainWindow, selectedItem, update, delete, productList):
    if messagebox.askyesno("Delete", "Are you sure?", parent=productMainWindow):
        db.remove_product(selectedItem[0])
        update['state'] = DISABLED
        delete['state'] = DISABLED
        show_products(productList)