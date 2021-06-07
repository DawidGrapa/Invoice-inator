import re


def delete_spaces(s):
    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s]", '', s)

    # Replace all runs of whitespace with a single dash
    s = re.sub(r"\s+", '', s)

    return s


def check_float(potential_float):
    try:
        float(potential_float)
        if len(potential_float.rsplit('.')[-1]) > 2:
            return False
        return True
    except ValueError:
        print(potential_float)
        return False


def validate_contractor(contractor):
    name = contractor['name'].get()
    street = contractor['street'].get()
    city = contractor['city'].get()
    zip = contractor['zip'].get()
    nip = contractor['nip'].get()

    x = None
    if len(name) == 0:
        x = "name"
    if len(street) == 0:
        x = "street"
    if len(city) == 0:
        x = "city"
    if len(zip) == 0:
        x = "zip-code"
    if len(nip) != 10 or not nip.isdecimal():
        x = "NIP"

    if x is None:
        return True, x
    else:
        return False, x


def validate_product(product):
    name = product['name'].get()
    unit = product['unit'].get()
    vat = product['vat'].get()
    price = product['price'].get().replace(",", ".")

    x = None
    if len(name) == 0:
        x = "name"
    if len(unit) == 0:
        x = "unit"
    if len(vat) == 0 or not check_float(vat) or not 0 <= int(vat) <= 100:
        x = "vat"
    if len(price) == 0 or float(price) < 0:
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
    bank = delete_spaces(bank)
    x = None
    if len(name) == 0:
        x = "name"
    if len(street) == 0:
        x = "street"
    if len(city) == 0:
        x = "city"
    if len(zip) == 0:
        x = "zip-code"
    if len(nip) != 10 or not nip.isdecimal():
        x = "NIP"
    if len(bank) == 0 or not bank.isdecimal():
        x = "bank"

    if x is None:
        return True, x
    else:
        return False, x


def validate_quantity(q):
    quantity = q.get().replace(",", ".")
    x = None
    try:
        if float(quantity) < 0:
            x = "quantity"
        if x is None:
            return True, x
        else:
            return False, x
    except ValueError:
        x = "quantity"
        return False, x


def validate_invoice_no(number):
    if number.isdecimal() is False:
        return False
    if int(number) < 0:
        return False
    return True
