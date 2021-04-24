def validate_contractor(contractor):
    name = contractor['name'].get()
    street = contractor['street'].get()
    city = contractor['city'].get()
    zip = contractor['zip'].get()
    nip = contractor['nip'].get()

    x = None
    if len(name) == 0: x = "name"
    if len(street) == 0: x = "street"
    if len(city) == 0: x = "city"
    if len(zip) == 0: x = "zip-code"
    if len(nip) != 10 or not nip.isdecimal():
        x = "NIP"

    if x is None:
        return True, x
    else:
        return False, x


def validate_product(product):
    # name = product['name'].get()
    # unit = product['unit'].get()
    # vat = product['vat'].get()
    # price = product['price'].get()
    #
    # x = None
    # if len(name) == 0:
    #     x = "name"
    # if len(unit) == 0:
    #     x = "unit"
    # if len(vat) == 0 or not vat.isdecimal():
    #     x = "vat"
    # if len(price) == 0 or not price.isdecimal():
    #     x = "price"
    #
    # if x is None:
    #     return True, x
    # else:
    #     return False, x

    return True