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


def check_float(potential_float):
    try:
        float(potential_float)
        if len(potential_float.rsplit('.')[-1]) > 2:
            return False
        return True

    except ValueError:
        print(potential_float)
        return False


def validate_product(product):
    name = product['name'].get()
    unit = product['unit'].get()
    vat = product['vat'].get()
    price = product['price'].get()

    x = None
    if len(name) == 0:
        x = "name"
    if len(unit) == 0:
        x = "unit"
    if len(vat) == 0 or not check_float(vat) or not 0 <= int(vat) <= 100:
        x = "vat"
    if len(price) == 0 or not check_float(price):
        x = "price"

    if x is None:
        return True, x
    else:
        return False, x


def validate_company(company):
    name = company['name'].get()
    street = company['street'].get()
    zip = company['zip'].get()
    city = company['city'].get()
    nip = company['nip'].get()
    bank = company['bank'].get()

    x = None
    if len(name) == 0: x = "name"
    if len(street) == 0: x = "street"
    if len(city) == 0: x = "city"
    if len(zip) == 0: x = "zip-code"
    if len(nip) != 10 or not nip.isdecimal():
        x = "NIP"
    if len(bank) == 0: x = "bank"

    if x is None:
        return True, x
    else:
        return False, x
